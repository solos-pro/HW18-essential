from flask import request
from flask_restx import Resource, Namespace, abort
from marshmallow import Schema, fields

from app.service.service_auth import AuthService
# from app.container import

# Debugger doesn't launch

'''
from app.container import director_service
from app.dao.model.director import DirectorSchema

director_ns = Namespace('directors')
director_schema = DirectorSchema()
'''
auth_ns = Namespace('auth')


@auth_ns.route('/')
class AuthView(Resource):
    # def post(self):
    #     r_json = request.json
    #     print(r_json)
    #     return "POST", 200
    def post(self):
        r_json = request.json
        print(r_json)

        # return "POST", 200
        username = r_json.get("username")
        password = r_json.get("password", None)
        print(username, password, "request.json")
        if None in [username, password]:
            return "", 400

        tokens = AuthService.validate_jwt_generate(username, password, False)

        return tokens, 201
        # else:
        #     return AuthService.validate_jwt_generate(username, password, False), 201

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
