from flask import request, jsonify, Blueprint

from elements import db, get_elements

daily = db.collection('daily')
simple_daily = Blueprint('daily', __name__)


@simple_daily.route('/add', methods=['POST'])
def create_task():
    try:
        id = request.json['id']
        daily.document(id).set(request.json)
        return jsonify({"success": True}), 200
    except Exception as e:
        return f"An Error Occured: {e}"


@simple_daily.route('/list', methods=['GET'])
def get_daily():
    return get_elements(daily)


@simple_daily.route('/update', methods=['POST', 'PUT'])
def update_task():
    try:
        id = request.json['id']
        daily.document(id).update(request.json)
        return jsonify({"success": True}), 200
    except Exception as e:
        return f"An Error Occured: {e}"


@simple_daily.route('/delete', methods=['GET', 'DELETE'])
def delete_task():
    try:
        # Check for ID in URL query
        todo_id = request.args.get('id')
        daily.document(todo_id).delete()
        return jsonify({"success": True}), 200
    except Exception as e:
        return f"An Error Occured: {e}"
