from flask import Flask
app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello from the test app! This is updated content!!"


if __name__ == "__main__":
    app.run(host='0.0.0.0')