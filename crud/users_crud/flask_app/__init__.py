from flask import Flask
app = Flask(__name__)
app.secret_key = 'blah blah blah'

from flask_app.controllers import users