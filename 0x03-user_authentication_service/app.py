#!/usr/bin/env python3
"""
Simple flask application
"""
from flask import Flask, json, request, abort, Response
from auth import Auth


app = Flask(__name__)
AUTH = Auth()


@app.route('/', methods=['GET'], strict_slashes=False)
def simple_return():
    """
    Return a simple json dictionary
    """
    return_message = {"message": "Bienvenue"}
    return json.jsonify(return_message)


@app.route('/users', methods=['POST'], strict_slashes=False)
def users():
    """
    POST method which implements adding a new user
    """
    email = request.form['email']
    password = request.form['password']
    try:
        AUTH.register_user(email, password)
        return json.jsonify({
            'email': email,
            'message': 'user created'
        })
    except ValueError:
        return json.jsonify({
            'message': 'email already registered'
        }), 400


@app.route('/sessions', methods=['POST'], strict_slashes=False)
def login():
    """
    POST method which implements adding a new session
    for already registered user
    """
    email = request.form['email']
    password = request.form['password']
    if AUTH.valid_login(email, password):
        user_session_id = AUTH.create_session(email)
        response_json = {
            'email': email,
            'message': 'logged in',
        }
        response = json.jsonify(response_json)
        response.set_cookie('session_id', user_session_id)
        return response
    else:
        abort(401)


if __name__ == "__main__":
    app.run(host='0.0.0.0', port='5000', debug=True)
