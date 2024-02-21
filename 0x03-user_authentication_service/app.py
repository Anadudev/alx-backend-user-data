#!/usr/bin/env python3
"""a simple flask application"""
from flask import Flask, jsonify, request
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
    email = data.("email")
    password = data."(password")
    try:
        AUTH.register_user(email, password)
        return jsonify({"email": "", "message": "user created"})
    except Exception:
        return jsonify({"message": "email already registered"})


if __name__ == "__main__":
    app.run(host="0.0.0.0", port="5000")
