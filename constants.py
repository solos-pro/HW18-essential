CONSTANT_NAME = "value"
LOG_DIR = "logs"
# PWD_HASH_SALT = b'secret_here'  # bytes, so you don't need to use encode('utf-8') method
PWD_HASH_SALT = 'jkl3l20jd0132'.encode('utf-8')
PWD_HASH_ITERATIONS = 100_000
PWD_HASH_ALGO = 'sha256'
SECRET = "secret"
REFRESH_TOKEN_EXPIRATION = 30 # days
ACCESS_TOKEN_EXPIRATION = 180 # minutes

