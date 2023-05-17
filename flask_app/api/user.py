from flask import Blueprint, jsonify, request

user = Blueprint('user', __name__)

# link acutal database
users = {}

@user.route('/user', methods=['POST'])
def create_user():
    data = request.get_json()
    users[data['id']] = data
    return jsonify(data), 201

@user.route('/user/<id>', methods=['GET'])
def get_user(id):
    if id in users:
        return jsonify(users[id])
    else:
        return jsonify({"error": "not found"}), 404