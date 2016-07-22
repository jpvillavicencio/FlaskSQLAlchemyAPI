# blueprint/postcodes.py
# description = routes for postcodes
# author = JP Villavicencio
# email = contact@jpvillavicencio.com
# status = Prototype
# last revision = 22 July 2016

from flask import Blueprint, jsonify, abort
from models import model

postcodes_blueprint = Blueprint('postcode', __name__, url_prefix='/api/postcode')


@postcodes_blueprint.route('/', methods=['GET'])
@postcodes_blueprint.route('/<postcode>', methods=['GET'])
def postcode_route(postcode=None):
    results = []
    postcodes = model.Postcodes.query.all()
    if postcode is not None:
        for pc in postcodes:
            if str(pc.postcode) == postcode:
                result = {
                    'postcode': pc.postcode,
                    'suburb': pc.suburb,
                    'state': pc.state,
                }
                results.append(result)
    else:
        for pc in postcodes:
            result = {
                'id': pc.id,
                'postcode': pc.postcode,
                'suburb': pc.suburb,
                'state': pc.state,
                'lat': pc.lat,
                'long': pc.long
            }
            results.append(result)
    if len(results) < 1:
        abort(404)
    return jsonify(results)


@postcodes_blueprint.route('/suburb/<suburb>', methods=['GET'])
def suburb_route(suburb=None):
    results = []

    if suburb is not None:
        postcodes = model.Postcodes.query.filter_by(suburb=suburb.upper())
        for pc in postcodes:
            result = {
                'postcode': pc.postcode,
                'suburb': pc.suburb
            }
            results.append(result)
    else:
        postcodes = model.Postcodes.query.all()
        for pc in postcodes:
            result = {
                'id': pc.id,
                'postcode': pc.postcode,
                'suburb': pc.suburb,
                'state': pc.state,
                'lat': pc.lat,
                'long': pc.long
            }
            results.append(result)
    if len(results) == 0:
        abort(404)
    return jsonify(results)
