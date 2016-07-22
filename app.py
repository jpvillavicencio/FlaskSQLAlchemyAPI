# app.py
# Main file for Demo App
# author = JP Villavicencio
# email = contact@jpvillavicencio.com
# status = Prototype
# last revision = 22 July 2016

from flask import Flask, make_response, jsonify
from blueprints import index_blueprint, users_blueprint, postcodes_blueprint
from database import db


def create_app():
    # Define the WSGI application object
    app = Flask(__name__)

    # Configurations
    app.config.from_object('config')
    app.debug = True
    db.init_app(app)

    # Add new blueprints below
    # e.g. app.register_blueprint(<name>_blueprint)
    app.register_blueprint(index_blueprint)
    app.register_blueprint(users_blueprint)
    app.register_blueprint(postcodes_blueprint)

    @app.errorhandler(404)
    def not_found(error):
        return make_response(jsonify({'status': 'failed', 'reason': 'no results found'}), 404)

    return app


if __name__ == '__main__':
    app = create_app()
    app.run()




