from cryptography.fernet import Fernet
import os

def generate_key():
    key = Fernet.generate_key()
    with open("secret.key", "wb") as key_file:
        key_file.write(key)
    print("--- Key generated and saved to secret.key")


def load_key():
    return open("secret.key", "rb").read()


def encrypt_message(message, key):
    f = Fernet(key)
    encrypted = f.encrypt(message.encode())
    return encrypted


def decrypt_message(encrypted_message, key):
    f = Fernet(key)
    decrypted = f.decrypt(encrypted_message).decode()
    return decrypted

def main():
    print("=== AES Encryption & Decryption Tool ===")
    if not os.path.exists("secret.key"):
        generate_key()
    else:
        print(":) Key already exists. Loaded for use.")

    key = load_key()

    action = input("Choose action - encrypt or decrypt: ").strip().lower()

    if action == "encrypt":
        msg = input("Enter the message you want to encrypt: ")
        encrypted = encrypt_message(msg, key)
        print(f"\n Encrypted Message:\n{encrypted.decode()}")

    elif action == "decrypt":
        encrypted_msg = input("Paste the encrypted message: ").encode()
        try:
            decrypted = decrypt_message(encrypted_msg, key)
            print(f"\n Decrypted Message:\n{decrypted}")
        except:
            print(" Decryption failed! Make sure you used the right key and message.")

    else:
        print(" Invalid action. Please type 'encrypt' or 'decrypt'.")

if __name__ == "__main__":
    main()