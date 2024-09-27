#!/usr/bin/env python3
"""
Simple flask application
"""
from flask import Flask, json, request, abort, Response, url_for, redirect
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


@app.route('/sessions', methods=['DELETE'], strict_slashes=False)
def logout():
    """
    Logout method for the DELETE HTTP Method
    Deletes session_id cookie and removes the session
    """
    session_id = request.cookies.get('session_id')
    user_result = AUTH.get_user_from_session_id(session_id)

    if user_result:
        AUTH.destroy_session(user_result.id)
        # return redirect(url_for('simple_return'))
        return redirect('/')
    else:
        abort(403)


@app.route('/profile', methods=['GET'], strict_slashes=False)
def profile_login():
    """
    Function that allows logged in user to continue with a session
    """
    session_id = request.cookies.get('session_id')
    user_result = AUTH.get_user_from_session_id(session_id)

    if not session_id:
        abort(403)
    if user_result:
        return json.jsonify({'email': user_result.email})
    else:
        abort(403)


if __name__ == "__main__":
    app.run(host='0.0.0.0', port='5000', debug=True)
