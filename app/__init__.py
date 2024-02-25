from flask import Flask
from config import Config
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_login import LoginManager
from logging.handlers import RotatingFileHandler
import os
import logging
from logging.handlers import SMTPHandler


microblog_app = Flask(__name__)
microblog_app.config.from_object(Config)
db = SQLAlchemy(microblog_app)
migrate = Migrate(microblog_app, db)
login = LoginManager(microblog_app)
login.login_view = 'login'


if not microblog_app.debug:


    if not os.path.exists('logs'):
        os.mkdir('logs')
    file_handler = RotatingFileHandler('logs/microblog.log', maxBytes=10240,
                                       backupCount=10)
    file_handler.setFormatter(logging.Formatter(
        '%(asctime)s %(levelname)s: %(message)s [in %(pathname)s:%(lineno)d]'))
    file_handler.setLevel(logging.INFO)
    microblog_app.logger.addHandler(file_handler)

    microblog_app.logger.setLevel(logging.INFO)
    microblog_app.logger.info('Microblog startup')

from app import routes, models, errors
