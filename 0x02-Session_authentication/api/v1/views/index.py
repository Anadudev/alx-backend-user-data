#!/usr/bin/env python3
""" Module of Index views
"""
from flask import jsonify, abort
from api.v1.views import app_views


@app_views.route("/status", methods=["GET"], strict_slashes=False)
def status() -> str:
    """GET /api/v1/status
    Return:
      - the status of the API
    """
    return jsonify({"status": "OK"})


@app_views.route(
    "/users/<int:user_id>", methods=["GET", "PUT", "DELETE"], strict_slashes=False
)
def users_id() -> str:
    """GET /api/v1/users_id
    Return:
      - the user_id of the API
    """
    return jsonify({"status": "OK"})


@app_views.route("/users", methods=["GET", "POST"], strict_slashes=False)
def users() -> str:
    """GET /api/v1/users
    Return:
      - the users of the API
    """
    return jsonify({"status": "OK"})


@app_views.route("/stats/", strict_slashes=False)
def stats() -> str:
    """GET /api/v1/stats
    Return:
      - the number of each objects
    """
    from models.user import User

    stats = {}
    stats["users"] = User.count()
    return jsonify(stats)


@app_views.route("/unauthorized/", methods=["GET"], strict_slashes=False)
def unauthorized():
    """GET /api/v1/unauthorized"""
    abort(401)


@app_views.route("/forbidden/", methods=["GET"], strict_slashes=False)
def forbidden():
    """GET /api/v1/forbidden"""
    abort(403)
