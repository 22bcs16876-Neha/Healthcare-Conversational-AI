from fastapi import FastAPI

from app.routers.authentication import router as authentication_router
from app.routers.claims import router as claims_router
from app.routers.eligibility import router as eligibility_router
from app.routers.benefits import router as benefits_router
from app.routers.providers import router as providers_router
from app.routers.preauthorization import router as preauthorization_router
from app.routers.members import router as members_router
from app.routers.policy import router as policy_router


app = FastAPI(
    title="Healthcare Claims API",
    description="""
Production-ready Healthcare Claims Backend built with FastAPI and Firestore.

Features:
- Member Authentication
- Claims Status
- Claims History
- Claim Submission
- Eligibility
- Benefits
- Provider Lookup
- Provider Search
- Policy Details
- Pre-Authorization
""",
    version="2.0.0"
)


app.include_router(authentication_router)
app.include_router(claims_router)
app.include_router(eligibility_router)
app.include_router(benefits_router)
app.include_router(providers_router)
app.include_router(preauthorization_router)
app.include_router(members_router)
app.include_router(policy_router)


@app.get(
    "/",
    tags=["Home"],
    summary="Home"
)
def home():

    return {
        "application": "Healthcare Claims Backend",
        "version": "2.0.0",
        "status": "Running"
    }


@app.get(
    "/health",
    tags=["Health"],
    summary="Health Check"
)
def health():

    return {
        "status": "Healthy",
        "service": "Healthcare Claims Backend",
        "database": "Firestore",
        "version": "2.0.0"
    }


@app.get(
    "/routes",
    tags=["Utilities"],
    summary="Available Routes"
)
def routes():

    return {
        "authentication": "/authentication",
        "claims": "/claims",
        "eligibility": "/eligibility",
        "benefits": "/benefits",
        "providers": "/providers",
        "preauthorization": "/preauthorization",
        "member": "/member",
        "policy": "/policy",
        "swagger": "/docs",
        "openapi": "/openapi.json"
    }