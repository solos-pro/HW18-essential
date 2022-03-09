from app.model.movie import Movie


# CRUD
class MovieDAO:
    def __init__(self, session):
        self.session = session

    def search(self, search_request):
        result = self.session.query(Movie)
        if search_request["director_id"]:
            result = result.filter(Movie.director_id == search_request["director_id"])
        if search_request["genre_id"]:
            result = result.filter(Movie.genre_id == search_request["genre_id"])

        return result.all()

    def update(self, movie):
        self.session.add(movie)
        self.session.commit()
        self.session.refresh(movie)
        return movie.id

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
