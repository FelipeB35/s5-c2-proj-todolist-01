from flask import Flask

def home():
    print("Hola ESEN!")

app = Flask(__name__)

@app.route("/")

def home():
    pass