# Это файл конфигурации приложения, здесь может хранится путь к бд, ключ шифрования, что-то еще.
# Чтобы добавить новую настройку, допишите ее в класс.


class Config(object):
    DEBUG = True
    SECRET_HERE = 'text'
    SQLALCHEMY_DATABASE_URI = 'sqlite:///./movie.db'
    SQLALCHEMY_TRACK_MODIFICATIONS = True
