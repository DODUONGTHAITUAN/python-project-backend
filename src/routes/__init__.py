def routes(app):
    from .home import home
    from .auth import auth

    app.register_blueprint(home, url_prefix="/")
    app.register_blueprint(auth, url_prefix="/auth")
