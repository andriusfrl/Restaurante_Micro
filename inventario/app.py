from flask import Flask, request, jsonify
import sqlite3
import os
import requests
from datetime import datetime

database_path = os.getenv("DATABASE_PATH", "/app/data/restaurant.db")


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
        return jsonify({"error": "Hubo un error en el servidor"}), 500  # Respuesta de error 500
    
@app.route('/comprar_tomato', methods=['GET'])
def actualizar_tomatos():
    # URL del servicio web
    url = "https://utadeoapi-6dae6e29b5b0.herokuapp.com/api/v1/software-architecture/market-place?ingredient=tomato"

    # Realiza una solicitud GET al servicio web
    response = requests.get(url)

    # Obtiene la fecha y hora actual
    fecha_compra = datetime.now()

    # Comprueba si la solicitud fue exitosa
    if response.status_code == 200:
        # Convierte la respuesta JSON en un diccionario
        data = response.json()

        # Accede a los valores que deseas extraer
        tomato_value = data['data']['tomato']

        # Accede a los valores que deseas extraer
        data = data['data']

        # Conecta a la base de datos SQLite
        conexion = sqlite3.connect(database_path)
        cursor = conexion.cursor()

        # Inserta la compra en la tabla 'compras'
        cursor.execute("INSERT INTO compras (ingrediente_id, cantidad_compras, fecha_compra) VALUES (?, ?, ?)",
                       ('1', tomato_value, fecha_compra))

        # Inserta los datos en la base de datos TABLA INGREDIENTES
        cursor.execute("UPDATE Ingredientes SET cantidad = cantidad + ? WHERE nombre = ?", (tomato_value, 'Tomato'))

        # Realiza la confirmación de los cambios en la base de datos y cierra la conexión
        conexion.commit()
        conexion.close()

        return jsonify({'mensaje': 'Datos agregados a la base de datos con éxito.', 'cantidad': tomato_value}), 200
    else:
        return jsonify({'error': 'Error al hacer la solicitud al servicio web'}), 500

@app.route('/comprar_lemon', methods=['GET'])
def actualizar_lemon():
    # URL del servicio web
    url = "https://utadeoapi-6dae6e29b5b0.herokuapp.com/api/v1/software-architecture/market-place?ingredient=lemon"

    # Realiza una solicitud GET al servicio web
    response = requests.get(url)

    # Obtiene la fecha y hora actual
    fecha_compra = datetime.now()

    # Comprueba si la solicitud fue exitosa
    if response.status_code == 200:
        # Convierte la respuesta JSON en un diccionario
        data = response.json()

        # Accede a los valores que deseas extraer
        lemon_value = data['data']['lemon']

        # Accede a los valores que deseas extraer
        data = data['data']

        # Conecta a la base de datos SQLite
        conexion = sqlite3.connect(database_path)
        cursor = conexion.cursor()

        # Inserta la compra en la tabla 'compras'
        cursor.execute("INSERT INTO compras (ingrediente_id, cantidad_compras, fecha_compra) VALUES (?, ?, ?)",
                       ('3', lemon_value, fecha_compra))

        # Inserta los datos en la base de datos TABLA INGREDIENTES
        cursor.execute("UPDATE Ingredientes SET cantidad = cantidad + ? WHERE nombre = ?", (lemon_value, 'Lemon'))

        # Realiza la confirmación de los cambios en la base de datos y cierra la conexión
        conexion.commit()
        conexion.close()

        return jsonify({'mensaje': 'Datos agregados a la base de datos con éxito.', 'cantidad': lemon_value}), 200
    else:
        return jsonify({'error': 'Error al hacer la solicitud al servicio web'}), 500

