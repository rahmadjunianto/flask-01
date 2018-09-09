from flask import Flask


def create_app():
    app = Flask (__name__)

    @app.route('/')
    def index():
        return 'Halo Flask, ini hot reload '


    @app.route('/about')
    def about():
        return 'About Me'

    return app