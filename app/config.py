from flask import Flask
from flask_marshmallow import Marshmallow

from .models import db

app = Flask(__name__)

DATABASE_URL = 'mysql+mysqlconnector://root:root@database/db'

app.config["SQLALCHEMY_DATABASE_URI"] = DATABASE_URL
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = True

db.init_app(app)

marsh = Marshmallow(app)
