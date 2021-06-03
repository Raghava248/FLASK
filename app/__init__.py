from app.views.index import HelloWord
from flask import Flask
from flask_restful import Api
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate, migrate

migrate = Migrate()
db = SQLAlchemy()
def create_app():

    app = Flask(__name__)
    api = Api(app)
    api.add_resource(HelloWord,'/')
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    app.config['SQLALCHEMY_DATABASE_URI'] = "postgresql://postgres:1234@localhost/flask"
    db.init_app(app)
    migrate.init_app(app,db)
    return app