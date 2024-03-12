from dotenv import load_dotenv
load_dotenv()
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from flask_bcrypt import Bcrypt
from GolfCarry_App.config import Config
import os

app = Flask(__name__)
app.config.from_object(Config)
app.secret_key = os.urandom(24)

db = SQLAlchemy(app)

###########################
# Authentication
###########################

# TODO: Add authentication setup code here!

login_manager = LoginManager()
login_manager.login_view = 'auth.login'
login_manager.init_app(app)

from GolfCarry_App.models import User

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(user_id)

bcrypt = Bcrypt(app)

###########################
# Blueprints
###########################

from GolfCarry_App.main.routes import main as main_routes
app.register_blueprint(main_routes)

from GolfCarry_App.auth.routes import auth as auth_routes
app.register_blueprint(auth_routes)

with app.app_context():
    db.create_all()