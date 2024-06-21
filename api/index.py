from flask import Flask
from functions import plustwo

app = Flask(__name__)

@app.route('/')
def home():
    return "hello world"

@app.route('/about')
def about():
    return "abouts"
