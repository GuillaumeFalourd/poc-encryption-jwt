import jwt
from encryption.file_utils import get_encrypted_file_content
from encryption.keys_utils import get_public_key
from encryption.machine_utils import MetricsBuilder

def decrypt_jwt():
    try:
        content = get_encrypted_file_content()
        token = content["token"]
        decoded_data = jwt.decode(
            jwt=token,
            key=get_public_key(),
            algorithms="RS256",
            options={"verify_aud": False}
        )
        if MetricsBuilder().machine_id != decoded_data["machine_id"]:
            raise Exception("This token doesn't belong to this user machine.")
        else:
            decoded_machine_id = decoded_data["machine_id"]
            print(f"The decoded machine id is {decoded_machine_id}")            

    except Exception:
        print("Your token is invalid.")
