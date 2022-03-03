from app.dao.model.user import User

# CRUD


class UserDAO:
    def __init__(self, session):
        self.session = session

    def get_one(self, password):
        return self.session.query(User).filter(User.password == password).get_one()

    def create(self, data):
        user = User(**data)
        return self.update(user)

    def generate_pass_hash(self, passw):

        pass

    def update(self, data):

        pass

    def delete(self, uid):
        user = self.get_original(uid)
        self.session.delete(user)
        self.session.commit()