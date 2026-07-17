from fastapi import APIRouter, HTTPException, Path

from app.models.request_models import BenefitsRequest
from app.services.firestore_service import FirestoreService

from app.utils.normalizers import normalize_member_id
from app.utils.validators import validate_member_id

router = APIRouter(
    prefix="/benefits",
    tags=["Benefits"]
)


@router.post(
    "/",
    summary="Get Member Benefits",
    description="Returns benefits available for an authenticated member."
)
def get_benefits(request: BenefitsRequest):

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

    benefits = FirestoreService.get_benefits(member_id)

    if not benefits:
        return {
            "success": False,
            "code": "BENEFITS_NOT_FOUND",
            "message": "Benefits information not found."
        }

    return {
        "success": True,
        "code": "SUCCESS",
        "message": "Benefits retrieved successfully.",
        "data": benefits
    }


@router.get(
    "/{member_id}",
    summary="Get Benefits",
    description="Returns benefits using Member ID."
)
def get_benefits_by_member(member_id: str = Path(...)):

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

    benefits = FirestoreService.get_benefits(member_id)

    if not benefits:
        raise HTTPException(
            status_code=404,
            detail="Benefits not found."
        )

    return {
        "success": True,
        "code": "SUCCESS",
        "message": "Benefits retrieved successfully.",
        "data": benefits
    }