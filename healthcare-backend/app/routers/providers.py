from fastapi import APIRouter, HTTPException, Path, Query

from app.models.request_models import ProviderLookupRequest
from app.services.firestore_service import FirestoreService

from app.utils.normalizers import (
    normalize_member_id,
    normalize_provider,
    normalize_zip,
    normalize_state,
    normalize_npi
)

from app.utils.validators import validate_member_id

router = APIRouter(
    prefix="/providers",
    tags=["Provider Lookup"]
)


@router.post(
    "/",
    summary="Provider Lookup",
    description="Returns provider details for an authenticated member."
)
def provider_lookup(request: ProviderLookupRequest):

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

    provider = FirestoreService.get_provider(member_id)

    if not provider:
        return {
            "success": False,
            "code": "PROVIDER_NOT_FOUND",
            "message": "Provider not found."
        }

    return {
        "success": True,
        "code": "SUCCESS",
        "message": "Provider retrieved successfully.",
        "data": provider
    }


# IMPORTANT: All specific GET routes (/search, /npi, /network, /city, /zipcode)
# MUST be declared BEFORE the dynamic /{member_id} route. Otherwise FastAPI
# treats "search", "city", etc. as a member_id and returns "Invalid Member ID".


@router.get(
    "/search",
    summary="Search Providers",
    description="Search providers by provider name, city, state or ZIP code."
)
def search_provider(

    providerName: str | None = Query(None),

    city: str | None = Query(None),

    state: str | None = Query(None),

    zipCode: str | None = Query(None)

):

    providers = FirestoreService.search_provider(

        provider_name=(
            normalize_provider(providerName)
            if providerName else None
        ),

        city=city.title() if city else None,

        state=normalize_state(state)
        if state else None,

        zip_code=normalize_zip(zipCode)
        if zipCode else None

    )

    return {
        "success": True,
        "code": "SUCCESS",
        "count": len(providers),
        "data": providers
    }


@router.get(
    "/npi/{npi}",
    summary="Search Provider by NPI",
    description="Returns provider details using NPI."
)
def get_provider_by_npi(
    npi: str = Path(...)
):

    npi = normalize_npi(npi)

    provider = FirestoreService.search_provider_by_npi(npi)

    if not provider:
        return {
            "success": False,
            "code": "PROVIDER_NOT_FOUND",
            "message": "Provider not found."
        }

    return {
        "success": True,
        "code": "SUCCESS",
        "message": "Provider retrieved successfully.",
        "data": provider
    }


@router.get(
    "/network/{state}",
    summary="Providers by State",
    description="Returns all providers available in a particular state."
)
def get_network_providers(
    state: str = Path(...)
):

    providers = FirestoreService.search_provider(
        state=normalize_state(state)
    )

    return {
        "success": True,
        "code": "SUCCESS",
        "count": len(providers),
        "data": providers
    }


@router.get(
    "/city/{city}",
    summary="Providers by City",
    description="Returns all providers available in a city."
)
def get_city_providers(
    city: str = Path(...)
):

    providers = FirestoreService.search_provider(
        city=city.title()
    )

    return {
        "success": True,
        "code": "SUCCESS",
        "count": len(providers),
        "data": providers
    }


@router.get(
    "/zipcode/{zip_code}",
    summary="Providers by ZIP Code",
    description="Returns providers for a ZIP Code."
)
def get_zip_providers(
    zip_code: str = Path(...)
):

    providers = FirestoreService.search_provider(
        zip_code=normalize_zip(zip_code)
    )

    return {
        "success": True,
        "code": "SUCCESS",
        "count": len(providers),
        "data": providers
    }


# Dynamic route LAST, so it does not swallow /search, /city, etc.
@router.get(
    "/{member_id}",
    summary="Get Provider",
    description="Returns provider information using Member ID."
)
def get_provider(member_id: str = Path(...)):

    member_id = normalize_member_id(member_id)

    if not validate_member_id(member_id):
        raise HTTPException(
            status_code=400,
            detail="Invalid Member ID."
        )

    provider = FirestoreService.get_provider(member_id)

    if not provider:
        raise HTTPException(
            status_code=404,
            detail="Provider not found."
        )

    return provider