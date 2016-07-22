# models/model.py
# description = schemas for tables in the database
# author = JP Villavicencio
# email = contact@jpvillavicencio.com
# status = Prototype
# last revision = 22 July 2016

from database import db


class Postcodes(db.Model):
    __tablename__ = 'postcodes'
    id = db.Column('idpostcode', db.Integer, primary_key=True)
    postcode = db.Column(db.String)
    suburb = db.Column(db.String)
    state = db.Column(db.String)
    lat = db.Column(db.Float)
    long = db.Column(db.Float)

    def __init__(self, postcode, suburb, state, lat, long):
        self.postcode = postcode
        self.suburb = suburb
        self.state = state
        self.lat = lat
        self.long = long

    @property
    def serialize(self):
        """Return object data in easily serializeable format"""
        return {
            'id': self.id,
            'postcode': self.postcode,
            'suburb': self.suburb,
            'state': self.state,
            'lat': self.lat,
            'long': self.long
        }

class Users(db.Model):
    __tablename__ = 'users'
    id = db.Column('idusers', db.Integer, primary_key=True)
    fname = db.Column(db.String)
    lname = db.Column(db.String)
    dob = db.Column(db.String)
    postcode = db.Column(db.Integer)

    def __init__(self, fname, lname, dob, postcode):
        self.fname = fname
        self.lname = lname
        self.dob = dob
        self.postcode = postcode

    @property
    def serialize(self):
        """Return object data in easily serializeable format"""
        return {
            'id': self.id,
            'fname': self.fname,
            'lname': self.lname,
            'dob': self.dob,
            'postcode': self.postcode
        }

