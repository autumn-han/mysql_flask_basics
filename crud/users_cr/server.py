from flask import Flask, render_template, request, redirect

from user import User

app = Flask(__name__)

@app.route('/')
def index():
    return redirect('/users')

@app.route('/users')
def users():    
    return render_template("read_all.html", users = User.get_all())

@app.route('/users/new')
def new():
    return render_template("new_user.html")

@app.route('/users/create', methods=["POST"])
def create():
    # # data = {
    #     "fname": request.form["fname"],
    #     "lname": request.form["lname"],
    #     "email": request.form["email"]
    # }
    # print(data)
    # User.save(data)
    print(request.form)
    User.save(request.form)
    return redirect('/users')

if __name__ == '__main__':
    app.run(debug=True, port=5001)