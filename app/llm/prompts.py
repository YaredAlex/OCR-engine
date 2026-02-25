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

def contract_letter_prompt(doc_type: str, text: str, schema: dict):
    CONTRACT_LETTER_PROMPT = f"""
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
    "'YYDTS', 'PERSONAL CARE', 'FACTORY', 'Y PLC', 'Employment Contract', 'hereunder.', '1. ADDRESS OF THE EMPLOYER', 'Kirkos Sub City; Kebele18; House No. 566; Telephone No. 09-11-16-23-09', 'P.O.Box', 'Aa a', '2. AGE AND ADDRESS OF THE EMPLOYEE', '2.1. Date of Birth: - 1971', 'Nationality: - Keyan Passport Number:- CK59113', '3. TYPE OF EMPLOYMENT AND PLACE OF WORK', "Coe  s eee ee pe 'oee  see ree e Im", 'his/her duties in his/her capacity as a Marketing Manager in accordance', 'with the directives of the employer on a full-time basis.', '3.2.', "The employee's place of work shall be in YYDTS Personal Care PLC, Alem", 'Gena, Ethiopia.', '4. REMUNERATION', 'The employee shall be paid Gross salary of 39,230.77 (Thirty-nine', '4.1.', 'thousand two hundred thirty birr & 77/100), House allowance 
of net', '30,000.00 (Thirty thousand birr). In addition, the employee will be eligible', 'for a round trip of ticket twice a year to visit his family.', "Income tax is deducted from the employee's gross payment according to", '4.2.', 'income tax regulations; and paid directly to the Inland Revenue', 'administration by the employer.', '5. CONDITIONS OF EMPLOYMENT;', '5.1. The parties have hereby agreed that the conditions stipulated in the', 'Ethiopian civil code of 1960 are applicable to this contract of employment.', '5.2.', 'lod/4', 'applicable to this contractof employment', 'HOt', 'PP.9', '', '0911162309', 'YYDTS Personal Care PLC', 'E-mail: info@yydts.com • www.yydts.com', ':+251 912 0049 11', 'Number', 'Manufacturer of beauty and personal care brands.'
'5.3.', ', devote his whole', 'employer and is', 's of the', 'Manual.', '6.1.', 'parties consent to.', '6.2.', 'service to the Employee, prior to the end of the probationary period will be', 'given.', '6.3.', "This agreement may be terminated by either party by giving a one month's", 'written notice of termination of service the one to the other, provided that', 'such notice must be given on the 1st day of the particular month.', 'IN wITNEsS hereof, the parties to this agreement have affixed their signature hereto,', 'on the date first mentioned in the agreement.', 'hc', 'TCASA', 'Lidya Esnetof', 'TEL', '  ', 'Joseph Njogu Kiando', 'YYDTS Personal Care PLC', '0911162309', '(The Employee)', '(The Employer)', 'WITNESSES:', 'Ju', 'I. Manlet fantaluy', 'tS', '2. Selam Degife'",
    Output:
    {{
  "contract_type": "Employment Contract",

  "employer": {
    "company_name": "YYDTS Personal Care PLC",
    "branch": null,
    "address": "Kirkos Sub City, Kebele 18, Addis Ababa, Ethiopia",
    "representative_name": null,
    "representative_title": null
  },

  "employee": {
    "full_name": "Joseph Njogu Kiando",
    "address": null,
    "phone": null,
    "nationality": "Kenyan",
    "passport_number": "CK59113",
    "date_of_birth": "1971"
  },

  "employment_details": {
    "job_title": "Marketing Manager",
    "employment_type": "Full-Time",
    "place_of_work": "Alem Gena, Ethiopia",
    "start_date": null,
    "end_date": null,
    "contract_duration": null,
    "probation_period": null
  },

  "compensation": {
    "basic_salary": "39,230.77",
    "currency": "ETB",
    "allowances": "30,000 ETB House Allowance",
    "payment_frequency": "Monthly"
  },

  "termination": {
    "notice_period": "1 Month Written Notice",
    "early_termination_conditions": null
  },

  "governing_law": "Ethiopian Civil Code of 1960",
  "jurisdiction": null,

  "signatures": {
    "employer_signatory": "YYDTS Personal Care PLC",
    "employee_signatory": "Joseph Njogu Kiando",
    "contract_signed_date": null
  }
}}


    Now extract the information from the following text:
    {text}
    """
    return CONTRACT_LETTER_PROMPT

