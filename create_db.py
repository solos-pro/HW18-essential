# Это файл конфигурации приложения, здесь может храниться путь к БД, ключ шифрования, что-то еще.
# Чтобы добавить новую настройку, допишите ее в класс.

from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import raw_data

from dao.model.director import Director
from dao.model.genre import Genre
from dao.model.movie import Movie

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///test.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

def create_data(raw_data):
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