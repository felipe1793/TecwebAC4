from flask import flask
app =flask(__name__)

@app.route('/')
def hello_world():
    return '<h1> Hello, World!</h1>'