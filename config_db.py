# Это файл конфигурации приложения, здесь может храниться путь к БД, ключ шифрования, что-то еще.
# Чтобы добавить новую настройку, допишите ее в класс.

from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import raw_data


    # DEBUG = True
    # SECRET_HERE = 'text'
    # SQLALCHEMY_DATABASE_URI = 'sqlite:///:memory:'
    # SQLALCHEMY_TRACK_MODIFICATIONS = True


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///test.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

class Director(db.Model):
    __tablename__ = 'director'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255))


class Genre(db.Model):
    __tablename__ = 'genre'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255))


class Movie(db.Model):
    __tablename__ = 'movie'
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(255))
    description = db.Column(db.String(255))
    trailer = db.Column(db.String(255))
    year = db.Column(db.Integer)
    rating = db.Column(db.Float)
    genre_id = db.Column(db.Integer, db.ForeignKey('genre.id'))
    genre = db.relationship('Genre')
    director_id = db.Column(db.Integer, db.ForeignKey('director.id'))
    director = db.relationship('Director')


db.drop_all()
db.create_all()

for movie in raw_data.movies:
    m = Movie(
        id=movie["pk"],
        title=movie["title"],
        description=movie["description"],
        trailer=movie["trailer"],
        year=movie["year"],
        rating=movie["rating"],
        genre_id=movie["genre_id"],
        director_id=movie["director_id"],
    )
    with db.session.begin():
        db.session.add(m)

for director in raw_data.directors:
    d = Director(
        id=director["pk"],
        name=director["name"],
    )
    with db.session.begin():
        db.session.add(d)

for genre in raw_data.genres:
    d = Genre(
        id=genre["pk"],
        name=genre["name"],
    )
    with db.session.begin():
        db.session.add(d)
