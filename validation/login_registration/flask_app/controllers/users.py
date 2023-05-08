from flask_app import app
from flask_app.models.user import User
from flask import Flask, render_template, redirect, request, session, flash

@app.route('/')
def index():
    return render_template('home.html')

@app.route('/process/registration', methods=['POST'])
def register():
    print(request.form)
    if not User.validate_user(request.form):
        return redirect('/')
    User.save(request.form)
    return redirect('/welcome')
    
@app.route('/welcome')
def welcome_page():
    return render_template('welcome.html')