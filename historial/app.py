from flask import Flask, request, jsonify, render_template
import os
import sqlite3

database_path = os.path.abspath("/app/restaurant.db")

app = Flask(__name__, static_folder='templates', static_url_path='/static')

@app.route('/health')
def health():
    return {"status": "ok"}

@app.route('/temp')
def hola_mundo():
    return render_template('historial.html')   

# Ruta para obtener el historial de pedidos
@app.route('/historial_pedidos', methods=['GET'])
def obtener_historial_pedidos():
    try:
        conexion = sqlite3.connect(database_path)
        cursor = conexion.cursor()
        cursor.execute('SELECT * FROM Pedidos')
        pedidos = cursor.fetchall()
        cursor.close()
        conexion.close()
        return jsonify({"historial_pedidos": pedidos})
    except Exception as e:
        app.logger.error(f"Error en obtener_historial_pedidos: {str(e)}")
        return jsonify({"error": "Hubo un error en el servidor"}), 500  # Respuesta de error 500


# Ruta para obtener el historial de compras
@app.route('/historial_compras', methods=['GET'])
def obtener_historial_compras():
    try:
        conexion = sqlite3.connect(database_path)
        cursor = conexion.cursor()
        cursor.execute('SELECT * FROM Compras')
        compras = cursor.fetchall()
        cursor.close()
        conexion.close()
        return jsonify({"historial_compras": compras})
    except Exception as e:
        app.logger.error(f"Error en obtener_historial_compras: {str(e)}")
        return jsonify({"error": "Hubo un error en el servidor"}), 500  # Respuesta de error 500

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)