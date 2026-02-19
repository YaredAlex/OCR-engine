from paddleocr import PaddleOCR,PPStructureV3
from pathlib import Path
ocr = PaddleOCR(
    use_angle_cls=True,
use_doc_orientation_classify=False,
    use_doc_unwarping=False,
    lang="en",
)
# pp_ocr = PPStructureV3(device="GPU",
# use_doc_orientation_classify=False,
#     use_doc_unwarping=False,)


def extract_text(image_path: list[str]) -> list[str]:
    results = ocr.predict(image_path)
    lines = []
    for result in results:
        lines.append(result['rec_texts'])
        print("extracted text is ",result['rec_texts'])
        result.save_to_img("output")
        # line.save_to_json("output")
    return lines

# def extract_text(image_path: list[str]) -> list[str]:
#     results = pp_ocr.predict(image_path)
#     lines = []
#     markdown_images = []
#     output_path = Path("output")
#     for result in results:
#         # print("result ",result)
#         print("markdown ",result.markdown)
#         markdown_content = result.markdown.get("markdown_texts","")
#         markdown_image = result.markdown.get("markdown_images",{})
#         lines.append(markdown_content)
#         markdown_images.append(markdown_image)
#         # print("extracted text is ",result['rec_texts'])
#         # result.save_to_img("output")
#         # line.save_to_json("output")
#     for item in markdown_images:
#         if item:
#             for path, image in item.items():
#                 file_path = output_path / path
#                 file_path.parent.mkdir(parents=True, exist_ok=True)
#                 print("image saveed to markdown image",file_path.absolute())
#                 image.save(file_path)
#     return lines


