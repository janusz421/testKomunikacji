import json
from flask import jsonify, request


def create_simple_json_hello():
    data = {}
    data['status'] = "ok"
    data['message'] = "Hello, JSON!"

    json_data = json.dumps(data)
    return jsonify(json_data)


def handle_json_post(posted_data: request):
    if not posted_data.get_json():
        return jsonify(create_error_json())

    else:
        print(posted_data.get_json())
        ok_json = create_ok_json()
        ok_json['sent_data'] = posted_data.get_json()
        return jsonify(ok_json)


def create_error_json():
    data = {}
    data['error'] = "Did not received json!"
    return data


def create_ok_json():
    data = {}
    data['response'] = "OK"
    return data