# app.py

from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
    return 'Welcome in my Flask app!'

@app.route('/about')
def about():
    return 'Coded przez Fluorky.'

@app.route('/contact')
def contact():
    return 'Email: contact@example.com.'

if __name__ == '__main__':
    app.run(debug=True)
