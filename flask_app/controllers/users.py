from flask_app import app
from flask import redirect, request
from flask_app.models.users import User


@app.route('/users/create', methods=['POST'])
def f_create_user():
    inbound = request.form
    data = {
        "first_name": inbound["first_name"],
        "last_name": inbound["last_name"]
    }
    User.add_user(data)
    return redirect('/friendships')