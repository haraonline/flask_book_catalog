from app import create_app, db
from app.auth.models import User

flask_app = create_app('prod')
with flask_app.app_context():
    if not User.query.filter_by(user_name='harry').first():
        User.create_user(user='harry', email='harry@potters.com', password='secret')
    db.create_all()
    flask_app.run()


