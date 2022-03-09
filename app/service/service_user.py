from app.dao.user_dao import UserDAO
from app.tools.security import get_password_hash
from typing import Optional
from app.dao.user_dao import User


class UserService:
    def __init__(self, dao: UserDAO):
        self.dao = dao

    def search(self, user):
        return self.dao.get_one_by_id(user)

    def get_one(self, uid):
        return self.dao.get_one_by_username(uid)

    def get_by_username(self, username) -> Optional[User]:
        print(username, "username_UserService-layer")
        return self.dao.get_one_by_username(username)

    def create(self, username, password, role: str="user"):
        self.dao.create({
            "username": username,
            "password": get_password_hash(password),
            "role": role
        })
        return self.dao.create(data)

    def update(self, data):
        uid = data.get("id")
        user = self.dao.get_one_by_id(uid)

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
