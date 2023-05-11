from flask_app import app
from flask_app.models.user import User
from flask import render_template, redirect, request, session
from flask_bcrypt import Bcrypt

bcrypt = Bcrypt(app)

@app.route('/')
def index():
    return render_template('home.html')

@app.route('/process/registration', methods=['POST'])
def create_user():
    print(request.form)
    pw_hash = bcrypt.generate_password_hash(request.form["password"])
    data = {
        "first_name": request.form["fname"],
        "last_name": request.form["lname"],
        "email": request.form["email"],
        "password": pw_hash
    }
    user_id = User.create(data)
    session["user_id"] = user_id
    return redirect('#')
