from typing import Any

from pydantic import BaseModel


class APIResponse(BaseModel):
    success: bool
    code: str
    message: str
    data: Any | None = None


class AuthenticationResponse(BaseModel):
    success: bool
    code: str
    message: str
    memberId: str
    memberName: str
    authenticated: bool


class ClaimResponse(BaseModel):
    success: bool
    code: str
    message: str
    claimId: str
    memberId: str
    status: str
    data: dict


class ClaimHistoryResponse(BaseModel):
    success: bool
    code: str
    message: str
    totalClaims: int
    data: list


class EligibilityResponse(BaseModel):
    success: bool
    code: str
    message: str
    data: dict


class BenefitsResponse(BaseModel):
    success: bool
    code: str
    message: str
    data: dict


class ProviderResponse(BaseModel):
    success: bool
    code: str
    message: str
    data: dict


class ProviderSearchResponse(BaseModel):
    success: bool
    code: str
    message: str
    count: int
    data: list


class PolicyResponse(BaseModel):
    success: bool
    code: str
    message: str
    data: dict


class MemberResponse(BaseModel):
    success: bool
    code: str
    message: str
    data: dict


class PreAuthorizationResponse(BaseModel):
    success: bool
    code: str
    message: str
    data: dict


class ErrorResponse(BaseModel):
    success: bool = False
    code: str
    message: str