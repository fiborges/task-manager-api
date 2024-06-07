import pytest
from app import app, db, Task
from models import User
from flask_jwt_extended import create_access_token

@pytest.fixture(scope='module')
def test_client():
    with app.test_client() as testing_client:
        with app.app_context():
            db.create_all()
            yield testing_client
            db.drop_all()

def test_register_login(test_client):
    response = test_client.post('/auth/register', json={'username': 'test', 'password': 'test'})
    assert response.status_code == 201

    response = test_client.post('/auth/login', json={'username': 'test', 'password': 'test'})
    assert response.status_code == 200
    assert 'token' in response.get_json()

def test_create_task(test_client):
    token = create_access_token(identity=1)
    response = test_client.post('/tasks', json={'title': 'Test Task'}, headers={'Authorization': f'Bearer {token}'})
    assert response.status_code == 201
    assert response.get_json()['title'] == 'Test Task'

def test_get_tasks(test_client):
    token = create_access_token(identity=1)
    response = test_client.get('/tasks', headers={'Authorization': f'Bearer {token}'})
    assert response.status_code == 200
    assert len(response.get_json()) > 0
