from flask import Blueprint, request, jsonify
import mysql.connector
from flask_jwt_extended import create_access_token
import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Initialize Blueprint
auth = Blueprint('auth', __name__)

# User Login Endpoint
@auth.route('/login', methods=['POST'])
def login():
    data = request.get_json()
    username = data.get("username")
    password = data.get("password")

    # Connect to MySQL
    db = mysql.connector.connect(
        host=os.getenv("DB_HOST"),
        user=os.getenv("DB_USER"),
        password=os.getenv("DB_PASSWORD"),
        database=os.getenv("DB_NAME")
    )
    cursor = db.cursor(dictionary=True)

    cursor.execute("SELECT * FROM users WHERE username = %s AND password = %s", (username, password))
    user = cursor.fetchone()
    
    if not user:
        return jsonify({"error": "Invalid credentials"}), 401

    access_token = create_access_token(identity=username)
    return jsonify(access_token=access_token), 200
