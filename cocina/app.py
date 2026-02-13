from flask import Flask, request, jsonify
import sqlite3
import os
import random

database_path = os.getenv("DATABASE_PATH", "/app/data/restaurant.db")

app = Flask(__name__)

@app.route('/health')
def health():
    return {"status": "ok"}

@app.route('/recetas', methods=['GET'])
def obtener_recetas():
    try:
        conexion = sqlite3.connect(database_path)
        cursor = conexion.cursor()
        cursor.execute('SELECT * FROM Recetas')
        recetas = cursor.fetchall()
        cursor.close()
        conexion.close()
        return jsonify({"obtener_recetas": recetas})
    except Exception as e:
        app.logger.error(f"Error en obtener_recetas: {str(e)}")
        return jsonify({"error": "Hubo un error en el servidor"}), 500  # Respuesta de error 500

@app.route('/agregar_pedido', methods=['GET'])
def agregar_pedido():
    try:
        conexion = sqlite3.connect(database_path)

        # Obtén todas las recetas disponibles
        cursor = conexion.cursor()
        cursor.execute('SELECT * FROM Recetas')
        recetas = cursor.fetchall()
        cursor.close()

        # Selecciona una receta aleatoria
        receta_aleatoria = random.choice(recetas)

        # Actualiza el estado del pedido anterior a "listo"
        cursor = conexion.cursor()
        cursor.execute('SELECT id FROM Pedidos WHERE estado = "en proceso" ORDER BY id DESC LIMIT 1')
        ultimo_pedido_id = cursor.fetchone()

        if ultimo_pedido_id:
            ultimo_pedido_id = ultimo_pedido_id[0]
            cursor.execute('UPDATE Pedidos SET estado = "listo" WHERE id = ?', (ultimo_pedido_id,))
            conexion.commit()

        # Crea un nuevo pedido con la receta seleccionada y estado "en proceso"
        cursor = conexion.cursor()
        cursor.execute('INSERT INTO Pedidos (plato, estado) VALUES (?, ?)',
                       (receta_aleatoria[0], 'en proceso'))
        conexion.commit()
        cursor.close()

        # Obtén los ingredientes de la receta
        cursor = conexion.cursor()
        cursor.execute('SELECT ingrediente_id, cantidad_ingredientes FROM Ingredientes_recetas WHERE receta_id = ?', (receta_aleatoria[0],))
        ingredientes = cursor.fetchall()
        cursor.close()

        # Resta unidades de cada ingrediente en la tabla de ingredientes
        for ingrediente_id, cantidad in ingredientes:
            cursor = conexion.cursor()
            cursor.execute('UPDATE Ingredientes SET cantidad = cantidad - ? WHERE id = ?', (cantidad, ingrediente_id))
            conexion.commit()
            cursor.close()

        return jsonify({'mensaje': 'Pedido agregado con éxito', 'plato': receta_aleatoria[0]})
    except Exception as e:
        return jsonify({"error": "Hubo un error en el servidor"}), 500  # Respuesta de error 500
    
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)