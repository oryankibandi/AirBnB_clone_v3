#!/usr/bin/python3

"""
Registers blueprint and adds the status route
"""

from api.v1.views import app_views
from flask import Flask, jsonify

app = Flask(__name__)
app.register_blueprint(app_views, url_prefix='/api/v1')


@app_views.route('/status')
def status():
    """returns response status"""
    return (jsonify({'status': 'OK'}))
