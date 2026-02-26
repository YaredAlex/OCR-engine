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
  "given_names": "//given name(s), surname, name, fullname",
  "surname": "",
  "date_of_birth": "",
  "gender": "",
  "nationality": "",
  "place_of_birth": "",
  "issue_date": "",
  "expiry_date": "",
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
EXPERIENCE_SCHEMA = {
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

EDUCATION_SCHEMA = {
  "institution_name": "",
  "student_name": "",
  "degree": "",
  "degree_classification": "",
  "date_of_award": "",
  "certificate_number": "",
  "signatories": [
    {
      "name": "",
      "position": ""
    },
    {
      "name": "",
      "position": ""
    }
  ],
  "document_authentication": {
    "notary_name": "",
    "notary_office": "",
    "authentication_date": "",
    "seal_verified": "",
  }
}

CLEARANCE_SCHEMA = {
  "document_type": "work_permit_cancellation_request",
  "letter_metadata": {
    "reference_number": "",
    "date": "",
    "subject": "",
    "recipient_organization": "",
    "recipient_location": ""
  },
  "requesting_organization": {
    "organization_name": "",
    "parent_organization": "",
    "branch_name": "",
    "organization_type": "",
    "address": "",
    "email": ""
  },
  "request_details": {
    "request_type": "work_permit_cancellation",
    "reason": "",
    "description": ""
  },
  "employees": [
    {
      "full_name": "",
      "first_name": "",
      "last_name": "",
      "passport_number": "",
      "nationality": "",
      "position": "",
      "gender": ""
    }
  ],
  "signatory": {
    "name": "",
    "position": "",
    "department": ""
  },
  "additional_information": {
    "attachments": "",
    "notes": ""
  }
}

DELEGATION_SCHEMA= {
  "document_type": "administrative_power_of_attorney",
  "document_metadata": {
    "document_number": "",
    "registration_number": "",
    "date_of_issue": "",
    "issuing_authority": "",
    "place_of_issue": ""
  },
  "principal": {
    "full_name": "",
    "represented_organization": "",
    "nationality": "",
    "passport_number": "",
    "address": {
      "city": "",
      "sub_city": "",
      "woreda": "",
      "house_number": ""
    }
  },
  "agent": {
    "full_name": "",
    "nationality": "",
    "id_type": "",
    "id_number": "",
    "date_of_birth": "",
    "gender": "",
    "phone_number": "",
    "address": {
      "city": "",
      "sub_city": "",
      "woreda": "",
      "house_number": ""
    }
  },
  "authorization": {
    "authorization_type": "general_administrative_power",
    "authorized_actions": [],
    "applicable_institutions": []
  },
  "legal_basis": {
    "civil_code_articles": [
      "Article 2199",
      "Article 2203"
    ]
  },
  "validity": {
    "effective_date": "",
    "expiry_date": "",
    "revocation_allowed": ""
  },
  "signatures": {
    "principal_signed": "",
    "agent_signed": "",
    "witnessed": ""
  },
  "supporting_documents": {
    "agent_id_attached": "",
    "principal_passport_attached": ""
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
