import re

from dateutil import parser


def normalize_member_id(member_id: str) -> str:

    if not member_id:
        return ""

    member_id = member_id.strip().upper()

    member_id = (
        member_id
        .replace("MEMBER", "")
        .replace("MEM", "")
        .replace("-", "")
        .replace("_", "")
        .replace(" ", "")
    )

    digits = "".join(
        filter(str.isdigit, member_id)
    )

    if not digits:
        return ""

    return f"MEM{digits.zfill(4)}"


def normalize_date(date_value: str) -> str:

    if not date_value:
        return ""

    try:

        parsed = parser.parse(
            date_value,
            dayfirst=True
        )

        return parsed.strftime("%Y-%m-%d")

    except Exception:

        return ""


def normalize_zip(zip_code: str) -> str:

    if not zip_code:
        return ""

    digits = re.sub(
        r"\D",
        "",
        zip_code
    )

    if len(digits) >= 5:
        return digits[:5]

    return digits


def normalize_ssn(ssn: str) -> str:

    if not ssn:
        return ""

    digits = re.sub(
        r"\D",
        "",
        ssn
    )

    if len(digits) >= 4:
        return digits[-4:]

    return digits


def normalize_provider(provider: str) -> str:

    if not provider:
        return ""

    return " ".join(
        provider.strip().title().split()
    )


def normalize_claim_type(claim_type: str) -> str:

    if not claim_type:
        return ""

    mapping = {
        "medical": "Medical",
        "dental": "Dental",
        "vision": "Vision",
        "pharmacy": "Pharmacy",
        "mental health": "Mental Health",
        "behavioral health": "Behavioral Health"
    }

    value = claim_type.strip().lower()

    return mapping.get(
        value,
        claim_type.strip().title()
    )


def normalize_city(city: str) -> str:

    if not city:
        return ""

    return city.strip().title()


def normalize_state(state: str) -> str:

    if not state:
        return ""

    return state.strip().upper()


def normalize_npi(npi: str) -> str:

    if not npi:
        return ""

    return re.sub(
        r"\D",
        "",
        npi
    )


def normalize_policy_number(policy_number: str) -> str:

    if not policy_number:
        return ""

    return (
        policy_number
        .strip()
        .upper()
        .replace("-", "")
        .replace(" ", "")
    )