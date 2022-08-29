from flask_app import app
from flask import render_template, redirect, request
from flask_app.models.users import User


@app.route('/friendships')
def r_friendships():
    friendships = User.get_friendships()
    users = User.get_all()
    return render_template('friendships.html', friends = friendships, users = users)

@app.route('/friendships/create', methods = ['POST'])
def f_create_friendship():
    inbound = request.form
    data = {
        "first_user": inbound['first_user'],
        "second_user": inbound['second_user']
    }
    User.add_friendship(data)
    return redirect('/friendships')