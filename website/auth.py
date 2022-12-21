from flask import Blueprint, render_template, request, redirect, url_for
from .modules import User
from . import db
from werkzeug.security import generate_password_hash, check_password_hash #store password that is secure
from flask_login import login_user, login_required, logout_user, current_user

auth = Blueprint('auth', __name__)

#Authorization

@auth.route('/login', methods=['POST', 'GET'])
def login():
    if request.method == 'POST':
        email = request.form['email']
        password = request.form['password']

        user = User.query.filter_by(email=email).first()
        if user:
            if check_password_hash(user.password, password):
                login_user(user, remember=True) 

                return redirect(url_for('views.home'))
    return  render_template('index.html')

@auth.route('/signup', methods=['POST', 'GET'])
def sign_up():
    if request.method == 'POST':
        email = request.form['email']
        first_name = request.form['first_name']
        password1 = request.form['password1']
        password2 = request.form['password2']
    # push to db
        user = User.query.filter_by(email=email).first()

        try:
            new_user = User(email=email, first_name=first_name, password=generate_password_hash(password1, method='sha256'))
            db.session.add(new_user)
            db.session.commit()
            login_user(user, remember=True) 

            return redirect(url_for('views.home'))

        except:
            return "There was an error"

    else:

        return redirect(url_for('views.home'))

@auth.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('auth.login'))