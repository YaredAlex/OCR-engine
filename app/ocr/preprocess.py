import cv2
import numpy as np

def preprocess_image(path: str) -> str:
    img = cv2.imread(path, cv2.IMREAD_GRAYSCALE)
    img = cv2.adaptiveThreshold(
        img, 255,
        cv2.ADAPTIVE_THRESH_GAUSSIAN_C,
        cv2.THRESH_BINARY, 31, 2
    )
    output_path = path.replace(".jpg", "_clean.jpg")
    cv2.imwrite(output_path, img)
    return output_path
