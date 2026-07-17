from typing import Dict, Any

def update_claim_state(
    claim_id: str = "",
    increment_claim_attempts: bool = False,
    reset_claim_attempts: bool = False,
) -> Dict[str, Any]:
    """
    Updates the Claims agent's session state for the Healthcare Claims Voice Assistant.
    Use this to remember the Claim ID the caller is working with, and to reliably increment
    the claim retry counter. The counter is incremented in code so it is accurate and does
    not depend on the model counting turns.

    Call this tool:
    - When the caller gives a Claim ID: pass claim_id to remember it.
    - When a claim action fails and should count as a retry (for example a Claim ID was not
      found): set increment_claim_attempts to true.
    - When starting a fresh successful claim action: set reset_claim_attempts to true.

    Args:
        claim_id: The Claim ID the caller provided, e.g. "CLM1001". Leave empty to not change it.
        increment_claim_attempts: True to add 1 to the claim retry counter.
        reset_claim_attempts: True to reset the claim retry counter to 0.

    Returns:
        A dictionary with the current claim_id and claim_attempts count.
    """

    saved = {}

    def save(name, value):
        if value is not None and value != "":
            set_variable(name, value)
            saved[name] = value

    save("claim_id", claim_id)

    if reset_claim_attempts:
        set_variable("claim_attempts", 0)
        saved["claim_attempts"] = 0
    elif increment_claim_attempts:
        current = get_variable("claim_attempts") or 0
        set_variable("claim_attempts", int(current) + 1)
        saved["claim_attempts"] = int(current) + 1

    return {
        "saved": saved,
        "claim_id": get_variable("claim_id"),
        "claim_attempts": get_variable("claim_attempts") or 0,
    }