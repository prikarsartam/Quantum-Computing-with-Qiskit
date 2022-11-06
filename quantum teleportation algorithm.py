from qiskit import *

# we are building a 2 qubit quantum register
qr = QuantumRegister(2)

# a classical register with 2 bits
cr = ClassicalRegister(2)

circuit = QuantumCircuit(qr, cr)

%matplotlib inline
circuit.draw(output='mpl')


#build up gates into the system
# build entanglement between them

circuit.h(qr[0])
circuit.draw(output='mpl')

circuit.cx(qr[0], qr[1])
circuit.draw(output='mpl')

circuit.measure(qr,cr)
circuit.draw(output='mpl')

#Aer simulates quantum circuits [unitary evolutions] on Local Computers
simulator = Aer.get_backend('qasm_simulator')

result = execute(circuit, backend=simulator).result()


from qistis.tools.visualization import plot_histogram

plot_histogram(result.get_counts(circuit))