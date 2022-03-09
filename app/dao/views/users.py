from flask import request
from flask_restx import Resource, Namespace
from marshmallow import ValidationError
from werkzeug.exceptions import BadRequest

from app.container import user_service
from app.dao.model.user import UserSchema
from app.dao.views.auth import LoginValidator
from app.exceptions import DuplicateError
from app.tools.auth import login_required
from app.tools.jwt_token import JwtSchema

user_ns = Namespace('users')
user_schema = UserSchema()


@user_ns.route('/all/')
class UserView(Resource):
    def get(self):
        all_genres = user_service.get_all()
        return user_schema.dump(all_genres, many=True), 200

    def post(self):
        r_json = request.json
        user_service.create(r_json)
        return "", 201


@user_ns.route('/') # <int:uid>
class UserView(Resource):
    @login_required
    def get(self, token_data):
        user = user_service.get_one(token_data['user_id'])
        if not user:
            return "", 404
        return user_schema.dump(user)

    def post(self):
        """ Create user """
        try:
            user_service.create(**LoginValidator().load(request.json))
        except ValidationError:
            raise BadRequest
        except DuplicateError:
            raise BadRequest('Username already exists')

    def put(self, uid):
        reg_json = request.json
        reg_json["id"] = uid

        user_service.get_update(reg_json)

        return "", 204

    def patch(self, uid):
        reg_json = request.json
        reg_json["id"] = uid

        user_service.update_partial(reg_json)

        return "", 204

    def delete(self, uid):
        user_service.delete(uid)

        return "", 204
