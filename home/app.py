from flask import Flask, jsonify, render_template, request
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


@app.after_request
def add_security_headers(response):
    response.headers['X-Content-Type-Options'] = 'nosniff'
    response.headers['X-Frame-Options'] = 'SAMEORIGIN'
    response.headers['X-XSS-Protection'] = '1; mode=block'
    response.headers['Strict-Transport-Security'] = 'max-age=31536000; includeSubDomains'
    return response


@app.route('/health')
def health():
    return {"status": "ok"}


@app.route('/')
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


@app.route('/api/<servicio>/<path:ruta>', methods=['GET', 'POST'])
def proxy(servicio, ruta):
    servicios = {
        'historial': HISTORIAL_SERVICE,
        'inventario': INVENTARIO_SERVICE,
        'cocina': COCINA_SERVICE,
    }

    url_servicio = servicios.get(servicio)
    if not url_servicio:
        return jsonify({"error": "Servicio no encontrado"}), 404

    if request.method == 'POST':
        body = request.get_json(silent=True)
        respuesta = requests.post(
            f'{url_servicio}/{ruta}',
            json=body if body else None,
            allow_redirects=False
        )
        if respuesta.status_code in (301, 302):
            respuesta = requests.post(
                respuesta.headers['Location'],
                json=body if body else None
            )
    else:
        respuesta = requests.get(f'{url_servicio}/{ruta}')

    return jsonify(respuesta.json()), respuesta.status_code


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
