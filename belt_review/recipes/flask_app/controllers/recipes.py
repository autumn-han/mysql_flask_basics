from flask_app import app
from flask import render_template, redirect, request, session, url_for
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
    if not Recipe.validate_recipe(request.form):
        return redirect('/recipes/new')
    Recipe.save(request.form)
    return redirect('/recipes')

@app.route('/recipes/<int:id>')
def display_recipe(id):
    data = {
        "id": id
    }
    user_data = {
        "id": session["user_id"]
    }
    user = User.get_by_id(user_data)
    recipe = Recipe.get_one(data)
    return render_template('view_recipe.html', user = user, recipe = recipe)

@app.route('/recipes/edit/<int:id>')
def display_edit(id):
    data = {
        "id": id
    }
    recipe = Recipe.get_one(data)
    session["id"] = id
    return render_template('edit_recipe.html', recipe = recipe)

@app.route('/process/update', methods=['POST'])
def update():
    if not Recipe.validate_recipe(request.form):
        return redirect(url_for('display_edit', id=session["id"]))
    Recipe.update(request.form)
    return redirect('/recipes')
