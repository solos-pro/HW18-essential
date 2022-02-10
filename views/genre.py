from flask import request
from flask_restx import Resource, Namespace
from config_db import db


genre_ns = Namespace('genres')


@genre_ns.route('/')
class GenresView(Resource):
    def get(self):
        genre_id = request.args.get('name')
        res = Genre.query
        if genre_id is not None:
            res = res.filter(Genre.id == genre_id)
        result = res.all()
        return genre_schema.dump(result, many=True), 200

    def post(self):
        r_json = request.json
        add_genre = Genre(**r_json)
        with db.session.begin():
            db.session.add(add_genre)
        return "", 201


@genre_ns.route('/<int:uid>')
class GenreView(Resource):
    def get(self, uid):
        genre = Genre.query.get(uid)
        if not genre:
            return "", 404
        return genre_schema.dump(genre)

    def put(self, uid):
        genre = Genre.query.get(uid)
        if not genre:
            return "", 404

        genre.name = request.json.get("name")
        db.session.add(genre)
        db.session.commit()
        return "", 204

    def delete(self, uid):
        genre = Genre.query.get(uid)
        if not genre:
            return "", 404
        db.session.delete(genre)
        db.session.commit()
        return "", 204