@app.route('/comprar_potato', methods=['GET'])
def actualizar_potatos():
    # URL del servicio web
    url = "https://utadeoapi-6dae6e29b5b0.herokuapp.com/api/v1/software-architecture/market-place?ingredient=potato"

    # Realiza una solicitud GET al servicio web
    response = requests.get(url)

    # Obtiene la fecha y hora actual
    fecha_compra = datetime.now()

    # Comprueba si la solicitud fue exitosa
    if response.status_code == 200:
        # Convierte la respuesta JSON en un diccionario
        data = response.json()

        # Accede a los valores que deseas extraer
        potato_value = data['data']['potato']

        # Accede a los valores que deseas extraer
        data = data['data']

        # Conecta a la base de datos SQLite
        conexion = sqlite3.connect(database_path)
        cursor = conexion.cursor()

        # Inserta la compra en la tabla 'compras'
        cursor.execute("INSERT INTO compras (ingrediente_id, cantidad_compras, fecha_compra) VALUES (?, ?, ?)",
                       ('3', potato_value, fecha_compra))

        # Inserta los datos en la base de datos TABLA INGREDIENTES
        cursor.execute("UPDATE Ingredientes SET cantidad = cantidad + ? WHERE nombre = ?", (potato_value, 'Potato'))

        # Realiza la confirmación de los cambios en la base de datos y cierra la conexión
        conexion.commit()
        conexion.close()

        return jsonify({'mensaje': 'Datos agregados a la base de datos con éxito.', 'cantidad': potato_value}), 200
    else:
        return jsonify({'error': 'Error al hacer la solicitud al servicio web'}), 500
    
@app.route('/comprar_rice', methods=['GET'])
def actualizar_rice():
    # URL del servicio web
    url = "https://utadeoapi-6dae6e29b5b0.herokuapp.com/api/v1/software-architecture/market-place?ingredient=rice"

    # Realiza una solicitud GET al servicio web
    response = requests.get(url)

    # Obtiene la fecha y hora actual
    fecha_compra = datetime.now()

    # Comprueba si la solicitud fue exitosa
    if response.status_code == 200:
        # Convierte la respuesta JSON en un diccionario
        data = response.json()

        # Accede a los valores que deseas extraer
        rice_value = data['data']['rice']

        # Accede a los valores que deseas extraer
        data = data['data']

        # Conecta a la base de datos SQLite
        conexion = sqlite3.connect(database_path)
        cursor = conexion.cursor()

        # Inserta la compra en la tabla 'compras'
        cursor.execute("INSERT INTO compras (ingrediente_id, cantidad_compras, fecha_compra) VALUES (?, ?, ?)",
                       ('4', rice_value, fecha_compra))

        # Inserta los datos en la base de datos TABLA INGREDIENTES
        cursor.execute("UPDATE Ingredientes SET cantidad = cantidad + ? WHERE nombre = ?", (rice_value, 'Rice'))

        # Realiza la confirmación de los cambios en la base de datos y cierra la conexión
        conexion.commit()
        conexion.close()

        return jsonify({'mensaje': 'Datos agregados a la base de datos con éxito.', 'cantidad': rice_value}), 200
    else:
        return jsonify({'error': 'Error al hacer la solicitud al servicio web'}), 500
    
@app.route('/comprar_ketchup', methods=['GET'])
def actualizar_ketchup():
    # URL del servicio web
    url = "https://utadeoapi-6dae6e29b5b0.herokuapp.com/api/v1/software-architecture/market-place?ingredient=ketchup"

    # Realiza una solicitud GET al servicio web
    response = requests.get(url)

    # Obtiene la fecha y hora actual
    fecha_compra = datetime.now()

    # Comprueba si la solicitud fue exitosa
    if response.status_code == 200:
        # Convierte la respuesta JSON en un diccionario
        data = response.json()

        # Accede a los valores que deseas extraer
        ketchup_value = data['data']['ketchup']

        # Accede a los valores que deseas extraer
        data = data['data']

        # Conecta a la base de datos SQLite
        conexion = sqlite3.connect(database_path)
        cursor = conexion.cursor()

        # Inserta la compra en la tabla 'compras'
        cursor.execute("INSERT INTO compras (ingrediente_id, cantidad_compras, fecha_compra) VALUES (?, ?, ?)",
                       ('5', ketchup_value, fecha_compra))

        # Inserta los datos en la base de datos TABLA INGREDIENTES
        cursor.execute("UPDATE Ingredientes SET cantidad = cantidad + ? WHERE nombre = ?", (ketchup_value, 'Ketchup'))

        # Realiza la confirmación de los cambios en la base de datos y cierra la conexión
        conexion.commit()
        conexion.close()

        return jsonify({'mensaje': 'Datos agregados a la base de datos con éxito.', 'cantidad': ketchup_value}), 200
    else:
        return jsonify({'error': 'Error al hacer la solicitud al servicio web'}), 500

