# this file makes the website folder to become a python package
# this will set up flask aplication

from flask import Flask

def create_app():        #set a function inisializing flask
    app = Flask(__name__)
    app.config['SECRET_KEY'] = 'thisisasecretkey!'# to secure cookies and sesssion data

#imported blueprints
    from .views import views
    from .auth import auth

    app.register_blueprint(views, url_prefix='/')
    app.register_blueprint(auth, url_prefix='/')
    
    return app