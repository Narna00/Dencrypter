# AES Encryption & Decryption Tool

A simple command-line Python tool for encrypting and decrypting messages using **symmetric encryption** via the `cryptography` library (Fernet). The tool generates and stores a key (`secret.key`) and uses it to encrypt and decrypt messages safely.

---

## Features
- Generate a secure symmetric key and save it to `secret.key`.
- Encrypt plaintext messages into secure tokens.
- Decrypt encrypted tokens back to plaintext (requires the correct `secret.key`).
- Simple, interactive command-line interface.

---

## How It Works (brief)
1. On first run the script will generate a `secret.key` file containing a Fernet key.
2. On subsequent runs the script will load the key for encryption/decryption.
3. Use the `encrypt` action to convert a plaintext message into an encrypted token.
4. Use the `decrypt` action to convert an encrypted token back to plaintext.

This uses Fernet (which uses AES in CBC mode with HMAC for authentication under the hood), provided by the `cryptography` library.

---

## Getting Started

### Prerequisites
- Python 3.7+ (recommended)
- `pip` for Python package installation

Install the required package:


pip install cryptography

### Example Run (sample session)

````bash
$ python dencrypter.py
=== AES Encryption & Decryption Tool ===
:) Key already exists. Loaded for use.
Choose action - encrypt or decrypt: encrypt
Enter the message you want to encrypt: secret data
Encrypted Message:
gAAAAABk... (pasteable token)

$ python dencrypter.py
=== AES Encryption & Decryption Tool ===
:) Key already exists. Loaded for use.
Choose action - encrypt or decrypt: decrypt
Paste the encrypted message: gAAAAABk...
Decrypted Message:
secret data


**### File Structure**
dencrypter.py
secret.key             # Generated AES/Fernet key (created automatically on first run)
README.md              # This file

### Security Notes (read carefully)
- **Protect `secret.key`.** Anyone with access to `secret.key` can decrypt messages encrypted with it.
- **Do not commit `secret.key` to version control.** Add it to `.gitignore`.
- This tool is for **learning and small personal use**. For production encryption, follow rigorous key management: rotate keys, use secure storage (HSM / KMS), and conduct formal security reviews.
- Always **validate and sanitize inputs** if you integrate this into larger systems.

**Add `secret.key` to `.gitignore`:**
`gitignore
secret.key `


### Troubleshooting / FAQ

**Q:** I get `InvalidToken` on decrypt.  
**A:** Make sure:

- You used the **exact** `secret.key` that encrypted the message.  
- The encrypted token was not truncated or altered when copying/pasting.

---

**Q:** I accidentally pushed `secret.key` to GitHub — what do I do?  
**A:** Treat the key as compromised:

1. **Remove the exposed key** from the repository and history (use tools like `git rm --cached secret.key` and consider rewriting history with `git filter-repo` or `git filter-branch`).  
2. **Generate a new key** (run the script or call `Fernet.generate_key()` and save to `secret.key`).  
3. **Re-encrypt** any sensitive data with the new key.  
4. **Rotate secrets** in any dependent systems (update keys, credentials, and access where the old key was used).

---

### Extending this Project (ideas)

- Add **file encryption/decryption** (read file bytes, encrypt, save as `.enc`, and decrypt back).  
- Add **CLI flags** using `argparse` to allow non-interactive usage and scripting (e.g., `--encrypt`, `--decrypt`, `--file path`).  
- Add **key rotation** and secure key storage integrations (AWS KMS, Azure Key Vault, Google KMS).  
- Add **unit tests** for `encrypt_message` and `decrypt_message` functions (use `pytest`).  
- Build a small **GUI** or web frontend (Flask / FastAPI) — **do not** expose `secret.key` or key-management endpoints to the public web.

---

### Author

Created by **Prince Amoako Atta**  
Cybersecurity | Data Analyst

---

### License

This project is open-source and free to use under the **MIT License**. See the `LICENSE` file for details.

---

### Contributing

If you want to contribute:

1. Fork the repository.  
2. Create a feature branch: `git checkout -b feature/your-feature`.  
3. Make your changes, commit, and push.  
4. Open a pull request with a clear description of what you changed and why.
