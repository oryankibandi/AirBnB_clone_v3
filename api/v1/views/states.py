from crypt import methods
from flask import Blueprint, Flask
from models import storage, state
from . import app_views

app = Flask(__name__)
app.register_blueprint(app_views)


@app.route('/states', methods=('GET'))
def get_states():
    """Gets all objects of the given class"""
    states = storage.all(state)
    return states.to_dict()
