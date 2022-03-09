import sqlalchemy
from typing import Optional

from sqlalchemy.exc import IntegrityError

from app.model.user import User

# CRUD
from app.exceptions import IncorrectData, DuplicateError


class UserDAO:
    def __init__(self, session):
        self.session = session
        self._roles = {"user", "admin"}

    def get_one_by_id(self, id):
        return self.session.query(User).get(id)

    def get_one_by_username(self, username) -> Optional[User]:
        return self.session.query(User).filter(User.username == username).one_or_none()

    def get_all(self):
        return self.session.query(User).all()

    def create(self, data):
        try:
            print(data)
            user = User(**data)
            self.session.add(user)
            self.session.commit()
            return user
        except IntegrityError as e:
            # print(str(e))
            raise DuplicateError


    def update_role(self, username: str, role: str):
        if role not in self._roles:
            raise IncorrectData

        user = self.get_one_by_username(username)
        user.role = role
        self.session.delete(user)
        self.session.commit()

    def update_password(self, username: str, password_hash: str):
        user = self.get_one_by_username(username)
        user.password = password_hash
        self.session.add(user)
        self.session.commit()

    def delete(self, uid):
        user = self.get_one_by_id(uid)
        self.session.delete(user)
        self.session.commit()
