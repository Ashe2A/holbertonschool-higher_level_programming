#!/usr/bin/python3
from flask import Flask
from flask import jsonify
from flask import request

app = Flask(__name__)
users = {}


@app.route("/")
def home():
    """Homepage

    Returns:
        str: Welcoming text
    """
    return "Welcome to the Flask API!"

@app.route("/data")
def users_to_json():
    """List of all users

    Returns:
        list: list of all users added
    """
    user_list = []
    for i in users:
        user_list.append(i)
    return user_list

@app.route("/status")
def get_status():
    """Check the status of the site

    Returns:
        str: Just "ok" to confirm the API works
    """
    return "OK"

@app.route("/users/<username>")
def get_user(username):
    """Get user data by username

    Args:
        username (str): The username

    Returns:
        _type_: _description_
    """
    if username in users:
        return users[username]
    else:
        return {"error": "User not found"}

@app.route("/add_user", methods=["POST"])
def add_user():
    if request.method == "POST":
        user_input = request.get_json()
        if not "username" in request.form:
            users[user_input["username"]] = user_input
            return {
                "message": "User added",
                user_input["username"]: user_input
                }, 201
        else:
            return {"error": "Username is required"}, 400
    else:
        return {"error": "Adding an user is a post request"}, 400


if __name__ == "__main__":
    app.run()
