from qiskit import *

from qiskit.tools.visualization import plot_bloch_multivector

circuit = QuantumCircuit(1,1)
circuit.x(0)
simulator = Aer.get_backend('statevector_simulator')
result = execute(circuit, backend = simulator).result()
statevector = result.get_statevector()
print(statevector)
print("\n")

%matplotlib inline
circuit.draw(output='mpl')

plot_bloch_multivector(statevector)


