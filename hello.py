from flask import Flask, request, render_template

app = Flask(__name__)


@app.route("/")
def hello_world():
    return "Hello,World"


# ログイン機能
@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "GET":
        return render_template("login.html")
    if request.method == "POST":
        return "Log in!"


if __name__ == '__main__':
    hostname = "127.0.0.1"
    port = 5001
    app.run(port=5001, debug=True)
