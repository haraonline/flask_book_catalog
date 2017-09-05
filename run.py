from app import create_app, db
from app.auth.models import User

flask_app = create_app('prod')
with flask_app.app_context():
    db.create_all()
    if User.query.filter_by(user_name='harry').first() is None:
        User.create_user(user='harry', email='harry@potters.com', password='secret')
        flask_app.run()


