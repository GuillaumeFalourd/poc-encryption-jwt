import jwt
from encryption.file_utils import create_encrypted_file
from encryption.keys_utils import get_private_key
from encryption.machine_utils import MetricsBuilder
from encryption.models import Token, Data


def encrypt_jwt():
    private_key = get_private_key()
    data = Data(
        machine_id = MetricsBuilder().machine_id
    )
    encrypted_data = jwt.encode(data.dict(), private_key, algorithm="RS256")
    token = Token(token=encrypted_data)
    create_encrypted_file(token.dict())