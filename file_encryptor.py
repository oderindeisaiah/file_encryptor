from cryptography.fernet import Fernet
import os

def generate_key():
    key = Fernet.generate_key()
    with open("filekey.key", "wb") as key_file:
        key_file.write(key)
    print("Encryption key generated and saved as 'filekey.key'.")

def load_key():
    return open("filekey.key", "rb").read()

def encrypt_file(filename):
    key = load_key()
    fernet = Fernet(key)
    with open(filename, "rb") as file:
        original = file.read()
    encrypted = fernet.encrypt(original)
    with open(filename + ".enc", "wb") as enc_file:
        enc_file.write(encrypted)
    print(f"File '{filename}' encrypted successfully!")

def decrypt_file(filename):
    key = load_key()
    fernet = Fernet(key)
    with open(filename, "rb") as enc_file:
        encrypted = enc_file.read()
    decrypted = fernet.decrypt(encrypted)
    original_name = filename.replace(".enc", ".dec")
    with open(original_name, "wb") as dec_file:
        dec_file.write(decrypted)
    print(f"File '{filename}' decrypted successfully to '{original_name}'.")

def main():
    print("=== File Encryptor / Decryptor ===")
    if not os.path.exists("filekey.key"):
        generate_key()

    while True:
        print("\n1. Encrypt a file\n2. Decrypt a file\n3. Exit")
        choice = input("Choice: ").strip()
        if choice == "1":
            filename = input("Enter filename to encrypt: ").strip()
            if os.path.exists(filename):
                encrypt_file(filename)
            else:
                print("File does not exist!")
        elif choice == "2":
            filename = input("Enter filename to decrypt: ").strip()
            if os.path.exists(filename):
                decrypt_file(filename)
            else:
                print("File does not exist!")
        elif choice == "3":
            break
        else:
            print("Invalid choice.")

if __name__ == "__main__":
    main()