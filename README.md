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
With the use of this algorithm one can increase the probabilities of the particular states detection and reduce the contributions of other states.
The constructed wave function, however, will differ from the desired solution but will provide a good approximation to it.
Another approach, which allows one to construct exactly the required wave function, is described in the next section.

The scematic representation of the Grover algorithm is following

![alt text](https://github.com/VAZaytsev/qosf/blob/main/grover-1.png)

where

![equation](https://latex.codecogs.com/gif.latex?U_f%5Cvert%20x%5Crangle%20%3D%20%5Cleft%5Clbrace%20%5Cbegin%7Baligned%7D%20-%26%5Cvert%20x%20%5Crangle%2C%20%26%20%5Ctext%7Bfor%7D%5C%20special%5C%20x%20%5C%5C%20%26%20%5Cvert%20x%20%5Crangle%2C%20%26%20%5Ctext%7Botherwise%20%7D%20%5Cend%7Baligned%7D%5Cright.)

and

![equation](https://latex.codecogs.com/gif.latex?U_%7Bf_0%7D%5Cvert%20x%5Crangle%20%3D%20%5Cleft%5Clbrace%20%5Cbegin%7Baligned%7D%20%26%5Cvert%20x%20%5Crangle%2C%20%26%20%26%5Ctext%7Bfor%7D%5C%20x%20%3D%200%20%5C%5C%20-%26%20%5Cvert%20x%20%5Crangle%2C%20%26%20%26%5Ctext%7Botherwise%20%7D%20%5Cend%7Baligned%7D%5Cright.)

The power ![equation](https://latex.codecogs.com/gif.latex?r) is the largest integer satisfying the condition

![equation](https://latex.codecogs.com/gif.latex?r%20%5Cleqslant%20%5Cfrac%7B%5Cpi%7D%7B4%5Carcsin%282%5E%7B-N/2%7D%29%7D%20-%20%5Cfrac%7B1%7D%7B2%7D)

with ![equation](https://latex.codecogs.com/gif.latex?N) standing for the number of qubits.

In our case, Grover's algorithm is applied to ![equation](https://latex.codecogs.com/gif.latex?N_l) qubits enumerating the components of the vector ![equation](https://latex.codecogs.com/gif.latex?%5Cvec%7Bn%7D). To encode the values of the components additional ![equation](https://latex.codecogs.com/gif.latex?N_v) qubits are used. As an example, for ![equation](https://latex.codecogs.com/gif.latex?N_l%20%3D%202) the encoding circuit is following 

![alt text](https://github.com/VAZaytsev/qosf/blob/main/U_n.png)

To construct circuits for ![equation](https://latex.codecogs.com/gif.latex?U_f) and ![equation](https://latex.codecogs.com/gif.latex?U_%7Bf_0%7D) one additional ancilla qubit is utilized. It is assumed that this auxilarly qubit is prepared in ![eqation](https://latex.codecogs.com/gif.latex?%5Cvert%201%5Crangle) state. The circuit for ![equation](https://latex.codecogs.com/gif.latex?U_f) is given by

![alt text](https://github.com/VAZaytsev/qosf/blob/main/U_f.png)

And the circuit for ![equation](https://latex.codecogs.com/gif.latex?U_%7Bf_0%7D) is

![alt text](https://github.com/VAZaytsev/qosf/blob/main/U_f_0.png)
