# 🔐 Advanced Encryption Tool

A powerful and user-friendly web application built with **Flask**, **JavaScript**, and **AES-256 encryption** using **PyCryptodome**. This tool allows you to **encrypt and decrypt** both **files and plain text** with a secure password.

---

## 🚀 Features

- 🔒 AES-256 encryption (CFB mode)
- 📁 Encrypt/Decrypt any file (PDF, TXT, etc.)
- ✍️ Encrypt/Decrypt plain text
- 👁️ Toggle password visibility
- 📥 Download encrypted or decrypted file instantly
- 📱 Fully responsive modern UI (HTML/CSS/JS)

---

## 🛠️ Tech Stack

- **Frontend**: HTML, CSS, JavaScript
- **Backend**: Python Flask
- **Crypto**: PyCryptodome (AES, PBKDF2)
- **Other**: CORS, FileReader, Base64

---

## 🧪 How to Run Locally

### 1. Clone the repository

```bash
git remote add origin https://github.com/160904160805/ADVANCE-ENCRYPTION-TOOL.git
```
cd ADVANCE-ENCRYPTION-TOOL

python -m venv venv

# On Windows:
venv\Scripts\activate

# On Mac/Linux:
source venv/bin/activate

pip install -r requirements.txt

python app.py

📝 Folder Structure
ADVANCE-ENCRYPTION-TOOL/
│
├── static/
│   └── script.js
│
├── templates/
│   └── index.html
│
├── encrypt_decrypt.py
├── app.py
├── requirements.txt
└── README.md

📦 Requirements
Python 3.8+

Flask

PyCryptodome

⚠️ Disclaimer
This encryption tool is strictly intended for educational purposes and authorized use only.
Do not use it to encrypt or decrypt any files, texts, or data without proper authorization or ownership.
Unauthorized access or manipulation of data is illegal and unethical.

By using this tool, you acknowledge that you are solely responsible for your actions.
