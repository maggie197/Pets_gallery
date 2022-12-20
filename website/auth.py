from flask import Blueprint, render_template


auth = Blueprint('auth', __name__)

#Authorization

@auth.route('/login')
def login():
    from .static.loginform import loginform
    return  render_template('login.html')