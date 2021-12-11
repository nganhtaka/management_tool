from flask import Blueprint

from elements import db, get_elements

levels = db.collection('levels')
simple_level= Blueprint('level', __name__)


@simple_level.route('/list', methods=['GET'])
def get_task():
    return get_elements(levels)
