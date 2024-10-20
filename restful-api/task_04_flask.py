#!/usr/bin/python3

"""
Flask
"""

from flask import Flask
from flask import jsonify
from flask import request


app = Flask(__name__)
users = {
    "jane": {
        "username": "jane",
        "name": "Jane",
        "age": 28,
        "city": "Los Angeles"
    },
    "john": {
        "username": "john",
        "name": "John",
        "age": 30,
        "city": "New York"
    }
}


@app.route("/")
def home():
    return "Welcome to the Flask API!"


@app.route("/data")
def data_jsonification():
    usernames = []
    for i in users:
        usernames.append(users[i]["username"])
    return jsonify(usernames)


@app.route("/status")
def status():
    return "OK"


@app.route("/users/<username>")
def user(username):
    if username not in users:
        return jsonify({"error": "User not found"}), 404
    else:
        return jsonify(users[username])


@app.route("/add_user/<username>", methods=['POST'])
def post_user(username):
    if username == "":
        return jsonify({"error": "Username is required"}), 400
    else:
        new_user_json = request.json
        users[username] = new_user_json
        res = {"message": "User added"}
        res[username] = new_user_json
        return jsonify(res), 201


if __name__ == "__main__":
    app.run()
