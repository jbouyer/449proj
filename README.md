RESTful API with Flask: Authentication, CRUD, and Error Handling
Overview
This project implements a RESTful API using Flask. The API features JWT authentication, CRUD operations with a MySQL database, and file handling. It includes public and admin routes with authentication and error handling.

Features
Error Handling: Handles errors (400, 401, 404, 500) with appropriate messages.

JWT Authentication: Users authenticate via the /login endpoint to receive a token for accessing protected routes.

CRUD Operations: Endpoints like /get_data (GET) and /insert_data (POST) interact with a MySQL database.

File Handling: Allows users to upload and store files, with validation for type and size.

Setup
Requirements
Python 3.x

MySQL

Postman (for testing)

Installing Dependencies
Create and activate virtual environment:

python -m venv venv
source venv/bin/activate  # On macOS/Linux
.\venv\Scripts\activate  # On Windows
Install dependencies:


pip install -r requirements.txt
Set up MySQL: Create a MySQL database and a users table:


CREATE DATABASE your_database_name;
USE your_database_name;
CREATE TABLE users (id INT AUTO_INCREMENT PRIMARY KEY, username VARCHAR(255), password VARCHAR(255));
Configure app: Set your MySQL credentials in app.py:


app.config['DB_HOST'] = 'localhost'
app.config['DB_USER'] = 'root'
app.config['DB_PASSWORD'] = 'your_mysql_password'
app.config['DB_DATABASE'] = 'your_database_name'
Run the app:


python app.py
Testing with Postman
1. Login
POST request to /login with:


{ "username": "admin", "password": "password" }
Receive a JWT token.

2. Access Protected Route
GET request to /protected with the token in the Authorization header:

Authorization: Bearer <your_jwt_token>
3. CRUD Operations
GET request to /get_data (requires token).

POST request to /insert_data with:

{ "username": "new_user", "password": "password123" }
Conclusion
This project demonstrates building a secure API with Flask, featuring authentication, CRUD operations, and error handling. It connects to a MySQL database and provides a functional API for testing and development.

License
MIT License.
