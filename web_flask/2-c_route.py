#!/usr/bin/python3
"""
Script that runs an app with Flask framework
- Listen on 0.0.0.0, port 5000
- Routes: /: display "Hello HBNB!"
- Routes: /hbnb: display "HBNB"
- Routes: /c/<text>: display "C" followed by the value of the text variable
(replace underscore _ symbols with a space )
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


@app.route('/c/<text>', strict_slashes=False)
def c_text(text):
    """ Function called with /c/<text> route """
    return 'C {}'.format(text.replace('_', ' '))


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
