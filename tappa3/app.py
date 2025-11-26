from flask import Flask, render_template

app = Flask(__name__)


@app.route("/")
def home():
    return render_template("index.html")

@app.route("/studenti")
def studenti():
    lista_studenti= ['Studente 1', 'Studente2', "Studente3", "fulvio Frapolli"]
    return render_template("studenti.html", studenti=lista_studenti)


@app.route("/about")
def about():
    mess = "Contenuto del mio messaggio üüüüüüü "
    return render_template("index.html", messaggio=mess)


@app.route("/classe/<string:nome>")
def nome_classe(nome):
    return f"Il nome è {nome}"


@app.route("/classe/<int:anno>")
def anno_classe(anno):
    return f"Anno: {anno}"


if __name__ == "__main__":
    app.run(debug=True)
