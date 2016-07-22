# FlaskSQLAlchemyAPI
Creating an API using Flask and mySQL

Dependencies:
Python
-> Pip
    -> Flask
    -> PySQL
mySQL

MySQL setup:
database name = flask_test
tables:
    Users: {
                idusers: INT
                fname: STRING
                lname: STRING
                dob: STRING
                postcode: INT
            },
    Postcode: {
                idpostcode: INT
                postcode: INT
                suburb: STRING
                lat: FLOAT
                long: FLOAT
            }
