from flask import request
from flask_restx import Resource, Namespace
from config_db import db


movie_ns = Namespace('movie')


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
        add_movie = Movie(**r_json)
        with db.session.begin():
            db.session.add(add_movie)
        return "", 201


@movie_ns.route('/<int:uid>')
class MovieView(Resource):
    def get(self, uid):
        movie = db.session.query(Movie.id, Movie.title, Movie.description, Movie.trailer, Movie.year, Movie.rating,
                                 Movie.director_id, Genre.name.label("genre"),
                                 Director.name.label("director")).join(Genre).join(Director).filter(Movie.id == uid).all()
        if not movie:
            return "", 404
        return movie_schema.dump(movie, many=True)

    def put(self, uid):
        movie = Movie.query.get(uid)
        if not movie:
            return "", 404

        movie.title = request.json.get("title")
        movie.description = request.json.get("description")
        movie.trailer = request.json.get("trailer")
        movie.year = request.json.get("year")
        movie.rating = request.json.get("rating")
        movie.genre = request.json.get("genre_id")
        movie.director_id = request.json.get("director_id")
        db.session.add(movie)
        db.session.commit()
        return "", 204

    def delete(self, uid):
        movie = Movie.query.get(uid)
        if not movie:
            return "", 404
        db.session.delete(movie)
        db.session.commit()
        return "", 204