from fastapi import APIRouter, HTTPException, Path

from app.models.request_models import PolicyRequest
from app.services.firestore_service import FirestoreService

from app.utils.normalizers import normalize_member_id
from app.utils.validators import validate_member_id

router = APIRouter(
    prefix="/policy",
    tags=["Policy"]
)


@router.post(
    "/",
    summary="Get Policy Details",
    description="Returns policy details for an authenticated member."
)
def get_policy(request: PolicyRequest):

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

    policy = FirestoreService.get_policy(member_id)

    if not policy:
        return {
            "success": False,
            "code": "POLICY_NOT_FOUND",
            "message": "Policy not found."
        }

    return {
        "success": True,
        "code": "SUCCESS",
        "message": "Policy retrieved successfully.",
        "data": policy
    }


@router.get(
    "/{member_id}",
    summary="Get Policy",
    description="Returns policy information using Member ID."
)
def get_policy_by_member(
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

    policy = FirestoreService.get_policy(member_id)

    if not policy:
        raise HTTPException(
            status_code=404,
            detail="Policy not found."
        )

    return {
        "success": True,
        "code": "SUCCESS",
        "message": "Policy retrieved successfully.",
        "data": {
            "policyNumber": policy.get("policyNumber"),
            "plan": policy.get("plan"),
            "medical": policy.get("medical"),
            "dental": policy.get("dental"),
            "vision": policy.get("vision"),
            "copay": policy.get("copay"),
            "deductible": policy.get("deductible"),
            "outOfPocket": policy.get("outOfPocket"),
            "effectiveDate": policy.get("effectiveDate"),
            "expirationDate": policy.get("expirationDate")
        }
    }


@router.get(
    "/summary/{member_id}",
    summary="Policy Summary",
    description="Returns a summarized view of the member's policy."
)
def get_policy_summary(
    member_id: str = Path(...)
):

    member_id = normalize_member_id(member_id)

    policy = FirestoreService.get_policy(member_id)

    if not policy:
        raise HTTPException(
            status_code=404,
            detail="Policy not found."
        )

    return {
        "success": True,
        "code": "SUCCESS",
        "message": "Policy summary retrieved successfully.",
        "data": {
            "plan": policy.get("plan"),
            "copay": policy.get("copay"),
            "deductible": policy.get("deductible"),
            "outOfPocket": policy.get("outOfPocket")
        }
    }