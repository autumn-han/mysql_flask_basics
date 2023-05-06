from flask_app import app
from flask_app.models.customer import Customer
from flask import render_template, redirect

@app.route('/')
def index():
    return redirect('/cookies')

@app.route('/cookies')
def all_orders(id):
    data = {
        "id": id
    }
    return render_template('cookie_orders.html', customer = Customer.one_customer(data))