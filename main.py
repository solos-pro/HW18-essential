from flask import Flask
from app.config import Config

def create_app(config: Config) -> Flask:
    pass

def configure_app(application: Flask):
    pass

if __name__ == '__main__':
    app_config = Config()
    app = create_app(app_config)
    configure_app(app)
    app.run()

