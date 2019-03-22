import os


class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY')
    # local
    # SQLALCHEMY_DATABASE_URI = os.environ.get('SQLALCHEMY_DB_URI')
    # hk
    SQLALCHEMY_DATABASE_URI = os.environ['DATABASE_URL']
