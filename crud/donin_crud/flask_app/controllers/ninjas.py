from flask_app import app
from flask import request, redirect, url_for
from flask_app.models.ninja import Ninja
from flask_app.models.dojo import Dojo

@app.route('/process/ninja', methods=['POST'])
def create_ninja():
    print(request.form)
    Ninja.save(request.form)
    return redirect(url_for('display_dojo', id = request.form['dojo_id']))

@app.route('/delete/ninja/<int:ninja_id>')
def destroy_ninja(ninja_id):
    data = {
        "id": ninja_id
    }
    Ninja.clear(data)
    return redirect(url_for('display_dojo', id = Dojo.id))


    
