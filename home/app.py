
from flask import Flask, request, jsonify, render_template
import requests
import os

HISTORIAL_SERVICE = os.getenv(
    "HISTORIAL_SERVICE",
    "http://historial:5000"
)
COCINA_SERVICE = os.getenv(
    "COCINA_SERVICE",
    "http://cocina:5000"
)

INVENTARIO_SERVICE = os.getenv(
    "INVENTARIO_SERVICE",
    "http://inventario:5000"
)

app = Flask(__name__, static_folder='templates', static_url_path='/static')

@app.route('/home')
def home():
    return render_template('home.html')

@app.route('/historial')
def historial():
    return render_template('historial.html')

@app.route('/inventario')
def inventario():
    return render_template('inventario.html')

@app.route('/cocina')
def cocina():
    return render_template('cocina.html')

@app.route('/test-historial')
def test_historial():
    response = requests.get(f'{HISTORIAL_SERVICE}/historial_pedidos')
    return response.json()

@app.route('/test-cocina')
def test_cocina():
    r = requests.get(f'{COCINA_SERVICE}/recetas')
    return r.json()

@app.route('/test-inventario')
def test_inventario():
    r = requests.get(f'{INVENTARIO_SERVICE}/inventario')
    return r.json()

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)