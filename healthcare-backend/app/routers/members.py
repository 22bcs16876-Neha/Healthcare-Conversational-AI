from fastapi import APIRouter, HTTPException, Path

from app.services.firestore_service import FirestoreService

from app.utils.normalizers import normalize_member_id
from app.utils.validators import validate_member_id

router = APIRouter(
    prefix="/member",
    tags=["Member"]
)


@router.get(
    "/{member_id}",
    summary="Get Member Details",
    description="Returns member profile information using Member ID."
)
def get_member_details(
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

    return {
        "success": True,
        "code": "SUCCESS",
        "message": "Member details retrieved successfully.",
        "data": {
            "memberId": member.get("memberId"),
            "memberName": member.get("memberName"),
            "policyNumber": member.get("policyNumber"),
            "plan": member.get("plan"),
            "email": member.get("email"),
            "phone": member.get("phone"),
            "dob": member.get("dob"),
            "zipCode": member.get("zipCode"),
            "createdAt": member.get("createdAt"),
            "updatedAt": member.get("updatedAt")
        }
    }


@router.get(
    "/",
    summary="Get All Members",
    description="Returns all registered members."
)
def get_all_members():

    members = FirestoreService.get_all_members()

    return {
        "success": True,
        "code": "SUCCESS",
        "message": "Members retrieved successfully.",
        "count": len(members),
        "data": members
    }