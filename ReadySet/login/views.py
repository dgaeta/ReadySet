# ReadySet/login/views.py 

from ../models import User
from flask import Blueprint, render_template
from ../__init__ import *
from flask.ext.login import LoginManager,  login_required
from passlib.apps import custom_app_context as pwd_context

login = Blueprint('login', __name__)
login_manager.init_app(app)


@login_manager.user_loader
def load_user(user_id):
  	"""Given *user_id*, return the associated User object.

    :param unicode user_id: user_id (username) user to retrieve
    """
    return User.query.get(user_id)


@login.route("/", methods=["GET", "POST"])
def login():
    """For GET requests, display the login form. For POSTS, login the current user
    by processing the form."""
    print db
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.get(form.username.data)
        if user:
            if bcrypt.check_password_hash(user.password, form.password.data):
                user.authenticated = True
                db.session.add(user)
                db.session.commit()
                login_user(user, remember=True)
                return "login success"
						else: 
							return "invalid password"
    		else:
					return "invalid username"


@login.route("/logout", methods=["GET"])
@login_required
def logout():
    """Logout the current user."""
    user = current_user
    user.authenticated = False
    db.session.add(user)
    db.session.commit()
    logout_user()
    return "logout successful"



