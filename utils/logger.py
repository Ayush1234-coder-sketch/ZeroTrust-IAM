import logging
import os

# Create the directory if it doesn't exist yet
if not os.path.exists('data'):
    os.makedirs('data')

logging.basicConfig(
    filename='data/security_audit.log',
    level=logging.INFO,
    format='%(asctime)s | %(levelname)s | %(message)s'
)

def log_event(user, action, status, ip):
    log_entry = f"User: {user}, Action: {action}, Status: {status}, IP: {ip}"
    if status == "GRANTED":
        logging.info(log_entry)
    else:
        logging.warning(log_entry)