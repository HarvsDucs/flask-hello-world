from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return jsonify({
        'message': 'Hello World'
    })

@app.route('/about')
def about():
    return 'About'
