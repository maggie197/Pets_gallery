# this file makes the website folder to become a python package
# this will set up flask aplication

from flask import Flask
from flask_sqlalchemy import SQLAlchemy 
from os import path 
from flask_login import LoginManager

db = SQLAlchemy()
DB_NAME = "user.db"   # create a database

def create_app():        #set a function inisializing flask
    app = Flask(__name__)
    app.config['SECRET_KEY'] = 'thisisasecretkey!'# to secure cookies and sesssion data
    app.config ['SQLALCHEMY_DATABASE_URI'] = f'sqlite:///{DB_NAME}' # database location
    db.init_app(app)  

#imported blueprints
    from .views import views
    from .auth import auth

    app.register_blueprint(views, url_prefix='/')
    app.register_blueprint(auth, url_prefix='/')
    
# runs the modules    
    from .modules import User

    with app.app_context():
        db.create_all()

# login manager

    login_manager = LoginManager()
    login_manager.login_view = 'auth.login'
    login_manager.init_app(app)

    @login_manager.user_loader
    def load_user(id):
        return User.query.get(int(id)) # looks for the primary key

    return app

def create_database(app): # checks if db already exist if not then create
    if not path.exists('website/' + DB_NAME):
        db.create_all(app=app)
        print('Created Database!')