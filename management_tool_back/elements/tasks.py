from flask import Blueprint

from elements import db, get_elements
from elements.dailies import simple_daily

tasks = db.collection('tasks')
simple_task = Blueprint('task', __name__)


@simple_task.route('/list', methods=['GET'])
def get_task():
    return get_elements(tasks)
