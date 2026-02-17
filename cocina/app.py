from flask import Flask, jsonify
import psycopg2
import os
import random

DATABASE_URL = os.getenv("DATABASE_URL")

app = Flask(__name__)

@app.route('/health')
def health():
    return {"status": "ok"}

@app.route('/recetas', methods=['GET'])
def obtener_recetas():
    conexion = None
    try:
        conexion = psycopg2.connect(DATABASE_URL)
        cursor = conexion.cursor()
        cursor.execute('SELECT * FROM Recetas')
        recetas = cursor.fetchall()
        return jsonify({"obtener_recetas": recetas})
    except Exception as e:
        app.logger.error(f"Error en obtener_recetas: {str(e)}")
        return jsonify({"error": "Hubo un error en el servidor"}), 500
    finally:
        if conexion:
            conexion.close()

@app.route('/agregar_pedido', methods=['GET'])
def agregar_pedido():
    conexion = None
    try:
        conexion = psycopg2.connect(DATABASE_URL)
        cursor = conexion.cursor()

        cursor.execute('SELECT * FROM Recetas')
        recetas = cursor.fetchall()

        receta_aleatoria = random.choice(recetas)

        cursor.execute("SELECT id FROM Pedidos WHERE estado = 'en proceso' ORDER BY id DESC LIMIT 1")
        ultimo_pedido_id = cursor.fetchone()

        if ultimo_pedido_id:
            cursor.execute('UPDATE Pedidos SET estado = %s WHERE id = %s', ('listo', ultimo_pedido_id[0]))

        cursor.execute('INSERT INTO Pedidos (plato, estado) VALUES (%s, %s)',
                       (receta_aleatoria[0], 'en proceso'))

        cursor.execute('SELECT ingrediente_id, cantidad_ingredientes FROM Ingredientes_recetas WHERE receta_id = %s',
                       (receta_aleatoria[0],))
        ingredientes = cursor.fetchall()

        for ingrediente_id, cantidad in ingredientes:
            cursor.execute('UPDATE Ingredientes SET cantidad = cantidad - %s WHERE id = %s',
                          (cantidad, ingrediente_id))

        conexion.commit()

        return jsonify({'mensaje': 'Pedido agregado con éxito', 'plato': receta_aleatoria[0]})

    except Exception as e:
        app.logger.error(f"Error en agregar_pedido: {str(e)}")
        return jsonify({"error": "Hubo un error en el servidor"}), 500
    finally:
        if conexion:
            conexion.close()

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)