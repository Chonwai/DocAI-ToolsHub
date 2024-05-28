# utils.py
from flask import jsonify

def create_response(success, data=None, errors=None, status_code=200):
    response = {
        "success": success,
        "data": data,
        "errors": errors
    }
    return jsonify(response), status_code