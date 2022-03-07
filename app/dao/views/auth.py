from flask import request
from flask_restx import Resource, Namespace, abort
from marshmallow import Schema, fields

from app.service.service_auth import AuthService
from app.container import


auth_ns = Namespace('auth')


@auth_ns.route('/')
class AuthView(Resource):
    def post(self):
        r_json = request.json
        username = r_json.get("username", None)
        password = r_json.get("password", None)
        if None in [username, password]:
            return "", 400

        tokens = AuthService.validate_jwt_generate(username, password)

        return tokens, 201

    def put(self):
        r_json = request.json
        token = r_json.get("refresh_token")
        tokens = AuthService.approve_refresh_token(token)
        return tokens, 201


'''
class Valid(Schema):
    username = fields.Str(required=True)
    password = fields.Str(required=True)

@auth_ns.route('/')
class AuthView(Resource):
    def post(self):
        try:
            validated_data = Valid().load(request.json)
            user = UserService.get_by_name(validated_data['username'])
            if not user:
                abort(404)
            token = {
                'user_id'
            }
        except Exception as e:
            abort(400, e)
'''
