import numpy as np
from qiskit import QuantumCircuit
from qiskit_aer import AerSimulator

def quantum_generate_random(bit_count = 8):
    '''
    generated truly random number
    Args:
        - bit length of random number
    '''
    qc = QuantumCircuit(bit_count, bit_count)

    for i in range(bit_count):
        qc.h(i)

    qc.measure(np.arange(bit_count), np.arange(bit_count))

    qc.draw('mpl')

    simulator = AerSimulator()
    job = simulator.run(qc, shots=1)

    return list(job.result().get_counts().keys())[0]

a_choices = [0, np.pi / 2]
b_choices = [np.pi / 4, 3 * np.pi / 4]


def measuring_in_basis(qc, qubit, basis):
    if basis == 'Z':
        pass
    if basis == 'X':
        qc.h(qubit)

def val_in_basis(bit):
    if bit == '0':
        return 1
    else:
        return -1

def quantum_generate_random_device_independent(bit_count = 8, rounds = 1000):
    

    results = []

    for _ in range(rounds):
        simulator = AerSimulator()

        qc = QuantumCircuit(2,2)

        qc.h(0)
        qc.cx(0,1)

        a_basis = np.random.choice(['X', 'Z'])
        b_basis = np.random.choice(['X', 'Z'])

        measuring_in_basis(qc, 0, a_basis)
        measuring_in_basis(qc, 1, b_basis)

        qc.measure([0, 1], [0, 1])

        job = simulator.run(qc, shots=1)
        counts = job.result().get_counts()
        outcome = list(counts.keys())[0]

        results.append({
            'a_basis': a_basis,
            'b_basis': b_basis,
            'outcome': outcome
        })

    E = {}

    for a in ['X', 'Z']:
        for b in ['X', 'Z']:
            subset = [result for result in results if result['a_basis'] == a and result['b_basis'] == b]
            if len(subset) == 0:
                E[(a, b)] = 0
            else:
                corr = np.mean([val_in_basis(result['outcome'][0]) * val_in_basis(result['outcome'][1]) for result in subset])
                E[(a, b)] = corr

    S = E[('X','X')] + E[('X','Z')] + E[('Z','X')] - E[('Z','Z')]

    print('S', S)

    for _ in range(bit_count):

        print(results[np.random.randint(0, len(results))]['outcome'][0])