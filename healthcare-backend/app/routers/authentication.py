from fastapi import APIRouter

from app.models.request_models import AuthenticationRequest
from app.services.firestore_service import FirestoreService

from app.utils.normalizers import (
    normalize_member_id,
    normalize_date,
    normalize_zip,
    normalize_ssn
)

from app.utils.validators import (
    validate_member_id,
    validate_date,
    validate_past_date,
    validate_zip,
    validate_ssn
)

router = APIRouter(
    prefix="/authentication",
    tags=["Authentication"]
)


@router.post(
    "/",
    summary="Authenticate Member",
    description="Authenticates a healthcare member using Member ID, DOB, ZIP Code and Last 4 SSN."
)
def authenticate(request: AuthenticationRequest):

    member_id = normalize_member_id(request.memberId)
    dob = normalize_date(request.dob)
    zip_code = normalize_zip(request.zipCode)
    ssn = normalize_ssn(request.last4SSN)

    if not validate_member_id(member_id):
        return {
            "success": False,
            "code": "INVALID_MEMBER_ID",
            "message": "Invalid Member ID."
        }

    if not validate_date(dob):
        return {
            "success": False,
            "code": "INVALID_DOB",
            "message": "Invalid Date of Birth."
        }

    if not validate_past_date(dob):
        return {
            "success": False,
            "code": "INVALID_DOB",
            "message": "Date of Birth cannot be today or a future date. Please provide a correct date of birth."
        }

    if not validate_zip(zip_code):
        return {
            "success": False,
            "code": "INVALID_ZIP",
            "message": "Invalid ZIP Code."
        }

    if not validate_ssn(ssn):
        return {
            "success": False,
            "code": "INVALID_SSN",
            "message": "Invalid Last 4 SSN."
        }

    member = FirestoreService.get_member(member_id)

    if not member:
        return {
            "success": False,
            "code": "MEMBER_NOT_FOUND",
            "message": "Member not found."
        }

    if (
        member.get("dob") != dob or
        member.get("zipCode") != zip_code or
        member.get("last4SSN") != ssn
    ):
        return {
            "success": False,
            "code": "AUTHENTICATION_FAILED",
            "message": "Authentication failed. Please verify your details."
        }

    return {
        "success": True,
        "code": "AUTHENTICATED",
        "message": "Authentication successful.",
        "data": {
            "memberId": member.get("memberId"),
            "memberName": member.get("memberName"),
            "plan": member.get("plan"),
            "policyNumber": member.get("policyNumber"),
            "email": member.get("email"),
            "phone": member.get("phone")
        }
    }


@router.get(
    "/member/{member_id}",
    summary="Verify Member",
    description="Verifies whether a member exists."
)
def verify_member(member_id: str):

    member_id = normalize_member_id(member_id)

    if not validate_member_id(member_id):
        return {
            "success": False,
            "code": "INVALID_MEMBER_ID",
            "message": "Invalid Member ID."
        }

    member = FirestoreService.get_member(member_id)

    if not member:
        return {
            "success": False,
            "code": "MEMBER_NOT_FOUND",
            "message": "Member not found."
        }

    return {
        "success": True,
        "code": "SUCCESS",
        "message": "Member verified successfully.",
        "data": {
            "memberId": member.get("memberId"),
            "memberName": member.get("memberName"),
            "plan": member.get("plan"),
            "policyNumber": member.get("policyNumber")
        }
    }