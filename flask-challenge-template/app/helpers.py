from flask import jsonify

def rest_response(data, ok=True, message='', status=200):
    return jsonify({
        'ok': ok,
        'message': message,
        'data': data
    }), status
