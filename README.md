# 🛡️ API Security Framework & BOLA Audit

A comprehensive API security testing framework built to simulate, detect, and remediate **Broken Object Level Authorization (BOLA / OWASP API1:2023)** vulnerabilities using **FastAPI**, **Postman**, and **OWASP ZAP**.

---

## 📌 Executive Summary

Broken Object Level Authorization (BOLA) occurs when an application does not properly validate whether the authenticated user has permission to access a requested resource ID. This project demonstrates:
1. **Simulation of BOLA:** An endpoint allowing unauthorized access to User B's profile using User A's JWT token.
2. **Automated Detection:** Postman integration testing with custom JavaScript assertions.
3. **Automated DAST Audit:** Dynamic application security scanning via OWASP ZAP to generate vulnerability reports.
4. **Remediation:** Implementation of strict token identity checks to enforce object-level authorization.

---

## 🚀 Key Features

* **JWT Authentication:** Secure user authentication using HS256 algorithm tokens.
* **Vulnerable Endpoint (`/api/v1/user/{user_id}/profile`):** Decodes JWT tokens but fails to cross-check token claims against requested path parameters.
* **Secured Endpoint (`/api/v2/user/{user_id}/profile`):** Validates decoded `user_id` against `user_id` in path parameters, returning `HTTP 403 Forbidden` on mismatch.
* **Postman Test Suite:** Automated assertions verifying HTTP status code transitions from `200 OK` (vulnerable) to `403 Forbidden` (remediated).
* **OWASP ZAP Dynamic Audit:** Security scan execution resulting in an HTML security audit report.

---

## 🛠️ Tech Stack & Tools

* **Backend Framework:** FastAPI (Python)
* **ASGI Server:** Uvicorn
* **Authentication:** PyJWT
* **API Testing & Automation:** Postman
* **DAST Scanner:** OWASP ZAP (Zed Attack Proxy)
* **Version Control:** Git & GitHub

---

## 📁 Project Structure

```text
api-security-framework/
│
├── main.py                    # FastAPI application (Vulnerable & Secured Endpoints)
├── zap-report.html            # OWASP ZAP Security Audit Report
├── .gitignore                 # Environment and cache exclusion file
└── README.md                  # Project documentation
