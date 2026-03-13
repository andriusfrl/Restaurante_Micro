from flask import Flask, jsonify, request
import random

app = Flask(__name__)

@app.route('/')
def index():
    return jsonify({"status": "ok"})

@app.route('/v1/marketplace', methods=['GET'])
def marketplace():
    ingrediente = request.args.get('ingredient')
    if not ingrediente:
        return jsonify({"error": "Falta el parámetro ingredient"}), 400

    cantidad = random.randint(1, 10)
    return jsonify({"data": {ingrediente: cantidad}})