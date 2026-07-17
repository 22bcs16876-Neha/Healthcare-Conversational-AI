from datetime import datetime, timezone

from google.cloud.firestore import Query

from app.database import db


class FirestoreService:

    @staticmethod
    def get_member(member_id: str):

        doc = db.collection("members").document(member_id).get()

        if doc.exists:
            return doc.to_dict()

        return None

    @staticmethod
    def member_exists(member_id: str):

        return (
            db.collection("members")
            .document(member_id)
            .get()
            .exists
        )

    @staticmethod
    def get_all_members():

        docs = db.collection("members").stream()

        members = []

        for doc in docs:
            members.append(doc.to_dict())

        return members

    @staticmethod
    def get_claim_by_member(member_id: str):

        docs = (
            db.collection("claims")
            .where("memberId", "==", member_id)
            .order_by(
                "submittedDate",
                direction=Query.DESCENDING
            )
            .limit(1)
            .stream()
        )

        for doc in docs:
            return doc.to_dict()

        return None

    @staticmethod
    def get_claim_history(member_id: str):

        docs = (
            db.collection("claims")
            .where("memberId", "==", member_id)
            .order_by(
                "submittedDate",
                direction=Query.DESCENDING
            )
            .stream()
        )

        history = []

        for doc in docs:
            history.append(doc.to_dict())

        return history

    @staticmethod
    def generate_claim_id():

        docs = db.collection("claims").stream()

        highest = 1000

        for doc in docs:

            data = doc.to_dict()

            claim_id = data.get("claimId", "")

            if claim_id.startswith("CLM"):

                try:

                    highest = max(
                        highest,
                        int(
                            claim_id.replace(
                                "CLM",
                                ""
                            )
                        )
                    )

                except ValueError:
                    pass

        return f"CLM{highest + 1}"

    @staticmethod
    def submit_claim(claim_data: dict):

        claim_id = FirestoreService.generate_claim_id()

        current_time = datetime.now(
            timezone.utc
        ).isoformat()

        claim_data["claimId"] = claim_id

        claim_data["status"] = "Submitted"

        claim_data["submittedDate"] = datetime.now(
            timezone.utc
        ).strftime("%Y-%m-%d")

        claim_data["createdAt"] = current_time

        claim_data["updatedAt"] = current_time

        claim_data["lastUpdated"] = current_time

        claim_data["claimStatusHistory"] = [
            {
                "status": "Submitted",
                "timestamp": current_time
            }
        ]

        db.collection("claims").document(
            claim_id
        ).set(claim_data)

        return claim_data
    @staticmethod
    def update_claim(claim_id: str, member_id: str, updated_data: dict):

        doc_ref = db.collection("claims").document(claim_id)

        doc = doc_ref.get()

        if not doc.exists:
            return "NOT_FOUND"

        existing_claim = doc.to_dict()

        # Ownership check: a member may only update their own claims.
        if existing_claim.get("memberId") != member_id:
            return "NOT_OWNED"

        current_time = datetime.now(
            timezone.utc
        ).isoformat()

        status = updated_data.get(
            "status",
            existing_claim.get(
                "status",
                "Processing"
            )
        )

        history = existing_claim.get(
            "claimStatusHistory",
            []
        )

        if (
            not history or
            history[-1]["status"] != status
        ):
            history.append(
                {
                    "status": status,
                    "timestamp": current_time
                }
            )

        updated_data["updatedAt"] = current_time

        updated_data["lastUpdated"] = current_time

        updated_data["claimStatusHistory"] = history

        doc_ref.update(updated_data)

        return doc_ref.get().to_dict()

    @staticmethod
    def delete_claim(claim_id: str, member_id: str):

        doc_ref = db.collection("claims").document(claim_id)

        doc = doc_ref.get()

        if not doc.exists:
            return "NOT_FOUND"

        claim = doc.to_dict()

        # Ownership check: a member may only cancel their own claims.
        if claim.get("memberId") != member_id:
            return "NOT_OWNED"

        doc_ref.delete()

        return "DELETED"

    @staticmethod
    def get_eligibility(member_id: str):

        doc = db.collection("eligibility").document(member_id).get()

        if doc.exists:
            return doc.to_dict()

        return None

    @staticmethod
    def get_benefits(member_id: str):

        doc = db.collection("benefits").document(member_id).get()

        if doc.exists:
            return doc.to_dict()

        return None

    @staticmethod
    def get_provider(member_id: str):

        docs = (
            db.collection("providers")
            .where("memberId", "==", member_id)
            .limit(1)
            .stream()
        )

        for doc in docs:
            return doc.to_dict()

        return None

    @staticmethod
    def search_provider(
        provider_name: str = None,
        city: str = None,
        state: str = None,
        zip_code: str = None
    ):

        query = db.collection("providers")

        if provider_name:
            query = query.where(
                "providerNameLower",
                "==",
                provider_name.lower()
            )

        if city:
            query = query.where(
                "city",
                "==",
                city
            )

        if state:
            query = query.where(
                "state",
                "==",
                state
            )

        if zip_code:
            query = query.where(
                "zipCode",
                "==",
                zip_code
            )

        docs = query.stream()

        providers = []

        for doc in docs:
            providers.append(doc.to_dict())

        return providers

    @staticmethod
    def search_provider_by_npi(npi: str):

        docs = (
            db.collection("providers")
            .where("npi", "==", npi)
            .limit(1)
            .stream()
        )

        for doc in docs:
            return doc.to_dict()

        return None

    @staticmethod
    def get_policy(member_id: str):

        doc = db.collection("policies").document(member_id).get()

        if doc.exists:
            return doc.to_dict()

        return None

    @staticmethod
    def get_member_policy(member_id: str):

        member = FirestoreService.get_member(member_id)

        if not member:
            return None

        policy = FirestoreService.get_policy(member_id)

        return {
            "member": member,
            "policy": policy
        }

    @staticmethod
    def get_preauthorization(member_id: str):

        docs = (
            db.collection("preauthorizations")
            .where("memberId", "==", member_id)
            .limit(1)
            .stream()
        )

        for doc in docs:
            return doc.to_dict()

        return None