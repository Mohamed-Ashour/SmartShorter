from flask import Blueprint, request, jsonify
from mongoframes import Q
from src.models import Link, IOS, Android


link_blueprint = Blueprint('shortlinks', __name__)


@link_blueprint.route('/', methods=['GET'])
def list_links():
    # testing
    l = Link.one({"slug":"jhdjk"}).to_json_type()
    return jsonify(l)


@link_blueprint.route('/', methods=['POST'])
def create_link():
    return "created"


@link_blueprint.route('/<string:slug>', methods=['PUT'])
def update_link(slug):
    return "updated"