from typing import Dict, Any

def update_auth_state(
    member_id: str = "",
    member_name: str = "",
    authenticated: bool = False,
    increment_auth_attempts: bool = False,
) -> Dict[str, Any]:
    """
    Updates the Authentication agent's session state for the Healthcare Claims Voice Assistant.
    After calling the authentication tool, use this to store the verified member details so
    every later agent can reuse them without asking again, mark the caller as authenticated,
    and reliably increment the failed-attempt counter. The counter is incremented in code so
    it is accurate and does not depend on the model counting turns.

    Call this tool:
    - On successful authentication: pass member_id and member_name from the auth response and
      set authenticated to true.
    - On a failed authentication attempt: set increment_auth_attempts to true.

    Args:
        member_id: The verified member ID from the auth response (data.memberId), e.g. "MEM1001".
            Leave empty to not change it.
        member_name: The member's name from the auth response (data.memberName). Leave empty to
            not change it.
        authenticated: True once the caller is verified. Leave false if not setting it.
        increment_auth_attempts: True to add 1 to the failed authentication counter.

    Returns:
        A dictionary with authenticated_member_id, member_name, authenticated, and auth_attempts.
    """

    saved = {}

    def save(name, value):
        if value is not None and value != "":
            set_variable(name, value)
            saved[name] = value

    def increment(name):
        current = get_variable(name) or 0
        new_value = int(current) + 1
        set_variable(name, new_value)
        saved[name] = new_value
        return new_value

    save("authenticated_member_id", member_id)
    save("member_name", member_name)

    if authenticated:
        set_variable("authenticated", True)
        saved["authenticated"] = True

    if increment_auth_attempts:
        increment("auth_attempts")

    return {
        "saved": saved,
        "authenticated_member_id": get_variable("authenticated_member_id"),
        "member_name": get_variable("member_name"),
        "authenticated": get_variable("authenticated") or False,
        "auth_attempts": get_variable("auth_attempts") or 0,
    }