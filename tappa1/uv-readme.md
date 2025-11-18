## Introduzione
Flask è un micro-framework web per Python che permette di creare applicazioni web in modo semplice e veloce.

## Prerequisiti
- Python 3.x installato sul sistema
- Conoscenza base di Python

---

## Installazione di uv (senza privilegi amministratore)

uv può essere installato senza diritti di amministratore.

### Windows


Con Git-bash:
```bash
# Scarica e installa uv nella directory utente
curl -LsSf https://astral.sh/uv/install.sh | sh
```

Eventualmente con powershell
```bash
# Installazione tramite PowerShell 
powershell -c "irm https://astral.sh/uv/install.ps1 | iex"
```

### Linux/Mac
```bash
# Installazione tramite shell script
curl -LsSf https://astral.sh/uv/install.sh | sh
```

**Dopo l'installazione:**
- Chiudi e riapri il terminale
- Verifica l'installazione con: `uv --version`

**Nota:** L'installazione avviene nella directory utente (`~/.local/bin` su Linux/Mac o `%USERPROFILE%\.cargo\bin` su Windows), quindi non servono privilegi amministratore.

Per maggiori dettagli: [https://docs.astral.sh/uv/](https://docs.astral.sh/uv/)

---

## Creazione del progetto con uv

uv gestisce automaticamente l'ambiente virtuale e le dipendenze del progetto.

### Inizializzare il progetto
```bash
# Creare un nuovo progetto Flask con uv
uv init 

# Questo crea:
# - pyproject.toml (configurazione del progetto)
# - .python-version (versione di Python)
# - hello.py (file di esempio, che possiamo rinominare/sostituire)
```

**Nota:** `uv init` crea automaticamente la struttura base del progetto con il nome specificato e la versione Python 3.12.

Si possono specificare il nome della directory e persino la versione di Python:
```bash
# Creare un nuovo progetto Flask con uv
uv init  flask-tutorial --python 3.12

# Questo crea:
# - la cartella flask-tutorial
# - utilizza la versione 3.12 di Python
# - pyproject.toml (configurazione del progetto)
# - .python-version (versione di Python)
# - hello.py (file di esempio, che possiamo rinominare/sostituire)
```
---

## Installazione di Flask

Con uv, aggiungiamo Flask come dipendenza del progetto:

```bash
uv add flask
```

Questo comando:
- Installa Flask e le sue dipendenze
- Crea/aggiorna automaticamente l'ambiente virtuale `.venv`
- Aggiorna il file `pyproject.toml` con la dipendenza
- Crea il file `uv.lock` per garantire build riproducibili

Per verificare le dipendenze installate:
```bash
uv tree
```

---

## Prima applicazione Flask

### Creare il file `app.py`

Crea un file chiamato `app.py` con il seguente contenuto:

```python
from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return "Benvenuti nel tutorial Flask!"

if __name__ == '__main__':
    app.run(debug=True)
```

### Spiegazione del codice:
- `from flask import Flask` - importa la classe Flask
- `app = Flask(__name__)` - crea un'istanza dell'applicazione Flask
- `@app.route('/')` - decoratore che definisce il percorso URL
- `def home()` - funzione che gestisce la richiesta
- `app.run(debug=True)` - avvia il server in modalità debug

### Eseguire l'applicazione

Con uv, esegui l'applicazione direttamente:

```bash
uv run app.py
```

**Nota:** `uv run` esegue automaticamente il codice nell'ambiente virtuale gestito da uv, senza bisogno di attivarlo manualmente.

Apri il browser e vai su: `http://127.0.0.1:5000/`

---

## Comandi utili di uv

```bash
# Aggiungere una dipendenza
uv add <package-name>

# Rimuovere una dipendenza
uv remove <package-name>

# Visualizzare l'albero delle dipendenze
uv tree

# Sincronizzare l'ambiente con pyproject.toml
uv sync

# Eseguire un comando nell'ambiente virtuale
uv run <comando>
```