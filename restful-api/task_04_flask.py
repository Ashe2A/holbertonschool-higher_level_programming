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
    return jsonify(user_list)


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
        dict: User JSON
    """
    if username in users:
        return jsonify(users[username])
    else:
        return jsonify({"error": "User not found"}), 404


@app.route("/add_user", methods=["POST"])
def add_user():
    """Add user to the user dictionary

    Returns:
        dict: JSON returns (message + user data / error)
    """
    if request.method == "POST":
        user_input = request.get_json()
        if user_input and "username" in user_input:
            users[user_input["username"]] = user_input
            return jsonify({
                "message": "User added",
                "user": user_input
                }), 201
        else:
                return jsonify({"error": "Username is required"}), 400
    else:
        return jsonify({"error": "Adding an user is a post request"}), 400


if __name__ == "__main__":
    app.run()
