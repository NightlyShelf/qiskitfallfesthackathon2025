from typing import Any

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
        if not self._certify_randomness(counts):
            raise Exception('Cant certify randomness. CORRPUTED!!!')
        # Get the single measurement result (bit string)
        bitstring = list(counts.keys())[0]
        return bitstring  # Returns string like '0101' or '1110'

    def generate_int(self):
        """Returns the random bits as an integer"""
        return int(self.generate(), 2)

    def _certify_randomness(self, counts: Any) -> bool:
        # TODO
        # https://quantum.cloud.ibm.com/docs/en/tutorials/chsh-inequality
        return True
