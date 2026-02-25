ID_SCHEMA = {
    "full_name": "",
    "id_number": "",
    "date_of_birth": "",
    "gender": "",
    "nationality": "",
    "issue_date": "",
    "expiry_date": ""
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
