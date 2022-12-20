# this file makes the website folder to become a python package
# this will set up flask aplication

from flask import Flask

def create_app():        #set a function inisializing flask
    app = Flask(__name__)
    app.config['SECRET_KEY'] = 'thisisasecretkey!'# to secure cookies and sesssion data

    return app