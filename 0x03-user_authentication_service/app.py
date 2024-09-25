#!/usr/bin/env python3
"""
Simple flask application
"""
from flask import Flask, json


app = Flask(__name__)


@app.route('/', methods=['GET'], strict_slashes=False)
def simple_return():
    """
    Return a simple json dictionary
    """
    return_message = {"message": "Bienvenue"}
    return json.jsonify(return_message)


if __name__ == "__main__":
    app.run(host='0.0.0.0', port='5000')
