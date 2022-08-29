from flask_app import app
from flask import render_template
from flask_app.models.users import User


@app.route('/friendships')
def r_friendships():
    friendships = User.get_friendships()
    return render_template('friendships.html', friends = friendships)