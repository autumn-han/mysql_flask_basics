from flask_app import app
from flask import render_template, redirect, request
from flask_app.models.dojo import Dojo

@app.route('/')
def index():
    return redirect('/dojos')

@app.route('/dojos')
def home():
    return render_template('dojos.html')

@app.route('/process', methods=['POST'])
def create():
    print(request.form)
    Dojo.save(request.form)
    return redirect('/')