def routes(app):
    from .home import home
    from .auth import auth
    from .user import user
<<<<<<< HEAD
=======
    from .allcodes import allcodes
>>>>>>> dev
    from .product import product

    app.register_blueprint(home, url_prefix="/")
    app.register_blueprint(auth, url_prefix="/auth")
    app.register_blueprint(user, url_prefix="/user")
<<<<<<< HEAD
=======
    app.register_blueprint(allcodes, url_prefix="/allcodes")
>>>>>>> dev
    app.register_blueprint(product, url_prefix="/product")
