from app import create_app, db

flask_app = create_app('prod')
db.create_all()
flask_app.run()


