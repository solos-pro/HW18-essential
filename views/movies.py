from flask import Flask, request
from flask_restx import Api, Resource, Namespace

movie_ns = Namespace('movies')


@movie_ns.route('/')
class MoviesView(Resource):
    def get(self):
        director_id = request.args.get('director_id')
        genre_id = request.args.get('genre_id')
        # res = Movie.query
        # db.session.query(User.id, User.name, Group.name.label("grp_name")).join(Group).all()
        res = db.session.query(Movie.id, Movie.title, Genre.name).join(Genre).join(Director)
        if director_id is not None:
            res = res.filter(Movie.director_id == director_id)
        if genre_id is not None:
            res = res.filter(Movie.genre_id == genre_id)
        if genre_id is not None and director_id is not None:
            res = res.filter(Movie.genre_id == genre_id, Movie.director_id == director_id)
        result = res.all()

        return movie_schema.dump(result, many=True), 200


@movie_ns.route('/<int: mid>')
class MoviesView(Resource):
    pass

