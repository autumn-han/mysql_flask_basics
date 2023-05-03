from flask_app import app
from flask import render_template, redirect, request
from flask_app.models.dojo import Dojo
from flask_app.models.ninja import Ninja

@app.route('/')
def index():
    return redirect('/dojos')

@app.route('/dojos')
def home():
    return render_template('home.html', dojos = Dojo.get_all_dojos())

@app.route('/dojos/<int:id>')
def display_dojo(id):
    data = {
        "id": id
    }
    return render_template('dojo_show.html', dojo = Dojo.get_one_dojo(data))

@app.route('/ninjas')
def new_ninja_form():
    return render_template('new_ninja.html', dojos = Dojo.get_all_dojos())

@app.route('/process/dojo', methods=['POST'])
def create_dojo():
    print(request.form)
    Dojo.save(request.form)
    return redirect('/')

@app.route('/process/ninja', methods=['POST'])
def create_ninja():
    print(request.form)
    Ninja.save(request.form)
    return redirect('/')