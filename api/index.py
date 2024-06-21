from flask import Flask
from function import plustwo

app = Flask(__name__)

@app.route('/')
def home():
    x = 2
    return f"Message is: {plustwo(x)}"

@app.route('/about')
def about():
    x = 2
    return f"Message is: {plustwo(x)}"
