from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_socketio import SocketIO

db = SQLAlchemy()

app = Flask(__name__, instance_relative_config=False)
app.config.from_object('config.Config')
socketio = SocketIO(app)
db.init_app(app)

from . import routes, models
