from google.cloud import firestore
from datetime import datetime

db = firestore.Client()

CURRENT_TIME = datetime.utcnow().isoformat() + "Z"


def seed_document(collection_name, document_id, data):
    db.collection(collection_name).document(document_id).set(data)
    print(f"Inserted {collection_name}/{document_id}")


MEMBERS_DATA = [

# ===========================
# MEMBER 1
# ===========================

{
    "member": {
        "memberId": "MEM1001",
        "memberName": "John Smith",
        "dob": "1985-04-15",
        "zipCode": "10001",
        "last4SSN": "1234",
        "plan": "Gold Plus",
        "policyNumber": "POL100001",
        "email": "john.smith@email.com",
        "phone": "+1-212-555-1001",
        "createdAt": CURRENT_TIME,
        "updatedAt": CURRENT_TIME
    },

    "claim": {
        "claimId": "CLM1001",
        "memberId": "MEM1001",
        "claimType": "Medical",
        "status": "Under Review",
        "provider": "City Medical Center",
        "submittedDate": "2026-06-20",
        "serviceDate": "2026-06-18",
        "amount": 320,
        "diagnosisCode": "I10",
        "message": "Claim under review."
    },

    "eligibility": {
        "memberId": "MEM1001",
        "status": "Active",
        "effectiveDate": "2025-01-01",
        "expirationDate": "2027-12-31"
    },

    "benefits": {
        "memberId": "MEM1001",
        "medical": "Covered",
        "dental": "Covered",
        "vision": "Covered",
        "copay": 20,
        "deductible": 500,
        "outOfPocket": 3000
    },

    "provider": {
        "providerId": "PR1001",
        "memberId": "MEM1001",
        "providerName": "City Medical Center",
        "providerNameLower": "city medical center",
        "speciality": "Primary Care",
        "officeHours": "Mon-Fri 09:00 AM - 05:00 PM",
        "acceptingNewPatients": True,
        "email": "contact@citymedical.com",
        "website": "https://citymedical.com",
        "npi": "1234567893",
        "address": "123 Main Street",
        "city": "New York",
        "state": "NY",
        "zipCode": "10001",
        "phone": "+1-212-555-7001",
        "distance": "2.5 miles",
        "network": "In Network"
    },

    "preAuthorization": {
        "authorizationId": "PA10001",
        "memberId": "MEM1001",
        "status": "Approved",
        "service": "MRI Scan",
        "procedureCode": "70551",
        "validUntil": "2027-01-15"
    },

    "policy": {
        "memberId": "MEM1001",
        "policyNumber": "POL100001",
        "plan": "Gold Plus",
        "medical": "Covered",
        "dental": "Covered",
        "vision": "Covered",
        "copay": 20,
        "deductible": 500,
        "outOfPocket": 3000,
        "effectiveDate": "2025-01-01",
        "expirationDate": "2027-12-31"
    }
},

# ===========================
# MEMBER 2
# ===========================

{
    "member": {
        "memberId": "MEM1002",
        "memberName": "Emily Johnson",
        "dob": "1990-08-22",
        "zipCode": "60601",
        "last4SSN": "5678",
        "plan": "Silver Care",
        "policyNumber": "POL100002",
        "email": "emily.johnson@email.com",
        "phone": "+1-312-555-1002",
        "createdAt": CURRENT_TIME,
        "updatedAt": CURRENT_TIME
    },

    "claim": {
        "claimId": "CLM1002",
        "memberId": "MEM1002",
        "claimType": "Dental",
        "status": "Approved",
        "provider": "Bright Smile Dental",
        "submittedDate": "2026-06-10",
        "serviceDate": "2026-06-08",
        "amount": 180,
        "diagnosisCode": "K02.9",
        "message": "Claim approved."
    },

    "eligibility": {
        "memberId": "MEM1002",
        "status": "Active",
        "effectiveDate": "2025-01-01",
        "expirationDate": "2027-12-31"
    },

    "benefits": {
        "memberId": "MEM1002",
        "medical": "Covered",
        "dental": "Covered",
        "vision": "Not Covered",
        "copay": 15,
        "deductible": 300,
        "outOfPocket": 2500
    },

    "provider": {
        "providerId": "PR1002",
        "memberId": "MEM1002",
        "providerName": "Bright Smile Dental",
        "providerNameLower": "bright smile dental",
        "speciality": "Dentistry",
        "officeHours": "Mon-Sat 08:30 AM - 06:00 PM",
        "acceptingNewPatients": True,
        "email": "contact@brightsmile.com",
        "website": "https://brightsmile.com",
        "npi": "1234567894",
        "address": "220 Lake Street",
        "city": "Chicago",
        "state": "IL",
        "zipCode": "60601",
        "phone": "+1-312-555-7002",
        "distance": "1.2 miles",
        "network": "In Network"
    },

    "preAuthorization": {
        "authorizationId": "PA10002",
        "memberId": "MEM1002",
        "status": "Not Required",
        "service": "Dental Cleaning",
        "procedureCode": "D1110",
        "validUntil": "-"
    },

    "policy": {
        "memberId": "MEM1002",
        "policyNumber": "POL100002",
        "plan": "Silver Care",
        "medical": "Covered",
        "dental": "Covered",
        "vision": "Not Covered",
        "copay": 15,
        "deductible": 300,
        "outOfPocket": 2500,
        "effectiveDate": "2025-01-01",
        "expirationDate": "2027-12-31"
    }
},
# ===========================
# MEMBER 3
# ===========================

{
    "member": {
        "memberId": "MEM1003",
        "memberName": "Michael Brown",
        "dob": "1982-12-10",
        "zipCode": "77001",
        "last4SSN": "9012",
        "plan": "Family Health",
        "policyNumber": "POL100003",
        "email": "michael.brown@email.com",
        "phone": "+1-713-555-1003",
        "createdAt": CURRENT_TIME,
        "updatedAt": CURRENT_TIME
    },

    "claim": {
        "claimId": "CLM1003",
        "memberId": "MEM1003",
        "claimType": "Vision",
        "status": "Rejected",
        "provider": "Clear Vision Optometry",
        "submittedDate": "2026-06-12",
        "serviceDate": "2026-06-10",
        "amount": 210,
        "diagnosisCode": "H52.4",
        "message": "Claim rejected. Appeal can be submitted within 60 days."
    },

    "eligibility": {
        "memberId": "MEM1003",
        "status": "Active",
        "effectiveDate": "2025-01-01",
        "expirationDate": "2027-12-31"
    },

    "benefits": {
        "memberId": "MEM1003",
        "medical": "Covered",
        "dental": "Covered",
        "vision": "Covered",
        "copay": 30,
        "deductible": 700,
        "outOfPocket": 5000
    },

    "provider": {
        "providerId": "PR1003",
        "memberId": "MEM1003",
        "providerName": "Clear Vision Optometry",
        "providerNameLower": "clear vision optometry",
        "speciality": "Optometry",
        "officeHours": "Mon-Fri 09:00 AM - 04:30 PM",
        "acceptingNewPatients": False,
        "email": "info@clearvision.com",
        "website": "https://clearvision.com",
        "npi": "1234567895",
        "address": "400 West Street",
        "city": "Houston",
        "state": "TX",
        "zipCode": "77001",
        "phone": "+1-713-555-7003",
        "distance": "3.8 miles",
        "network": "In Network"
    },

    "preAuthorization": {
        "authorizationId": "PA10003",
        "memberId": "MEM1003",
        "status": "Pending",
        "service": "Eye Surgery",
        "procedureCode": "66984",
        "validUntil": "-"
    },

    "policy": {
        "memberId": "MEM1003",
        "policyNumber": "POL100003",
        "plan": "Family Health",
        "medical": "Covered",
        "dental": "Covered",
        "vision": "Covered",
        "copay": 30,
        "deductible": 700,
        "outOfPocket": 5000,
        "effectiveDate": "2025-01-01",
        "expirationDate": "2027-12-31"
    }
},

# ===========================
# MEMBER 4
# ===========================

{
    "member": {
        "memberId": "MEM1004",
        "memberName": "Sarah Davis",
        "dob": "1995-06-05",
        "zipCode": "90001",
        "last4SSN": "3456",
        "plan": "Basic Care",
        "policyNumber": "POL100004",
        "email": "sarah.davis@email.com",
        "phone": "+1-310-555-1004",
        "createdAt": CURRENT_TIME,
        "updatedAt": CURRENT_TIME
    },

    "claim": {
        "claimId": "CLM1004",
        "memberId": "MEM1004",
        "claimType": "Medical",
        "status": "Processing",
        "provider": "Westside Family Clinic",
        "submittedDate": "2026-06-18",
        "serviceDate": "2026-06-17",
        "amount": 450,
        "diagnosisCode": "M54.5",
        "message": "Claim is currently being processed."
    },

    "eligibility": {
        "memberId": "MEM1004",
        "status": "Active",
        "effectiveDate": "2025-01-01",
        "expirationDate": "2027-12-31"
    },

    "benefits": {
        "memberId": "MEM1004",
        "medical": "Covered",
        "dental": "Not Covered",
        "vision": "Covered",
        "copay": 25,
        "deductible": 600,
        "outOfPocket": 4000
    },

    "provider": {
        "providerId": "PR1004",
        "memberId": "MEM1004",
        "providerName": "Westside Family Clinic",
        "providerNameLower": "westside family clinic",
        "speciality": "Family Medicine",
        "officeHours": "Mon-Fri 08:00 AM - 05:00 PM",
        "acceptingNewPatients": True,
        "email": "hello@westsideclinic.com",
        "website": "https://westsideclinic.com",
        "npi": "1234567896",
        "address": "80 Sunset Blvd",
        "city": "Los Angeles",
        "state": "CA",
        "zipCode": "90001",
        "phone": "+1-310-555-7004",
        "distance": "5.1 miles",
        "network": "In Network"
    },

    "preAuthorization": {
        "authorizationId": "PA10004",
        "memberId": "MEM1004",
        "status": "Approved",
        "service": "CT Scan",
        "procedureCode": "70450",
        "validUntil": "2027-02-10"
    },

    "policy": {
        "memberId": "MEM1004",
        "policyNumber": "POL100004",
        "plan": "Basic Care",
        "medical": "Covered",
        "dental": "Not Covered",
        "vision": "Covered",
        "copay": 25,
        "deductible": 600,
        "outOfPocket": 4000,
        "effectiveDate": "2025-01-01",
        "expirationDate": "2027-12-31"
    }
},
# ===========================
# MEMBER 5
# ===========================

{
    "member": {
        "memberId": "MEM1005",
        "memberName": "David Wilson",
        "dob": "1988-09-18",
        "zipCode": "33101",
        "last4SSN": "7890",
        "plan": "Premium Plus",
        "policyNumber": "POL100005",
        "email": "david.wilson@email.com",
        "phone": "+1-305-555-1005",
        "createdAt": CURRENT_TIME,
        "updatedAt": CURRENT_TIME
    },

    "claim": {
        "claimId": "CLM1005",
        "memberId": "MEM1005",
        "claimType": "Pharmacy",
        "status": "Paid",
        "provider": "MedPlus Pharmacy",
        "submittedDate": "2026-06-08",
        "serviceDate": "2026-06-08",
        "amount": 95,
        "diagnosisCode": "E11.9",
        "message": "Claim paid successfully."
    },

    "eligibility": {
        "memberId": "MEM1005",
        "status": "Active",
        "effectiveDate": "2025-01-01",
        "expirationDate": "2027-12-31"
    },

    "benefits": {
        "memberId": "MEM1005",
        "medical": "Covered",
        "dental": "Covered",
        "vision": "Covered",
        "copay": 10,
        "deductible": 250,
        "outOfPocket": 2000
    },

    "provider": {
        "providerId": "PR1005",
        "memberId": "MEM1005",
        "providerName": "MedPlus Pharmacy",
        "providerNameLower": "medplus pharmacy",
        "speciality": "Pharmacy",
        "officeHours": "Daily 09:00 AM - 09:00 PM",
        "acceptingNewPatients": True,
        "email": "support@medplus.com",
        "website": "https://medplus.com",
        "npi": "1234567897",
        "address": "12 Ocean Drive",
        "city": "Miami",
        "state": "FL",
        "zipCode": "33101",
        "phone": "+1-305-555-7005",
        "distance": "0.8 miles",
        "network": "In Network"
    },

    "preAuthorization": {
        "authorizationId": "PA10005",
        "memberId": "MEM1005",
        "status": "Approved",
        "service": "Specialty Medication",
        "procedureCode": "J3490",
        "validUntil": "2027-12-31"
    },

    "policy": {
        "memberId": "MEM1005",
        "policyNumber": "POL100005",
        "plan": "Premium Plus",
        "medical": "Covered",
        "dental": "Covered",
        "vision": "Covered",
        "copay": 10,
        "deductible": 250,
        "outOfPocket": 2000,
        "effectiveDate": "2025-01-01",
        "expirationDate": "2027-12-31"
    }
},

# ===========================
# MEMBER 6
# ===========================

{
    "member": {
        "memberId": "MEM1006",
        "memberName": "Olivia Martinez",
        "dob": "1992-03-11",
        "zipCode": "85001",
        "last4SSN": "1122",
        "plan": "Gold Plus",
        "policyNumber": "POL100006",
        "email": "olivia.martinez@email.com",
        "phone": "+1-602-555-1006",
        "createdAt": CURRENT_TIME,
        "updatedAt": CURRENT_TIME
    },

    "claim": {
        "claimId": "CLM1006",
        "memberId": "MEM1006",
        "claimType": "Medical",
        "status": "Submitted",
        "provider": "Phoenix Heart Center",
        "submittedDate": "2026-06-25",
        "serviceDate": "2026-06-24",
        "amount": 640,
        "diagnosisCode": "I25.10",
        "message": "Claim submitted successfully."
    },

    "eligibility": {
        "memberId": "MEM1006",
        "status": "Active",
        "effectiveDate": "2025-01-01",
        "expirationDate": "2027-12-31"
    },

    "benefits": {
        "memberId": "MEM1006",
        "medical": "Covered",
        "dental": "Covered",
        "vision": "Covered",
        "copay": 20,
        "deductible": 500,
        "outOfPocket": 3500
    },

    "provider": {
        "providerId": "PR1006",
        "memberId": "MEM1006",
        "providerName": "Phoenix Heart Center",
        "providerNameLower": "phoenix heart center",
        "speciality": "Cardiology",
        "officeHours": "Mon-Fri 08:00 AM - 05:00 PM",
        "acceptingNewPatients": True,
        "email": "info@phoenixheart.com",
        "website": "https://phoenixheart.com",
        "npi": "1234567898",
        "address": "101 Central Ave",
        "city": "Phoenix",
        "state": "AZ",
        "zipCode": "85001",
        "phone": "+1-602-555-7006",
        "distance": "2.1 miles",
        "network": "In Network"
    },

    "preAuthorization": {
        "authorizationId": "PA10006",
        "memberId": "MEM1006",
        "status": "Pending",
        "service": "Cardiac Stress Test",
        "procedureCode": "93017",
        "validUntil": "-"
    },

    "policy": {
        "memberId": "MEM1006",
        "policyNumber": "POL100006",
        "plan": "Gold Plus",
        "medical": "Covered",
        "dental": "Covered",
        "vision": "Covered",
        "copay": 20,
        "deductible": 500,
        "outOfPocket": 3500,
        "effectiveDate": "2025-01-01",
        "expirationDate": "2027-12-31"
    }
},
# ===========================
# MEMBER 7
# ===========================

{
    "member": {
        "memberId": "MEM1007",
        "memberName": "James Anderson",
        "dob": "1979-11-02",
        "zipCode": "98101",
        "last4SSN": "4455",
        "plan": "Silver Care",
        "policyNumber": "POL100007",
        "email": "james.anderson@email.com",
        "phone": "+1-206-555-1007",
        "createdAt": CURRENT_TIME,
        "updatedAt": CURRENT_TIME
    },

    "claim": {
        "claimId": "CLM1007",
        "memberId": "MEM1007",
        "claimType": "Medical",
        "status": "Approved",
        "provider": "Seattle Orthopedic Center",
        "submittedDate": "2026-06-15",
        "serviceDate": "2026-06-14",
        "amount": 780,
        "diagnosisCode": "M17.11",
        "message": "Claim approved successfully."
    },

    "eligibility": {
        "memberId": "MEM1007",
        "status": "Active",
        "effectiveDate": "2025-01-01",
        "expirationDate": "2027-12-31"
    },

    "benefits": {
        "memberId": "MEM1007",
        "medical": "Covered",
        "dental": "Covered",
        "vision": "Covered",
        "copay": 20,
        "deductible": 450,
        "outOfPocket": 3200
    },

    "provider": {
        "providerId": "PR1007",
        "memberId": "MEM1007",
        "providerName": "Seattle Orthopedic Center",
        "providerNameLower": "seattle orthopedic center",
        "speciality": "Orthopedics",
        "officeHours": "Mon-Fri 08:00 AM - 05:00 PM",
        "acceptingNewPatients": True,
        "email": "info@seattleortho.com",
        "website": "https://seattleortho.com",
        "npi": "1234567899",
        "address": "450 Pine Street",
        "city": "Seattle",
        "state": "WA",
        "zipCode": "98101",
        "phone": "+1-206-555-7007",
        "distance": "2.0 miles",
        "network": "In Network"
    },

    "preAuthorization": {
        "authorizationId": "PA10007",
        "memberId": "MEM1007",
        "status": "Approved",
        "service": "Knee Replacement",
        "procedureCode": "27447",
        "validUntil": "2027-03-31"
    },

    "policy": {
        "memberId": "MEM1007",
        "policyNumber": "POL100007",
        "plan": "Silver Care",
        "medical": "Covered",
        "dental": "Covered",
        "vision": "Covered",
        "copay": 20,
        "deductible": 450,
        "outOfPocket": 3200,
        "effectiveDate": "2025-01-01",
        "expirationDate": "2027-12-31"
    }
},

# ===========================
# MEMBER 8
# ===========================

{
    "member": {
        "memberId": "MEM1008",
        "memberName": "Sophia Taylor",
        "dob": "1993-01-19",
        "zipCode": "19103",
        "last4SSN": "6677",
        "plan": "Premium Plus",
        "policyNumber": "POL100008",
        "email": "sophia.taylor@email.com",
        "phone": "+1-215-555-1008",
        "createdAt": CURRENT_TIME,
        "updatedAt": CURRENT_TIME
    },

    "claim": {
        "claimId": "CLM1008",
        "memberId": "MEM1008",
        "claimType": "Medical",
        "status": "Under Review",
        "provider": "Philadelphia Neuro Clinic",
        "submittedDate": "2026-06-22",
        "serviceDate": "2026-06-20",
        "amount": 1250,
        "diagnosisCode": "G43.909",
        "message": "Claim is under medical review."
    },

    "eligibility": {
        "memberId": "MEM1008",
        "status": "Active",
        "effectiveDate": "2025-01-01",
        "expirationDate": "2027-12-31"
    },

    "benefits": {
        "memberId": "MEM1008",
        "medical": "Covered",
        "dental": "Covered",
        "vision": "Covered",
        "copay": 15,
        "deductible": 200,
        "outOfPocket": 1800
    },

    "provider": {
        "providerId": "PR1008",
        "memberId": "MEM1008",
        "providerName": "Philadelphia Neuro Clinic",
        "providerNameLower": "philadelphia neuro clinic",
        "speciality": "Neurology",
        "officeHours": "Mon-Fri 09:00 AM - 05:00 PM",
        "acceptingNewPatients": True,
        "email": "support@phillyneuro.com",
        "website": "https://phillyneuro.com",
        "npi": "1234567900",
        "address": "250 Market Street",
        "city": "Philadelphia",
        "state": "PA",
        "zipCode": "19103",
        "phone": "+1-215-555-7008",
        "distance": "1.4 miles",
        "network": "In Network"
    },

    "preAuthorization": {
        "authorizationId": "PA10008",
        "memberId": "MEM1008",
        "status": "Pending",
        "service": "Brain MRI",
        "procedureCode": "70553",
        "validUntil": "-"
    },

    "policy": {
        "memberId": "MEM1008",
        "policyNumber": "POL100008",
        "plan": "Premium Plus",
        "medical": "Covered",
        "dental": "Covered",
        "vision": "Covered",
        "copay": 15,
        "deductible": 200,
        "outOfPocket": 1800,
        "effectiveDate": "2025-01-01",
        "expirationDate": "2027-12-31"
    }
},

{
    "member": {
        "memberId": "MEM1009",
        "memberName": "William Thomas",
        "dob": "1987-07-28",
        "zipCode": "30301",
        "last4SSN": "8899",
        "plan": "Family Health",
        "policyNumber": "POL100009",
        "email": "william.thomas@email.com",
        "phone": "+1-404-555-1009",
        "createdAt": CURRENT_TIME,
        "updatedAt": CURRENT_TIME
    },

    "claim": {
        "claimId": "CLM1009",
        "memberId": "MEM1009",
        "claimType": "Medical",
        "status": "Processing",
        "provider": "Atlanta Skin Clinic",
        "submittedDate": "2026-06-21",
        "serviceDate": "2026-06-20",
        "amount": 350,
        "diagnosisCode": "L20.9",
        "message": "Claim is currently being processed."
    },

    "eligibility": {
        "memberId": "MEM1009",
        "status": "Active",
        "effectiveDate": "2025-01-01",
        "expirationDate": "2027-12-31"
    },

    "benefits": {
        "memberId": "MEM1009",
        "medical": "Covered",
        "dental": "Covered",
        "vision": "Covered",
        "copay": 25,
        "deductible": 600,
        "outOfPocket": 4000
    },

    "provider": {
        "providerId": "PR1009",
        "memberId": "MEM1009",
        "providerName": "Atlanta Skin Clinic",
        "providerNameLower": "atlanta skin clinic",
        "speciality": "Dermatology",
        "officeHours": "Mon-Fri 09:00 AM - 05:00 PM",
        "acceptingNewPatients": True,
        "email": "contact@atlantaskin.com",
        "website": "https://atlantaskin.com",
        "npi": "1234567901",
        "address": "890 Peach Street",
        "city": "Atlanta",
        "state": "GA",
        "zipCode": "30301",
        "phone": "+1-404-555-7009",
        "distance": "1.8 miles",
        "network": "In Network"
    },

    "preAuthorization": {
        "authorizationId": "PA10009",
        "memberId": "MEM1009",
        "status": "Approved",
        "service": "Skin Biopsy",
        "procedureCode": "11102",
        "validUntil": "2027-05-15"
    },

    "policy": {
        "memberId": "MEM1009",
        "policyNumber": "POL100009",
        "plan": "Family Health",
        "medical": "Covered",
        "dental": "Covered",
        "vision": "Covered",
        "copay": 25,
        "deductible": 600,
        "outOfPocket": 4000,
        "effectiveDate": "2025-01-01",
        "expirationDate": "2027-12-31"
    }
},

{
    "member": {
        "memberId": "MEM1010",
        "memberName": "Emma Harris",
        "dob": "1998-02-14",
        "zipCode": "75201",
        "last4SSN": "2468",
        "plan": "Basic Care",
        "policyNumber": "POL100010",
        "email": "emma.harris@email.com",
        "phone": "+1-214-555-1010",
        "createdAt": CURRENT_TIME,
        "updatedAt": CURRENT_TIME
    },

    "claim": {
        "claimId": "CLM1010",
        "memberId": "MEM1010",
        "claimType": "Medical",
        "status": "Approved",
        "provider": "Dallas Children's Hospital",
        "submittedDate": "2026-06-11",
        "serviceDate": "2026-06-09",
        "amount": 520,
        "diagnosisCode": "J06.9",
        "message": "Claim approved successfully."
    },

    "eligibility": {
        "memberId": "MEM1010",
        "status": "Active",
        "effectiveDate": "2025-01-01",
        "expirationDate": "2027-12-31"
    },

    "benefits": {
        "memberId": "MEM1010",
        "medical": "Covered",
        "dental": "Covered",
        "vision": "Covered",
        "copay": 30,
        "deductible": 700,
        "outOfPocket": 5000
    },

    "provider": {
        "providerId": "PR1010",
        "memberId": "MEM1010",
        "providerName": "Dallas Children's Hospital",
        "providerNameLower": "dallas children's hospital",
        "speciality": "Pediatrics",
        "officeHours": "24 Hours",
        "acceptingNewPatients": True,
        "email": "info@dallaschildrens.com",
        "website": "https://dallaschildrens.com",
        "npi": "1234567902",
        "address": "1200 Elm Street",
        "city": "Dallas",
        "state": "TX",
        "zipCode": "75201",
        "phone": "+1-214-555-7010",
        "distance": "3.2 miles",
        "network": "In Network"
    },

    "preAuthorization": {
        "authorizationId": "PA10010",
        "memberId": "MEM1010",
        "status": "Not Required",
        "service": "Emergency Consultation",
        "procedureCode": "99284",
        "validUntil": "-"
    },

    "policy": {
        "memberId": "MEM1010",
        "policyNumber": "POL100010",
        "plan": "Basic Care",
        "medical": "Covered",
        "dental": "Covered",
        "vision": "Covered",
        "copay": 30,
        "deductible": 700,
        "outOfPocket": 5000,
        "effectiveDate": "2025-01-01",
        "expirationDate": "2027-12-31"
    }
},
]
def seed_members():

    for item in MEMBERS_DATA:
        seed_document(
            "members",
            item["member"]["memberId"],
            item["member"]
        )


