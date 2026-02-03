
from llm.ollam_client import call_llm


def classify_document(ocr_text: str) -> str:
    prompt = f"""
You are a document classification system.

Classify the document into one of:
- National ID
- Passport
- Driver License
- Invoice
- Bank Statement
- License compitency
- Commercial registration
- Unknown

Text:
{ocr_text}

Respond with ONLY the document type.
"""
    return call_llm(prompt).strip()
