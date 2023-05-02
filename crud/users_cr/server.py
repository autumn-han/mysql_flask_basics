from flask import Flask, render_template, request, redirect

from user import User

app = Flask(__name__)

@app.route('/')
def index():
    return redirect('/users')

@app.route('/users')
def users():    
    return render_template("read_all.html", users = User.get_all())

@app.route('/show/<int:user_id>')
def show(user_id):
    user = User.get_one(user_id)
    return render_template("read_one.html", user = user)

@app.route('/users/new')
def new():
    return render_template("new_user.html")

@app.route('/users/create', methods=["POST"])
def create():
    print(request.form)
    User.save(request.form)
    return redirect('/users')

@app.route('/user/update/form')
def update_form():
    return render_template("edit_user.html")

@app.route('/user/update', methods=["POST"])
def update():
    User.update(request.form)
    return redirect('/')

if __name__ == '__main__':
    app.run(debug=True, port=5001)