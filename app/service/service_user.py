import base64
import hashlib
import hmac
import datetime
import calendar
import jwt
from flask import request, abort
from app.dao.user_dao import UserDAO
from constants import PWD_HASH_SALT, PWD_HASH_ITERATIONS, PWD_HASH_ALGO, SECRET


class UserService:
    def __init__(self, dao: UserDAO):
        self.dao = dao

    def validate_jwt_generate(self, r_json):
        user = {
            "username": r_json.get("username"),
            "password": r_json.get("password")
        }
        request_pass = hash_str_encode(hash_encode(user))   # TODO: Hash from (pass & name)

    def search(self, user):
        return self.dao.get_one(user)

    def get_one(self, uid):
        return self.dao.get_one(uid)

    def create(self, data):
        return self.dao.create(data)

    def update(self, data):
        uid = data.get("id")
        user = self.dao.get_one(uid)

        user.username = data.get("username")
        user.password = data.get("password")
        user.role = data.get("role")

        self.dao.update(user)

    def update_partial(self, data):
        uid = data.get("id")
        user = self.get_one(uid)

        if "id" in data:
            user.id = data.get("id")
        if "username" in data:
            user.username = data.get("username")
        if "password" in data:
            user.password = data.get("password")
        if "role" in data:
            user.role = data.get("role")

        self.dao.update(user)

    def delete(self, mid):
        self.dao.delete(mid)


# ===============================================================================


def admin_required(func):
    def wrapper(*args, **kwargs):
        if 'Authorization' not in request.headers:
            abort(401)

        data = request.headers['Authorization']
        token = data.split("Bearer ")[-1]
        try:
            user = jwt.decode(token, SECRET, algorithms=[PWD_HASH_ALGO])
            role = user.get("role")
        except Exception as e:
            print("JWT Decode Exception", e)
            abort(401)
        if role != "admin":
            abort(403)
        return func(*args, **kwargs)

    return wrapper


def auth_required(func):
    def wrapper(*args, **kwargs):
        if 'Authorization' not in request.headers:
            abort(401)
        data = request.headers['Authorization']
        token = data.split("Bearer ")[-1]
        try:
            jwt.decode(token, SECRET, algorithms=[PWD_HASH_ALGO])
        except Exception as e:
            print(f"Traceback: {e}")
            abort(401)
        return func(*args, **kwargs)

    return wrapper


def compare_passwords(password_hash, other_password):
    return hmac.compare_digest(
        password_hash,
        hashlib.pbkdf2_hmac(PWD_HASH_ALGO, other_password.encode(), PWD_HASH_SALT, PWD_HASH_ITERATIONS)
    )


def hash_encode(password_and_name):
    return hashlib.pbkdf2_hmac(
        'sha256',
        password_and_name.encode('utf-8'),  # Convert the password to bytes
        PWD_HASH_SALT,
        PWD_HASH_ITERATIONS
    )  # .decode("utf-8", "ignore")


def hash_str_encode(data):
    return base64.b64encode(data)


def generate_jwt(user_obj):
    data = {
        "username": user_obj.get('username'),
        "password": user_obj.get('password')
    }

    min30 = datetime.datetime.utcnow() + datetime.timedelta(minutes=30)
    data["exp"] = calendar.timegm(min30.timetuple())
    access_token = jwt.encode(data, SECRET, algorithm=PWD_HASH_ALGO)

    days130 = datetime.datetime.utcnow() + datetime.timedelta(days=130)
    data["exp"] = calendar.timegm(days130.timetuple())
    refresh_token = jwt.encode(data, SECRET, algorithm=PWD_HASH_ALGO)

    return {"access_token": access_token, "refresh_token": refresh_token}
