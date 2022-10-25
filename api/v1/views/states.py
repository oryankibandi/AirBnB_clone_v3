from email.policy import default
from flask import Flask, abort, Response, jsonify, request
from models import storage, state
from . import app_views

app = Flask(__name__)
app.register_blueprint(app_views)


@app.route('/states', methods=('GET'))
def get_states():
    """Gets all objects of the given class"""
    states = storage.all(state)
    return states.to_dict()


@app.route('/states/<state_id>', methods=('GET'))
def get_state(state_id):
    """returns the state with the matchind state_id"""
    matching_state = storage.get(state, state_id)
    if matching_state is None:
        abort(404)
    return matching_state.to_dict()


@app.route('/states/<state_id>', methods=('DELETE'))
def delete_state(state_id):
    """deletes a state object with the matching state_id"""
    matching_state = storage.get(state, state_id)
    if matching_state is None:
        abort(404)
    else:
        storage.delete(matching_state)
        return Response(jsonify('{}'), status=200)


@app.route('/states/<state_id>', methods=('PUT'))
def update_state(state_id):
    """Updates a state object"""
    matching_state = storage.get(state, state_id)
    if matching_state is None:
        abort(404)
    updated_state = request.get_json
    if update_state is None:
        return 'Not a JSON', 400

    new_keys = updated_state.keys()
    for key in new_keys:
        if key != 'id' or key != 'created_at' or key != 'updated_at':
            matching_state[key] = update_state[key]

    storage.new(matching_state)
    storage.save()
    return matching_state.to_dict(), 200


@app.route('/states', methods=('POST'))
def new_state():
    """adds a new state object to storage"""
    new_state = request.get_json
    if new_state is None:
        return 'Not a JSON', 400

    if new_state.get('name', default=None) is None:
        return 'Missing name', 400

    new_state_obj = state.State({'name': new_state['name']})
    storage.new(new_state_obj)

    return new_state_obj.to_dict(), 201
