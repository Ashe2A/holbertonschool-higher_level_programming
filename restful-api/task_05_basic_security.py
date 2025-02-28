#!/usr/bin/python3
"""
API Security and Authentication Techniques
"""

from flask import Flask
from flask import jsonify
from flask_httpauth import HTTPBasicAuth
from werkzeug.security import generate_password_hash
from werkzeug.security import check_password_hash


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
app = Flask(__name__)
auth = HTTPBasicAuth()


@auth.verify_password
def verify_password(username, password):
    if username in users and \
            check_password_hash(users.get(username), password):
        return username


@app.route("/basic-protected", methods=["GET"])
@auth.login_required
def basic_protected():
    return jsonify({"message": "Basic Auth: Access Granted"})


if __name__ == '__main__':
    app.run()
