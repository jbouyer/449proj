from flask import jsonify

def handle_400_error(e):
    return jsonify({"error": "Bad Request"}), 400

def handle_401_error(e):
    return jsonify({"error": "Unauthorized"}), 401

def handle_404_error(e):
    return jsonify({"error": "Not Found"}), 404

def handle_500_error(e):
    return jsonify({"error": "Internal Server Error"}), 500
