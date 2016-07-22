# blueprint/index.py
# description = routes for index and etc
# author = JP Villavicencio
# email = contact@jpvillavicencio.com
# status = Prototype
# last revision = 22 July 2016

from flask import Blueprint, jsonify

index_blueprint = Blueprint('index', __name__)


@index_blueprint.route('/')
def home_page():
    return jsonify({'status': 'alive', 'comment': 'welcome to the home page'}), 200


@index_blueprint.route('/api')
def api():
    '''Returns API status.'''
    return jsonify({'status': 'alive', 'hello': 'world'}), 200
