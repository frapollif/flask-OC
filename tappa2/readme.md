# Tappa 2 - Route e Parametri in Flask

## Sommario degli argomenti

In questa tappa del tutorial abbiamo imparato a:

### 1. Creare Route Multiple
- Definire diverse route per gestire pagine differenti dell'applicazione
- Ogni route corrisponde a un URL specifico (es. `/`, `/about`)
- Usare il decoratore `@app.route()` per associare funzioni a URL

### 2. Route con Parametri
- Passare parametri dinamici nelle route usando la sintassi `<nome_parametro>`
- I parametri vengono catturati dall'URL e passati alla funzione

### 3. Tipi di Parametri nelle Route

Flask supporta diversi tipi di parametri che possono essere specificati nella route:

#### Tipi più usati:
- **`string`** (default) - Accetta qualsiasi testo senza slash
  ```python
  @app.route('/classe/<string:nome>')
  def nome_classe(nome):
      return f"Il nome è {nome}"
  ```

- **`int`** - Accetta solo numeri interi
  ```python
  @app.route('/classe/<int:anno>')
  def anno_classe(anno):
      return f"Anno: {anno}"
  ```

- **`float`** - Accetta numeri decimali
  ```python
  @app.route('/prezzo/<float:valore>')
  def prezzo(valore):
      return f"Prezzo: {valore}€"
  ```

- **`path`** - Come string, ma accetta anche gli slash (/)
  ```python
  @app.route('/files/<path:filepath>')
  def show_file(filepath):
      return f"File: {filepath}"
  ```

#### Altri tipi disponibili:
- **`uuid`** - Accetta stringhe UUID
  ```python
  @app.route('/user/<uuid:user_id>')
  def user_profile(user_id):
      return f"User ID: {user_id}"
  ```

### Esempio Completo

```python
from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return "Benvenuti nel tutorial Flask!"

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
```

### Testare le Route

Dopo aver avviato l'applicazione con `uv run app.py`, puoi testare:
- `http://127.0.0.1:5000/` - Home page
- `http://127.0.0.1:5000/about` - Pagina About
- `http://127.0.0.1:5000/classe/3A` - Parametro stringa (nome = "3A")
- `http://127.0.0.1:5000/classe/2024` - Parametro intero (anno = 2024)

---

## Prossimi Passi

Nella prossima tappa esploreremo i template HTML con Jinja2 per creare pagine web più complesse e dinamiche.
