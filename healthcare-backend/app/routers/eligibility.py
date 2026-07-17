from fastapi import APIRouter, HTTPException, Path

from app.models.request_models import EligibilityRequest
from app.services.firestore_service import FirestoreService

from app.utils.normalizers import normalize_member_id
from app.utils.validators import validate_member_id

router = APIRouter(
    prefix="/eligibility",
    tags=["Eligibility"]
)


@router.post(
    "/",
    summary="Check Eligibility",
    description="Checks member eligibility using Member ID."
)
def check_eligibility(request: EligibilityRequest):

    member_id = normalize_member_id(request.memberId)

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

    eligibility = FirestoreService.get_eligibility(member_id)

    if not eligibility:
        return {
            "success": False,
            "code": "ELIGIBILITY_NOT_FOUND",
            "message": "Eligibility information not found."
        }

    return {
        "success": True,
        "code": "SUCCESS",
        "message": "Eligibility retrieved successfully.",
        "data": eligibility
    }


@router.get(
    "/{member_id}",
    summary="Get Eligibility",
    description="Returns eligibility details using Member ID."
)
def get_eligibility(member_id: str = Path(...)):

    member_id = normalize_member_id(member_id)

    if not validate_member_id(member_id):
        raise HTTPException(
            status_code=400,
            detail="Invalid Member ID."
        )

    member = FirestoreService.get_member(member_id)

    if not member:
        raise HTTPException(
            status_code=404,
            detail="Member not found."
        )

    eligibility = FirestoreService.get_eligibility(member_id)

    if not eligibility:
        raise HTTPException(
            status_code=404,
            detail="Eligibility not found."
        )

    return {
        "success": True,
        "code": "SUCCESS",
        "message": "Eligibility retrieved successfully.",
        "data": eligibility
    }