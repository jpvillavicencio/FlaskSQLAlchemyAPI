# blueprint/users.py
# User Routes
# description = routes for users
# author = JP Villavicencio
# email = contact@jpvillavicencio.com
# status = Prototype
# last revision = 22 July 2016

from flask import Blueprint, jsonify, abort
from models import model

users_blueprint = Blueprint('users', __name__, url_prefix='/api/users')


@users_blueprint.route('/', methods=['GET'])
@users_blueprint.route('/<user>', methods=['GET'])
def suburb_route(user = None):
    results = []

    if user is not None:
        users = model.Users.query.filter_by(fname=user)
        for res in users:
            result = {
                'id': res.id,
                'fname': res.fname,
                'lname': res.lname,
                'dob': res.dob,
                'postcode': res.postcode
            }
            results.append(result)
    else:
        users = model.Users.query.all()
        for res in users:
            result = {
                'id': res.id,
                'fname': res.fname,
                'lname': res.lname,
                'dob': res.dob,
                'postcode': res.postcode
            }
            results.append(result)
    if len(results) < 1:
        abort(404)
    return jsonify(results)
