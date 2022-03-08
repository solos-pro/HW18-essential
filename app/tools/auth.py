from flask import request
from flask_restx import abort
from jwt import PyJWTError

from app.tools.jwt_token import JwtToken


def login_required(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        auth_header = request.headers.get("Authorization")
        if not auth_header:
            abort(401)

        try:
            data = JwtToken.decode_token(auth_header.split("Bearer ")[-1])
            return func(*args, **kwargs, user_id=data["user_id"])
        except PyJWTError:
            abort(401)

    return wrapper
