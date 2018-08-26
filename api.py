#!/usr/bin/env python
import sys
import requests
from time import time
from datetime import datetime
from flask import Flask, request, jsonify
from flask_restful import Resource, Api

app = Flask(__name__)
api = Api(app)

def gettimestamp():
    now = time()
    timestamp = datetime.fromtimestamp(now).strftime('%d-%m-%Y %H:%M:%S')
    jsonTimestamp = {'timestamp': timestamp}
    return jsonTimestamp

class Responder(Resource):
    def get(self):
        response = gettimestamp()
        return response

    def post(self):
        def logthis(esdata,
                    eshost='http://elasticsearch:9200',
                    esindex='eventlog'):
            '''
            Saves data into Elasticsearch.
            '''
            URL = '{}/{}/_doc'.format(eshost,esindex)
            R = requests.post(URL, json=esdata)
            if R.status_code != "201":
                return False

        logthis(gettimestamp())
        return gettimestamp(), 201

api.add_resource(Responder, '/app')

if __name__ == '__main__':
    app.run(port=8080, host='0.0.0.0', threaded=True)
