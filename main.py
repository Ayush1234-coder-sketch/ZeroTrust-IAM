from core.auth import register_user, login_user, generate_token
from core.mfa import setup_mfa, verify_mfa
from core.policy import access_policy_engine
from middleware.gateway import api_gateway, protected_service
from utils.logger import log_event

# Color Codes
BLUE = "\033[94m"
GREEN = "\033[92m"
CYAN = "\033[96m"
RESET = "\033[0m"
BOLD = "\033[1m"

BANNER = f"""{BLUE}{BOLD}
      ======================================================
      ||                                                  ||
      ||   ███████╗██████╗     ██╗ █████╗ ███╗   ███╗     ||
      ||   ╚══███╔╝██╔══██╗    ██║██╔══██╗████╗ ████║     ||
      ||     ███╔╝ ██████╔╝    ██║███████║██╔████╔██║     ||
      ||    ███╔╝  ██╔══██╗    ██║██╔══██║██║╚██╔╝██║     ||
      ||   ███████╗██║  ██║    ██║██║  ██║██║ ╚═╝ ██║     ||
      ||   ╚══════╝╚═╝  ╚═╝    ╚═╝╚═╝  ╚═╝╚═╝     ╚═╝     ||
      ||                                                  ||
      ||        ZERO-TRUST IDENTITY & ACCESS MANAGER      ||
      ======================================================
                [ {GREEN}SYSTEM STATUS: ACTIVE{BLUE} ]{RESET}
"""

SUCCESS_SHIELD = f"""{GREEN}{BOLD}
              .----------.
             /   S A F E  \\
            |    .----.    |
            |   | DONE |   |
            |    '----'    |
             \\  VERIFIED  /
              '----------'
{RESET}"""

def print_session_summary(user, role, action, token):
    """Prints a clean security report of the authorized session."""
    print(SUCCESS_SHIELD)
    print(f"{CYAN}{BOLD}" + "="*50)
    print(f"       🔒 SESSION SECURITY SUMMARY")
    print("="*50 + f"{RESET}")
    print(f"{BOLD}👤 User:{RESET}      {user}")
    print(f"{BOLD}🏷️ Role:{RESET}      {role}")
    print(f"{BOLD}🎯 Action:{RESET}    {action}")
    print(f"{BOLD}🔑 Token:{RESET}     {token[:15]}...{token[-10:]}")
    print(f"{GREEN}{BOLD}📍 Status:    VERIFIED & AUTHORIZED{RESET}")
    print(f"{CYAN}{BOLD}" + "="*50 + f"{RESET}\n")


def run_iam():
    print(BANNER)
    user_ip = "192.168.1.100" 

    print(f"{CYAN}--- Authentication Portal ---{RESET}")
    choice = input("1. Register\n2. Login\nSelect option (1 or 2): ")

    if choice == "1":
        username = input("Enter new username: ")
        password = input("Enter new password: ")
        success, msg = register_user(username, password)
        print(f"\n{GREEN if success else BLUE}{msg}{RESET}")
        if not success: return
        print("Please restart the tool to login.")
        return

    elif choice == "2":
        username = input("Username: ")
        password = input("Password: ")
        
        # 1. Identity Check
        success, msg = login_user(username, password)
        if not success:
            log_event(username, "login_attempt", "DENIED", user_ip)
            print(f"\n{BLUE}{msg}{RESET}")
            return
        
        print(f"\n{GREEN}✔ Identity Verified.{RESET}")

        # 2. MFA Layer
        # Note: In a real app, we'd fetch the secret from the DB. 
        # For this demo, we'll generate a fresh one for the session.
        secret, _ = setup_mfa(username)
        print(f"{BOLD}Step 2: MFA Required{RESET}")
        print(f"DEBUG: Setup Key: {CYAN}{secret}{RESET}")
        otp = input("Enter 6-digit MFA Code: ")
        
        if not verify_mfa(secret, otp):
            log_event(username, "mfa_verify", "DENIED", user_ip)
            print(f"{BLUE}Invalid MFA Code!{RESET}")
            return

        # 3. Token Generation
        # Let's ask what role they want to simulate for the demo
        role = input("Simulate role (admin/intern): ").lower()
        token = generate_token(username, role=role)
        print(f"\n{GREEN}✔ MFA Passed. JWT Generated.{RESET}")

        # 4. Gateway & Policy Check
        print(f"\n{CYAN}--- Resource Access ---{RESET}")
        action = input("Enter action to perform (view_dashboard/delete_database): ")
        
        is_valid, payload = api_gateway(token)
        
        if is_valid:
            allowed, policy_msg = access_policy_engine(payload['role'], action, True)
            if allowed:
                print(f"\n{GREEN}{protected_service(action)}{RESET}")
                log_event(username, action, "GRANTED", user_ip)
                print_session_summary(username, payload['role'], action, token)
            else:
                print(f"\n{BLUE}{policy_msg}{RESET}")
                log_event(username, action, "DENIED", user_ip)
        else:
            print(f"{BLUE}Gateway blocked: Invalid Token{RESET}")
    
    else:
        print("Invalid choice.")

if __name__ == "__main__":
    run_iam()