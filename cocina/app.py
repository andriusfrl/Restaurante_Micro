from flask import Flask, jsonify
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
        return jsonify({"error": "Hubo un error en el servidor"}), 500

@app.route('/agregar_pedido', methods=['GET'])
def agregar_pedido():
    try:
        conexion = sqlite3.connect(database_path)
        cursor = conexion.cursor()

        # Obtén todas las recetas disponibles
        cursor.execute('SELECT * FROM Recetas')
        recetas = cursor.fetchall()

        # Selecciona una receta aleatoria
        receta_aleatoria = random.choice(recetas)

        # Actualiza el estado del pedido anterior a "listo"
        cursor.execute('SELECT id FROM Pedidos WHERE estado = "en proceso" ORDER BY id DESC LIMIT 1')
        ultimo_pedido_id = cursor.fetchone()

        if ultimo_pedido_id:
            cursor.execute('UPDATE Pedidos SET estado = "listo" WHERE id = ?', (ultimo_pedido_id[0],))

        # Crea un nuevo pedido
        cursor.execute('INSERT INTO Pedidos (plato, estado) VALUES (?, ?)',
                       (receta_aleatoria[0], 'en proceso'))

        # Obtén los ingredientes y resta del inventario
        cursor.execute('SELECT ingrediente_id, cantidad_ingredientes FROM Ingredientes_recetas WHERE receta_id = ?',
                       (receta_aleatoria[0],))
        ingredientes = cursor.fetchall()

        for ingrediente_id, cantidad in ingredientes:
            cursor.execute('UPDATE Ingredientes SET cantidad = cantidad - ? WHERE id = ?',
                          (cantidad, ingrediente_id))

        # Un solo commit para todo
        conexion.commit()
        conexion.close()

        return jsonify({'mensaje': 'Pedido agregado con éxito', 'plato': receta_aleatoria[0]})

    except Exception as e:
        app.logger.error(f"Error en agregar_pedido: {str(e)}")
        return jsonify({"error": "Hubo un error en el servidor"}), 500

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)