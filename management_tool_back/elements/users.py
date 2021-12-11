from flask import Blueprint

from elements import db, get_elements

users = db.collection('users')
simple_user = Blueprint('user', __name__)


@simple_user.route('/list', methods=['GET'])
def get_task():
    return get_elements(users)
