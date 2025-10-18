import numpy as np
from qiskit import QuantumCircuit, QuantumRegister, ClassicalRegister
from qiskit_aer import AerSimulator


class RandomQuantumGenerator:
    def __init__(self, num_qubits):
        self.simulator = AerSimulator()
        self.num_qubits = num_qubits
        self.qr = QuantumRegister(num_qubits)
        self.cr = ClassicalRegister(num_qubits)
        self.circuit = QuantumCircuit(self.qr, self.cr)
    def generate(self):
        self.circuit.h(self.qr)
        self.circuit.measure(self.qr, self.cr)
        compiled_circuit = self.simulator.run(self.circuit, shots=1)
        result = compiled_circuit.result()
        counts = result.get_counts(self.circuit)
        bitstring = list(counts.keys())[0]
        return bitstring

    def generate_int(self):
        """Returns the random bits as an integer"""
        return int(self.generate(), 2)

    def generate_list(self):
        """Returns the random bits as a list of integers [0, 1, 0, 1]"""
        return [int(bit) for bit in self.generate()]


rqg = RandomQuantumGenerator(4)
print(rqg.generate_int())
