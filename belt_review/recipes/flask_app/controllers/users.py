from flask_app import app
from flask import render_template

@app.route('/')
def index():
    return render_template('home.html')