#!/usr/bin/env python3
"""_summary_
"""
from flask import jsonify, request
from api.v1.views import app_views
from models.user import User
from os import getenv


@app_views.route("/auth_session/login", methods=["POST"], strict_slashes=False)
def status() -> str:
    """GET /api/v1/status
    Return:
        - the status of the API
    """
    email = request.form.get("email")
    password = request.form.get("password")
    if not email:
        return jsonify({"error": "email missing"}), 400
    if not password:
        return jsonify({"error": "password missing"}), 400
    user_search = User.search({"email": email})
    if not user_search:
        return jsonify({"error": "no user found for this email"}), 404
    for user in user_search:
        password_search = User.is_valid_password(password)
        if password_search:
            from api.v1.app import auth

            user_id = auth.create_session(user.id)
            SESSION_NAME = getenv("SESSION_NAME")
            data = jsonify(user.to_json())
            data.set_cookie(SESSION_NAME, user_id)
            return data
        return jsonify({"error": "wrong password"}), 401
