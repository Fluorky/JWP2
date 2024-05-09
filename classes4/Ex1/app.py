from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///teachers.db'
db = SQLAlchemy(app)

class Teacher(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False)
    subject = db.Column(db.String(50), nullable=False)
    time = db.Column(db.String(20), nullable=False)

def __repr__(self):
    return f'<Teacher {self.name}>'

@app.route('/')
def index():
    teachers = Teacher.query.all()
    return render_template('index.html', teachers=teachers)

@app.route('/add_teacher', methods=['GET', 'POST'])
def add_teacher():
    if request.method == 'POST':
        name = request.form['name']
        subject = request.form['subject']
        time = request.form['time']
        new_teacher = Teacher(name=name, subject=subject, time=time)
        db.session.add(new_teacher)
        db.session.commit()
        return redirect(url_for('index'))
    return render_template('add_teacher.html')

@app.route('/delete_teacher', methods=['GET','POST'])
def delete_teacher():
    if request.method == 'POST':
        teacher_id = request.form['teacher_id']
        teacher_to_delete = Teacher.query.get_or_404(teacher_id)
        db.session.delete(teacher_to_delete)
        db.session.commit()
        return redirect(url_for('index'))
    return render_template('delete_teacher.html')

if __name__ == '__main__':
    app.run(debug=True)
