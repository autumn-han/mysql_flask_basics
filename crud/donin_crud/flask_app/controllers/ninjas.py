from flask_app import app
from flask import render_template, redirect, request
from flask_app.models.ninja import Ninja
from flask_app.models.dojo import Dojo

# @app.route('/process/ninja', methods=['POST'])
# def create_ninja():
#     print(request.form)
#     Ninja.save(request.form)
#     return redirect('/dojos/<int:id>')