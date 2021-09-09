from logging import debug
from flask import Flask

app = Flask(__name__)


@app.route("/")
@app.route("/home")
def home():
    return "<h1>Welcome to the portal of SAVIOUR </h1>"


@app.route("/about")
def about():
    return "<h1>We are here to save you. </h1>"


if __name__ == "__main__":
    app.run(debug=True)
