from flask import Flask, jsonify, make_response

from src.views import link_blueprint


app = Flask(__name__)

app.config.from_object("config")

app.register_blueprint(link_blueprint, url_prefix="/shortlinks")

# error handlers

@app.errorhandler(400)
def bad_request(error):
    return make_response(jsonify( { "status": "failed", "message": "Bad Request" } ), 400)

@app.errorhandler(404)
def not_found(error):
    return make_response(jsonify( { "status": "failed", "message": "not found" } ), 404)

@app.errorhandler(500)
def server_error(error):
    return make_response(jsonify( {} ), 500)


# database initialization
from src import database