def seed_claims():

    for item in MEMBERS_DATA:
        seed_document(
            "claims",
            item["claim"]["claimId"],
            item["claim"]
        )


def seed_eligibility():

    for item in MEMBERS_DATA:
        seed_document(
            "eligibility",
            item["eligibility"]["memberId"],
            item["eligibility"]
        )


def seed_benefits():

    for item in MEMBERS_DATA:
        seed_document(
            "benefits",
            item["benefits"]["memberId"],
            item["benefits"]
        )


def seed_providers():

    for item in MEMBERS_DATA:
        seed_document(
            "providers",
            item["provider"]["providerId"],
            item["provider"]
        )


def seed_preauthorizations():

    for item in MEMBERS_DATA:
        seed_document(
            "preauthorizations",
            item["preAuthorization"]["authorizationId"],
            item["preAuthorization"]
        )


def seed_policies():

    for item in MEMBERS_DATA:
        seed_document(
            "policies",
            item["policy"]["memberId"],
            item["policy"]
        )


def main():

    print("=" * 50)
    print("Healthcare Firestore Seeding Started")
    print("=" * 50)

    seed_members()
    print("Members Seeded")

    seed_claims()
    print("Claims Seeded")

    seed_eligibility()
    print("Eligibility Seeded")

    seed_benefits()
    print("Benefits Seeded")

    seed_providers()
    print("Providers Seeded")

    seed_preauthorizations()
    print("Preauthorizations Seeded")

    seed_policies()
    print("Policies Seeded")

    print("=" * 50)
    print("Healthcare Firestore Database Seeded Successfully")
    print("=" * 50)


if __name__ == "__main__":
    main()