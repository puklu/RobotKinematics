import numpy as np
from numpy.linalg import eig

#creating the matix given in the task
a= np.array([[0,1,0,0],[0,0,1,0],[0,0,0,1],[-18,9,11,-1]])

#printing the matrix given in the task
print(a)

#finding eignevalues of the matrix
values, vectors = eig(a)

#printing eigenvalues of the matrix
print("Eigenvalues (and hence solutions of the polynomial) are: "+str(values))