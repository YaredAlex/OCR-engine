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
    " OBSERVATIONS', '2', 'E34837925', 'R', 'CON', '', '', 'The Ministry of Foreign Affairs of', "the People's Republic of China", 'requests all civil and military', 'authorities of foreign countries to', 'allow the bearer of this passport to', 'pass freely and afford assistance in', 'case of need.', '', "PEOPLE'S REPUBLIC OF CHINA", ' OBSERVATIONS', '', '/Type', '/Country Code', '/Passport No.', 'P', 'CHN', 'PASSPORT', 'EJ7792313', 'k/Name', 'ATT88NrE3', '4', 'FENG, JINHUA', '#38/Sex', '#/Nationality', 'UE U M/Date of birth', '/M', '/CHINESE15 SEP1970', 'eU', 'i/Place of birth', 'H /Date of issue', '/FUJIAN', '28 1A/JAN 2023', '18314245324', 'ARV-O', '/Place of issue', '7  W/Date of expiry', 'ARV019 ARV019', '/FUJIAN', 'ARV 019', '27 1/JAN 2033', '/Authority', "/Bearer's signature", 'Ph.7981.9:7617 0000124', 'R#HEB', '$$', 'National Immigration Administration, PRC', 'ARV019', '2 1 AUG 2073', 'ETHIOPVAN', 'POCHNFENG<<INHUA<<<<<<<<<<<<<<<<<<<<<<<<<<<', 'EJ77997741CHN7O0915OM3301270LH0LLNPALLKKA952', '610AY 610A",
    Output:
    {{
  "document_type": "Passport",
  "passport_number": "EJ7792313",
  "country_code": "CHN",
  "issuing_country": "People's Republic of China",
  "full_name": "FENG, JINHUA",
  "surname": "FENG",
  "given_names": "JINHUA",
  "date_of_birth": "15 SEP 1970",
  "gender": "M",
  "nationality": "CHINESE",
  "place_of_birth": "FUJIAN",
  "issue_date": "28 JAN 2023",
  "expiry_date": "27 JAN 2033",
  "place_of_issue": "FUJIAN",
  "mrz_line_1": "P<CHNFENG<<JINHUA<<<<<<<<<<<<<<<<<<<<<<<<<<<",
  "mrz_line_2": "EJ77997741CHN7009150M3301270<<<<<<<<<<<<<<"
}}


    Now extract the information from the following text:
    {text}
    """
    return PASSPORT_ID_PROMT

def visa_prompt(doc_type: str, text: str, schema: dict):
    VISA_PROMT = f"""
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
    " 'ICS', 'P26377A7', 'IMMIGRATION AND CITIZENSHIP SERVICE', 'e-Visa', 'ToV3563468_JCeH5752', 'First/Given Name :', 'Ranvijay', 'SurName :', 'Singh', 'Nationality:', 'India', 'Date of Birth :', '02 Jan 1984', 'Birth Place:', 'Gonda, Uttar Pradesh', 'Travel Document :', 'Ordinary Passport/Z68127445', 'Travel Doc. Issue Date :', '28 Nov 2022', 
    'Travel Doc. Expiry Date:', '27 Nov 2032', 'Valid From :', '27 Sep 2023', 'Valid Until :', '27 Oct 2023', 'Visa Validity Type :', 'Tourist Visa Single Entry 30 Days', 'Reference code :', 'JCeH5752', 'Note: On your arrival at Addis Ababa Bole International Airport Immigration counter,', "please go directly to the counter that's dedicated for e-Visa holders. Don't line up", 'with the travelers applying for on-arrival visa', 'ENJOY YOUR VISIT AND LEAVE BEFORE YOUR VISA EXPIRES SO THAT WE CAN WELCOME YOU AGAIN!', 'Immigration and Citizenship services', 'Addis Ababa, Ethiopia', 'Pλ.7P*8619', 'SMUX', 'EqhA&TMA.h', 'Federal Democratic', 'Republic of Ethiopia', 'Ptàm 7/Date of Issue', 'A7Aa: P7.90n 47/Date ofExpiry', '10 OCT 23', '09 NOV 
    23', 'Ptamnt n-/Place of Issue', 'Pn.n %ert/ Visa Type', 'MDINA', 'W', 'P. dTC/Visa Number', 'V', 'Pa0.  / No. Entries', 'VS5241245', 'S', 'Ph, n/Surname', 'hg hihn/ Given Name', 'SINGH', 'RANVIJAY', '9/Sex', 'Po/Date of Birth', 'H.777/Nationality', 'M', '02 JAN 84', 'IND', 'P.T. TC/Passport Number', 'h-d.o- Pg3 / No. of Applicants', 'Z6812712', '1', 'P4 .C 
    /Authorized Signature', 'Ppf', 'VS5241245', 'VWEHSINGH<GANVIAY<<<<<<<<<<<<', 'Z6812712<4IND8401027M231109052476073', '3', 'VSISIMSSA'",
    Output:
    {{
  "visa_number": "VS5241245",
  "visa_type": "Tourist Visa Single Entry 30 Days",
  "valid_from": "27 SEP 2023",
  "valid_until": "27 OCT 2023",
  "number_of_entries": "Single",
  "issuing_country": "Federal Democratic Republic of Ethiopia",
  "place_of_issue": "MDINA",
  "issue_date": "10 OCT 2023",
  "full_name": "SINGH, RANVIJAY",
  "surname": "SINGH",
  "given_names": "RANVIJAY",
  "sex": "M",
  "date_of_birth": "02 JAN 1984",
  "nationality": "INDIA",
  "passport_number": "Z6812712",
  "passport_issue_date": "28 NOV 2022",
  "passport_expiry_date": "27 NOV 2032",
  "reference_code": "JCeH5752",
  "mrz_line_1": "VWEHSINGH<RANVIJAY<<<<<<<<<<<<",
  "mrz_line_2": "Z6812712<4IND8401027M231109052476073"
}}


    Now extract the information from the following text:
    {text}
    """
    return VISA_PROMT

def support_letter_prompt(doc_type: str, text: str, schema: dict):
    SUPPORT_LETTER_PROMPT = f"""
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
    " 'A STAR ALLIANCE MEMBER', 'Ethiopian', 'PhTPAS', 'The New Spirit Of Africa', 'Ref: EAL/GIPD/1905/24', 'Date: December 27, 2024', 'FDRE, Ministry of Labour and Skills', 'Addis Ababa', 'Ref: Design-Build, Financing and Commissioning of Ethiopian Airlines Group', 'Employees Housing Phase II Lot-II Construction Project', 'Request to Get a Work Permit', 'Ethiopian Airlines Group has entered into a Contract Agreement with Dar Al-Handasah', 'Consultants (Shair and Partners) 
