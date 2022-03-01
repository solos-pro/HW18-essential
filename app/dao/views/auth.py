from flask import request
from flask_restx import Resource, Namespace, abort
from marshmallow import Schema, fields

from app.service.service_user import UserService


auth_ns = Namespace('auth')


@auth_ns.route('/')
class AuthView(Resource):
    def post(self):
        r_json = request.json
        UserService.validate_jwt_generate(r_json)
        return "", 201


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
