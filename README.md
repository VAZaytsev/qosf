# Problem Formulation
The task is to find two different *special* numbers in an integer-valued vector ![equation](https://latex.codecogs.com/gif.latex?%5Cvec%7Bn%7D), which is provided to the quantum computer by a user. The number is called *special* if in its binary representation all adjacent bits have different values. The positions ![equation](https://latex.codecogs.com/gif.latex?i) and ![equation](https://latex.codecogs.com/gif.latex?j) of these numbers are to be returned to the user as a state of the quantum computer with the wave function 

![equation](https://latex.codecogs.com/gif.latex?%5Cvert%5Cpsi%5Crangle%20%3D%20%5Cfrac%7B1%7D%7B%5Csqrt%7B2%7D%7D%5Cleft%28%5Cvert%7B%5Crm%20bin%7D%28i%29%5Crangle%20&plus;%20%5Cvert%7B%5Crm%20bin%7D%28i%29%5Crangle%5Cright%29)

where bin(a) stands for the binary representetion of the number ![equation](https://latex.codecogs.com/gif.latex?a).

It is assumed that 
1. the length of the vector is ![equation](https://latex.codecogs.com/gif.latex?2%5E%7BN_l%7D)
1. all vector components are different and can take values in the range from 0 to ![equation](https://latex.codecogs.com/gif.latex?2%5E%7BN_v%7D)

# Example
Let us consider the vector

![equation](https://latex.codecogs.com/gif.latex?%5Cvec%7Bn%7D%20%3D%20%5B1%2C2%2C7%2C5%5D)

corresponding to ![equation](https://latex.codecogs.com/gif.latex?N_l%20%3D%202) and ![equation](https://latex.codecogs.com/gif.latex?N_v%20%3D%203).

In the binary representation this vector is given by

![equation](https://latex.codecogs.com/gif.latex?%5Cvec%7Bn%7D_%7B%5Crm%20bin%7D%20%3D%20%5B001%2C%20010%2C%20111%2C%20101%5D)

The special numbers are on the 1 and 3 positions, therefore, the solution to the problem is given by the wave function 

![equation](https://latex.codecogs.com/gif.latex?%5Cvert%5Cpsi%5Crangle%20%3D%20%5Cfrac%7B1%7D%7B%5Csqrt%7B2%7D%7D%28%5Cvert%20%7B%5Crm%20bin%7D%281%29%20%5Crangle%20&plus;%20%5Cvert%20%7B%5Crm%20bin%7D%283%29%20%5Crangle%29%20%3D%20%5Cfrac%7B1%7D%7B%5Csqrt%7B2%7D%7D%28%5Cvert%2001%20%5Crangle%20&plus;%20%5Cvert%2011%20%5Crangle%29)

# Solution

The most direct way to solve the problem is to use Grover's algorithm.
With the use of this algorithm, one can increase the probabilities of the particular states detection and reduce the contributions of other states.
The constructed wave function, however, will differ from the desired solution but will provide a good approximation to it.
Another approach, which allows one to construct exactly the required wave function, is described in the next section.

The schematic representation of Grover's algorithm is following

![alt text](circuits/grover.png)

where

![equation](https://latex.codecogs.com/gif.latex?U_f%5Cvert%20x%5Crangle%20%3D%20%5Cleft%5Clbrace%20%5Cbegin%7Baligned%7D%20-%26%5Cvert%20x%20%5Crangle%2C%20%26%20%5Ctext%7Bfor%7D%5C%20special%5C%20x%20%5C%5C%20%26%20%5Cvert%20x%20%5Crangle%2C%20%26%20%5Ctext%7Botherwise%20%7D%20%5Cend%7Baligned%7D%5Cright.)

and

![equation](https://latex.codecogs.com/gif.latex?U_%7Bf_0%7D%5Cvert%20x%5Crangle%20%3D%20%5Cleft%5Clbrace%20%5Cbegin%7Baligned%7D%20%26%5Cvert%20x%20%5Crangle%2C%20%26%20%26%5Ctext%7Bfor%7D%5C%20x%20%3D%200%20%5C%5C%20-%26%20%5Cvert%20x%20%5Crangle%2C%20%26%20%26%5Ctext%7Botherwise%20%7D%20%5Cend%7Baligned%7D%5Cright.)

The power ![equation](https://latex.codecogs.com/gif.latex?r) is the largest integer satisfying the condition

![equation](https://latex.codecogs.com/gif.latex?r%20%5Cleqslant%20%5Cfrac%7B%5Cpi%7D%7B4%5Carcsin%282%5E%7B-N/2%7D%29%7D%20-%20%5Cfrac%7B1%7D%7B2%7D)

with ![equation](https://latex.codecogs.com/gif.latex?N) standing for the number of qubits.

In our case, Grover's algorithm is applied to ![equation](https://latex.codecogs.com/gif.latex?N_l) qubits enumerating the components of the vector ![equation](https://latex.codecogs.com/gif.latex?%5Cvec%7Bn%7D). To encode the values of the components additional ![equation](https://latex.codecogs.com/gif.latex?N_v) qubits are used. As an example, for ![equation](https://latex.codecogs.com/gif.latex?N_l%20%3D%202) the encoding circuit is following 

![alt text](circuits/U_n.png)

To construct circuits for ![equation](https://latex.codecogs.com/gif.latex?U_f) and ![equation](https://latex.codecogs.com/gif.latex?U_%7Bf_0%7D) one additional ancilla qubit is utilized. It is assumed that this auxiliary qubit is prepared in ![eqation](https://latex.codecogs.com/gif.latex?%5Cvert%201%5Crangle) state. The circuit for ![equation](https://latex.codecogs.com/gif.latex?U_f) is given by

![alt text](circuits/U_f.png)

And the circuit for ![equation](https://latex.codecogs.com/gif.latex?U_%7Bf_0%7D) is

![alt text](circuits/U_f_0.png)

The realization of this algorithm is presented in the files [grover.py](grover.py) and [grover.ipynb](grover.ipynb).

# Alternative solution

Instead of reflecting the amplitudes of the states in accordance with Grover's algorithm, one can try to transform the states which do not encode the positions of special numbers into the ones carrying such numbers. This can be performed by applying x-gates controlled by ancilla qubits. As an example, let us consider the circuit

![alt text](circuits/alternative_circ.png)

which solves the problem for the case of vectors with 4 entries. After the second ![equation](https://latex.codecogs.com/gif.latex?U_%7B%5Cvec%7Bn%7D%7D) operator the system takes one of the following states

![equation](https://latex.codecogs.com/gif.latex?%5Cvert%5Cpsi_%7B01%7D%5Crangle%20%3D%20%5Cfrac%7B1%7D%7B2%7D%5Cleft%28%20%5Cvert%2000%20%5Crangle%20%5Cvert%201%20%5Crangle_a%20&plus;%20%5Cvert%2001%20%5Crangle%20%5Cvert%201%20%5Crangle_a%20&plus;%20%5Cvert%2010%20%5Crangle%20%5Cvert%200%20%5Crangle_a%20&plus;%20%5Cvert%2011%20%5Crangle%20%5Cvert%200%20%5Crangle_a%20%5Cright%29)

![equation](https://latex.codecogs.com/gif.latex?%5Cvert%5Cpsi_%7B02%7D%5Crangle%20%3D%20%5Cfrac%7B1%7D%7B2%7D%5Cleft%28%20%5Cvert%2000%20%5Crangle%20%5Cvert%201%20%5Crangle_a%20&plus;%20%5Cvert%2001%20%5Crangle%20%5Cvert%200%20%5Crangle_a%20&plus;%20%5Cvert%2010%20%5Crangle%20%5Cvert%201%20%5Crangle_a%20&plus;%20%5Cvert%2011%20%5Crangle%20%5Cvert%200%20%5Crangle_a%20%5Cright%29)

![equation](https://latex.codecogs.com/gif.latex?%5Cvert%5Cpsi_%7B03%7D%5Crangle%20%3D%20%5Cfrac%7B1%7D%7B2%7D%5Cleft%28%20%5Cvert%2000%20%5Crangle%20%5Cvert%201%20%5Crangle_a%20&plus;%20%5Cvert%2001%20%5Crangle%20%5Cvert%200%20%5Crangle_a%20&plus;%20%5Cvert%2010%20%5Crangle%20%5Cvert%200%20%5Crangle_a%20&plus;%20%5Cvert%2011%20%5Crangle%20%5Cvert%201%20%5Crangle_a%20%5Cright%29)

![equation](https://latex.codecogs.com/gif.latex?%5Cvert%5Cpsi_%7B12%7D%5Crangle%20%3D%20%5Cfrac%7B1%7D%7B2%7D%5Cleft%28%20%5Cvert%2000%20%5Crangle%20%5Cvert%200%20%5Crangle_a%20&plus;%20%5Cvert%2001%20%5Crangle%20%5Cvert%201%20%5Crangle_a%20&plus;%20%5Cvert%2010%20%5Crangle%20%5Cvert%201%20%5Crangle_a%20&plus;%20%5Cvert%2011%20%5Crangle%20%5Cvert%200%20%5Crangle_a%20%5Cright%29)

![equation](https://latex.codecogs.com/gif.latex?%5Cvert%5Cpsi_%7B13%7D%5Crangle%20%3D%20%5Cfrac%7B1%7D%7B2%7D%5Cleft%28%20%5Cvert%2000%20%5Crangle%20%5Cvert%200%20%5Crangle_a%20&plus;%20%5Cvert%2001%20%5Crangle%20%5Cvert%201%20%5Crangle_a%20&plus;%20%5Cvert%2010%20%5Crangle%20%5Cvert%200%20%5Crangle_a%20&plus;%20%5Cvert%2011%20%5Crangle%20%5Cvert%201%20%5Crangle_a%20%5Cright%29)

![equation](https://latex.codecogs.com/gif.latex?%5Cvert%5Cpsi_%7B23%7D%5Crangle%20%3D%20%5Cfrac%7B1%7D%7B2%7D%5Cleft%28%20%5Cvert%2000%20%5Crangle%20%5Cvert%200%20%5Crangle_a%20&plus;%20%5Cvert%2001%20%5Crangle%20%5Cvert%200%20%5Crangle_a%20&plus;%20%5Cvert%2010%20%5Crangle%20%5Cvert%201%20%5Crangle_a%20&plus;%20%5Cvert%2011%20%5Crangle%20%5Cvert%201%20%5Crangle_a%20%5Cright%29)

where the lower indexes of the wave function stand for the positions related to the *special* states and, for the sake of simplicity, only the states of the first two qubits and the first ancilla qubit are presented. It is seen that after applying anticontrolled ![equation](https://latex.codecogs.com/gif.latex?X_1) gate, the wave functions with subscripts 01, 03, 12, and 23 will become the solution to the problem and will not be changed by the rest part of the circuit, which converts the wave functions with subscripts 02 and 13 into the solution.

Though similar circuits can be constructed for the vectors with a larger number of components, this approach seems to be unfeasible since the number of the required operations and auxiliary qubits grows exponentially with the size of the vector.

# Naive solution
The most naive approach to the solution of this problem is based on the postprocessing of the measurement data and corresponds to the circuit

![alt text](circuits/naive.png)

The solution of the problem will be encoded in the state of the first two qubits if the ancilla qubit will be detected in the state ![equation](https://latex.codecogs.com/gif.latex?%5Cvert%201%20%5Crangle). To decrease the number of gates and their complexity, one can utilize ![equation](https://latex.codecogs.com/gif.latex?N_v) auxiliary qubits. Such an approach being more appropriate for NISQ devices, will require a larger number of measurements. Moreover, the probability to detect the ancilla qubit (or qubits) in the desired state will rapidly decrease with the growth of the vector size.
