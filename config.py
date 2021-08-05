from os import environ, path
from dotenv import load_dotenv

basedir = path.abspath(path.dirname(__file__))
load_dotenv(path.join(basedir, '.env'))


class Config:
    """Set Flask configuration from .env file."""

    # General Config
    SECRET_KEY = 'you-will-never-guess'
    FLASK_APP = 'application.py'
    FLASK_ENV = 'production'

    # Database
    # SQLite
    root = path.dirname(path.realpath(__file__))
    db_file = 'test.db'
    db_file = path.join(root,db_file)
    SQLALCHEMY_DATABASE_URI = ''.join(['sqlite:///', db_file])

    # mysql
    # username = 'diptoghosh'
    # password = 'mysql9433dip'
    # server = 'diptoghosh.mysql.pythonanywhere-services.com'
    # db = 'diptoghosh$mydb'
    # SQLALCHEMY_DATABASE_URI = 'mysql://' + username + ':' + password + '@' + server + '/' + db
    # SQLALCHEMY_ECHO = False
    # SQLALCHEMY_TRACK_MODIFICATIONS = False
    
    MQTT_BROKER_URL = 'mqtt.eclipseprojects.io'
    MQTT_BROKER_PORT = 1883
    MQTT_REFRESH_TIME = 1.0
