import math
import numpy as np
import itertools

from qiskit import *


# Number of qubits for storing the values of the integer vector
N_v = 4

# Determine *special* numbers 1010... 0101...
bn_a = "".join(["1" if i%2 == 1 else "0" for i in range(N_v)])
a = int( bn_a, 2)

bn_b = "".join(["0" if i%2 == 1 else "1" for i in range(N_v)])
b = int( bn_b, 2)
print("Special numbers are", a, "(",bn_a,") and", b,"(",bn_b,")")


# Length of the vector
N_l = 4
Nvec_len = 2**N_l 


# Number of steps in Grover's algorithm
r = math.floor( 0.25*math.pi / math.asin(1/math.sqrt(2**N_l)) - 0.5 )
print( "r = ", r )
#exit()




# Generation of an arbitrary integer-valued vector
vec = [-1]*Nvec_len

# Place *special* numbers on arbitrary positions
vec[ np.random.randint(0, Nvec_len) ] = a

while b not in vec:
  pos = np.random.randint(0, Nvec_len)

  if vec[pos] == a:
    continue
  vec[pos] = b

# Fill in randomly the rest components of the vector
for i in range(Nvec_len):
  if vec[i] != -1:
    continue

  while True:
    val = np.random.randint(0, 2**N_v)
    if val in vec:
      continue
    vec[i] = val
    break


# Generate the initial state of the system
Nq_tot = N_l + N_v + 1
qc_in = QuantumCircuit(Nq_tot, Nq_tot)

qc_in.h(range(N_l))


# The quantum circuit encoding the vector of integers (U_n)
qc_U_n = QuantumCircuit(Nq_tot, Nq_tot)

print("Integer-valued vector")
print(f'{"position": >10}', f'{"value": >9}')
for i,x in enumerate(vec):
  i_bn = bin(i)[2:].zfill(N_l)
  x_bn = bin(x)[2:].zfill(N_v)

  txt = ""
  if x_bn == bn_a or x_bn == bn_b:
    txt = "!!!"
  print(f'{i: >2}',"(",i_bn,")", f'{x: >2}', "(",x_bn,")", txt)

  for ia, a in enumerate(i_bn):
    if a == "0":
      qc_U_n.x(N_l - 1 - ia)

  for n,b in enumerate(x_bn):
    if b == "1":
      qc_U_n.mct(list(range(N_l)), N_l + N_v - 1 - n)

  for ia, a in enumerate(i_bn):
    if a == "0":
      qc_U_n.x(N_l - 1 - ia)

#print(qc_U_n)
#exit()


# Construct the circuit for U_f
qc_mark = QuantumCircuit(Nq_tot, Nq_tot)

qc_a = QuantumCircuit(Nq_tot, Nq_tot)
qc_b = QuantumCircuit(Nq_tot, Nq_tot)

for ii in range(N_v):
  if ii%2 == 0:
    qc_a.x(N_l + ii)
  else:
    qc_b.x(N_l + ii)

qc_mark = qc_mark.compose(qc_a)
qc_mark.mct( list(range(N_l,N_l+N_v)), N_l + N_v)
qc_mark = qc_mark.compose(qc_a)

qc_mark = qc_mark.compose(qc_b)
qc_mark.mct( list(range(N_l,N_l+N_v)), N_l + N_v)
qc_mark = qc_mark.compose(qc_b)

qc_Uf = QuantumCircuit(Nq_tot, Nq_tot)
qc_Uf = qc_Uf.compose(qc_U_n)
qc_Uf = qc_Uf.compose(qc_mark)
qc_Uf.z(N_l + N_v)
qc_Uf = qc_Uf.compose(qc_mark)
qc_Uf = qc_Uf.compose(qc_U_n)


# Construct the circuit for V = H U_f_0 H
qc_V = QuantumCircuit(Nq_tot, Nq_tot)
qc_V.h(range(N_l))
qc_V.x(range(N_l))
qc_V.mct( list(range(N_l)), N_l + N_v)
qc_V.z(N_l + N_v)
qc_V.mct( list(range(N_l)), N_l + N_v)
qc_V.x(range(N_l))
qc_V.h(range(N_l))
#print(qc_V)
#exit()


# Measurement
qc_meas = QuantumCircuit(Nq_tot, Nq_tot)
qc_meas.measure( range(Nq_tot), range(Nq_tot) )


# Construct the whole circuit
qc_tot = QuantumCircuit(Nq_tot, Nq_tot)

qc_tot = qc_tot.compose(qc_in)

for ir in range(r):
  qc_tot = qc_tot.compose(qc_Uf)
  qc_tot = qc_tot.compose(qc_V)

qc_tot = qc_tot.compose(qc_meas)


# Launch on simulator with 1000 shots
simulator = Aer.get_backend('qasm_simulator')
res = execute(qc_tot, 
              backend = simulator).result()
dct = res.get_counts()


# Print the results which are larger than the statistical error
print("The measured state is")
for k in dct.keys():
  if dct[k]*1.e-3 < 2 / math.sqrt(1000):
    continue
  print(int(k[1+N_v:],2), k[1+N_v:], dct[k])
