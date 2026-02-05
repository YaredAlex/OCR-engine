from collections import defaultdict
import os
import json
import tempfile
from multiprocessing import Pool
from typing import List
from pdf2image import convert_from_path
from PIL import Image
from llm.ollam_client import call_llm
from ocr.engine import extract_text
from ocr.preprocess import preprocess_image
from document.classifier import classify_document
from llm.prompts import extraction_prompt
from document.schemas import BUSINESS_LICENSE, ID_SCHEMA, LICENSE_COMPITENCY


INPUT_DIR = "data/input"
OUTPUT_DIR = "data/output"
SUPPORTED_IMAGES = {".jpg", ".jpeg", ".png", ".bmp", ".tiff", ".webp"}


def is_pdf(path: str) -> bool:
    return path.lower().endswith(".pdf")


def is_image(path: str) -> bool:
    return os.path.splitext(path)[1].lower() in SUPPORTED_IMAGES


def pdf_to_images(pdf_path: str) -> List[str]:
    """
    Convert PDF pages to temporary image files.
    Returns list of image paths.
    """
    images = convert_from_path(pdf_path, dpi=300)

    temp_dir = tempfile.mkdtemp(prefix="pdf_ocr_")
    image_paths = []

    for i, img in enumerate(images):
        img_path = os.path.join(temp_dir, f"page_{i+1}.png")
        img.save(img_path, "PNG")
        image_paths.append(img_path)

    return image_paths

def process_file(filenames: list[str] = None, single_path: str = None):
    """
    Args:
        filenames: list[filename]
    Process a single image or PDF file.
    Works for batch mode and API mode.
    """
    paths = [single_path] if single_path else [os.path.join(INPUT_DIR, f) for f in filenames]

    for p in paths:
        if not os.path.exists(p):
            raise FileNotFoundError(f"File not found: {p}")

    extracted_text_parts = []
    # different key same value
    image_key = defaultdict(list)
    batch_images = []
    for path in paths:
        if is_pdf(path):
            image_paths = pdf_to_images(path)

            for img_path in image_paths:
                clean_img = preprocess_image(img_path)
                batch_images.append(clean_img)
                image_key[path].append(len(batch_images)-1)

                # text = extract_text(clean_img)
                # extracted_text_parts.append(text)

        elif is_image(path):
            clean_img = preprocess_image(path)
            batch_images.append(clean_img)
            image_key[path].append(len(batch_images)-1)
            # text = extract_text(clean_img)
            # extracted_text_parts.append(text)

        else:
            raise ValueError(f"Unsupported file type: {path}")

    #call paddle ocr batch processing
    ocr_results = extract_text(batch_images)
    combined_texts = defaultdict(str)
    for img,indexs in image_key.items():
        combined_texts[img] = f"{combined_texts[img]} {"\n".join(ocr_results[indexs])}"
        
    # Combine text (important for PDFs)
    full_text = "\n".join(extracted_text_parts)
    doc_type = classify_document(full_text)

    schema = {}
    print("doctype is ", doc_type)
    if doc_type in ["National ID", "Passport"]:
        schema = ID_SCHEMA
    if doc_type in ["License compitency"]:
        schema = LICENSE_COMPITENCY
    if doc_type in ["Commercial registration"]:
        schema = BUSINESS_LICENSE
        
    prompt = extraction_prompt(doc_type, full_text, schema)
    result = call_llm(prompt)


    os.makedirs(OUTPUT_DIR, exist_ok=True)
    output_name = os.path.basename(path) + ".json"
    output_path = os.path.join(OUTPUT_DIR, output_name)

    with open(output_path, "w", encoding="utf-8") as f:
        f.write(result)

    try:
        structured = json.loads(result)
    except json.JSONDecodeError:
        structured = {"raw_output": result}

    return {
        "file": os.path.basename(path),
        "document_type": doc_type,
        "data": structured
    }


def run_batch():
    files = [
        f for f in os.listdir(INPUT_DIR)
        if is_image(f) or is_pdf(f)
    ]

    # with Pool(processes=8) as pool:
    #     pool.map(process_file, files)
    # using batch processing instead of thread pooling
    process_file(files)


if __name__ == "__main__":
    run_batch()
