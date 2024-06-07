# Task Manager API

This project is a simple task manager API built with Flask, allowing users to register, login, and manage their tasks. The frontend is built with plain HTML, CSS, and JavaScript to interact with the backend API.

## Features

- User registration and authentication
- Create, read, update, and delete tasks
- Simple frontend for interacting with the API

## Requirements

- Python 3.8 or higher
- Flask
- Flask-SQLAlchemy
- Flask-JWT-Extended
- Werkzeug
- pytest

## Setup

### 1. Clone the Repository

```bash
git clone https://github.com/fiborges/task-manager-api.git
cd task-manager-api
```

## Create and Activate a Virtual Environment
### For Linux/Mac
```bash

python3 -m venv venv
source venv/bin/activate
```

### For Windows
```bash

python -m venv venv
.\venv\Scripts\activate
```

## Install Dependencies
```bash

pip install -r requirements.txt
```

## Run the Application
```bash

python app.py
```

The application will start running on http://127.0.0.1:5000.

## Testing the Application
You can test the API using Postman or the provided frontend.

### Using Postman
#### Register a New User

Method: POST
URL: http://127.0.0.1:5000/auth/register

#### Body (JSON):
```json

{
  "username": "testuser",
  "password": "testpassword"
}
```
#### Response:
```json

{
  "message": "User created successfully"
}
```
#### Login

Method: POST
URL: http://127.0.0.1:5000/auth/login

#### Body (JSON):
```json

{
  "username": "testuser",
  "password": "testpassword"
}
```
#### response:
```json

{
  "token": "<jwt_token>"
}
```
#### Create a New Task

Method: POST
URL: http://127.0.0.1:5000/tasks
Headers:
Authorization: Bearer <jwt_token>

#### Body (JSON):
```json

{
  "title": "My first task",
  "description": "This is a test task"
}
```
#### Response:
```json

{
  "id": 1,
  "title": "My first task",
  "description": "This is a test task",
  "done": false
}
```
### Get All Tasks

Method: GET
URL: http://127.0.0.1:5000/tasks
Headers:
Authorization: Bearer <jwt_token>

#### Response:
```json

[
  {
    "id": 1,
    "title": "My first task",
    "description": "This is a test task",
    "done": false
  }
]
```
#### Update a Task

Method: PUT
URL: http://127.0.0.1:5000/tasks/1
Headers:
Authorization: Bearer <jwt_token>

#### Body (JSON):
```json

{
  "title": "Updated task title",
  "description": "Updated task description",
  "done": true
}
```
#### Response:
```json

{
  "id": 1,
  "title": "Updated task title",
  "description": "Updated task description",
  "done": true
}
```
### Delete a Task

Method: DELETE
URL: http://127.0.0.1:5000/tasks/1
Headers:
Authorization: Bearer <jwt_token>
Response: 204 No Content

## Using the Frontend

Open a web browser and go to http://127.0.0.1:5000.
Register a new user.
Login with the registered user.
Add, update, and delete tasks using the provided interface.

## Running Tests
To run the automated tests, use the following command:

```bash

pytest

```
Project Structure
```arduino

task-manager-api/
├── README.md
├── requirements.txt
├── venv/
├── app.py
├── auth.py
├── models.py
├── static/
│   ├── index.html
│   ├── style.css
│   └── app.js
└── tests/
    └── test_app.py
```
app.py: The main application file.
auth.py: Contains authentication routes.
models.py: Defines the database models.
static/: Contains the frontend files.
tests/: Contains the automated tests.
venv/: The virtual environment directory.
requirements.txt: Lists the dependencies for the project.

### Dependencies
Flask: Micro web framework.
Flask-SQLAlchemy: Adds SQLAlchemy support to Flask.
Flask-JWT-Extended: Adds JWT support to Flask.
Werkzeug: Comprehensive WSGI web application library.
pytest: Framework for testing Python code.