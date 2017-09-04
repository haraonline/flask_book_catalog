import os
from urllib.parse import urlparse

DEBUG = False
SECRET_KEY = 'topsecret'
SQLALCHEMY_DATABASE_URI = urlparse(os.environ["DATABASE_URL"])
SQLALCHEMY_TRACK_MODIFICATIONS = False
