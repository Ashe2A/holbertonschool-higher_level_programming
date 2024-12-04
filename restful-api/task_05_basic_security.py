#!/usr/bin/python3

"""
Basic security
"""

from flask import Flask
from flask import jsonify
from flask import request
from werkzeug.security import generate_password_hash, check_password_hash

app = Flask(__name__)
users = {
    "user1": {
        "username": "user1",
        "password": generate_password_hash("password"),
        "role": "user"
        },
    "admin1": {
        "username": "admin1",
        "password": generate_password_hash("password"),
        "role": "admin"
        }
}
auth = request.authorization

@app.route("/basic-protected", methods=["GET"])
@auth.login_required
def basic_auth():
    if not auth:
        return jsonify({"message": "Authentication required"}), 401
    elif auth.username not in users:
        return jsonify({"message": "User doesn't exist"}), 401
    elif check_password_hash(users[auth.username]["password"], auth.password):
        return jsonify({"message": "Basic Auth: Access Granted"}), 200
    else:
        return jsonify({"message": "Basic Auth : Access Denied"}), 401


if __name__ == '__main__':
    app.run()
