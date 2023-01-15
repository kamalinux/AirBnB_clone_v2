#!/usr/bin/python3
"""
Script that runs an app with Flask framework
- Listen on 0.0.0.0, port 5000
- Routes: /: display "Hello HBNB!"
- Routes: /hbnb: display "HBNB"
"""
from flask import Flask


app = Flask(__name__)


@app.route('/', strict_slashes=False)
def hello_hbnb():
    """ Function called with / route """
    return 'Hello HBNB!'


@app.route('/hbnb', strict_slashes=False)
def hbnb():
    """ Function called with /hbnb route """
    return 'HBNB'


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)