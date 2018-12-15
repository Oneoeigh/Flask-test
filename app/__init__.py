import eventlet
import redis
from flask import Flask
from config import Config
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_login import LoginManager
from flask_socketio import SocketIO

# Greenify all standard libs
eventlet.monkey_patch()

# Define extensions
db = SQLAlchemy()
migrate = Migrate()
login_manager = LoginManager()
socketio = SocketIO()

# Create app
app = Flask(__name__)
app.config.from_object(Config)
# config extensions
db.init_app(app)
migrate.init_app(app, db)
login_manager.init_app(app)
socketio.init_app(app, message_queue='redis://127.0.0.1:6379/0', async_mode="eventlet")

login_manager.login_view = 'app.login'

from app import routes, models