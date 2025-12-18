# Tappa 5 - Fetch API: Comunicazione Frontend-Backend

## Sommario della lezione

In questa tappa abbiamo integrato JavaScript con Flask per creare un'applicazione web dinamica che comunica con l'API backend senza ricaricare la pagina.

### 1. Introduzione alla Fetch API

La **Fetch API** è il metodo moderno di JavaScript per fare richieste HTTP al server in modo asincrono.

**Vantaggi:**
- Nessun reload della pagina
- Aggiornamenti in tempo reale
- Migliore esperienza utente
- Comunicazione JSON nativa

### 2. Struttura del Progetto

```
tappa5-fetch/
│
├── app.py                  # Backend Flask con API REST
├── templates/
│   ├── base.html          # Template base
│   ├── index.html         # Home page
│   └── jsdemo.html        # Pagina demo JavaScript
└── static/
    └── js/
        └── api.js         # Codice JavaScript per fetch
```

### 3. GET: Recuperare Dati dal Server

**Obiettivo:** Caricare la lista degli studenti dal backend e visualizzarla nella pagina.

**File: `static/js/api.js`**
```javascript
async function caricaStudenti() {
    // Seleziona l'elemento lista HTML
    const lista = document.getElementById("lista-studenti");
    lista.textContent = "Caricamento lista";

    // Richiesta GET all'API
    const response = await fetch('/api/studenti');
    const studenti = await response.json();

    // Pulisci la lista
    lista.textContent = "";
    
    // Crea un elemento <li> per ogni studente
    studenti.forEach(studente => {
        const item = document.createElement('li');
        item.textContent = `${studente.nome} - Classe ${studente.classe}`;
        lista.appendChild(item);
    });
}

// Carica automaticamente gli studenti quando la pagina è pronta
document.addEventListener('DOMContentLoaded', function() {
    caricaStudenti();
});
```

**Spiegazione:**
1. `fetch('/api/studenti')` - Fa una richiesta GET all'endpoint
2. `await response.json()` - Converte la risposta in oggetto JavaScript
3. `forEach()` - Itera su ogni studente ricevuto
4. `createElement('li')` - Crea dinamicamente elementi HTML
5. `DOMContentLoaded` - Esegue il codice quando il DOM è pronto

### 4. POST: Inviare Dati al Server

**Obiettivo:** Permettere all'utente di aggiungere nuovi studenti tramite un form.

**File: `templates/jsdemo.html`**
```html
{% extends "base.html" %}

{% block title %}JS Demo{% endblock %}

{% block content %}
    <h1>JS DEMO</h1>
    
    <h2>Lista studenti</h2>
    <ul id="lista-studenti"></ul>
    
    <h2>Aggiungi studente</h2>
    <input type="text" id="nome_studente" placeholder="Inserisci Nome" required>
    <input type="text" id="classe_studente" placeholder="Classe" required>
    <button id="bottone-aggiungi">Aggiungi studente</button>
    
    <script src="{{ url_for('static', filename='js/api.js') }}"></script>
{% endblock %}
```

**File: `static/js/api.js`**
```javascript
const bottone_aggiungi = document.getElementById('bottone-aggiungi');
bottone_aggiungi.addEventListener('click', aggiungiStudente);

async function aggiungiStudente() {
    // Legge i valori dagli input
    const nome = document.getElementById("nome_studente").value;
    const classe = document.getElementById("classe_studente").value;
    
    // Validazione
    if (!nome || !classe) {
        alert("Inserisci nome e classe!");
        return;
    }

    // Crea l'oggetto da inviare
    const nuovoStudente = {
        nome: nome,
        classe: classe
    };

    // Richiesta POST all'API
    const response = await fetch('/api/studenti', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
        },
        body: JSON.stringify(nuovoStudente)
    });

    const studenteCreato = await response.json();
    console.log(studenteCreato);

    // Ricarica la lista aggiornata
    caricaStudenti();
}
```

**Spiegazione:**
1. `addEventListener('click')` - Collega la funzione al click del bottone
2. `value` - Legge il contenuto degli input
3. Validazione - Controlla che i campi non siano vuoti
4. `JSON.stringify()` - Converte l'oggetto JavaScript in stringa JSON
5. **Headers** - Specifica che stiamo inviando JSON
6. **method: 'POST'** - Indica il tipo di richiesta
7. `caricaStudenti()` - Ricarica la lista per vedere il nuovo studente

