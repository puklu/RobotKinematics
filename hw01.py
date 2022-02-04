import numpy as np
from numpy.linalg import eig

##### Task 3b #####################################################################
#creating the matrix given in the task
a= np.array([[0,1,0,0],[0,0,1,0],[0,0,0,1],[-18,9,11,-1]])

#printing the matrix given in the task
print(a)

#finding eignevalues of the matrix
values, vectors = eig(a)

#printing eigenvalues of the matrix
print("Eigenvalues (and hence solutions of the polynomial) are: "+str(values))


###############################################################################################
## Task 4 #########################################################################

#companion matrix for the given polynomial
# given polynomial = x^4 - 15x^2 + 10x + 24

compMat = ([[0,0,0, -24],[1,0,0,-10],[0,1,0,15],[0,0,1,0]])
#printing the companion matrix
print(compMat)

#finding eignevalues of the matrix
values1, vectors1 = eig(compMat)

#printing eigenvalues of the matrix
print("Eigenvalues (and hence solutions of the polynomial) are: "+str(values1))


