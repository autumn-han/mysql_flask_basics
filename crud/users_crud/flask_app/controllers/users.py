from flask_app import app
from flask import Flask, render_template, redirect, request 
from flask_app.models.user import User

@app.route('/')
def index():
    return redirect('/users')

@app.route('/users')
def users():    
    return render_template("read_all.html", users = User.get_all())

@app.route('/show/<int:id>')
def show(id):
    data = {
        "id": id
    }
    return render_template("read_one.html", user = User.get_one(data))

@app.route('/users/new')
def new():
    return render_template("new_user.html")

@app.route('/users/create', methods=["POST"])
def create():
    print(request.form)
    User.save(request.form)
    return redirect('/users')

@app.route('/delete/<int:id>')
def delete(id):
    data = {
        "id": id
    }
    User.delete(data)
    return redirect('/')

@app.route('/user/update/form/<int:id>')
def update_form(id):
    data = {
        "id": id
    }
    return render_template("edit_user.html", user = User.get_one(data))

@app.route('/user/update', methods=["POST"])
def update():
    print(request.form)
    User.update(request.form)
    return redirect('/')