def clearance_letter_prompt(doc_type: str, text: str, schema: dict):
    CLEARANCE_LETTER_PROMPT = f"""
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
    "'DRC', 'CAINAK', 'REEEE', 'COUNCIL', 'Ref: DRC/034/2024', 'Date: February 14, 2024', 'FDRE Ministry of Labor and Skills', 'Addis Ababa', 'Dear Sir Madam,', 'Subject: Request for Work Permit Cancellation', 'The Danish Refugee Council (DRC) is an independent international non-governmental', 'organization, working in 35 countries throughout the world and our primary mandate is to', 'promote durable solutions for Refugees and displaced populations. DRC Regional office in 
Nairobi', 'covers the Horn of Africa region and provides support and guidance to DRC programs in Kenya,', 'Ethiopia, Somalia, Somaliland, Puntland, and Uganda.', 'Mrs. AGNES OYELLA a Ugandan national holder of passport number A00339838, has a contract to', 'work as an AREA MANAGER. This is, therefore, to request your esteemed 
office to cancel the', 'Work Permit of Mr. AGNES OYELLA.', 'Thank you and your usual cooperation is highly appreciated.', 'Danish', 'Sincerely,', 'DRC', 'Aurélie Leroyer', 'Ei', 'Country Direetor', '2', 'I', 'Danish Refugee Council -Ethiopia', 'fuge', 'COHR'",
    Output:
    {{
  "document_type": "work_permit_cancellation_request",
  "letter_metadata": {
    "reference_number": "DRC/034/2024",
    "date": "February 14, 2024",
    "subject": "Request for Work Permit Cancellation",
    "recipient_organization": "FDRE Ministry of Labor and Skills",
    "recipient_location": "Addis Ababa"
  },
  "requesting_organization": {
    "organization_name": "Danish Refugee Council - Ethiopia",
    "parent_organization": "Danish Refugee Council (DRC)",
    "branch_name": "Ethiopia Country Office",
    "organization_type": "International NGO",
    "address": null,
    "email": null
  },
  "request_details": {
    "request_type": "work_permit_cancellation",
    "reason": "End of contract",
    "description": "Request to cancel the work permit of the employee holding a Ugandan passport."
  },
  "employees": [
    {
      "full_name": "AGNES OYELLA",
      "first_name": "AGNES",
      "last_name": "OYELLA",
      "passport_number": "A00339838",
      "nationality": "Ugandan",
      "position": "Area Manager",
      "gender": null
    }
  ],
  "signatory": {
    "name": "Aurélie Leroyer",
    "position": "Country Director",
    "department": null
  },
  "additional_information": {
    "attachments": null,
    "notes": null
  }
}}


    Now extract the information from the following text:
    {text}
    """
    return CLEARANCE_LETTER_PROMPT

