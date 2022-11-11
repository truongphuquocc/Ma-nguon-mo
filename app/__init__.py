from flask import Flask
from config import Config

app = Flask(__name__)

from app import routes
app.config.from_object(Config)

from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
app.app_context().push()

db = SQLAlchemy(app)
migrate = Migrate(app, db)

from app import models

