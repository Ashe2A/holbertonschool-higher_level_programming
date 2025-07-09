#!/usr/bin/python3
from flask import Flask, request, jsonify
from flask_httpauth import HTTPBasicAuth
from werkzeug.security import generate_password_hash, check_password_hash
from flask_jwt_extended import create_access_token, jwt_required,\
    get_jwt_identity, JWTManager

app = Flask(__name__)
auth = HTTPBasicAuth()

app.config["JWT_SECRET_KEY"] = "secret"
jwt = JWTManager(app)


@jwt.unauthorized_loader
def handle_unauthorized_error(err):
    return jsonify({"error": "Missing or invalid token"}), 401


@jwt.invalid_token_loader
def handle_invalid_token_error(err):
    return jsonify({"error": "Invalid token"}), 401


@jwt.expired_token_loader
def handle_expired_token_error(err):
    return jsonify({"error": "Token has expired"}), 401


@jwt.revoked_token_loader
def handle_revoked_token_error(err):
    return jsonify({"error": "Token has been revoked"}), 401


@jwt.needs_fresh_token_loader
def handle_needs_fresh_token_error(err):
    return jsonify({"error": "Fresh token required"}), 401


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


@auth.verify_password
def verify_password(username, password):
    if username in users and\
        check_password_hash(users[username]["password"], password):
            return username, 200


@app.route('/basic-protected', methods=["GET"])
@auth.login_required
def index():
    return "Basic Auth: Access Granted", 200


@app.route('/login', methods=["POST"])
def login():    
    data = request.json
    if data and isinstance(data, dict):
        if "username" in data:
            username = data["username"]
        else:
            return jsonify({"error": "Username is required"}), 401

        if "password" in data:
            password = data["password"]
        else:
            return jsonify({"error": "Password is required"}), 401

        if username and username in users and password:
            if check_password_hash(
                users[username]["password"],
                password):
                return jsonify({
                    "access_token": create_access_token(identity={
                        "username": username,
                        "role": users[username]["role"]
                        })
                    }), 200
            return jsonify({"error": "Wrong password"}), 401
        return jsonify({"error": "Unknown username"}), 401
    else:
        return jsonify({"error": "Invalid JSON request"}), 401


@app.route("/jwt-protected", methods=["GET"])
@jwt_required()
def jwt_protected():
    return "JWT Auth: Access Granted", 200

@app.route("/admin-only", methods=["GET"])
@jwt_required()
def admin_protected_jwt():
    current_user = get_jwt_identity()
    if current_user in users:
        if users[current_user]["role"] == "admin":
            return jsonify({"msg": "Admin Access: Granted"}), 200
    return jsonify({"error": "Admin access required"}), 403


if __name__ == '__main__':
    app.run()