@app.route('/comprar_lettuce', methods=['GET'])
def actualizar_():
    # URL del servicio web
    url = "https://utadeoapi-6dae6e29b5b0.herokuapp.com/api/v1/software-architecture/market-place?ingredient=lettuce"

    # Realiza una solicitud GET al servicio web
    response = requests.get(url)

    # Obtiene la fecha y hora actual
    fecha_compra = datetime.now()

    # Comprueba si la solicitud fue exitosa
    if response.status_code == 200:
        # Convierte la respuesta JSON en un diccionario
        data = response.json()

        # Accede a los valores que deseas extraer
        lettuce_value = data['data']['lettuce']

        # Accede a los valores que deseas extraer
        data = data['data']

        # Conecta a la base de datos SQLite
        conexion = sqlite3.connect(database_path)
        cursor = conexion.cursor()

        # Inserta la compra en la tabla 'compras'
        cursor.execute("INSERT INTO compras (ingrediente_id, cantidad_compras, fecha_compra) VALUES (?, ?, ?)",
                       ('6', lettuce_value, fecha_compra))

        # Inserta los datos en la base de datos TABLA INGREDIENTES
        cursor.execute("UPDATE Ingredientes SET cantidad = cantidad + ? WHERE nombre = ?", (lettuce_value, 'Lettuce'))

        # Realiza la confirmación de los cambios en la base de datos y cierra la conexión
        conexion.commit()
        conexion.close()

        return jsonify({'mensaje': 'Datos agregados a la base de datos con éxito.', 'cantidad': lettuce_value}), 200
    else:
        return jsonify({'error': 'Error al hacer la solicitud al servicio web'}), 500
    
@app.route('/comprar_onion', methods=['GET'])
def actualizar_onion():
    # URL del servicio web
    url = "https://utadeoapi-6dae6e29b5b0.herokuapp.com/api/v1/software-architecture/market-place?ingredient=onion"

    # Realiza una solicitud GET al servicio web
    response = requests.get(url)

    # Obtiene la fecha y hora actual
    fecha_compra = datetime.now()

    # Comprueba si la solicitud fue exitosa
    if response.status_code == 200:
        # Convierte la respuesta JSON en un diccionario
        data = response.json()

        # Accede a los valores que deseas extraer
        onion_value = data['data']['onion']

        # Accede a los valores que deseas extraer
        data = data['data']

        # Conecta a la base de datos SQLite
        conexion = sqlite3.connect(database_path)
        cursor = conexion.cursor()

        # Inserta la compra en la tabla 'compras'
        cursor.execute("INSERT INTO compras (ingrediente_id, cantidad_compras, fecha_compra) VALUES (?, ?, ?)",
                       ('7', onion_value, fecha_compra))

        # Inserta los datos en la base de datos TABLA INGREDIENTES
        cursor.execute("UPDATE Ingredientes SET cantidad = cantidad + ? WHERE nombre = ?", (onion_value, 'Onion'))

        # Realiza la confirmación de los cambios en la base de datos y cierra la conexión
        conexion.commit()
        conexion.close()

        return jsonify({'mensaje': 'Datos agregados a la base de datos con éxito.', 'cantidad': onion_value}), 200
    else:
        return jsonify({'error': 'Error al hacer la solicitud al servicio web'}), 500
    
