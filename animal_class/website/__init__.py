from flask import Flask

def create_app():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = 'x831jo239nx903109jxğ02jx'

    from .views import views

    app.register_blueprint(views, url_prefix="/")

    return app
