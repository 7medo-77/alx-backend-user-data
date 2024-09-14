#!/usr/bin/env python3
""" Module of Index views
"""
from flask import jsonify, request
from models.user import User
from os import getenv
from api.v1.views import app_views


@app_views.route('/auth_session/login/', methods=['POST'], strict_slashes=False)
def validate_login() -> str:
    """
    Endpoint for validating User credentials and
    creating a new session with a cookie
    """
    email = request.form.get('email')
    password = request.form.get('password')

    if not password:
        return jsonify({"error": "password missing"}), 400
    if not email:
        return jsonify({"error": "email missing"}), 400

    user_instance = User.search({'email': email})[0]\
        if len(User.search({'email': email})) > 0\
        else None
    if not user_instance:
        return jsonify({"error": "no user found for this email"}), 404
    elif not user_instance.is_valid_password(password):
        return jsonify({"error": "wrong password"}), 401
    else:
        from api.v1.app import auth
        session_id = auth.create_session(user_instance.id)
        response_object = jsonify(user_instance.to_json())
        response_object.set_cookie(
            getenv('SESSION_NAME'),
            session_id
            )
        return response_object
