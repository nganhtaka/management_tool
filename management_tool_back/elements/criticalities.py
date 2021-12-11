from flask import Blueprint

from elements import db, get_elements

criticality = db.collection('criticalities')
simple_criticality = Blueprint('criticality', __name__)


@simple_criticality.route('/list', methods=['GET'])
def get_task():
    return get_elements(criticality)
