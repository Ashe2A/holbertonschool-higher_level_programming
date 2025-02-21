#!/usr/bin/python3
"""
Develop a Simple API using Python with Flask
"""

from flask import Flask
from flask import jsonify
from flask import request

app = Flask(__name__)
users = {}


@app.route("/")
def home():
    return "Welcome to the Flask API!"


@app.route("/data")
def jsonify_data():
    usernames = []
    for i in users:
        usernames.append(i)
    return jsonify(usernames)


@app.route("/status")
def status():
    return "OK"


@app.route("/users/<username>")
def user_fetch(username):
    if username not in users:
        return {"error": "User not found"}, 404
    else:
        return jsonify(users[username])


@app.route("/add_user", methods=["POST"])
def add_user():
    incoming_json = request.json
    if not incoming_json or "username" not in incoming_json:
        return jsonify({"error": "Username is required"}), 400
    elif incoming_json["username"] in users:
        return jsonify({"message": "User already exists",
                        "user": incoming_json["username"]}), 409
    else:
        username = incoming_json["username"]
        users[username] = incoming_json
        return jsonify({"message": "User added", "user": users[username]}), 201


if __name__ == "__main__":
    app.run()
