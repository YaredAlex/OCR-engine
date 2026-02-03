def extraction_prompt(doc_type: str, text: str, schema: dict) -> str:
    return f"""
You are an OCR post-processing AI.

Document type: {doc_type}

Extract the information and return STRICT JSON
following this schema:
{schema}

Rules:
- If field not found, use null
- No explanation
- JSON only

OCR TEXT:
{text}
"""
