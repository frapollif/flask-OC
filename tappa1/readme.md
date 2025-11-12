## Introduzione
Flask è un micro-framework web per Python che permette di creare applicazioni web in modo semplice e veloce.

## Prerequisiti
- Python 3.x installato sul sistema
- Conoscenza base di Python

---

## Creazione dell'ambiente virtuale (.venv)

L'ambiente virtuale permette di isolare le dipendenze del progetto.

### Windows
```bash
# Creare l'ambiente virtuale
python -m venv .venv

# Attivare l'ambiente virtuale
.venv\Scripts\activate
```

### Linux/Mac
```bash
# Creare l'ambiente virtuale
python3 -m venv .venv

# Attivare l'ambiente virtuale
source .venv/bin/activate
```

**Nota:** Quando l'ambiente virtuale è attivo, vedrai `(.venv)` all'inizio della riga di comando.

---

## Installazione di Flask

Con l'ambiente virtuale attivo, installiamo Flask usando pip:

```bash
pip install Flask
```

Per verificare l'installazione:
```bash
pip list
```

Dovresti vedere Flask e le sue dipendenze nella lista.

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

```bash
python app.py
```

Apri il browser e vai su: `http://127.0.0.1:5000/`

---