def access_policy_engine(user_role, action, context_is_safe):
    if not context_is_safe:
        return False, "ACCESS DENIED !!(Unsafe Context)"
    
    permissions = {
        "admin": ["delete_database", "view_dashboard", "edit_settings"],
        "intern": ["view_dashboard"]
    }

    user_allowed_actions = permissions.get(user_role, [])
    if action in user_allowed_actions:
        return True, f"ACCESS GRANTED: {user_role} can perform {action}."
    return False, f"ACCESS DENIED: {user_role} lacks permissions."