# Problem Formulation
The task is to find two different *special* numbers in an integer-valued vector ![equation](https://latex.codecogs.com/gif.latex?%5Cvec%7Bn%7D), which is provided to the quantum computer by a user. The number is called *special* if in its binary representation all adjacent bits have different values. The positions ![equation](https://latex.codecogs.com/gif.latex?i) and ![equation](https://latex.codecogs.com/gif.latex?j) of these numbers are to be returned to the user as a state of the quantum computer with the wave function 

![equation](https://latex.codecogs.com/gif.latex?%5Cvert%5Cpsi%5Crangle%20%3D%20%5Cfrac%7B1%7D%7B%5Csqrt%7B2%7D%7D%5Cleft%28%5Cvert%7B%5Crm%20bin%7D%28i%29%5Crangle%20&plus;%20%5Cvert%7B%5Crm%20bin%7D%28i%29%5Crangle%5Cright%29)

where bin(a) stands for the binary representetion of the number ![equation](https://latex.codecogs.com/gif.latex?a).

It is assumed that 
1. the length of the vector is ![equation](https://latex.codecogs.com/gif.latex?2%5E%7BN_l%7D)
1. all vector components are different and can take values in the range from 0 to ![equation](https://latex.codecogs.com/gif.latex?2%5E%7BN_v%7D)

The number is called *special* if its binary representation is either 010101... or 101010... 

# Example
Let us consider the vector
![equation](https://latex.codecogs.com/gif.latex?%5Cvec%7Bn%7D%20%3D%20%5B1%2C2%2C7%2C5%5D)
corresponding to ![equation](https://latex.codecogs.com/gif.latex?N_l%20%3D%202) and ![equation](https://latex.codecogs.com/gif.latex?N_v%20%3D%203).

In the binary representation this vector is given by
![equation](https://latex.codecogs.com/gif.latex?%5Cvec%7Bn%7D_%7B%5Crm%20bin%7D%20%3D%20%5B001%2C%20010%2C%20111%2C%20101%5D)

The special numbers are on the 1 and 3 positions, therefore, the solution to the problem is given by the wave function 

![equation](https://latex.codecogs.com/gif.latex?%5Cvert%5Cpsi%5Crangle%20%3D%20%5Cfrac%7B1%7D%7B%5Csqrt%7B2%7D%7D%28%5Cvert%20%7B%5Crm%20bin%7D%281%29%20%5Crangle%20&plus;%20%5Cvert%20%7B%5Crm%20bin%7D%283%29%20%5Crangle%29%20%3D%20%5Cfrac%7B1%7D%7B%5Csqrt%7B2%7D%7D%28%5Cvert%2001%20%5Crangle%20&plus;%20%5Cvert%2011%20%5Crangle%29)

# Solution No1
