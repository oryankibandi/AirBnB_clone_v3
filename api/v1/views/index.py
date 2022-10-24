#!/usr/bin/python3

"""
Registers blueprint and adds the status route
"""

from api.v1.views import app_views
from flask import Flask, jsonify
from models.amenity import Amenity
from models.base_model import BaseModel
from models import storage
from models.city import City
from models.place import Place
from models.review import Review
from models.state import State
from models.user import User

classes = {"Amenity": Amenity, "BaseModel": BaseModel, "City": City,
           "Place": Place, "Review": Review, "State": State, "User": User}

app = Flask(__name__)
app.register_blueprint(app_views, url_prefix='/api/v1')


@app_views.route('/status')
def status():
    """returns response status"""
    return (jsonify({'status': 'OK'}))

@app_views.route('/api/v1/stats')
def stats():
    """Retrieves the number of each objects by type"""
    obj_dict = {}
    for clss in classes:
        obj_dict[clss] = storage.count()

    return obj_dict
