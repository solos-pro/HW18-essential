import base64
import hashlib
import hmac

from app.dao.user_dao import UserDAO
from constants import PWD_HASH_SALT, PWD_HASH_ITERATIONS, PWD_HASH_ALGO


class UserService:
    def __init__(self, dao: UserDAO):
        self.dao = dao

    def hash_encode(self, password):
        return hashlib.pbkdf2_hmac(
            'sha256',
            password.encode('utf-8'),  # Convert the password to bytes
            PWD_HASH_SALT,
            PWD_HASH_ITERATIONS
        ).decode("utf-8", "ignore")

    def hash_str_encode(self, data):
        return base64.b64encode(data)

    def compare_passwords(self, password_hash, other_password):
        return hmac.compare_digest(
            password_hash,
            hashlib.pbkdf2_hmac(PWD_HASH_ALGO, other_password.encode(), PWD_HASH_SALT, PWD_HASH_ITERATIONS)
        )

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


"""
"""

# здесь бизнес логика, в виде классов или методов. сюда импортируются DAO классы из пакета dao и модели из dao.model
# некоторые методы могут оказаться просто прослойкой между dao и views,
# но чаще всего будет какая-то логика обработки данных сейчас или в будущем.

# Пример

# class BookService:
#
#     def __init__(self, book_dao: BookDAO):
#         self.book_dao = book_dao
#
#     def get_books(self) -> List["Book"]:
#         return self.book_dao.get_books()
