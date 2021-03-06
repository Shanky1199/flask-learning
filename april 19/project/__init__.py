from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager 
db = SQLAlchemy()
def create_app():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = '9OLW'
    app.config['SQLALCHEMY_DATABASE_URI'] = "postgresql://postgres:root@localhost:5432/user"
    db.init_app(app)

    login_manager = LoginManager()
    login_manager.login_view = 'auth.login'
    login_manager.init_app(app)

    from .models import User
    @login_manager.user_loader
    def load_user(user_id):
        return User.query.get(int(user_id))

    #this usually will take blueprint to the auth
    from .auth import auth as auth_blueprint
    app.register_blueprint(auth_blueprint)

    # same way here to main.py
    
    from .main import main as main_blueprint
    app.register_blueprint(main_blueprint)

    return app