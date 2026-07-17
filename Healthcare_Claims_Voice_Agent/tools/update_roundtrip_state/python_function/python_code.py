from typing import Dict, Any

def update_roundtrip_state(
    pending_claim_details: str = "",
    pending_provider: str = "",
    awaiting_provider: bool = False,
    clear_roundtrip: bool = False,
) -> Dict[str, Any]:
    """
    Manages the claim-to-provider round trip for the Healthcare Claims Voice Assistant.
    Use this when a caller is submitting a claim but does not know the provider, so they are
    sent to the Provider agent to find one and then returned to Claims to finish the submission.

    Call this tool:
    - In Claims, before sending the caller to the Provider agent: pass pending_claim_details
      (a short text summary of the claim type, service date, diagnosis code, and amount that
      have already been collected) and set awaiting_provider = true.
    - In the Provider agent, once the caller picks a provider: pass pending_provider with the
      chosen provider's name.
    - In Claims, after the claim is submitted: set clear_roundtrip = true to reset this state.

    Args:
        pending_claim_details: A short text summary of the already-collected claim details.
            Leave empty to not change it.
        pending_provider: The chosen provider name. Leave empty to not change it.
        awaiting_provider: True when a claim is waiting for a provider to be found.
        clear_roundtrip: True to clear all round-trip state after the claim is submitted.

    Returns:
        A dictionary with the current round-trip state.
    """

    saved = {}

    def save(name, value):
        if value is not None and value != "":
            set_variable(name, value)
            saved[name] = value

    if clear_roundtrip:
        set_variable("pending_claim_details", "")
        set_variable("pending_provider", "")
        set_variable("awaiting_provider", False)
        return {
            "cleared": True,
            "pending_claim_details": "",
            "pending_provider": "",
            "awaiting_provider": False,
        }

    save("pending_claim_details", pending_claim_details)
    save("pending_provider", pending_provider)

    if awaiting_provider:
        set_variable("awaiting_provider", True)
        saved["awaiting_provider"] = True

    return {
        "saved": saved,
        "pending_claim_details": get_variable("pending_claim_details"),
        "pending_provider": get_variable("pending_provider"),
        "awaiting_provider": get_variable("awaiting_provider") or False,
    }