# database.py
# description = configurations for the app
# author = JP Villavicencio
# email = contact@jpvillavicencio.com
# status = Prototype
# last revision = 22 July 2016

# Change the url to you local database
SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://root:root@localhost/flask_test'
DEBUG = True
SQLALCHEMY_ECHO = False
SQLALCHEMY_TRACK_MODIFICATIONS = True