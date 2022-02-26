class Config(object):
    DEBUG = True
    SECRET = 'test'
    SQLALCHEMY_DATABASE_URI = 'sqlite:///./test.db'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    # PWD_HASH_SALT = b'secret here'
    # PWD_HASH_ITERATIONS = 100_000
