from fastapi import APIRouter, HTTPException, Path

from app.models.request_models import PreAuthorizationRequest
from app.services.firestore_service import FirestoreService

from app.utils.normalizers import normalize_member_id
from app.utils.validators import validate_member_id

router = APIRouter(
    prefix="/preauthorization",
    tags=["Pre Authorization"]
)


@router.post(
    "/",
    summary="Get Pre-Authorization",
    description="Returns pre-authorization details for an authenticated member."
)
def get_preauthorization(request: PreAuthorizationRequest):

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

    preauth = FirestoreService.get_preauthorization(member_id)

    if not preauth:
        return {
            "success": False,
            "code": "PREAUTHORIZATION_NOT_FOUND",
            "message": "Pre-authorization not found."
        }

    return {
        "success": True,
        "code": "SUCCESS",
        "message": "Pre-authorization retrieved successfully.",
        "data": preauth
    }


@router.get(
    "/{member_id}",
    summary="Get Pre-Authorization",
    description="Returns pre-authorization details using Member ID."
)
def get_preauthorization_by_member(
    member_id: str = Path(...)
):

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

    preauth = FirestoreService.get_preauthorization(member_id)

    if not preauth:
        raise HTTPException(
            status_code=404,
            detail="Pre-authorization not found."
        )

    return {
        "success": True,
        "code": "SUCCESS",
        "message": "Pre-authorization retrieved successfully.",
        "data": preauth
    }