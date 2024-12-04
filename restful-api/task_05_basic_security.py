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

@auth.verify_password
def verify_password(username, password):
    if username in users and \
            check_password_hash(users.get(username), password):
        return username

@app.route("/basic-protected", methods=["GET"])
@auth.login_required
def basic_auth():
    return jsonify({"message": "Basic Auth: Access Granted"}), 200


if __name__ == '__main__':
    app.run()
