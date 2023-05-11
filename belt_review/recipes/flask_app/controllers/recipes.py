from flask_app import app
from flask import render_template, redirect, request, session
from flask_app.models.recipe import Recipe
from flask_app.models.user import User

@app.route('/recipes/new')
def new_recipe_form():
    data = {
        "id": session["user_id"]
    }
    user = User.get_by_id(data)
    return render_template('new_recipe.html', user = user)

@app.route('/process/new_recipe', methods=['POST'])
def create_recipe():
    print(request.form)
    Recipe.save(request.form)
    return redirect('/recipes')


