def _payload(tool_response):
    if not isinstance(tool_response, dict):
        return {}
    result = tool_response.get("result")
    return result if isinstance(result, dict) else tool_response


def _is_not_found(payload) -> bool:
    code = str(payload.get("code", "") or "").upper()
    message = str(payload.get("message", "") or "").lower()
    return code in ("CLAIM_NOT_FOUND", "NOT_FOUND", "404") or "not found" in message


def after_tool_callback(tool, args, tool_context, tool_response):
    """Records success/failure of claim actions and counts cancel not-found attempts."""
    tool_name = str(getattr(tool, "name", "") or "")

    if tool_name in ("update_claim_update_claim", "update_claim"):
        payload = _payload(tool_response)
        tool_context.variables["last_claim_failed"] = not bool(payload.get("success", False))
        return None

    if tool_name not in ("cancel_claim_cancel_claim", "cancel_claim"):
        return None

    payload = _payload(tool_response)
    success = bool(payload.get("success", False))
    tool_context.variables["last_claim_failed"] = not success

    if success:
        tool_context.variables["claim_attempts"] = 0
    elif _is_not_found(payload):
        current = int(tool_context.variables.get("claim_attempts", 0) or 0)
        tool_context.variables["claim_attempts"] = current + 1

    return None