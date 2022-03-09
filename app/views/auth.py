from flask import request
from flask_restx import Resource, Namespace, abort
from marshmallow import Schema, fields, ValidationError
from werkzeug.exceptions import BadRequest

from app.exceptions import DuplicateError
from app.service.service_auth import AuthService
from app.service.service_user import UserService
from app.container import user_service
from app.tools.jwt_token import JwtSchema, JwtToken

# Debugger doesn't launch

'''
from app.container import director_service
from app.dao.model.director import DirectorSchema

director_ns = Namespace('directors')
director_schema = DirectorSchema()
'''
auth_ns = Namespace('auth')





class LoginValidator(Schema):
    username = fields.Str(required=True)
    password = fields.Str(required=True)
    role = fields.Str()



@auth_ns.route('/')
class AuthView(Resource):

    def post(self):
        """ Create tokens """
        try:
            validated_data = LoginValidator().load(request.json)
            user = user_service.get_by_username(validated_data['username'])
            if not user:
                abort(404)

            token_data = JwtSchema().load({'user_id': user.id, 'role': user.role})

            return JwtToken(token_data).get_tokens(), 201



        except ValidationError:
            abort(400)

    def put(self):
        """ Update refresh token """
        ...

'''
@auth_ns.route('/')
class AuthView(Resource):
    def post(self):
        r_json = request.json
        print(r_json)

        username = r_json.get("username")
        password = r_json.get("password", None)
        print(username, password, "request.json")
        if None in [username, password]:
            return "", 400

        tokens = user_service.validate_jwt_generate(username, password, False)

        return tokens, 201

    def put(self):
        r_json = request.json
        token = r_json.get("refresh_token")
        tokens = AuthService.approve_refresh_token(token)
        return tokens, 201

'''