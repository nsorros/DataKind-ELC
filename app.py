#!flask/bin/python

from flask import Flask, request
from flask_restful import Resource, Api
from sqlalchemy import create_engine
import json

app = Flask(__name__)
api = Api(app)

class Lsoa(Resource):
    def get(self, lsoa_code):
        # Connect to database
        e = create_engine('sqlite:////media/windows-share/db_landcat.sqlite')
        conn = e.connect()
        
        #Perform query and return JSON data
        query = conn.execute("select distinct lsoa.postcode from lsoa where lsoa_11_cd='%s'"%lsoa_code.upper())
        
        #Query the result and get cursor.Dumping that data to a JSON is looked by extension
        result = {'data': [dict(zip(tuple (query.keys()) ,i)) for i in query.cursor]}
        return result

class Demo(Resource):
    def get(self):
        data = json.loads('farms_geo.json')
        return data

api.add_resource(Demo, '/', '/demo', '/demo/')
api.add_resource(Lsoa, '/lsoa/<string:lsoa_code>')

if __name__ == '__main__':
    app.run(debug=True)

