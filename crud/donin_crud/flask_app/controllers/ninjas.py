from flask_app import app
from flask import request, redirect, url_for, render_template
from flask_app.models.ninja import Ninja
from flask_app.models.dojo import Dojo

@app.route('/process/ninja', methods=['POST'])
def create_ninja():
    print(request.form)
    Ninja.save(request.form)
    return redirect(url_for('display_dojo', id = request.form['dojo_id']))

@app.route('/delete/ninja/<int:ninja_id>/<int:dojo_id>')
def destroy_ninja(ninja_id, dojo_id):
    data = {
        "id": ninja_id
    }
    Ninja.clear(data)
    return redirect(url_for('display_dojo', id = dojo_id))

@app.route('/update/form/<int:ninja_id>')
def update_form(ninja_id):
    data = {
        "id": ninja_id
    }
    return render_template('edit_ninja.html', ninja = Ninja.get_one_ninja(data))

@app.route('/update/ninja', methods=['POST'])
def update():
    print(request.form)
    Ninja.update(request.form)
    return redirect(url_for('display_dojo', id = request.form['dojo_id']))

# Friday To-List #
# 1. do chapter reading
# 2. watch lecture
# 3. work on how to grab the ninja id for the update process/html page
# if time: start working on next practice problem and/or figure out bootstrap for the donin_crud assignment