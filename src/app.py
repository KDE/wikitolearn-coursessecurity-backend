#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import os,sys
from eve import Eve
from flask import jsonify
import json

mongo_host = os.environ.get("MONGO_HOST")
service_port = int(os.environ.get('SERVICE_PORT'))

eve_settings = {}
eve_settings['MONGO_HOST'] = mongo_host
eve_settings['MONGO_DBNAME'] = "coursessecurity"
eve_settings['DEBUG'] = True

eve_settings['SOFT_DELETE'] = True
eve_settings['API_VERSION'] = "v1"
eve_settings['VERSIONING'] = True
eve_settings['XML'] = False
eve_settings['RESOURCE_METHODS'] = ['GET', 'POST']
eve_settings['ITEM_METHODS'] = ['GET', 'PATCH', 'DELETE']
eve_settings['DOMAIN'] = {}
eve_settings['DOMAIN']['coursessecurity'] = {
    'schema': {
        'course': {
            'type': 'dict',
            'schema': {
                '_id': {'type': 'objectid'},
                '_version': {'type': 'integer'}
            },
        },
        'private':{
            'type': 'boolean',
            'default': False,
            'required': True
        },
        'owner_id':{
            'type': 'string'
        },
    },
}


app = Eve(settings=eve_settings)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=service_port)
