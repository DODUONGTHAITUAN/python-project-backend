from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from os import environ
from .routes import routes
from .configs import config_app
from .configs.configDB import config_db


app = Flask(__name__)
db = SQLAlchemy(app)

from .models.allcodes import Allcode
from .models.user import User
from .models.order import Order
from .models.detail_product import DetailProduct
from .models.line_item import LineItem
from .models.option import Option
from .models.product import Product


def create_app():
    """Config app"""
    config_app(app)

    """Routes app"""
    routes(app)

    """Config database app"""
    config_db(app)
    db.init_app(app)

    db.create_all()

    # from .models.product import Product

    return app
