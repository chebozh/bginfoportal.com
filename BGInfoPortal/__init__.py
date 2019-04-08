from flask import Flask
from flask_sqlalchemy import SQLAlchemy
# from flask_heroku import Heroku

from BGInfoPortal.config import Config

db = SQLAlchemy()


def create_app(config_class=Config):
    app = Flask(__name__)
    # heroku = Heroku()
    # heroku.init_app(app)
    app.config.from_object(config_class)
    db.init_app(app)

    from BGInfoPortal.main.routes import main
    from BGInfoPortal.errors.handlers import errors

    app.register_blueprint(main)
    app.register_blueprint(errors)

    return app
