from urllib.parse import urlparse
import os

DEBUG = False
SECRET_KEY = 'topsecret'
SQLALCHEMY_DATABASE_URI = urlparse(os.environ['DATABASE_URL']).netloc
SQLALCHEMY_TRACK_MODIFICATIONS = False
