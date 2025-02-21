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
        return jsonify({"error": "User not found"}), 404
    else:
        return jsonify(users[username])


@app.route("/add_user", methods=["POST"])
def post_user():
    new_user_json = request.json
    if not new_user_json or "username"	 not in new_user_json:
        return jsonify({"error": "Username is required"}), 400
    else:
        res = {"message": "User added"}
        users[new_user_json["username"]] = new_user_json
        res["user"] = users[new_user_json["username"]]
        return jsonify(res), 201


if __name__ == "__main__":
    app.run()