for the consultancy service of the subject project.', "Following the Contractor's request, the Employer's representative requested us, through", 'its letter dated December 24, 2024, with Ref. No. ET23222-0200S/E/442-24 to issue a', "supporting letter for the issuance of work permit for the underlisted contractors' staffs.", "Thus, we kindly request the Ministry to assist the underlisted contractor's staffs to get", 'work permit and stay in Ethiopia for the project duration.', 'No.', 'Name', 'Passport No.', 'Position/Professional', '1', 'Edwin Alex', 'W 1393123', 'Project Engineer', '2', 'Saravana Muthu', 'X 3331123', 'Supervisor', '3', 'Prabu Pillappan', 'P 3453123', 'Technician', 'Your cooperation is highly appreciated.', 'Sincerely,', 'RPC', 'ony', 'Abraham Tesfaye', 'AENWOLN', 'Director Group Infrastructure', 'Planning & development', 'AG/mw', 'Encl: 3-pages passport copy', 'Bole International Airport, P.O.Box 1755, Addis Ababa, Ethiopia Tel: (251-011) 617 9900, Hotline Number 6787,', 'Fax: (251-011) 661 1474', 'www.ethiopianairlines.com'",
    Output:
    {{
  "letter_reference_number": "EAL/GIPD/1905/24",
  "letter_date": "27 December 2024",
  "issuing_organization": "Ethiopian Airlines Group",
  "issuing_department": "Group Infrastructure Planning & Development",
  "recipient_organization": "FDRE Ministry of Labour and Skills",
  "recipient_location": "Addis Ababa, Ethiopia",
  "project_title": "Employees Housing Phase II Lot-II Construction Project",
  "project_reference": "Design-Build, Financing and Commissioning of Ethiopian Airlines Group Employees Housing Phase II",
  "purpose": "Request to Get a Work Permit",
  "contracting_company": "Dar Al-Handasah",
  "consultant_company": "Dar Al-Handasah Consultants (Shair and Partners)",
  "employees": [
    {
      "serial_number": 1,
      "full_name": "Edwin Alex",
      "passport_number": "W1393123",
      "position": "Project Engineer"
    },
    {
      "serial_number": 2,
      "full_name": "Saravana Muthu",
      "passport_number": "X3331123",
      "position": "Supervisor"
    },
    {
      "serial_number": 3,
      "full_name": "Prabu Pillappan",
      "passport_number": "P3453123",
      "position": "Technician"
    }
  ],
  "signatory_name": "Abraham Tesfaye",
  "signatory_title": "Director Group Infrastructure Planning & Development",
  "contact_address": "Bole International Airport, P.O.Box 1755, Addis Ababa, Ethiopia",
  "contact_phone": "(251-011) 617 9900",
  "contact_website": "www.ethiopianairlines.com",
  "attachments": "3-pages passport copy"
}}


    Now extract the information from the following text:
    {text}
    """
    return SUPPORT_LETTER_PROMPT
