from flask import Flask

app = Flask(__name__)


@app.route("/")
def home():
    return "Benvenuti nel tutorial Flask!  CIAO"


@app.route("/about")
def about():
    return "<h1>About section</h1>"


@app.route("/classe/<string:nome>")
def nome_classe(nome):
    return f"Il nome è {nome}"


@app.route("/classe/<int:anno>")
def anno_classe(anno):
    return f"Anno: {anno}"


if __name__ == "__main__":
    app.run(debug=True)
