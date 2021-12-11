import json
from functools import wraps

import pyrebase
from firebase_admin import firestore, credentials, initialize_app, auth
from flask import request, jsonify

# Initialize Firestore DB
cred = credentials.Certificate('key.json')
default_app = initialize_app(cred)
db = firestore.client()
pb = pyrebase.initialize_app(json.load(open('fbconfig.json')))


def check_token(f):
    @wraps(f)
    def wrap(*args, **kwargs):
        if not request.headers.get('authorization'):
            return {'message': 'No token provided'}, 400
        try:
            user = auth.verify_id_token(request.headers['authorization'])
            request.user = user
        except:
            return {'message': 'Invalid token provided.'}, 400
        return f(*args, **kwargs)

    return wrap


#@check_token
def get_elements(an_object):
    try:
        # Check if ID was passed to URL query
        an_id = request.args.get('id')
        if an_id:
            todo = an_object.document(an_id).get()
            return jsonify(todo.to_dict()), 200
        else:
            all_elements = [doc.to_dict() for doc in an_object.stream()]
            return jsonify(all_elements), 200
    except Exception as e:
        return f"An Error Occured: {e}"

