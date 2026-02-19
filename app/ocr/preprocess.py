import cv2
import numpy as np
from pathlib import Path
import uuid
def preprocess_image(path: str) -> str:
    img = cv2.imread(path)
    # img = cv2.adaptiveThreshold(
    #     img, 255,
    #     cv2.ADAPTIVE_THRESH_GAUSSIAN_C,
    #     cv2.THRESH_BINARY, 31, 2
    # )
    output_path = path.replace(".jpg", "_clean.jpg")
    cv2.imwrite(output_path, img)
    save_path = Path("output/clean")
    save_path = save_path / f"{str(uuid.uuid4())}.jpg"
    # print("save path ",str(save_path))
    cv2.imwrite(str(save_path),img)
    return output_path
