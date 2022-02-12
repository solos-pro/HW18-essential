from app.dao.model.movie import Movie
from app.dao.model.genre import Genre
from app.dao.model.director import Director
# from app.database import db
# from sqlalchemy import label

# CRUD
class MovieDAO:
    def __init__(self, session):
        self.session = session

    def update(self, movie):
        self.session.add(movie)
        self.session.commit()
        self.session.refresh(movie)
        return movie.id

    def get_one(self, mid):
        return self.session.query(Movie.id, Movie.title, Movie.description, Movie.trailer, Movie.year, Movie.rating,
                                  Movie.director_id, Genre.name.label("genre"),
                                  Director.name.label("director")).join(Genre).join(Director).filter(Movie.id == mid).all()

    def get_original(self, mid):
        return self.session.query(Movie).get(mid)

    def get_all(self):
        return self.session.query(Movie).all()

    def create(self, data):
        movie = Movie(**data)
        return self.update(movie)

    def delete(self, mid):
        movie = self.get_original(mid)
        self.session.delete(movie)
        self.session.commit()


"""
class GenreDAO:
    def __init__(self, session):
        self.session = session

    def db_update(self, genre):
        self.session.add(genre)
        self.session.commit()
        self.session.refresh(genre)
        return genre.id

    def get_one(self, gid):
        return self.session.query(Genre).get(gid)

    def get_all(self):
        return self.session.query(Genre).all()

    def create(self, data):
        genre = Genre(**data)
        return self.db_update(genre)

    def delete(self, gid):
        genre = self.get_one(gid)
        self.session.delete(genre)
        self.session.commit()



# это файл для классов доступа к данным 
(Data Access Object). Здесь должен быть класс с 
методами доступа к данным
# здесь в методах можно построить сложные запросы 
к БД

# Например

# class BookDAO:
#     def get_all_books(self):
#         books = Book.query.all()
#         return

"""
