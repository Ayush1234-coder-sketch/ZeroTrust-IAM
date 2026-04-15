# 🛡️ Zero-Trust Identity & Access Manager (IAM)

[![Python](https://img.shields.io/badge/Python-3.10+-blue.svg)](https://www.python.org/downloads/)
[![Security](https://img.shields.io/badge/Security-Zero--Trust-red.svg)]()
[![License](https://img.shields.io/badge/License-MIT-green.svg)]()

A modular, backend-heavy Identity & Access Management system built with a **Defense-in-Depth** architecture. This project implements the core "Never Trust, Always Verify" philosophy of Zero-Trust security.

---

## 🚀 Key Features

* **Secure Identity Store:** Uses `bcrypt` with adaptive salting for industry-standard password hashing.
* **Stateless Authentication:** Implements **JWT (JSON Web Tokens)** for session management, ensuring scalability and security across microservices.
* **Multi-Factor Authentication (MFA):** Integrated **TOTP (Time-based One-Time Password)** support compatible with Google Authenticator and Authy.
* **Contextual Verification:** Adaptive security layer that validates requests based on source IP and time-of-day constraints.
* **Granular RBAC (Role-Based Access Control):** A centralized **Policy Engine** that enforces Least Privilege access.
* **API Gateway Proxy:** A centralized security middleware that intercepts and validates all internal service requests.
* **VAPT-Ready Logging:** Comprehensive security audit trails recording every `GRANTED` and `DENIED` event with metadata.

---

## 🏗️ Architecture & Flow

The system follows a strict 5-stage verification pipeline for every request:

1.  **Context Check:** Is the request coming from a trusted IP during authorized hours?
2.  **Identity Verification:** Does the salted hash match the database?
3.  **Assurance Layer:** Is the 6-digit TOTP code valid and current?
4.  **Token Validation:** Is the JWT signature intact and not expired?
5.  **Policy Enforcement:** Does the user's role have explicit permission for the specific action?



---

## 🛠️ Tech Stack

* **Language:** Python 3.x
* **Cryptography:** `bcrypt` (Hashing), `PyJWT` (Tokenization)
* **MFA Protocol:** `pyotp` (RFC 6238)
* **Data Storage:** JSON (Flat-file identity store)
* **Logging:** Python Standard `logging` library

---

## Video Demo Link:
https://screenrec.com/share/AD0Q6haO3Y


## 📦 Installation & Usage

1. **Clone the repository:**
   ```bash
   git clone [https://github.com/Ayush1234-coder-sketch/ZeroTrust-IAM.git](https://github.com/Ayush1234-coder-sketch/ZeroTrust-IAM.git)
   cd ZeroTrust-IAM

## Install dependencies:
pip install -r requirements.txt

## Run the system:
python main.py

## 🔒 Security Principles Implemented

    Least Privilege: Users are granted the minimum level of access required.

    Assume Breach: The internal network is treated as untrusted; every request is verified.

    Non-Repudiation: Every action is logged in security_audit.log for forensic analysis.

    Separation of Concerns: Modular design where Auth, Policy, and Gateway logic are decoupled.


## 👨‍💻 About the Author
Ayush Singh Cybersecurity Researcher & Future B.Tech Computer Science Student

I am a security-focused developer currently completing my Diploma in Computer Science (Class of 2026) and preparing to transition into a B.Tech program via Lateral Entry in August 2026. My professional focus lies at the intersection of Web Application Security, VAPT (Vulnerability Assessment and Penetration Testing), and Identity & Access Management (IAM).

🎯 Professional Focus & Philosophy

I believe that in the modern threat landscape, perimeter-based security is obsolete. My work is centered on the Zero-Trust architecture, where identity is the new perimeter. This project, ZeroTrust-IAM, is a testament to my commitment to building systems that "Never Trust, Always Verify."

🛠️ Technical Expertise

    Offensive Security: Bug Bounty Hunting, Web App Pentesting (XSS, SQLi, IDOR), and automated vulnerability scanning.

    Security Engineering: Developing secure-by-design backends, implementing cryptographically secure session management, and Multi-Factor Authentication (MFA).

    Programming: Proficient in Python for security automation and C/C++ for core computer science fundamentals.

    Tools: Burp Suite Professional, Metasploit, Nmap, and PyJWT.

📈 Current Projects & Training

    VAPT Training: Currently undergoing a rigorous 6-month specialized VAPT program at Ansh Infotech (Started Jan 2026).

    AI Security: Developing an AI-driven vulnerability scanner to automate the detection of injection-based flaws in modern web architectures.

    Identity Research: Exploring Zero-Trust Identity and Access Management to eliminate the risk of lateral movement in enterprise networks.

🤝 Connect with Me

I am actively seeking Remote-First Cybersecurity Internships where I can contribute to the defense of critical infrastructure while continuing to sharpen my offensive security skills.

    GitHub: Ayush1234-coder-sketch

    LinkedIn: www.linkedin.com/in/ayush-singh-67050b333

    Location: Jamshedpur, Jharkhand, India (Available for Remote Global Roles)
