import base64
import hashlib
import hmac

from constants import PWD_HASH_SALT, PWD_HASH_ITERATIONS, PWD_HASH_ALGO, SECRET
from flask import current_app


def get_password_digest(password: str) -> bytes:
    return hashlib.pbkdf2_hmac(
        hash_name=PWD_HASH_ALGO,
        password=password.encode("utf-8"),
        salt=PWD_HASH_SALT,
        iterations=PWD_HASH_ITERATIONS
    )


def get_password_hash(password: str) -> str:
    return base64.b64encode(get_password_digest(password).decode('utf-8'))

def compare_passwords(password_hash, other_password):
    return hmac.compare_digest(
        base64.decode(password_hash),
        get_password_digest(other_password)
    )


# hash_name=current_app.config["PWD_HASH_ALGO"]
# salt=current_app.config["PWD_HASH_SALT"],
# iterations=current_app.config["PWD_HASH_ITERATIONS"]


# def hash_encode(password):
#     return hashlib.pbkdf2_hmac(
#         'sha256',
#         password.encode('utf-8'),  # Convert the password to bytes
#         PWD_HASH_SALT,
#         PWD_HASH_ITERATIONS
#     )  # .decode("utf-8", "ignore")
