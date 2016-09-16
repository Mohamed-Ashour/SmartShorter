import random
import string

from flask import Blueprint, request, jsonify, abort
from mongoframes import Q
from src.models import Link


link_blueprint = Blueprint('shortlinks', __name__)


@link_blueprint.route('/', methods=['GET'])
def list_links():
    links_objects = Link.many()
    links = [link.to_json_type() for link in links_objects]
    return jsonify({"shortlinks" : links})


@link_blueprint.route('/', methods=['POST'])
def create_link():

    # generating random slug if not exist
    slug = request.json.get("slug", ''.join(random.choice(string.ascii_letters + string.digits) for i in range(6)))

    link = Link(
        slug = slug,
        ios = request.json['ios'],
        android = request.json['android'],
        web = request.json['web']
    )
    link.insert()
    return jsonify({
          "status": "successful",
          "slug": link.slug,
          "message": "created successfully"
        })


@link_blueprint.route('/<string:slug>', methods=['PUT'])
def update_link(slug):
    link = Link.one({"slug":slug})
    if "web" in request.json:
        link.web = request.json["web"]
    if "ios" in request.json:
        if "primary" in request.json["ios"]:
            link.ios["primary"] = request.json["ios"]["primary"]
        if "fallback" in request.json["ios"]:
            link.ios["fallback"] = request.json["ios"]["fallback"]
    if "android" in request.json:
        if "primary" in request.json["android"]:
            link.android["primary"] = request.json["android"]["primary"]
        if "fallback" in request.json["android"]:
            link.android["fallback"] = request.json["android"]["fallback"]

    link.upsert()

    return jsonify({
          "status": "successful",
          "message": "updated successfully"
        })
