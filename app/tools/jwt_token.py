# JwtToken(data).get_token() -> acces, refresh
# JwtToken.decode(data) -> Dict[str, Any]
from calendar import timegm
from datetime import datetime, timedelta
from typing import Any, Dict

from marshmallow import Schema, fields

from constants import PWD_HASH_SALT, PWD_HASH_ITERATIONS, PWD_HASH_ALGO, SECRET
from constants import ACCESS_TOKEN_EXPIRATION, REFRESH_TOKEN_EXPIRATION
import jwt


class JwtSchema(Schema):
    user_id = fields.Int(required=True)
    role = fields.Str(required=True)
    exp = fields.Int()


class JwtToken:
    def __init__(self, data: Dict[str, Any]):
        self._now = datetime.now()
        self._data = data


    def _get_token(self, time_delta: timedelta) -> str:
        self._data.update({
            "exp": timegm((self._now + time_delta).timetuple())
        })
        return jwt.encode(self._data, SECRET, algorithm=PWD_HASH_ALGO)

    def _refresh_token(self) -> str:
        return self._get_token(time_delta=timedelta(days=REFRESH_TOKEN_EXPIRATION))

    def _access_token(self) -> str:
        return self._get_token(time_delta=timedelta(minutes=ACCESS_TOKEN_EXPIRATION))

    def get_tokens(self) -> Dict[str, str]:
        return {
            "access_token": self._access_token(),
            "refresh_token": self._refresh_token()
        }

    @staticmethod
    def decode_token(token: str) -> Dict[str, Any]:
        return jwt.decode(token, SECRET, PWD_HASH_ALGO)
