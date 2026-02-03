import pytesseract
from PIL import Image
import cv2
import os

  

def extract_text(image_path: str) -> str:
    """
    Extract text from image using Tesseract OCR
    """
    if not os.path.exists(image_path):
        raise FileNotFoundError(image_path)

    image = cv2.imread(image_path)
    if image is None:
        raise ValueError(f"Cannot read image: {image_path}")

    # Convert BGR → RGB
    image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

    text = pytesseract.image_to_string(
        image,
        lang="eng",
        config="--oem 3 --psm 6"
    )

    return text.strip()
