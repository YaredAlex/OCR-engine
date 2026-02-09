from paddleocr import PaddleOCR

ocr = PaddleOCR(
    use_angle_cls=True,
use_doc_orientation_classify=False,
    use_doc_unwarping=False,
    lang="en",
)

def extract_text(image_path: list[str]) -> list[str]:
    results = ocr.predict(image_path)
    lines = []
    for result in results:
        lines.append(result['rec_texts'])
        result.save_to_img("output")
        # line.save_to_json("output")
    return lines


