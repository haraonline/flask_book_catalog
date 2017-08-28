# app/auth/__init__.py
from flask import Blueprint
authentication = Blueprint('authentication', __name__, template_folder='templates')
from app.auth import routes
