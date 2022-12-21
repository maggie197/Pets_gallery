from flask import Blueprint, render_template, request, redirect, url_for
from .modules import User
from . import db
from werkzeug.security import generate_password_hash, check_password_hash #store password that is secure


auth = Blueprint('auth', __name__)

#Authorization

@auth.route('/login', methods=['POST', 'GET'])
def login():
    if request.method == 'POST':
        email = request.form['email']
        password = request.form['password']
    
    return  render_template('index.html')

@auth.route('/signup', methods=['POST', 'GET'])
def sign_up():
    if request.method == 'POST':
        email = request.form['email']
        first_name = request.form['first_name']
        password1 = request.form['password1']
        password2 = request.form['password2']
    # push to db
        try:
            new_user = User(email=email, first_name=first_name, password=generate_password_hash(password1, method='sha256'))
            db.session.add(new_user)
            db.session.commit()
            return redirect(url_for('views.home'))

        except:
            return "There was an error"

    else:

        return redirect(url_for('views.home'))


