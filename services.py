import mysql.connector
from flask import jsonify
#from app import app

# MySQL connection setup
def get_db_connection():
    db_connection = mysql.connector.connect(
        host='localhost',
        user='root',
        password='Silasbouyer4',  # Replace with your MySQL password
        database='449_database'  # Replace with your actual database name
    )
    return db_connection

# Handle user login for authentication
def login_user(username, password):
    # Validate username and password (you should check it against your database)
    if username != 'admin' or password != 'password':  # Replace with actual validation logic
        return jsonify({"msg": "Bad username or password"}), 401

    # Create and return a JWT token
    from flask_jwt_extended import create_access_token
    access_token = create_access_token(identity=username)
    return jsonify(access_token=access_token)

# Get data from the database
def get_data_from_db():
    db = get_db_connection()
    cursor = db.cursor(dictionary=True)
    
    query = "SELECT * FROM users"  # Replace with your actual table name
    cursor.execute(query)
    rows = cursor.fetchall()
    
    db.close()
    return rows

# Insert data into the database
def insert_data_into_db(data):
    db = get_db_connection()
    cursor = db.cursor()

    field1 = data.get('field1')
    field2 = data.get('field2')
    
    query = "INSERT INTO users (username, password) VALUES (%s, %s)"
    cursor.execute(query, (field1, field2))
    db.commit()
    
    db.close()
    return {"message": "Data inserted successfully"}

# Handle errors for JWT
def expired_token_callback(jwt_header, jwt_payload):
    return jsonify(message="The token has expired"), 401

def invalid_token_callback(error):
    return jsonify(message="The token is invalid"), 401
