from app.dao.user_dao import UserDAO


class UserService:
    def __init__(self, dao: UserDAO):
        self.dao = dao

    def search(self, user):
        return self.dao.get_one(user)

    def get_one(self, uid):
        return self.dao.get_by_username(uid)

    def get_by_username(self, username):
        print(username, "username_UserService-layer")
        return self.dao.get_one_by_username(username)

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
