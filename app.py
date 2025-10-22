from flask import Flask, Response
from collections import OrderedDict
import json

app = Flask(__name__)

def calcular_factorial(n):
    if n < 0:
        return None
    factorial = 1
    for i in range(1, n + 1):
        factorial *= i
    return factorial

@app.route('/')
def home():
    data = OrderedDict([
        ("mensaje", "Bienvenido al microservicio de cálculo de factorial."),
        ("instrucciones", "Para usarlo, accede a la ruta /factorial/<numero> con un número entero."),
        ("ejemplo", "http://127.0.0.1:8000/factorial/5")
    ])
    return Response(json.dumps(data, ensure_ascii=False, indent=2),
                    mimetype="application/json")

@app.route('/factorial/<int:numero>', methods=['GET'])
def factorial_route(numero):
    resultado = calcular_factorial(numero)
    if resultado is None:
        return Response(
            json.dumps({"error": "El número debe ser mayor o igual a cero"}, ensure_ascii=False),
            status=400,
            mimetype="application/json"
        )

    etiqueta = "par" if numero % 2 == 0 else "impar"

    data = OrderedDict([
        ("numero_recibido", numero),
        ("factorial", resultado),
        ("etiqueta", etiqueta)
    ])
    return Response(json.dumps(data, ensure_ascii=False, indent=2),
                    mimetype="application/json")

if __name__ == '__main__':
    app.run(debug=True, port=8000)
