from flask import Blueprint, render_template, request, redirect, url_for
from .modules import User
from . import db
from werkzeug.security import generate_password_hash, check_password_hash #store password that is secure


auth = Blueprint('auth', __name__)

#Authorization

@auth.route('/login')
def login():
    return  render_template('login.html')

@auth.route('/signup', methods=['GET', 'POST'])
def sign_up():
    if request.method == 'POST':
        email = request.form.get('email')
        first_name = request.form.get('firstName')
        password1 = request.form.get('password1')
        password2 = request.form.get('password2')
    else:
        new_user = User(email=email, first_name=first_name, password=generate_password_hash(password1, method='sha256'))
        db.session.add(new_user)
        db.session.commit()
        return redirect(url_for('views.home'))

    return render_template("signup.html")