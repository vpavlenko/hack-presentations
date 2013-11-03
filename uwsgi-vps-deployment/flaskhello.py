from flask import Flaskapp = Flask(__name__)@app.route('/<address>')def hello_world(address):    return 'Hello World! Called with ' + addressfrom flask import Flask
app = Flask(__name__)

@app.route('/<address>')
def hello_world(address):
    return 'Hello World! Called with ' + address
