# Tappa 4 - API REST e Gestione Dati JSON

## Sommario degli argomenti

In questa tappa del tutorial abbiamo imparato a creare una API REST completa per gestire una risorsa (studenti) con operazioni CRUD (Create, Read, Update, Delete).

### 1. API REST e JSON
- Creare endpoint API con Flask
- Usare `jsonify()` per restituire dati in formato JSON
- Strutturare risposte API con codici di stato HTTP

### 2. Metodi HTTP

Flask supporta diversi metodi HTTP per le operazioni CRUD:

| Metodo | Operazione | Descrizione |
|--------|-----------|-------------|
| **GET** | Read | Leggere/ottenere dati |
| **POST** | Create | Creare nuovi dati |
| **PUT** | Update | Aggiornare dati esistenti |
| **DELETE** | Delete | Eliminare dati |

**Sintassi:**
```python
@app.route("/api/studenti", methods=['GET'])
def get_studenti():
    # gestione richiesta GET
    pass

@app.route("/api/studenti", methods=['POST'])
def add_studente():
    # gestione richiesta POST
    pass
```

### 3. Codici di Stato HTTP

I codici di stato indicano l'esito di una richiesta:

| Codice | Significato | Quando usarlo |
|--------|-------------|---------------|
| **200** | OK | Operazione riuscita |
| **201** | Created | Risorsa creata con successo |
| **400** | Bad Request | Dati inviati non validi |
| **404** | Not Found | Risorsa non trovata |
| **500** | Server Error | Errore interno del server |

**Sintassi:**
```python
return jsonify(dati), 200  # Successo
return jsonify({"errore": "Messaggio"}), 404  # Non trovato
```

### 4. Ricevere Dati JSON
- Usare `request.get_json()` per leggere il body della richiesta
- Validare i dati ricevuti
- Gestire dati mancanti o non validi

```python
from flask import request

dati = request.get_json()
if not dati or 'nome' not in dati:
    return jsonify({"errore": "Dati incompleti"}), 400
```

### 5. Database Simulato
In questa tappa usiamo una lista Python come database temporaneo:

```python
studenti_db = [
    {"id": 1, "nome": "Mario Rossi", "classe": "4A"},
    {"id": 2, "nome": "Laura Bianchi", "classe": "4B"},
    {"id": 3, "nome": "Giovanni Verdi", "classe": "4A"},
]
```

### 6. Thunder Client (o Postman)

**Thunder Client** è un'estensione di VS Code per testare API REST.

#### Come installarlo:
1. Aprire VS Code
2. Andare su Extensions (Ctrl+Shift+X)
3. Cercare "Thunder Client"
4. Cliccare su "Install"

#### Come testare le API:

**1. GET - Ottenere tutti gli studenti**
- Metodo: GET
- URL: `http://127.0.0.1:5000/api/studenti`

**2. GET - Ottenere uno studente specifico**
- Metodo: GET
- URL: `http://127.0.0.1:5000/api/studenti/1`

**3. POST - Aggiungere un nuovo studente**
- Metodo: POST
- URL: `http://127.0.0.1:5000/api/studenti`
- Headers: `Content-Type: application/json`
- Body (JSON):
```json
{
    "nome": "Paolo Neri",
    "classe": "4C"
}
```

**4. PUT - Modificare uno studente esistente**
- Metodo: PUT
- URL: `http://127.0.0.1:5000/api/studenti/1`
- Headers: `Content-Type: application/json`
- Body (JSON):
```json
{
    "nome": "Mario Rossi",
    "classe": "5A"
}
```

**5. DELETE - Eliminare uno studente**
- Metodo: DELETE
- URL: `http://127.0.0.1:5000/api/studenti/1`

### Esempio Completo

**File: `app.py`**
```python
from flask import Flask, render_template, jsonify, request

app = Flask(__name__)

# Database simulato
studenti_db = [
    {"id": 1, "nome": "Mario Rossi", "classe": "4A"},
    {"id": 2, "nome": "Laura Bianchi", "classe": "4B"},
    {"id": 3, "nome": "Giovanni Verdi", "classe": "4A"},
]

@app.route("/")
def home():
    return render_template("index.html")

# GET - Ottenere tutti gli studenti
@app.route("/api/studenti", methods=['GET'])
def get_studenti():
    return jsonify(studenti_db)

# GET - Ottenere uno studente specifico
@app.route("/api/studenti/<int:studente_id>")
def get_studente(studente_id):
    for studente in studenti_db:
        if studente["id"] == studente_id:
            return jsonify(studente), 200        
    return jsonify({"errore": "Studente non trovato"}), 404

# POST - Aggiungere un nuovo studente
@app.route("/api/studenti", methods=['POST'])
def add_studente():
    dati = request.get_json()
    
    # Validazione: ci sono tutti i dati?
    if not dati or 'nome' not in dati or 'classe' not in dati:
        return jsonify({"errore": "Dati incompleti"}), 400

    # Creiamo l'elemento da aggiungere
    new_id = studenti_db[-1]['id'] + 1
    
    nuovo_studente = {
        "id": new_id,
        "nome": dati['nome'],
        "classe": dati['classe']
    }

    studenti_db.append(nuovo_studente)
    return jsonify(nuovo_studente), 200

# PUT - Modificare uno studente esistente
@app.route("/api/studenti/<int:studente_id>", methods=['PUT'])
def update_studente(studente_id):
    dati = request.get_json()
    
    for studente in studenti_db:
        if studente['id'] == studente_id:
            # Aggiorniamo solo i campi presenti nei dati
            if 'nome' in dati:
                studente['nome'] = dati['nome']
            if 'classe' in dati:
                studente['classe'] = dati['classe']
            return jsonify(studente), 200
    
    return jsonify({"errore": "Studente non trovato"}), 404

# DELETE - Eliminare uno studente
@app.route("/api/studenti/<int:studente_id>", methods=['DELETE'])
def delete_student(studente_id):
    for studente in studenti_db:
        if studente['id'] == studente_id:
            studenti_db.remove(studente)
            return jsonify(studente), 200

    return jsonify({"errore": "Studente non trovato"}), 404

if __name__ == "__main__":
    app.run(debug=True)
```

### Testare l'API con Thunder Client

Dopo aver avviato l'applicazione con `uv run app.py`, apri Thunder Client in VS Code e testa i vari endpoint:

1. **GET tutti gli studenti** → Dovresti vedere la lista completa
2. **GET studente specifico** → Prova con ID 1, 2, 3
3. **POST nuovo studente** → Aggiungi "Paolo Neri" in classe "4C"
4. **PUT modifica studente** → Cambia la classe di uno studente
5. **DELETE elimina studente** → Rimuovi uno studente dalla lista

### Struttura del Progetto

```
progetto/
│
├── app.py
└── templates/
    └── base.html
    └── index.html
    └── studenti.html
```