@app.route('/comprar_cheese', methods=['GET'])
def actualizar_cheese():
    # URL del servicio web
    url = "https://utadeoapi-6dae6e29b5b0.herokuapp.com/api/v1/software-architecture/market-place?ingredient=cheese"

    # Realiza una solicitud GET al servicio web
    response = requests.get(url)

    # Obtiene la fecha y hora actual
    fecha_compra = datetime.now()

    # Comprueba si la solicitud fue exitosa
    if response.status_code == 200:
        # Convierte la respuesta JSON en un diccionario
        data = response.json()

        # Accede a los valores que deseas extraer
        cheese_value = data['data']['cheese']

        # Accede a los valores que deseas extraer
        data = data['data']

        # Conecta a la base de datos SQLite
        conexion = sqlite3.connect(database_path)
        cursor = conexion.cursor()

        # Inserta la compra en la tabla 'compras'
        cursor.execute("INSERT INTO compras (ingrediente_id, cantidad_compras, fecha_compra) VALUES (?, ?, ?)",
                       ('8', cheese_value, fecha_compra))

        # Inserta los datos en la base de datos TABLA INGREDIENTES
        cursor.execute("UPDATE Ingredientes SET cantidad = cantidad + ? WHERE nombre = ?", (cheese_value, 'Cheese'))

        # Realiza la confirmación de los cambios en la base de datos y cierra la conexión
        conexion.commit()
        conexion.close()

        return jsonify({'mensaje': 'Datos agregados a la base de datos con éxito.', 'cantidad': cheese_value}), 200
    else:
        return jsonify({'error': 'Error al hacer la solicitud al servicio web'}), 500
    
@app.route('/comprar_meat', methods=['GET'])
def actualizar_meat():
    # URL del servicio web
    url = "https://utadeoapi-6dae6e29b5b0.herokuapp.com/api/v1/software-architecture/market-place?ingredient=meat"

    # Realiza una solicitud GET al servicio web
    response = requests.get(url)

    # Obtiene la fecha y hora actual
    fecha_compra = datetime.now()

    # Comprueba si la solicitud fue exitosa
    if response.status_code == 200:
        # Convierte la respuesta JSON en un diccionario
        data = response.json()

        # Accede a los valores que deseas extraer
        meat_value = data['data']['meat']

        # Accede a los valores que deseas extraer
        data = data['data']

        # Conecta a la base de datos SQLite
        conexion = sqlite3.connect(database_path)
        cursor = conexion.cursor()

        # Inserta la compra en la tabla 'compras'
        cursor.execute("INSERT INTO compras (ingrediente_id, cantidad_compras, fecha_compra) VALUES (?, ?, ?)",
                       ('9', meat_value, fecha_compra))

        # Inserta los datos en la base de datos TABLA INGREDIENTES
        cursor.execute("UPDATE Ingredientes SET cantidad = cantidad + ? WHERE nombre = ?", (meat_value, 'Meat'))

        # Realiza la confirmación de los cambios en la base de datos y cierra la conexión
        conexion.commit()
        conexion.close()

        return jsonify({'mensaje': 'Datos agregados a la base de datos con éxito.', 'cantidad': meat_value}), 200
    else:
        return jsonify({'error': 'Error al hacer la solicitud al servicio web'}), 500
    
@app.route('/comprar_chicken', methods=['GET'])
def actualizar_chicken():
    # URL del servicio web
    url = "https://utadeoapi-6dae6e29b5b0.herokuapp.com/api/v1/software-architecture/market-place?ingredient=chicken"

    # Realiza una solicitud GET al servicio web
    response = requests.get(url)

    # Obtiene la fecha y hora actual
    fecha_compra = datetime.now()

    # Comprueba si la solicitud fue exitosa
    if response.status_code == 200:
        # Convierte la respuesta JSON en un diccionario
        data = response.json()

        # Accede a los valores que deseas extraer
        chicken_value = data['data']['chicken']

        # Accede a los valores que deseas extraer
        data = data['data']

        # Conecta a la base de datos SQLite
        conexion = sqlite3.connect(database_path)
        cursor = conexion.cursor()

        # Inserta la compra en la tabla 'compras'
        cursor.execute("INSERT INTO compras (ingrediente_id, cantidad_compras, fecha_compra) VALUES (?, ?, ?)",
                       ('10', chicken_value, fecha_compra))

        # Inserta los datos en la base de datos TABLA INGREDIENTES
        cursor.execute("UPDATE Ingredientes SET cantidad = cantidad + ? WHERE nombre = ?", (chicken_value, 'Chicken'))

        # Realiza la confirmación de los cambios en la base de datos y cierra la conexión
        conexion.commit()
        conexion.close()

        return jsonify({'mensaje': 'Datos agregados a la base de datos con éxito.', 'cantidad': chicken_value}), 200
    else:
        return jsonify({'error': 'Error al hacer la solicitud al servicio web'}), 500
    
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)