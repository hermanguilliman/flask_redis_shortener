from flask import Flask
from flask_bootstrap import Bootstrap
from flask_redis import FlaskRedis

from config import Config

app = Flask(__name__)
Bootstrap(app)
app.config.from_object(Config)
redis = FlaskRedis(app)


from app import routes, services
