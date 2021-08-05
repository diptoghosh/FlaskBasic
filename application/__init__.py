from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_socketio import SocketIO
from flask_mqtt import Mqtt
import eventlet

db = SQLAlchemy()

eventlet.monkey_patch()

app = Flask(__name__, instance_relative_config=False)
app.config.from_object('config.Config')

# MQTT
mqtt = Mqtt(app)
socketio = SocketIO(app)

db.init_app(app)

from . import routes, models
