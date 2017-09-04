from urllib.parse import urlparse

DEBUG = False
SECRET_KEY = 'topsecret'
SQLALCHEMY_DATABASE_URI = urlparse('DATABASE_URL').netloc
SQLALCHEMY_TRACK_MODIFICATIONS = False
