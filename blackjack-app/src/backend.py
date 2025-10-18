from flask import Flask, jsonify
from random_qiskit import RandomQuantumGenerator

app = Flask(__name__)
generator  = RandomQuantumGenerator(32)
@app.route("/seed")

def get_seed():
    seed_value = generator.generate_int()
    return jsonify({"seed":seed_value})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port= 5000)