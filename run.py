from app import create_app, db
# from app.auth.models import User

flask_app = create_app('prod')
flask_app.run()


