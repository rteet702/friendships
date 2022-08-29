from flask_app import app
from flask import redirect, request, render_template
from flask_app.models.users import User


@app.route('/friendships')
def r_friendships():
    friendships = User.get_friendships()
    print(friendships)
    return render_template('friendships.html', friends = friendships)