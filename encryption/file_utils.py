import json
import os

ENCRYPTED_FILE = os.path.abspath(".encrypted_file")

def get_encrypted_file_content():
    with open(ENCRYPTED_FILE, "r", encoding="utf-8") as encrypted_file:
        return json.loads(encrypted_file.read())


def create_encrypted_file(content: dict):
    try:
        with open(ENCRYPTED_FILE, "w", encoding="utf-8") as encrypted_file:
            encrypted_file.write(json.dumps(content))
            
        print(f"Encrypted file created successfully at {ENCRYPTED_FILE}")    

    except Exception as err:
        print(f"Couldn't create encrypted file at {ENCRYPTED_FILE}")
        raise err