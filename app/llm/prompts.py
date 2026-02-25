from document.schemas import GENERAL_SCHEMA, PERMIT_REQUEST


def extraction_prompt(doc_type: str, text: str, schema: dict) -> str:
    doc_type = doc_type.replace("\n","").lower()
    if doc_type =="passport" or doc_type=="visa" or doc_type=="national id":
        return passport_id_prompt(doc_type,text,schema)
    return f"""
You are an information extraction system.

Extract only the following fields from the provided identity document text.

Document type: {doc_type}

Extract the information and return STRICT JSON NO ADDITIONAL fields.
following this schema:
{schema}

IF Schema is NOT FOUND make appropriate Schema according to extracted text. 
Example for how to construct schema if not found:
1. For Work Permit
{PERMIT_REQUEST}
2. General perpose
{GENERAL_SCHEMA}

Return STRICT JSON only.
- Do NOT add extra fields.
- Do NOT add metadata.
- Do NOT nest the response.
- Do NOT include explanations.
- Do NOT include markdown formatting.
- Do NOT include text before or after the JSON.
- If a field is missing, return an empty string "".
- Do not start with new line or \n
- Start with {{}} 

Now extract the information from the following text:
{text}
"""

def passport_id_prompt(doc_type: str, text: str, schema: dict):
    PASSPORT_ID_PROMT = f"""
    You are an information extraction system.

    Extract only the following fields from the provided identity document text.

    Document type: {doc_type}

    Extract the information and return STRICT JSON NO ADDITIONAL fields.
    following this schema:
    {schema}


    Return STRICT JSON only.
    - Do NOT add extra fields.
    - Do NOT add metadata.
    - Do NOT nest the response.
    - Do NOT include explanations.
    - Do NOT include markdown formatting.
    - Do NOT include text before or after the JSON.
    - If a field is missing, return an empty string "".
    - The output must match EXACTLY this schema structure.
    - Do not start with new line or \n
    - Start with {{}} 

    Example 
    Input:
    "\n\n\n08\nThe Ministry of Foreign Affairs of\nthe People's Republic of China\nrequests all civil and military\nauthorities of foreign countries to\n
    allow the bearer of this passport to\npass freely and afford assistance in\ncase of need.\nA\nPEOPLE'S REPUBLIC OF CHINA\n$\nM/Type\n/Country Code\n
    /Passport No.\nP\nCHN\nED7508204\nPASSPORT\n4/Name\n5\nFANG, YI\nt31/Sex\n/Nationality\n I / Date of birth\n/CHINESE\n26 DEC 1985\n/M\nH1 /Place of birth\n
    Date ofissue\n/HUNAN\n13 73/JUL 2018\n1390369166\nPlace of issue\n/Date of expiry\n12 7/JUL 2028\n/HUNAN\n/Authority\n/Bearer's signature\nB\nA\n
    MPS Exit & Entry Administration\nPOCHNFANG<<YI<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<\nED75082045CHN8512268M2807122LHLPNC0D<<<<A998",
    Output:
    {{
    "full_name": "FANG, YI",
    "id_number": "ED7508204",
    "date_of_birth": "26 DEC 1985",
    "gender": "M",
    "nationality": "CHINESE",
    "issue_date": "13 JUL 2018",
    "expiry_date": "12 JUL 2028"
     }}


    Now extract the information from the following text:
    {text}
    """
    return PASSPORT_ID_PROMT
