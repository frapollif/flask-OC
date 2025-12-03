# Tappa 3 - Templates HTML e Jinja2

## Sommario degli argomenti

In questa tappa del tutorial abbiamo imparato:

### 1. Template HTML con Flask
- Usare `render_template()` per caricare file HTML
- Creare la cartella `templates/` per contenere i file HTML
- Separare la logica Python dalla presentazione HTML

### 2. Passare Parametri ai Template
- Inviare dati dalla route Python al template HTML
- Usare parametri nominati nella funzione `render_template()`
- Esempio: `render_template('index.html', messaggio=mess)`

### 3. Sintassi Jinja2

Jinja2 è il motore di template utilizzato da Flask. Permette di inserire logica dinamica nei file HTML.

#### Principali elementi della sintassi Jinja2:

**1. Variabili - `{{ }}`**
```html
<!-- Visualizzare una variabile -->
<p>{{ messaggio }}</p>
<h1>Benvenuto {{ nome_utente }}!</h1>
<p>Il prezzo è {{ prezzo }}€</p>
```

**2. Commenti - `{# #}`**
```html
{# Questo è un commento e non viene visualizzato #}
<p>Contenuto visibile</p>
```

**3. Istruzioni di controllo - `{% %}`**

**Condizioni (if/else):**
```html
{% if utente_loggato %}
    <p>Benvenuto, {{ nome }}!</p>
{% else %}
    <p>Per favore, effettua il login.</p>
{% endif %}
```

**Loop (for):**
```html
<ul>
{% for studente in lista_studenti %}
    <li>{{ studente }}</li>
{% endfor %}
</ul>
```

**4. Filtri - `|`**
```html
<!-- Convertire in maiuscolo -->
<p>{{ nome | upper }}</p>

<!-- Convertire in minuscolo -->
<p>{{ nome | lower }}</p>

<!-- Capitalizzare la prima lettera -->
<p>{{ nome | capitalize }}</p>

<!-- Valore di default se la variabile è vuota -->
<p>{{ messaggio | default('Nessun messaggio') }}</p>

<!-- Lunghezza di una lista -->
<p>Numero studenti: {{ lista_studenti | length }}</p>
```

**5. Ereditarietà dei template**
```html
<!-- base.html - template base -->
<!DOCTYPE html>
<html>
<head>
    <title>{% block title %}Titolo di default{% endblock %}</title>
</head>
<body>
    {% block content %}
    <!-- Il contenuto sarà inserito qui -->
    {% endblock %}
</body>
</html>

<!-- pagina.html - template figlio -->
{% extends "base.html" %}

{% block title %}Titolo personalizzato{% endblock %}

{% block content %}
    <h1>Contenuto della pagina</h1>
{% endblock %}
```

### Esempio Completo

**File: `app.py`**
```python
from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def home():
    return render_template('index.html')

@app.route("/about")
def about():
    mess = "Contenuto del mio messaggio"
    return render_template('index.html', messaggio=mess)

@app.route("/studenti")
def studenti():
    lista = ["Mario", "Luigi", "Anna", "Sofia"]
    return render_template('studenti.html', studenti=lista)

if __name__ == "__main__":
    app.run(debug=True)
```

**File: `templates/base.html`** (Template Base)
```html
<!DOCTYPE html>
<html lang="it">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{% block title %}Tutorial Flask{% endblock %}</title>
</head>
<body>
    <header>
        <nav>
            <a href="/">Home</a> | 
            <a href="/about">About</a> | 
            <a href="/studenti">Studenti</a>
        </nav>
    </header>
    
    <main>
        {% block content %}
        <!-- Il contenuto delle pagine figlie sarà inserito qui -->
        {% endblock %}
    </main>
    
    <footer>
        <p>&copy; 2025 Tutorial Flask</p>
    </footer>
</body>
</html>
```

**File: `templates/index.html`** (Eredita da base.html)
```html
{% extends "base.html" %}

{% block title %}Home - Tutorial Flask{% endblock %}

{% block content %}
    <h1>TITOLO DELLA PAGINA</h1>
    <p>Contenuto della pagina</p>
    
    <!-- Visualizzare una variabile passata da Python -->
    {% if messaggio %}
        <p><strong>Messaggio:</strong> {{ messaggio }}</p>
    {% endif %}
{% endblock %}
```

**File: `templates/studenti.html`** (Eredita da base.html)
```html
{% extends "base.html" %}

{% block title %}Lista Studenti - Tutorial Flask{% endblock %}

{% block content %}
    <h1>Lista degli Studenti</h1>
    <ul>
    {% for studente in studenti %}
        <li>{{ studente }}</li>
    {% endfor %}
    </ul>
    
    <p><strong>Totale studenti:</strong> {{ studenti | length }}</p>
{% endblock %}
```

### Struttura delle Cartelle

```
progetto/
│
├── app.py
└── templates/
    ├── base.html
    ├── index.html
    └── studenti.html
```

**Importante:** La cartella `templates` deve trovarsi nella stessa directory del file `app.py`.

### Testare i Template

Dopo aver avviato l'applicazione con `uv run app.py`:
- `http://127.0.0.1:5000/` - Home page senza messaggio
- `http://127.0.0.1:5000/about` - Pagina con messaggio dinamico
- `http://127.0.0.1:5000/studenti` - Lista di studenti con loop

---


