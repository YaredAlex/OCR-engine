ID_SCHEMA = {
    "full_name": "",
    "id_number": "",
    "date_of_birth": "",
    "gender": "",
    "nationality": "",
    "issue_date": "",
    "expiry_date": ""
}
PASSPORT_SCHEMA = {
  "document_type": "",
  "passport_number": "",
  "country_code": "",
  "issuing_country": "",
  "full_name": "",
  "surname": "",
  "given_names": "",
  "date_of_birth": "",
  "gender": "",
  "nationality": "",
  "place_of_birth": "",
  "issue_date": "",
  "expiry_date": "",
  "place_of_issue": "",
  "mrz_line_1": "",
  "mrz_line_2": ""
}

VISA_SCHEMA = {
  "visa_number": "",
  "visa_type": "",
  "valid_from": "",
  "valid_until": "",
  "number_of_entries": "",
  "issuing_country": "",
  "place_of_issue": "",
  "issue_date": "",
  "full_name": "",
  "surname": "",
  "given_names": "",
  "sex": "",
  "date_of_birth": "",
  "nationality": "",
  "passport_number": "",
  "passport_issue_date": "",
  "passport_expiry_date": "",
  "reference_code": "",
  "mrz_line_1": "",
  "mrz_line_2": ""
}

SUPPORT_LETTER_SCHEMA = {
  "letter_reference_number": "",
  "letter_date": "",
  "issuing_organization": "",
  "issuing_department": "",
  "recipient_organization": "",
  "recipient_location": "",
  "project_title": "",
  "project_reference": "",
  "purpose": "",
  "contracting_company": "",
  "consultant_company": "",
  "employees": [
    {
      "serial_number": "",
      "full_name": "",
      "passport_number": "",
      "position": ""
    },
  ],
  "signatory_name": "",
  "signatory_title": "",
  "contact_address": "",
  "contact_phone": "",
  "contact_website": "",
  "attachments": ""
}

CONTRACT_SCHEMA = {
  "contract_type": "",
  "employer": {
    "company_name": "",
    "branch":"",
    "address": "",
    "representative_name":"",
    "representative_title":"" 
  },

  "employee": {
    "full_name": "",
    "address":"",
    "phone":"",
    "nationality": "",
    "passport_number": "",
    "date_of_birth": ""
  },

  "employment_details": {
    "job_title": "",
    "employment_type": "",
    "place_of_work": "",
    "start_date":"",
    "end_date":"",
    "contract_duration":"",
    "probation_period": ""
  },

  "compensation": {
    "basic_salary": "",
    "currency": "",
    "allowances": "",
    "payment_frequency": ""
  },

  "termination": {
    "notice_period": "",
    "early_termination_conditions": ""
  },

  "governing_law": "",
  "jurisdiction":"",

  "signatures": {
    "employer_signatory": "",
    "employee_signatory": "",
    "contract_signed_date":"" 
  }
}
EXPERIANCE_SCHEMA = {
  "organization": {
    "name": "",
    "address": "",
    "contact": {
      "phone": "",
      "email": ""
    },
    "reference_number": "",
    "issue_date": ""
  },
  "employee": {
    "full_name": "",
    "role": "",
    "start_date": "",
    "end_date": "",
    "currently_employed": ""
  },
  "performance_summary": "",
  "authorized_signatory": {
    "name": "",
    "designation": ""
  }
}

BUSINESS_LICENSE = {
    "tin":"",
    "principa_registration_no":"",
    "previous_license_no":"",
    "business_license_no":"",
    "previous_date_of_issuance":"",
    "date_of_issuance":"",
    "company_name":"",
    "nationality":"",
    "trade_name":"",
    "general_manager":"",
    "business_address":"",
    "field_of_business":"",
    "capital_in_etb":"",

}
LICENSE_COMPITENCY = {
    "name_of_agency":"",
    "owner_manager":"",
    "nationality":"",
    "address":"",
    "country_of_destination":"",
    "license_valid":""
}

PERMIT_REQUEST = {
  "document_type": "work_permit_request",
  "company": {
    "name": "",
    "reference_number": "",
    "date": ""
  },
  "recipient": {
    "organization": "",
    "city": ""
  },
  "subject": "",
  "project": {
    "contract_reference": "",
    "description": ""
  },
  "employees": [
    {
      "full_name": "",
      "passport_number": "",
      "nationality": "",
      "position": ""
    }
  ],
  "request_statement": "",
  "signatory": {
    "name": "",
    "position": ""
  }
}

GENERAL_SCHEMA = {
  "document_type": "",
  "metadata": {},
  "entities": {},
  "dates": {},
  "identifiers": {},
  "table_data": [],
  "signatories": [],
  "raw_text": ""
}
