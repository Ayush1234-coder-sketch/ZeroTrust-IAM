import jwt

SECRET_KEY = "ayush_singh_zero_trust_iam_project_key_2026_secured"

def api_gateway(token):
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=['HS256'])
        return True, payload
    except Exception:
        return False, None

def protected_service(resource_name):
    return f"SUCCESS: Accessed {resource_name} via Gateway !!"