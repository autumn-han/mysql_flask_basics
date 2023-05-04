from flask_app import app
from flask import request, redirect, url_for
from flask_app.models.ninja import Ninja

@app.route('/process/ninja', methods=['POST'])
def create_ninja():
    print(request.form)
    Ninja.save(request.form)
    return redirect(url_for('display_dojo', id = request.form['dojo_id']))

