# Problem Formulation
The task is to find two different *special* numbers inside an integer-valued vector ![equation](https://latex.codecogs.com/gif.latex?%5Cvec%7Bn%7D), which is provided to the quantum computer by a user. The positions ![equation](https://latex.codecogs.com/gif.latex?i) and ![equation](https://latex.codecogs.com/gif.latex?j) of these numbers are to be returned to the user as a state of the quantum computer with the wave function 

![equation](https://latex.codecogs.com/gif.latex?%5Cvert%5Cpsi%5Crangle%20%3D%20%5Cfrac%7B1%7D%7B%5Csqrt%7B2%7D%7D%5Cleft%28%5Cvert%7B%5Crm%20bin%7D%28i%29%5Crangle%20&plus;%20%5Cvert%7B%5Crm%20bin%7D%28i%29%5Crangle%5Cright%29)

where bin(a) stands for the binary representetion of the number ![equation](https://latex.codecogs.com/gif.latex?a).

It is assumed that 
(i) the length of the vector is 2^N_l
and 
(ii) all vector components are different and can take values in the range from 0 to 2^N_v
Two numbers are called *special* if their binary representation is either or 010101... or 101010... 

The solution to the problem is expected 
to be given by the wave function 
the wave function of the form (|a> + |b>) / sqrt(2)

The positions of the *special* numbers 
translated into the binary representation
is the solution of the task and 

##Example
Let us consider the vector
n = [1,2,7,5]
that is related to N_l = 2 and N_v = 3

In the binary representation this vector is given by
n_{\rm bin} = [001, 010, 111, 101]
The special numbers are on the 1 and 3 positions

The solution to the problem is the wave function of the form (1 + 3) / sqrt(2) or in the binary representation (01 + 11) / sqrt(2)

##Solution