### 5. Concetti Chiave di Fetch

**Anatomia di una richiesta Fetch:**

```javascript
const response = await fetch(url, {
    method: 'GET|POST|PUT|DELETE',    // Metodo HTTP
    headers: {                         // Intestazioni
        'Content-Type': 'application/json'
    },
    body: JSON.stringify(data)         // Dati da inviare (solo POST/PUT)
});

const data = await response.json();   // Parsing della risposta
```

**Metodi HTTP usati:**
- **GET** - Recuperare dati (default, non richiede `body`)
- **POST** - Creare nuovi dati (richiede `body`)

**Async/Await:**
- `async function` - Dichiara una funzione asincrona
- `await` - Aspetta il completamento di una Promise
- Rende il codice più leggibile rispetto ai `.then()`

### 6. Collegare JavaScript al Template

Per usare file JavaScript esterni, usa `url_for()` in Jinja2:

```html
<script src="{{ url_for('static', filename='js/api.js') }}"></script>
```

Questo genera automaticamente il path corretto: `/static/js/api.js`

### 7. Backend Flask

**File: `app.py`**
```python
from flask import Flask, render_template, jsonify, request

app = Flask(__name__)

studenti_db = [
    {"id": 1, "nome": "Mario Rossi", "classe": "4A"},
    {"id": 2, "nome": "Laura Bianchi", "classe": "4B"},
    {"id": 3, "nome": "Giovanni Verdi", "classe": "4A"},
]

@app.route("/jsdemo")
def js_demo():
    return render_template("jsdemo.html")

# GET - Tutti gli studenti
@app.route("/api/studenti", methods=['GET'])
def get_studenti():
    return jsonify(studenti_db)

# POST - Aggiungi studente
@app.route("/api/studenti", methods=['POST'])
def add_studente():
    dati = request.get_json()
    
    if not dati or 'nome' not in dati or 'classe' not in dati:
        return jsonify({"errore": "Dati incompleti"}), 400

    new_id = studenti_db[-1]['id'] + 1
    nuovo_studente = {
        "id": new_id,
        "nome": dati['nome'],
        "classe": dati['classe']
    }
    studenti_db.append(nuovo_studente)
    return jsonify(nuovo_studente), 200

if __name__ == "__main__":
    app.run(debug=True)
```

### 8. Workflow Completo

**Quando l'utente clicca "Aggiungi studente":**

1. **Frontend (JavaScript):**
   - Legge i valori dagli input HTML
   - Crea un oggetto JSON con i dati
   - Invia richiesta POST a `/api/studenti`

2. **Backend (Flask):**
   - Riceve la richiesta POST
   - Valida i dati
   - Aggiunge lo studente al database
   - Restituisce il nuovo studente come JSON

3. **Frontend (JavaScript):**
   - Riceve la risposta
   - Richiama `caricaStudenti()` per aggiornare la lista
   - La nuova lista viene visualizzata senza reload

### 9. Console del Browser per Debug

Usa la console del browser per debuggare:

```javascript
console.log(studenteCreato);  // Vedere i dati ricevuti
console.log(response);         // Vedere l'oggetto response
```

**Come aprire la console:**
- Chrome/Edge: F12 → Tab "Console"
- Firefox: F12 → Tab "Console"

### 10. Testare l'Applicazione

1. Avvia il server: `uv run app.py`
2. Vai su: `http://127.0.0.1:5000/jsdemo`
3. La lista studenti appare automaticamente (GET)
4. Compila i campi e clicca "Aggiungi studente" (POST)
5. La lista si aggiorna senza ricaricare la pagina!

---

## Cosa Abbiamo Imparato

✅ **Fetch API** - Comunicazione asincrona con il server  
✅ **GET** - Recuperare dati con `fetch(url)`  
✅ **POST** - Inviare dati con `method: 'POST'` e `body`  
✅ **Async/Await** - Gestire operazioni asincrone  
✅ **DOM Manipulation** - Creare elementi HTML dinamicamente  
✅ **Event Listeners** - Rispondere a eventi utente  
✅ **JSON** - Scambiare dati tra frontend e backend  
✅ **SPA Basics** - Aggiornamenti dinamici senza reload

---

