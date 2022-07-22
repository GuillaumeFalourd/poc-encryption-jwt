from cryptography.hazmat.primitives import serialization
from cryptography.hazmat.backends import default_backend
import os

PASSPHRASE = "@test123"

def get_private_key(): 
    PRIVATE_KEY_FILE = os.path.abspath("encryption/jwtRS256.key")
    with open(PRIVATE_KEY_FILE, "r", encoding="utf-8") as private_key_file:
        pk = private_key_file.read()
        
    if pk is not None:
        return serialization.load_pem_private_key(
                data=str.encode(pk),
                password=str.encode(PASSPHRASE),
                backend=default_backend()
            )
    
    else:
        print("Couldn't retrieve private key.")


def get_public_key():
    PUBLIC_KEY_FILE = os.path.abspath("encryption/jwtRS256.key.pub")
    with open(PUBLIC_KEY_FILE, "r", encoding="utf-8") as public_key_file:
        return public_key_file.read()