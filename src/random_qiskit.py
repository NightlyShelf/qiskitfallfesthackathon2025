import numpy as np
from qiskit import QuantumCircuit
from qiskit_aer import AerSimulator

n = 12

qc = QuantumCircuit(n, n)

for i in range(n):
    qc.h(i)

qc.measure(np.arange(n), np.arange(n))

qc.draw('mpl')

simulator = AerSimulator()
job = simulator.run(qc, shots=1)
# plot_histogram(job.result().get_counts())
print(int(list(job.result().get_counts().keys())[0],2))