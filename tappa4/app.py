from flask import Flask, render_template, jsonify, request

app = Flask(__name__)


studenti_db=[
    {"id" : 1 , "nome" : "Mario Rossi" , "classe" : "4A"},
    {"id" : 2 , "nome" : "Laura Bianchi" , "classe" : "4B"},
    {"id" : 3 , "nome" : "Giovani Verdi" , "classe" : "4A"},
]


@app.route("/")
def home():
    return render_template("index.html")




@app.route("/api/studenti/<int:studente_id>")
def get_studente(studente_id):
    for studente in studenti_db:
        if studente["id"]==studente_id:
            return jsonify(studente), 200        
    return jsonify({"errore": "Studente non trovato"}), 404

@app.route("/api/studenti", methods=['GET'])
def get_studenti():
    return jsonify(studenti_db)


@app.route("/api/studenti", methods=['POST'])
def add_studente():
    dati= request.get_json()
    print(dati) ## Testiamo 
    ## Validazione, ci sono tutti i dati?
    if not(dati) or 'nome' not in dati or 'classe' not in dati:
        return jsonify({"errore": "Dati incompleti"}), 400

    #Creiamo l'elemento da aggiungere alla lista e lo aggiungiamo
    new_id = studenti_db[-1]['id']+1
    
    nuovo_studente= {
        "id": new_id,
        "nome" : dati['nome'],
        "classe" : dati['classe']
    }

    studenti_db.append(nuovo_studente)

    return jsonify(nuovo_studente), 200

@app.route("/api/studenti/<int:studente_id>" , methods=['PUT'])
def update_studente(studente_id):

    print(request.method)
    #validazione 
    dati = request.get_json()
    for studente in studenti_db:
        if studente['id']==studente_id:
            if 'nome' in dati:
                studente['nome'] = dati['nome']
            if 'classe' in dati:
                studente['classe'] = dati['classe']
            return jsonify(studente), 200
    
    return jsonify({"errore": "Studente non trovato"}), 404
    
@app.route("/api/studenti/<int:studente_id>" , methods=['DELETE'])
def delete_student(studente_id):
    for studente in studenti_db:
        if studente['id']==studente_id:
            studenti_db.remove(studente)
            return jsonify(studente), 200

    return jsonify({"errore": "Studente non trovato"}), 404

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
