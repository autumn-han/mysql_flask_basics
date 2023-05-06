from flask_app import app
from flask_app.models.order import Order
from flask_app.models.customer import Customer
from flask import render_template, redirect, request

@app.route('/')
def index():
    return redirect('/cookies')

@app.route('/cookies')
def all_orders():
    return render_template('cookie_orders.html', orders = Order.all_orders())

@app.route('/cookies/edit/<int:id>')
def change_form(id):
    data = {
        "id": id
    }
    return render_template('change_order.html', order = Order.one_order(data))

@app.route('/cookies/edit/process', methods=['POST'])
def update():
    print(request.form)
    Order.update(request.form)
    return redirect('/')