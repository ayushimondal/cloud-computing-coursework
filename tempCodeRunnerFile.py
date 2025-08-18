from markupsafe import escape
from flask import flask

@app.route("/")
def hello():
    return '<h1>Hello, World!</h1>'

