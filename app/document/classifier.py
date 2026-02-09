
from llm.ollam_client import call_llm, ollama_chain


def classify_document_single(ocr_text: str) -> str:
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


def classify_documents(ocr_texts: list[str]) -> list[str]:
    
    prompt = lambda x: f"""
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
{x}

Respond with ONLY the document type.
"""
    
    return ollama_chain([prompt(doc) for doc in ocr_texts])
