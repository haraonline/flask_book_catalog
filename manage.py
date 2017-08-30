from app import create_app, db
from app.auth.models import User

if __name__ == '__main__':
    app = create_app('prod')
    with app.app_context():
        db.create_all()
        if not User.query.filter_by(user_name='harry').first():
            User.create_user(user='harry', email='harry@potters.com', password='secret')
    app.run(host='127.0.0.1', port=5432)
