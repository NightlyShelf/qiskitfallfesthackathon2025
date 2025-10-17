import numpy as np
from qiskit import QuantumCircuit
from qiskit_aer import AerSimulator

def quantum_generate_random(bit_count = 8):
    qc = QuantumCircuit(bit_count, bit_count)

    for i in range(bit_count):
        qc.h(i)

    qc.measure(np.arange(bit_count), np.arange(bit_count))

    qc.draw('mpl')

    simulator = AerSimulator()
    job = simulator.run(qc, shots=1)

    return list(job.result().get_counts().keys())[0]
