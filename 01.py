from flask import Flask

app = Flask(__name__)


@app.route("/")
def hello_world():
    return "Hello, World!"


@app.route("/hello")
def hello():
    html = "<html><body><h1>Hello</h1></body></html>"
    return html


@app.route("/hello/<name>")
def hello_user(name):
    html = f"<html><body><h1>Hello {name}</h1></body></html>"
    return html


if __name__ == '__main__':
    app.run(debug=True)
