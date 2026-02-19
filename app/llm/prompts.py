def extraction_prompt(doc_type: str, text: str, schema: dict) -> str:
    return f"""
You are an OCR post-processing AI.

Document type: {doc_type}

Extract the information and return STRICT JSON and START WIHT CURLY BRACES
following this schema:
<schema>
{schema}
</schema>
Rules:
- If field not found, use null
- No explanation
- JSON only
- I No schema matches make a schema that fits the document

OCR TEXT:
{text}
"""