def delegation_letter_prompt(doc_type: str, text: str, schema: dict):
    DELEGATION_LETTER_PROMPT = f"""
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
    "'title', 'hitp://10.1.7.17/DARIS/Representation/FullGeneralRepresentatior', 'Doc No: B11/0014006/1/2017', 'Date: 1/24/2025', '4451239', 'Federal Document Authentication and Registration Service', 'Addis Ababa', 'Adminstrative Power of Attorney', 'Principal : I Mr/ Agada Andrew On behalf of Dunamis interanational Gospel Center GM Nationality/', 'Nigerian', 'Address : Addis Ababa Sub City :lmikura Woreda: 8House No :new PassPoret No A12657503', 'Agent:-1', 'Mss. Hawi Marekos Terfa Nationality/Ethiopian/', 'Address : Addis Ababa Sub City : Yeka Woreda: 11House No :new', 'I the principal authorize the agent to act on my behalf To enter into a lease agreement To renew the', 'contract to cancel the contract The agent is authorized to act and perform the following activities on behalf of', 'the principal to represent the principal at the federal offices, ministry of labor and social affairs, immigration', 'office, sub city offices Kebele offices and all government offices. The agent is also given power to process,', 'pay and receive residence ID, Visa, work permit for expatriates, foreign visitors on behalf of the principal', 'registered Property. To manage, to preserve and supervise, To pay any kind of payment, To terminate/revoke a', 'contract , To appoint advocate and litigate at any court and(or) at any body of justice , To give and receive', 'any form of DocumentsI witness where of I have subscribed my signature in accordance with Article 2199', 'and 2203 of the Ethiopian Civil Code.', "Principal's Name and Signature", 'NameA....p', 'PN 9227 9H MA7A', 'P/11 /0 X', 'Signature.....', 'L6To NXM* &Cno LCq9A;', 'cB11/00/4006/1/2017', '1/24/2025', '10750', '7L', 'VE', '+n4f', 'Fov', '0077n', 'reg sn', '9', 'Moo8/IV', 'Pris', 'incroal', 'P35 NC AC: MhA', 'PaU', '1 of 1', '1/24/2025, 2:29'
  'DUNAMIS INTERNATIONAL GOSPEL CENTER ETHOPIA', 'DUNAMIS', 'Id no DIGCE/addis/0001/25/PA', '7f', 'Name :-Hawi Markos Terfa', 'AS', 'NUO', 'ADVENI', 'Isuued date:- 01/01/25', 'IMMER', '**', '×', 'Expired date;- 01/01/30', 'Center', 'Ethiop'
 'TCOZSSTCEMALEBEUHONIV', '', '0900434588', 'DUN', 'Gonbi', '*', 'Fomsh', 'n011269', 'es1t012091ahhsnu2', 'Exbpeq9are-011or13'
  '*', 'PATrACe', 'f6∞+8', 'Ethiopian Digital ID Card', 'National ID', '2024/Dec/26', 'Mn9IFull', 'Name', 'on', '9C8n +C4', 'Hawi Markos', 'Terfa', '+mn+2017/04/17 Date of Issue', 'P  | Date of Birth', '23/02/1982|', '1989/Nov/02', '25| Sex', 'nt', '| Female', '400', 'pn+ ? | Date of Expiry', '2025/04/17', '2032/Dec/26', 'nce', '4915071687513620', '$mC', 'FAN'
  'nAh |Phone', 'Number', '0911057452', '4169', 'Nationality', '(n+)A&MMnc+|Self Declared)', 'X+PAS', '|Ethiopian', 'X|Address', 'UUYYOY', 'Addis 
Ababa', 'ph', 'Yeka', 'M11', 'Woreda 11', '48e', 'FIN784532651946', 'AROTC', 'BU D M nX 7M M D-SCh= A 9779 E Mi.t/arpnt=', 'SN:', '7165010', 'If lost and found, please return to nearby police station or to the institution. Call 9779 or visit id.et/cardprint for more.'",
    Output:
    {{
  "document_type": "administrative_power_of_attorney",
  "document_metadata": {
    "document_number": "B11/0014006/1/2017",
    "registration_number": "4451239",
    "date_of_issue": "2025-01-24",
    "issuing_authority": "Federal Document Authentication and Registration Service",
    "place_of_issue": "Addis Ababa"
  },
  "principal": {
    "full_name": "Agada Andrew",
    "represented_organization": "Dunamis International Gospel Center",
    "nationality": "Nigerian",
    "passport_number": "A12657503",
    "address": {
      "city": "Addis Ababa",
      "sub_city": "Lemi Kura",
      "woreda": "8",
      "house_number": "new"
    }
  },
  "agent": {
    "full_name": "Hawi Marekos Terfa",
    "nationality": "Ethiopian",
    "id_type": "Ethiopian Digital ID",
    "id_number": "4915071687513620",
    "date_of_birth": "1982-02-23",
    "gender": "Female",
    "phone_number": "0911057452",
    "address": {
      "city": "Addis Ababa",
      "sub_city": "Yeka",
      "woreda": "11",
      "house_number": "new"
    }
  },
  "authorization": {
    "authorization_type": "general_administrative_power",
    "authorized_actions": [
      "enter_lease_agreement",
      "renew_contract",
      "cancel_contract",
      "represent_before_government_offices",
      "process_visa",
      "process_work_permit",
      "process_residence_id",
      "make_and_receive_payments",
      "appoint_advocate",
      "litigate_in_court",
      "manage_registered_property",
      "receive_and_submit_documents"
    ],
    "applicable_institutions": [
      "Federal Offices",
      "Ministry of Labor and Social Affairs",
      "Immigration Office",
      "Sub City Offices",
      "Kebele Offices",
      "Courts"
    ]
  },
  "legal_basis": {
    "civil_code_articles": [
      "Article 2199",
      "Article 2203"
    ]
  },
  "validity": {
    "effective_date": "2025-01-24",
    "expiry_date": null,
    "revocation_allowed": true
  },
  "signatures": {
    "principal_signed": true,
    "agent_signed": null,
    "witnessed": true
  },
  "supporting_documents": {
    "agent_id_attached": true,
    "principal_passport_attached": true
  }
}}


    Now extract the information from the following text:
    {text}
    """
    return DELEGATION_LETTER_PROMPT
