import pyotp

def setup_mfa(username):
    secret = pyotp.random_base32()
    uri = pyotp.totp.TOTP(secret).provisioning_uri(name=username, issuer_name="ZeroTrustIAM")
    return secret, uri

def verify_mfa(secret, user_input_code):
    totp = pyotp.TOTP(secret)
    return totp.verify(user_input_code)