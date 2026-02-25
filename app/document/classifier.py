
from llm.ollam_client import call_llm, ollama_chain


def classify_document_single(ocr_text: str) -> str:
    prompt = f"""
You are a document classification system.

Classify the document into one of the following types:
- Passport
- Visa
- Support Letter
- Contract
- Work Experience
- Education Certificate
- Clearance Request Letter
- Letter of Delegation

Hints for classification (use these to identify the document type from the text):
1. Passport: Look for words like 'Passport No.', 'Nationality', 'Date of Birth', 'Place of Issue', 'Expiry Date', 'Bearer'.
2. Visa: Look for 'Visa Number', 'Travel Document', 'Valid From', 'Valid Until', 'Nationality', 'Entry Type'.
3. Support Letter: Look for references to a company/organization requesting assistance or permission, often for employees, contractors, or work permits.
4. Contract: Look for 'Agreement', 'Employer', 'Employee', 'Terms and Conditions', 'Duration', 'Salary', 'Article'.
5. Work Experience: Look for 'Experience Certificate', 'worked as', 'from DATE to DATE', 'performance', 'roles', 'responsibilities'.
6. Education Certificate: Look for 'Degree', 'Certificate', 'Graduation', 'Institution', 'Course', 'CGPA'.
7. Clearance Request Letter: Look for 'Request for Clearance', 'Work Permit Cancellation', 'Staff Members', 'Ref'.
8. Letter of Delegation: Look for 'Power of Attorney', 'Authorized Agent', 'Principal', 'Agent', 'authorization', 'represent', 'government offices'.

Text:
{ocr_text}

Respond with ONLY the document type, no explanations or extra text.
"""
    return call_llm(prompt).strip()


def classify_documents(ocr_texts: list[str]) -> list[str]:
    
    prompt = lambda x: f"""
You are a document classification system.

Classify the document into one of the following types:
- Passport
- Visa
- Support Letter
- Contract
- Work Experience
- Education Certificate
- Clearance Request Letter
- Letter of Delegation

Hints for classification (use these to identify the document type from the text):
1. Passport: Look for words like 'Passport No.', 'Nationality', 'Date of Birth', 'Place of Issue', 'Expiry Date', 'Bearer'.
2. Visa: Look for 'Visa Number', 'Travel Document', 'Valid From', 'Valid Until', 'Nationality', 'Entry Type'.
3. Support Letter: Look for references to a company/organization requesting assistance or permission, often for employees, contractors, or work permits.
4. Contract: Look for 'Agreement', 'Employer', 'Employee', 'Terms and Conditions', 'Duration', 'Salary', 'Article'.
5. Work Experience: Look for 'Experience Certificate', 'worked as', 'from DATE to DATE', 'performance', 'roles', 'responsibilities'.
6. Education Certificate: Look for 'Degree', 'Certificate', 'Graduation', 'Institution', 'Course', 'CGPA'.
7. Clearance Request Letter: Look for 'Request for Clearance', 'Work Permit Cancellation', 'Staff Members', 'Ref'.
8. Letter of Delegation: Look for 'Power of Attorney', 'Authorized Agent', 'Principal', 'Agent', 'authorization', 'represent', 'government offices'.

Text:
{x}

Respond with ONLY the document type, no explanations or extra text.
"""
    
    return ollama_chain([prompt(doc) for doc in ocr_texts])
