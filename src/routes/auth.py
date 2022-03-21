from flask import Blueprint

auth = Blueprint("auth", __name__)


@auth.route("/login")
def login():
    return "<h1>Hello auth Page</h1>"


@auth.route("/register")
def register():
    return "<h1>Hello world Register Page</h1>"
