from flask import Flask, request, jsonify, send_from_directory
from flask_sqlalchemy import SQLAlchemy
from flask_jwt_extended import JWTManager, jwt_required, get_jwt_identity
from models import db, Task, User
from auth import auth

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///tasks.db'
app.config['JWT_SECRET_KEY'] = 'your_secret_key'  # Troque por uma chave secreta forte
db.init_app(app)
jwt = JWTManager(app)

app.register_blueprint(auth, url_prefix='/auth')

# Use @app.before_request para criar tabelas no banco de dados se necessário
@app.before_request
def create_tables():
    db.create_all()

@app.route('/tasks', methods=['GET'])
@jwt_required()
def get_tasks():
    user_id = get_jwt_identity()
    tasks = Task.query.filter_by(user_id=user_id).all()
    return jsonify([{'id': task.id, 'title': task.title, 'description': task.description, 'done': task.done} for task in tasks])

@app.route('/tasks', methods=['POST'])
@jwt_required()
def create_task():
    data = request.get_json()
    new_task = Task(title=data['title'], description=data.get('description'), user_id=get_jwt_identity())
    db.session.add(new_task)
    db.session.commit()
    return jsonify({'id': new_task.id, 'title': new_task.title, 'description': new_task.description, 'done': new_task.done}), 201

@app.route('/tasks/<int:id>', methods=['PUT'])
@jwt_required()
def update_task(id):
    data = request.get_json()
    task = Task.query.get(id)
    if not task or task.user_id != get_jwt_identity():
        return jsonify({'error': 'Task not found or not authorized'}), 404
    task.title = data['title']
    task.description = data.get('description', task.description)
    task.done = data.get('done', task.done)
    db.session.commit()
    return jsonify({'id': task.id, 'title': task.title, 'description': task.description, 'done': task.done})

@app.route('/tasks/<int:id>', methods=['DELETE'])
@jwt_required()
def delete_task(id):
    task = Task.query.get(id)
    if not task or task.user_id != get_jwt_identity():
        return jsonify({'error': 'Task not found or not authorized'}), 404
    db.session.delete(task)
    db.session.commit()
    return '', 204

@app.route('/')
def serve_index():
    return send_from_directory('static', 'index.html')

@app.route('/<path:path>')
def serve_static(path):
    return send_from_directory('static', path)

if __name__ == '__main__':
    app.run(debug=True)
