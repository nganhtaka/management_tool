from functools import wraps

from firebase_admin import auth
from flask import Blueprint, request

from elements import pb, check_token

simple_auth = Blueprint('authentication', __name__)

# Data source
users = [{'uid': 1, 'name': 'User Test'}]


# Api route to get users
@simple_auth.route('/userinfo')
@check_token
def userinfo():
    return {'data': users}, 200


# Api route to sign up a new user
@simple_auth.route('/signup')
def signup():
    email = request.form.get('email')
    password = request.form.get('password')
    if email is None or password is None:
        return {'message': 'Error missing email or password'}, 400
    try:
        user = auth.create_user(
            email=email,
            password=password
        )
        return {'message': f'Successfully created user {user.uid}'}, 200
    except:
        return {'message': 'Error creating user'}, 400


# Api route to get a new token for a valid user
@simple_auth.route('/authenticate')
def token():
    email = request.form.get('email')
    password = request.form.get('password')
    try:
        user = pb.auth().sign_in_with_email_and_password(email, password)
        jwt = user['idToken']
        return {'token': jwt}, 200
    except:
        return {'message': 'There was an error logging in'}, 400



