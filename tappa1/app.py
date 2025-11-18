from flask import Flask

app = Flask(__name__)


@app.route("/")
def home():
    return "Benvenuti nel tutorial Flask!"


if __name__ == "__main__":
    app.run(debug=True)
