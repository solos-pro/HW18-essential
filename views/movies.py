from flask import Flask, request
from flask_restx import Api, Resource, Namespace

movie_ns = Namespace('movies')


@movie_ns.route('/')
class MoviesView(Resource):
    pass


@movie_ns.route('/<int: mid>')
class MoviesView(Resource):
    pass

