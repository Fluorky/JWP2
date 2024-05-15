# app.py - Flask backend for handling tasks

from flask import Flask, render_template, request, jsonify
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///tasks.db'
db = SQLAlchemy(app)

class Task(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    description = db.Column(db.String(200), nullable=False)

def create_tables():
    with app.app_context():
        db.create_all()

create_tables()

@app.route('/')
def index():
    tasks = Task.query.all()
    return render_template('index.html', tasks=tasks)

@app.route('/add_task', methods=['POST'])
def add_task():
    data = request.get_json()
    description = data['description']
    new_task = Task(description=description)
    db.session.add(new_task)
    db.session.commit()
    return jsonify({'id': new_task.id, 'description': new_task.description})

@app.route('/delete_task/<int:id>', methods=['DELETE'])
def delete_task(id):
    task_to_delete = Task.query.get_or_404(id)
    db.session.delete(task_to_delete)
    db.session.commit()
    return '', 204

@app.route('/edit_task/<int:id>', methods=['PUT'])
def edit_task(id):
    task = Task.query.get_or_404(id)
    data = request.get_json()
    task.description = data['description']
    db.session.commit()
    return jsonify({'id': task.id, 'description': task.description})

if __name__ == '__main__':
    app.run(debug=True)
