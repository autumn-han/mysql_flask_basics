from flask_app import app
from flask_app.models.order import Order
from flask import flash, render_template, redirect, request, session, url_for


@app.route('/')
def index():
    return redirect('/cookies')

@app.route('/cookies')
def home():
    return render_template('all_orders.html', orders = Order.all_orders())

@app.route('/cookies/new')
def new_order():
    return render_template('new_order.html')

@app.route('/process/new', methods=['POST'])
def create():
    print(request.form)
    if not Order.validate_user(request.form):
        return redirect('/cookies/new')
    Order.save(request.form)
    return redirect('/')

@app.route('/cookies/edit/<int:id>')
def change_order(id):
    data = {
        "id": id
    }
    return render_template('change_order.html', order = Order.one_order(data))

@app.route('/process/edit', methods=['POST'])
def edit():
    print(request.form)
    if not Order.validate_user(request.form):
        return redirect(url_for('change_order', id = request.form["id"]))
    Order.update(request.form)
    return redirect('/')

