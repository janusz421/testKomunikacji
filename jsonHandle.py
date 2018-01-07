import json
from flask import jsonify


def create_simple_json_hello():
    data = {}
    data['status'] = "ok"
    data['message'] = "Hello, JSON!"

    json_data = json.dumps(data)
    return jsonify(json_data)
