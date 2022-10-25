#!/usr/bin/python3
"""Runs a flask app"""
import os
from flask import Flask, Blueprint, jsonify
from models import storage
from api.v1.views import app_views

app = Flask(__name__)

app.register_blueprint(app_views, url_prefix="/api/v1")


@app.teardown_appcontext
def teardown():
    """performs this when a connection is closed"""
    storage.close()

@app.errorhandler(404)
def handle_404():
    """Handles 404 error"""
    return jsonify({ "error": "Not found" })

if __name__ == '__main__':
    host = os.getenv('HBNB_API_HOST') if not None else '0.0.0.0'
    port = os.getenv('HBNB_API_PORT') if not None else '5000'
    app.run(host=host, port=port, threaded=True)
