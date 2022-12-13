from flask import Flask
from src.database.models import db, ProductModel
from src.routes_controllers_blueprint.product import Product 
import os

def create_app(testconfig = None):
    app = Flask(__name__, instance_relative_config= True)
    if testconfig is None:
        app.config.from_mapping(
        SECRET_KEY = os.environ.get("SECRET_KEY"),
        SQLALCHEMY_DATABASE_URI = os.environ.get('SQLALCHEMY_DATABASE_URI'),
        )
    else:
        app.config.from_mapping(testconfig)

    db.app = app
    db.init_app(app)
    app.register_blueprint(Product)
        

    @app.before_first_request
    def create_table():
        db.create_all()

    return app
    