from flask import Flask  # type: ignore

app = Flask(__name__)

@app.route("/")
def pagina_inicial():
    return "Hello World"