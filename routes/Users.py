from flask import request, jsonify, Blueprint

userBlueprint = Blueprint('userBlueprint', __name__)

users = []


@userBlueprint.route('/signup')
def create_user():
    name = request.json['name']
    uname = request.json['username']
    password = request.json['password']
    if len(name) == 0 or len(uname) == 0 or len(password) == 0:
        return jsonify({'status': 201, 'message': "Check the validations"})

    result = list(filter(lambda user: (user['username'] == uname), users))
    if len(result) == 0:
        users.append({
            'name': name,
            'username': uname,
            'password': password
        })
        return jsonify({'status': 200, 'message': "User Created"})
    else:
        return jsonify({'status': 201, 'message': "User already exist"})
