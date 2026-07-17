from datetime import datetime

from fastapi import APIRouter, HTTPException, Path, Query

from app.models.request_models import (
    ClaimStatusRequest,
    ClaimSubmissionRequest,
    ClaimUpdateRequest,
)

from app.services.firestore_service import FirestoreService

from app.utils.normalizers import (
    normalize_member_id,
    normalize_claim_type,
    normalize_provider,
    normalize_date,
)

from app.utils.validators import (
    validate_member_id,
    validate_claim_type,
    validate_date,
    validate_not_future_date,
)

router = APIRouter(
    prefix="/claims",
    tags=["Claims"]
)


@router.post(
    "/status",
    summary="Get Claim Status",
    description="Returns the latest claim status for an authenticated member."
)
def get_claim_status(request: ClaimStatusRequest):

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

    claim = FirestoreService.get_claim_by_member(member_id)

    if not claim:
        return {
            "success": False,
            "code": "CLAIM_NOT_FOUND",
            "message": "No claims found for this member."
        }

    return {
        "success": True,
        "code": "SUCCESS",
        "message": "Claim retrieved successfully.",
        "data": claim
    }


@router.get(
    "/status/{member_id}",
    summary="Get Claim Status (GET)",
    description="Returns the latest claim status using Member ID."
)
def get_claim_status_get(
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

    claim = FirestoreService.get_claim_by_member(member_id)

    if not claim:
        raise HTTPException(
            status_code=404,
            detail="Claim not found."
        )

    return claim


@router.get(
    "/history/{member_id}",
    summary="Claim History",
    description="Returns all claims submitted by a member."
)
def claim_history(
    member_id: str = Path(...)
):

    member_id = normalize_member_id(member_id)

    claims = FirestoreService.get_claim_history(member_id)

    if not claims:
        return {
            "success": False,
            "code": "CLAIM_HISTORY_EMPTY",
            "message": "No claim history found."
        }

    return {
        "success": True,
        "code": "SUCCESS",
        "message": "Claim history retrieved successfully.",
        "totalClaims": len(claims),
        "data": claims
    }


@router.post(
    "/submit",
    summary="Submit New Claim",
    description="Creates a new healthcare claim."
)
def submit_claim(request: ClaimSubmissionRequest):

    member_id = normalize_member_id(request.memberId)

    claim_type = normalize_claim_type(request.claimType)

    provider = normalize_provider(request.provider)

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

    if not validate_claim_type(claim_type):
        return {
            "success": False,
            "code": "INVALID_CLAIM_TYPE",
            "message": "Unsupported claim type."
        }

    if request.amount <= 0:
        return {
            "success": False,
            "code": "INVALID_AMOUNT",
            "message": "Claim amount must be greater than zero."
        }

    # Accept the service date in any common format (DD-MM-YYYY, MM-DD-YYYY, spoken, etc.)
    # and convert it to YYYY-MM-DD. The future check below uses the server's real date.
    service_date = normalize_date(request.serviceDate)

    if not validate_date(service_date):
        return {
            "success": False,
            "code": "INVALID_SERVICE_DATE",
            "message": "Invalid service date. Please provide a real date."
        }

    if not validate_not_future_date(service_date):
        return {
            "success": False,
            "code": "INVALID_SERVICE_DATE",
            "message": "Service date cannot be in the future. It must be today or a past date."
        }

    claim = {
        "memberId": member_id,
        "claimType": claim_type,
        "provider": provider,
        "serviceDate": service_date,
        "diagnosisCode": request.diagnosisCode,
        "amount": request.amount,
        "status": "Submitted",
        "submittedDate": datetime.utcnow().strftime("%Y-%m-%d")
    }

    result = FirestoreService.submit_claim(claim)

    return {
        "success": True,
        "code": "CLAIM_SUBMITTED",
        "message": "Claim submitted successfully.",
        "data": result
    }


@router.put(
    "/{claim_id}",
    summary="Update Claim",
    description="Updates an existing healthcare claim. Only the fields provided are changed."
)
def update_claim(
    claim_id: str,
    request: ClaimUpdateRequest
):

    # Build an update with only the fields the caller actually provided.
    update_data = {}

    if request.claimType is not None:

        claim_type = normalize_claim_type(request.claimType)

        if not validate_claim_type(claim_type):
            return {
                "success": False,
                "code": "INVALID_CLAIM_TYPE",
                "message": "Unsupported claim type."
            }

        update_data["claimType"] = claim_type

    if request.provider is not None:
        update_data["provider"] = normalize_provider(request.provider)

    if request.serviceDate is not None:

        # Accept any common date format and convert to YYYY-MM-DD.
        service_date = normalize_date(request.serviceDate)

        if not validate_date(service_date):
            return {
                "success": False,
                "code": "INVALID_SERVICE_DATE",
                "message": "Invalid service date. Please provide a real date."
            }

        if not validate_not_future_date(service_date):
            return {
                "success": False,
                "code": "INVALID_SERVICE_DATE",
                "message": "Service date cannot be in the future. It must be today or a past date."
            }

        update_data["serviceDate"] = service_date

    if request.diagnosisCode is not None:
        update_data["diagnosisCode"] = request.diagnosisCode

    if request.amount is not None:

        if request.amount <= 0:
            return {
                "success": False,
                "code": "INVALID_AMOUNT",
                "message": "Claim amount must be greater than zero."
            }

        update_data["amount"] = request.amount

    if not update_data:
        return {
            "success": False,
            "code": "NO_UPDATE_FIELDS",
            "message": "No fields provided to update."
        }

    update_data["updatedAt"] = datetime.utcnow().strftime("%Y-%m-%d")

    updated = FirestoreService.update_claim(
        claim_id,
        request.memberId,
        update_data
    )

    # Same message whether the claim does not exist or belongs to another member,
    # so a caller cannot tell someone else's claim exists (prevents enumeration).
    if updated in ("NOT_FOUND", "NOT_OWNED"):
        return {
            "success": False,
            "code": "CLAIM_NOT_FOUND",
            "message": "No claim with that ID was found under your account."
        }

    return {
        "success": True,
        "code": "CLAIM_UPDATED",
        "message": "Claim updated successfully.",
        "data": updated
    }


@router.delete(
    "/{claim_id}",
    summary="Cancel Claim",
    description="Deletes a submitted claim that belongs to the authenticated member."
)
def delete_claim(claim_id: str, memberId: str = Query(...)):

    result = FirestoreService.delete_claim(claim_id, memberId)

    # Same message whether the claim does not exist or belongs to another member,
    # so a caller cannot tell someone else's claim exists (prevents enumeration).
    if result in ("NOT_FOUND", "NOT_OWNED"):
        return {
            "success": False,
            "code": "CLAIM_NOT_FOUND",
            "message": "No claim with that ID was found under your account."
        }

    return {
        "success": True,
        "code": "CLAIM_DELETED",
        "message": "Claim deleted successfully."
    }