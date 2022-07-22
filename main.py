import questionary
import os
from pathlib import Path
from encryption.encrypt_jwt import encrypt_jwt
from encryption.decrypt_jwt import decrypt_jwt

def main():
    print("- The program started!")
    answer = questionary.select(
             "What do you want to do?",
             choices=[
                 "Encrypt",
                 "Decrypt",
             ]).ask()
    if answer == "Encrypt":
        encrypt_jwt()

    if answer == "Decrypt":
        ENCRYPTED_FILE = os.path.abspath(".encrypted_file")
        if Path(ENCRYPTED_FILE).exists():
            decrypt_jwt()
        else:
            print(f"You need an encrypted file at {ENCRYPTED_FILE} first.")
            
    print("- The program ended!")
    
    
if __name__ == "__main__":
    main()