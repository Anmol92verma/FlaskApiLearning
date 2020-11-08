from flask import request, jsonify, Blueprint

from database import mysql

userBlueprint = Blueprint('userBlueprint', __name__)


@userBlueprint.route('/signup')
def create_user():
    name = request.json['name']
    uname = request.json['username']
    id = request.json['id']

    conn = mysql.get_db()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM employee where email = %s", uname)
    data = cursor.fetchall()
    if cursor.rowcount == 1:
        return jsonify({'status': 201, 'message': "User already exist"})
    else:
        sql = "INSERT INTO employee (id, email,name) VALUES (%s, %s,%s)"
        val = (id, uname, name)
        cursor.execute(sql, val)
        conn.commit()
        return jsonify({'status': 200, 'message': "User Created"})
