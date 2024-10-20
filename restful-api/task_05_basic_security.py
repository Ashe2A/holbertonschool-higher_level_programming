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

@app.route("/basic-protected", methods=["GET"])
def basic_auth(username, password):
    auth = request.authorization
    if not auth:
        return "Authentication required", 401
    elif username not in users:
        return "User doesn't exist", 401
    elif check_password_hash(users[username]["password"], password):
        return "Basic Auth: Access Granted", 200
    else:
        return "Basic Auth : Access Denied", 401

if __name__ == '__main__':
    app.run()
