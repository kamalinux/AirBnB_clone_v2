#!/usr/bin/python3
"""
Script that runs an app with Flask framework
- Listen on 0.0.0.0, port 5000
- Routes: /: display "Hello HBNB!"
- Routes: /hbnb: display "HBNB"
- Routes: /c/<text>: display "C" followed by the value of the text variable
(replace underscore _ symbols with a space ).

- Routes: /python/(<text>): display "Python", followed by the value of the text
variable (replace underscore _ symbols with a space ).
- The default value of text is "is cool"

- Routes: /number/<n>: display "n is a number" only if n is an integer

- Routes: /number_template/<n>: display a HTML page only if n is an integer:
H1 tag: "Number: n" inside the tag BODY

- Routes: /number_odd_or_even/<n>: display a HTML page only if n is an integer:
H1 tag: "Number: n is even|odd" inside the tag BODY

- Routes: /states_list: display HTML and state info from storage.

- Routes: /cities_by_states: display HTML and state, city relations

- Routes: /states/<id>: display HTML and state, city given state id
"""
from flask import Flask, render_template
from models import storage
from models.state import State
from models.city import City


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


@app.route('/python/', strict_slashes=False)
@app.route('/python/<text>', strict_slashes=False)
def python_text(text='is cool'):
    """ Function called with /python/<text> route """
    return 'Python {}'.format(text.replace('_', ' '))


@app.route('/number/<int:n>', strict_slashes=False)
def number(n):
    """ Function called with /number/<n> route """
    return "{:d} is a number".format(n)


@app.route('/number_template/<int:n>', strict_slashes=False)
def number_template(n):
    """ Function called with /number_template/<n> route """
    return render_template('5-number.html', number=n)


@app.route('/number_odd_or_even/<int:n>', strict_slashes=False)
def number_odd_or_even(n):
    """ Function called with /number_template/<n> route """
    odd_or_even = "even" if (n % 2 == 0) else "odd"
    return render_template('6-number_odd_or_even.html',
                           number=n, odd_or_even=odd_or_even)


@app.teardown_appcontext
def tear_down(self):
    """after each request remove current SQLAlchemy session"""
    storage.close()


@app.route('/states/', strict_slashes=False)
@app.route('/states_list', strict_slashes=False)
def html_fetch_states():
    """ Function called with /states_list route """
    state_objs = [s for s in storage.all("State").values()]
    return render_template('7-states_list.html',
                           state_objs=state_objs)


@app.route('/cities_by_states', strict_slashes=False)
def html_fetch_cities_by_states():
    """ Function called with /states_list route """
    state_objs = [s for s in storage.all("State").values()]
    return render_template('8-cities_by_states.html',
                           state_objs=state_objs)


@app.route('/states/<id>', strict_slashes=False)
def html_if_stateID(id):
    """display html page; customize heading with state.name
       fetch sorted cities for this state ID into LI tag ->in HTML file
    """
    state_obj = None
    for state in storage.all("State").values():
        if state.id == id:
            state_obj = state
    return render_template('9-states.html',
                           state_obj=state_obj)


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
