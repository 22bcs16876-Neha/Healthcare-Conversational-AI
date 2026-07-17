def before_tool_callback(tool, args, tool_context):
    """Injects the authenticated member id into cancel and update calls, and
    avoids counting a successful claim action as a failure."""
    tool_name = str(getattr(tool, "name", "") or "")

    # Retry-counter guard for update_claim_state.
    if tool_name == "update_claim_state":
        if args.get("increment_claim_attempts") and not tool_context.variables.get(
            "last_claim_failed", False
        ):
            return {
                "skipped": True,
                "reason": "Previous claim action succeeded; not counting as a failure."
            }
        return None

    member_id = tool_context.variables.get("authenticated_member_id", "")

    # Always send the authenticated member id on cancel and update, so a member
    # can only act on their own claims (backend enforces ownership).
    if tool_name in (
        "cancel_claim_cancel_claim", "cancel_claim",
        "update_claim_update_claim", "update_claim"
    ):
        args["memberId"] = member_id
        return None

    return None