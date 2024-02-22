#!/usr/bin/env python3
"""a simple flask application"""
from flask import Flask, jsonify, request, abort
from auth import Auth


app = Flask(__name__)
AUTH = Auth()


@app.route("/", methods=["GET"])
def home():
    """application home route"""
    return jsonify({"message": "Bienvenue"})


@app.route("/users", methods=["POST"])
def register_users():
    """method that handles user registration"""
    data = request.form
    email = data.get("email")
    password = data.get("password")
    try:
        AUTH.register_user(email, password)
        return jsonify({"email": f"{email}", "message": "user created"})
    except Exception:
        return jsonify({"message": "email already registered"}), 400


@app.route("/sessions", methods=["POST"])
def login():
    """method that validates user login"""
    data = request.form
    email = data.get("email")
    password = data.get("password")
    if not AUTH.valid_login(email, password):
        abort(401)
    session_id = AUTH.create_session(email)
    req = jsonify({"email": f"{email}", "message": "logged in"})
    req.set_cookie("session_id", session_id)
    return req


if __name__ == "__main__":
    app.run(host="0.0.0.0", port="5000")
