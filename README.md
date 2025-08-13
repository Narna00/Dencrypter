🔐 AES Encryption & Decryption Tool
This is a simple command-line Python tool for encrypting and decrypting messages using AES symmetric encryption powered by the cryptography library (Fernet module).

✨ Features
Generates a secure key (secret.key) for encryption and decryption.

Encrypts plaintext messages to protect sensitive information.

Decrypts encrypted messages (only with the correct key).

Friendly terminal prompts for ease of use.

🛠️ How It Works
On first run, it generates a secret.key file to securely store your AES key.

If the key already exists, it loads it for reuse.

You choose whether to encrypt or decrypt a message.

The program uses the Fernet class to securely perform AES-based encryption and decryption.

🚀 Getting Started
📦 Prerequisites
Make sure you have Python 3 and the cryptography library installed:

bash
Copy
Edit
pip install cryptography
▶️ Usage
Run the script in your terminal:

bash
Copy
Edit
python encryption_tool.py
Follow the prompt to:

Encrypt a message: input a plain message and receive an encrypted output.

Decrypt a message: paste the encrypted string and retrieve the original message.

📁 File Structure
graphql
Copy
Edit
encryption_tool.py     # Main script
secret.key             # Generated AES key (automatically created)
⚠️ Security Notes
Keep the secret.key safe. Without it, encrypted messages cannot be decrypted.

Do not share your key file publicly.

Use this tool for educational and personal purposes — not for high-stakes production systems.

👨‍💻 Author
Created by [Your Name]
Cybersecurity Enthusiast | Python Developer

📜 License
This project is open-source and free to use under the MIT License.
