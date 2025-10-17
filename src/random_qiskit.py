import numpy as np
from qiskit import QuantumCircuit, QuantumRegister, ClassicalRegister
from qiskit_aer import AerSimulator



class RandomQuantumGenerator():
    def __init__(self, num_qubits):
        self.num_qubits = num_qubits
        self.qr = QuantumRegister(num_qubits)
        self.cr = ClassicalRegister(num_qubits)
        self.circuit = QuantumCircuit(self.qr, self.cr)
    def generate(self):
        # TODO try just self.circuit.h(self.qr)
        for i in range(self.num_qubits):
            self.circuit.h(i)
        self.circuit.measure_all()




#n = 12

#qc = QuantumCircuit(n, n)

#for i in range(n):
 #   qc.h(i)

#qc.measure(np.arange(n), np.arange(n))

#qc.draw('mpl')

#simulator = AerSimulator()
#job = simulator.run(qc, shots=1)
## plot_histogram(job.result().get_counts())
#print(int(list(job.result().get_counts().keys())[0],2))