import json
from app import db
from flask import Blueprint, render_template, request, redirect, url_for, jsonify
from models import SampleDB
from models import model_schemas, model_schema


bp = Blueprint('sample', __name__)


@bp.route("/api/item")
def index():
    data = SampleDB.query.all()
    response_data = model_schemas.dump(data)
    return jsonify(response_data), 200


@bp.route("/api/item", methods=["POST"])
def create():
    print(request)
    name = request.json["name"]
    price = request.json["price"]
    request_data = SampleDB(name=name, price=price)
    db.session.add(request_data)
    db.session.commit()
    return jsonify({'id': request_data.id}), 201


@bp.route("/api/item/<int:sample_id>", methods=["PUT"])
def update(sample_id):
    update_data = SampleDB.query.get_or_404(sample_id)

    update_data.name = request.json["name"]
    update_data.price = request.json["price"]
    db.session.commit()
    return jsonify({'messsage': 'success'}), 200


@bp.route("/api/item/<int:sample_id>", methods=["DELETE"])
def delete(sample_id):
    delete_data = SampleDB.query.filter(SampleDB.id == sample_id).one()
    db.session.delete(delete_data)
    db.session.commit()
    return jsonify({'messsage': 'success'}), 200


from werkzeug.exceptions import NotFound

@bp.errorhandler(NotFound)
def show_404_page(error):
    msg = error.description
    result_json = {
        "body": {},
        "status": {
            "code": 404,
            "message": msg,
        },
    }
    return jsonify(result_json), 404
