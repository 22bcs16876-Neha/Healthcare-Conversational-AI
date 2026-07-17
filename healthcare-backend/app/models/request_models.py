from pydantic import BaseModel, Field


class AuthenticationRequest(BaseModel):
    memberId: str
    dob: str
    zipCode: str
    last4SSN: str


class ClaimStatusRequest(BaseModel):
    memberId: str


class ClaimSubmissionRequest(BaseModel):
    memberId: str
    claimType: str
    provider: str
    serviceDate: str
    diagnosisCode: str
    amount: float = Field(..., gt=0)


class ClaimUpdateRequest(BaseModel):
    memberId: str
    claimType: str | None = None
    provider: str | None = None
    serviceDate: str | None = None
    diagnosisCode: str | None = None
    amount: float | None = None


class EligibilityRequest(BaseModel):
    memberId: str


class BenefitsRequest(BaseModel):
    memberId: str


class ProviderLookupRequest(BaseModel):
    memberId: str


class ProviderSearchRequest(BaseModel):
    providerName: str | None = None
    city: str | None = None
    state: str | None = None
    zipCode: str | None = None


class PreAuthorizationRequest(BaseModel):
    memberId: str


class MemberRequest(BaseModel):
    memberId: str


class PolicyRequest(BaseModel):
    memberId: str


class EscalationRequest(BaseModel):
    memberId: str | None = None
    reason: str | None = None