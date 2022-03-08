from flask import request
from flask_restx import Resource, Namespace

from app.container import user_service
from app.dao.model.user import UserSchema

user_ns = Namespace('users')
user_schema = UserSchema()


@user_ns.route('/')
class GenresView(Resource):
    def get(self):
        all_genres = user_service.get_all()
        return user_schema.dump(all_genres, many=True), 200

    def post(self):
        r_json = request.json
        user_service.create(r_json)
        return "", 201


@user_ns.route('/<int:gid>')
class GenreView(Resource):

    def get(self, gid):
        user = user_service.get_one(gid)
        if not user:
            return "", 404
        return user_schema.dump(user)

    def put(self, gid):
        reg_json = request.json
        reg_json["id"] = gid

        user_service.get_update(reg_json)

        return "", 204

    def patch(self, gid):
        reg_json = request.json
        reg_json["id"] = gid

        user_service.update_partial(reg_json)

        return "", 204

    def delete(self, gid):
        user_service.delete(gid)

        return "", 204
