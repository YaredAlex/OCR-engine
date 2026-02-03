import easyocr
import cv2
from typing import List

# Initialize once (important for performance)
reader = easyocr.Reader(
    ['en'],
    gpu=True  # set False if no GPU
)

def extract_text(image_path: str) -> str:
    """
    Extract text from image using EasyOCR
    """
    image = cv2.imread(image_path)
    if image is None:
        raise ValueError(f"Cannot read image: {image_path}")

    results = reader.readtext(image)

    lines: List[str] = []
    for bbox, text, confidence in results:
        if text.strip():
            lines.append(text)

    return "\n".join(lines)
