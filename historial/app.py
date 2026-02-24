from flask import Flask, jsonify
import os
import psycopg2


DATABASE_URL = os.getenv("DATABASE_URL")


app = Flask(__name__)


@app.after_request
def add_security_headers(response):
    response.headers['X-Content-Type-Options'] = 'nosniff'
    response.headers['X-Frame-Options'] = 'DENY'
    response.headers['X-XSS-Protection'] = '1; mode=block'
    return response


@app.route('/health')
def health():
    return {"status": "ok"}


@app.route('/historial_pedidos', methods=['GET'])
def obtener_historial_pedidos():
    conexion = None
    try:
        conexion = psycopg2.connect(DATABASE_URL)
        cursor = conexion.cursor()
        cursor.execute('SELECT * FROM Pedidos')
        pedidos = cursor.fetchall()
        return jsonify({"historial_pedidos": pedidos})
    except Exception as e:
        app.logger.error(f"Error en obtener_historial_pedidos: {str(e)}")
        return jsonify({"error": "Hubo un error en el servidor"}), 500
    finally:
        if conexion:
            conexion.close()


@app.route('/historial_compras', methods=['GET'])
def obtener_historial_compras():
    conexion = None
    try:
        conexion = psycopg2.connect(DATABASE_URL)
        cursor = conexion.cursor()
        cursor.execute('SELECT * FROM Compras')
        compras = cursor.fetchall()
        return jsonify({"historial_compras": compras})
    except Exception as e:
        app.logger.error(f"Error en obtener_historial_compras: {str(e)}")
        return jsonify({"error": "Hubo un error en el servidor"}), 500
    finally:
        if conexion:
            conexion.close()


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
