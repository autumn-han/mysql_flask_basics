from flask_app import app
from flask_app.models.user import User
from flask import render_template, redirect, request, session, flash
from flask_bcrypt import Bcrypt

bcrypt = Bcrypt(app)

@app.route('/')
def index():
    return render_template('home.html')

@app.route('/process/registration', methods=['POST'])
def register():
    print(request.form)
    if not User.validate_user(request.form):
        return redirect('/')
    pw_hash = bcrypt.generate_password_hash(request.form["password"])
    print(pw_hash)
    data = {
        "fname": request.form["fname"],
        "lname": request.form["lname"],
        "email": request.form["email"], 
        "password": pw_hash
    }
    user_id = User.save(data)
    session["user_id"] = user_id
    print(session)
    session["fname"] = request.form["fname"] # there should be a way to clean this up? figure out how to access dictionary within session
    return redirect('/welcome')

@app.route('/process/login', methods=['POST'])
def login():
    data = {
        "email": request.form["email"]
    }
    user_in_db = User.get_by_email(data)
    if not user_in_db:
        flash("No account found, please register with the form on the left")
        return redirect('/')
    print(request.form)
    return redirect('/welcome')
    
@app.route('/welcome')
def welcome_page():
    return render_template('welcome.html')

@app.route('/logout')
def logout():
    session.clear()
    print(session)
    return redirect('/')