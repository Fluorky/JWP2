# app.py

from flask import Flask, render_template, request

app = Flask(__name__)

tasks = []  # Lista zadan

@app.route('/')
def index():
    return render_template('index.html', tasks=tasks)

@app.route('/add', methods=['POST'])
def add_task():
    if request.method == 'POST':
        task_content = request.form['content']
        tasks.append(task_content)
        return render_template('index.html', tasks=tasks)

@app.route('/delete/<int:task_id>', methods=['DELETE'])
def delete_task(task_id):
    if request.method == 'DELETE':
        try:
            del tasks[task_id]
        except IndexError:
            pass
        return render_template('index.html', tasks=tasks)

@app.route('/edit/<int:task_id>', methods=['PUT'])
def edit_task(task_id):
    if request.method == 'PUT':
        try:
            new_content = request.form['content']
            tasks[task_id] = new_content
        except IndexError:
            pass
        return render_template('index.html', tasks=tasks)

if __name__ == '__main__':
    app.run(debug=True)
