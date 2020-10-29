from flask import Flask
app = Flask(__name__)

@app.route("/")
def hello():
    return "Content to be approved in PR"


if __name__ == "__main__":
    app.run(host='0.0.0.0')