from flask import request
from flask_restx import Resource, Namespace

from app.container import genre_service
from app.dao.model.genre import GenreSchema

genre_ns = Namespace('genres')
genre_schema = GenreSchema()


@genre_ns.route('/')
class GenresView(Resource):
    def get(self):
        all_genres = genre_service.get_all()
        return genre_schema.dump(all_genres, many=True), 200

    def post(self):
        r_json = request.json
        genre_service.create(r_json)
        return "", 201


@genre_ns.route('/<int:gid>')
class GenreView(Resource):

    def get(self, gid):
        genre = genre_service.get_one(gid)
        if not genre:
            return "", 404
        return genre_schema.dump(genre)

    def put(self, gid):
        reg_json = request.json
        reg_json["id"] = gid

        genre_service.get_update(reg_json)

        return "", 204

    def patch(self, gid):
        reg_json = request.json
        reg_json["id"] = gid

        genre_service.update_partial(reg_json)

        return "", 204

    def delete(self, gid):
        genre_service.delete(gid)

        return "", 204

"""
# здесь контроллеры/хендлеры/представления для обработки запросов (flask ручки). сюда импортируются сервисы из пакета service

# Пример
# from flask_restx import Resource, Namespace
#
# book_ns = Namespace('books')
#
#
# @book_ns.route('/')
# class BooksView(Resource):
#     def get(self):
#         return "", 200
#
#     def post(self):
#         return "", 201
"""