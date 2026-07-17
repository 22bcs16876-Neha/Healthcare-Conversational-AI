import re
from datetime import datetime


VALID_CLAIM_TYPES = {
    "Medical",
    "Dental",
    "Vision",
    "Pharmacy",
    "Mental Health",
    "Behavioral Health"
}


def validate_member_id(member_id: str) -> bool:
    return bool(re.fullmatch(r"MEM\d{4}", member_id))


def validate_date(date_string: str) -> bool:
    try:
        datetime.strptime(date_string, "%Y-%m-%d")
        return True
    except ValueError:
        return False


def validate_zip(zip_code: str) -> bool:
    return bool(re.fullmatch(r"\d{5}", zip_code))


def validate_ssn(ssn: str) -> bool:
    return bool(re.fullmatch(r"\d{4}", ssn))


def validate_claim_type(claim_type: str) -> bool:
    return claim_type in VALID_CLAIM_TYPES


def validate_amount(amount: float) -> bool:
    try:
        return float(amount) > 0
    except Exception:
        return False


def validate_npi(npi: str) -> bool:
    return bool(re.fullmatch(r"\d{10}", npi))


def validate_policy_number(policy_number: str) -> bool:
    return bool(re.fullmatch(r"POL\d{6}", policy_number))


def validate_claim_id(claim_id: str) -> bool:
    return bool(re.fullmatch(r"CLM\d{4,}", claim_id))


def validate_state(state: str) -> bool:
    return bool(re.fullmatch(r"[A-Z]{2}", state))


def validate_email(email: str) -> bool:
    return bool(
        re.fullmatch(r"^[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}$", email)
    )


def validate_phone(phone: str) -> bool:
    digits = re.sub(r"\D", "", phone)
    return len(digits) >= 10


def validate_past_date(date_string: str) -> bool:
    """Date of birth must be a valid date strictly in the past (not today, not future).
    Uses the server's current date, so it is always correct."""
    try:
        d = datetime.strptime(date_string, "%Y-%m-%d").date()
        return d < datetime.utcnow().date()
    except ValueError:
        return False


def validate_not_future_date(date_string: str) -> bool:
    """Service date must be today or in the past (not in the future).
    Uses the server's current date, so it is always correct."""
    try:
        d = datetime.strptime(date_string, "%Y-%m-%d").date()
        return d <= datetime.utcnow().date()
    except ValueError:
        return False