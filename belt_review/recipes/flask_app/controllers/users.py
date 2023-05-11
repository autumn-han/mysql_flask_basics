from flask_app import app
from flask_app.models.user import User
from flask_app.models.recipe import Recipe
from flask import render_template, redirect, request, session
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
    return redirect('/recipes')

@app.route('/process/login', methods=['POST'])
def login():
    print(request.form)
    user = User.validate_login(request.form)
    if not user:
        return redirect('/')
    session["user_id"] = user.id
    return redirect('/recipes')

@app.route('/logout')
def logout():
    session.clear()
    return redirect('/')

@app.route('/recipes')
def all_recipes():
    data = {
        "id": session["user_id"]
    }
    main_user = User.get_by_id(data)
    users = Recipe.get_all()
    return render_template('all_recipes.html', main_user = main_user, users = users)
