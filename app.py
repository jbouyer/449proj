import os
import mysql.connector
from flask import Flask, jsonify, request
from flask_jwt_extended import JWTManager, jwt_required, create_access_token
from flask_cors import CORS
import secrets
from services import login_user, get_data_from_db, insert_data_into_db

# Generate a secure secret key (You can use a .env file for better security in production)
secret_key = secrets.token_hex(16)  # Generate a 32-character hex string (16 bytes)

# Initialize Flask app
app = Flask(__name__)

# Enable Cross-Origin Resource Sharing (CORS)
CORS(app)

# Set the secret key for JWT
app.config['JWT_SECRET_KEY'] = secret_key  # Use the generated secret key here
app.config['DB_HOST'] = 'localhost'
app.config['DB_USER'] = 'root'
app.config['DB_PASSWORD'] = 'Silasbouyer4'  # Replace with your MySQL password
app.config['DB_DATABASE'] = '449_database'  # Replace with your actual database name

# Initialize JWT Manager
jwt = JWTManager(app)

# MySQL connection setup
def get_db_connection():
    return mysql.connector.connect(
        host=app.config['DB_HOST'],
        user=app.config['DB_USER'],
        password=app.config['DB_PASSWORD'],
        database=app.config['DB_DATABASE']
    )

# Route for login (JWT token generation)
@app.route('/', methods=["GET", "POST"])
def index():
    return "Testing"

@app.route('/login', methods=['POST'])
def login():
    username = request.json.get('username', None)
    password = request.json.get('password', None)

    return login_user(username, password)

# Protected route that requires a valid JWT token
@app.route('/protected', methods=['GET'])
@jwt_required()
def protected():
    return jsonify(message="This is a protected route.")

# Example of a CRUD operation (GET) - Retrieve data from MySQL
@app.route('/get_data', methods=['GET'])
@jwt_required() 
def get_data():
    db = get_db_connection()
    cursor = db.cursor(dictionary=True)
    
    query = "SELECT * FROM users"  # Replace with your actual table name
    cursor.execute(query)
    rows = cursor.fetchall()
    
    db.close()
    return jsonify(rows)

# Example of a CRUD operation (POST) - Insert data into MySQL
@app.route('/insert_data', methods=['POST'])
@jwt_required() 
def insert_data():
    data = request.json
    response = insert_data_into_db(data)
    return jsonify(response), 201

# Handle errors for JWT
@jwt.expired_token_loader
def expired_token_callback(jwt_header, jwt_payload):
    return jsonify(message="The token has expired"), 401

@jwt.invalid_token_loader
def invalid_token_callback(error):
    return jsonify(message="The token is invalid"), 401

if __name__ == '__main__':
    app.run(debug=True)
