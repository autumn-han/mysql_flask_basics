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
def create_user():
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

@app.route('/recipes')
def all_recipes():
    data = {
        "id": session["user_id"]
    }
    user = User.get_by_id(data)
    recipes = Recipe.get_all_recipes()
    return render_template('all_recipes.html', user = user, recipes = recipes)
