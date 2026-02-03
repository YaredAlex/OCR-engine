from paddleocr import PaddleOCR

ocr = PaddleOCR(
    use_angle_cls=True,
use_doc_orientation_classify=False,
    use_doc_unwarping=False,
    lang="en",
)

def extract_text(image_path: str) -> str:
    result = ocr.predict(image_path)
    lines = []
    for line in result:
        # print("line,",line)
        lines.extend(line['rec_texts'])
        # line.print()
        line.save_to_img("output")
        # line.save_to_json("output")
        print("texts are ",line['rec_texts'])
    return "\n".join(lines)


# from paddleocr import PPStructureV3

# # Initialize layout engine
# layout_engine = PPStructureV3()

# def extract_layout(image_path: str):
#     """
#     Extract document layout and structured content
#     """
#     result = layout_engine(image_path)

#     structured_output = []

#     for block in result:
#         block_type = block["type"]   # text / title / table / figure
#         bbox = block["bbox"]

#         entry = {
#             "type": block_type,
#             "bbox": bbox,
#             "text": None,
#             "html": None
#         }

#         if block_type in ["text", "title"]:
#             entry["text"] = block["res"]

#         if block_type == "table":
#             entry["html"] = block["res"]["html"]
#         block.save_to_img("output")
#         print(block)
#         structured_output.append(entry)

#     return structured_output
