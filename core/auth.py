import bcrypt
import json
import os
import jwt
import datetime

DB_FILE = 'data/users_db.json' # Updated path
SECRET_KEY = "ayush_singh_zero_trust_iam_project_key_2026_secured"

def init_db():
    if not os.path.exists('data'):
        os.makedirs('data')
    if not os.path.exists(DB_FILE):
        with open(DB_FILE, 'w') as f:
            json.dump({}, f)

def register_user(username, password):
    init_db()
    password_bytes = password.encode('utf-8')
    hash_pw = bcrypt.hashpw(password_bytes, bcrypt.gensalt())
    
    with open(DB_FILE, 'r') as f:
        users = json.load(f)
        
    if username in users:
        return False, "User Already Exists !!"
    
    users[username] = hash_pw.decode('utf-8')
    with open(DB_FILE, 'w') as f:
        json.dump(users, f)
    return True, f"User {username} registered successfully !!"

def login_user(username, password):
    with open(DB_FILE, 'r') as f:
        users = json.load(f)
    if username not in users:
        return False, "User Not Found !!"
    
    stored_hash = users[username].encode('utf-8')
    password_bytes = password.encode('utf-8')

    if bcrypt.checkpw(password_bytes, stored_hash):
        return True, "ACCESS GRANTED !!"
    return False, "ACCESS DENIED !!"

def generate_token(username, role="intern"):
    payload = {
        "sub": username,
        "iat": datetime.datetime.utcnow(),
        "exp": datetime.datetime.utcnow() + datetime.timedelta(minutes=30),
        "role": role
    }
    return jwt.encode(payload, SECRET_KEY, algorithm='HS256')