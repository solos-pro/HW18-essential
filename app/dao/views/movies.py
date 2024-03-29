from flask import request
from flask_restx import Resource, Namespace
from app.dao.model.movie import MovieSchema, MovieSchemaSearch
from app.container import movie_service

movie_ns = Namespace('movies')
movie_schema = MovieSchema()
movie_schema_search = MovieSchemaSearch()


@movie_ns.route('/')
class MoviesView(Resource):
    def get(self):
        search_request = {"director_id": request.args.get('director_id'), "genre_id": request.args.get('genre_id')}
        result = movie_service.search(search_request)
        return movie_schema_search.dump(result, many=True), 200

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