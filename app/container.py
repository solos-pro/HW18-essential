from app.database import db

from app.dao.movie_dao import MovieDAO
from app.dao.genre_dao import GenreDAO
from app.dao.director_dao import DirectorDAO

from app.service.service_genre import GenreService
from app.service.service_movie import MovieService
from app.service.service_director import DirectorService


movie_dao = MovieDAO(db.session)
movie_service = MovieService(movie_dao)

genre_dao = GenreDAO(db.session)
genre_service = GenreService(genre_dao)

director_dao = DirectorDAO(db.session)
director_service = DirectorService(director_dao)
