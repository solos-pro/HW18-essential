from flask import request
from flask_restx import Resource, Namespace
# from app.database import db
from app.dao.model.movie import MovieSchema, Movie
from app.dao.model.genre import Genre
from app.dao.model.director import Director
from app.container import movie_service

movie_ns = Namespace('movies')
movie_schema = MovieSchema()


@movie_ns.route('/')
class MoviesView(Resource):
    def get(self):
        director_id = request.args.get('director_id')
        genre_id = request.args.get('genre_id')
        res = db.session.query(Movie.id, Movie.title, Genre.name).join(Genre).join(Director)
        if director_id is not None:
            res = res.filter(Movie.director_id == director_id)
        if genre_id is not None:
            res = res.filter(Movie.genre_id == genre_id)
        if genre_id is not None and director_id is not None:
            res = res.filter(Movie.genre_id == genre_id, Movie.director_id == director_id)
        result = res.all()

        return movie_schema.dump(result, many=True), 200

    def post(self):
        r_json = request.json
        movie_service.create(r_json)
        return "", 201


@movie_ns.route('/<int:mid>')
class MovieView(Resource):
    def get(self, mid):
        movie = movie_service.get_one(mid)
        return movie_schema.dump(movie, many=True)

    def put(self, mid):
        reg_json = request.json
        reg_json["id"] = mid
        movie_service.update(reg_json)
        return "", 204

    def patch(self, mid):
        reg_json = request.json
        reg_json["id"] = mid
        movie_service.update_partial(reg_json)
        return "", 204

    def delete(self, mid: int):
        movie_service.delete(mid)
        return "", 204