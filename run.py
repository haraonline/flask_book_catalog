from app import create_app, db
from app.auth.models import User

flask_app = create_app('prod')
db.create_all()
flask_app.run()


