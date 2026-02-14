from flask import Flask, jsonify
import sqlite3
import os
import requests
from datetime import datetime

database_path = os.getenv("DATABASE_PATH", "/app/data/restaurant.db")

API_URL = "https://utadeoapi-6dae6e29b5b0.herokuapp.com/api/v1/software-architecture/market-place"

INGREDIENTES = {
    'tomato': '1',
    'lemon': '3',
    'potato': '3',
    'rice': '4',
    'ketchup': '5',
    'lettuce': '6',
    'onion': '7',
    'cheese': '8',
    'meat': '9',
    'chicken': '10'
}

app = Flask(__name__)

@app.route('/health')
def health():
    return {"status": "ok"}

@app.route('/consultar_inventario', methods=['GET'])
def obtener_inventario():
    try:
        conexion = sqlite3.connect(database_path)
        cursor = conexion.cursor()
        cursor.execute('SELECT * FROM Ingredientes')
        inventario = cursor.fetchall()
        cursor.close()
        conexion.close()
        return jsonify({"obtener_inventario": inventario})
    except Exception as e:
        app.logger.error(f"Error en obtener_inventarios: {str(e)}")
        return jsonify({"error": "Hubo un error en el servidor"}), 500

@app.route('/comprar/<ingrediente>', methods=['GET'])
def comprar_ingrediente(ingrediente):
    # Verificar que el ingrediente existe
    ingrediente_id = INGREDIENTES.get(ingrediente)
    if not ingrediente_id:
        return jsonify({"error": f"Ingrediente '{ingrediente}' no encontrado"}), 404

    try:
        # Consultar API externa
        response = requests.get(f'{API_URL}?ingredient={ingrediente}')

        if response.status_code != 200:
            return jsonify({'error': 'Error al hacer la solicitud al servicio web'}), 500

        data = response.json()
        cantidad = data['data'][ingrediente]
        fecha_compra = datetime.now()

        # Actualizar base de datos
        conexion = sqlite3.connect(database_path)
        cursor = conexion.cursor()

        cursor.execute(
            "INSERT INTO compras (ingrediente_id, cantidad_compras, fecha_compra) VALUES (?, ?, ?)",
            (ingrediente_id, cantidad, fecha_compra)
        )

        cursor.execute(
            "UPDATE Ingredientes SET cantidad = cantidad + ? WHERE nombre = ?",
            (cantidad, ingrediente.capitalize())
        )

        conexion.commit()
        conexion.close()

        return jsonify({'mensaje': 'Datos agregados a la base de datos con éxito.', 'cantidad': cantidad}), 200

    except Exception as e:
        app.logger.error(f"Error en comprar_{ingrediente}: {str(e)}")
        return jsonify({"error": "Hubo un error en el servidor"}), 500

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)