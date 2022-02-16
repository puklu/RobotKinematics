


import numpy as np
from numpy.linalg import norm
from sympy import Matrix
from numpy.matrixlib.defmatrix import matrix
import sympy as sp
import matplotlib.pyplot as plt
from sympy.matrices.subspaces import _nullspace


#approximate rotation
R = np.array([[0.8047,   -0.5059,   -0.3106],
              [0.3106,    0.8047,   -0.5059],
              [0.5059,    0.3106,    0.8047]])

#for testing
# R = np.array([[3/5,   -4/5,   0],
#               [4/5,   3/5,   0],
#               [0,   0,   1]])

#inverse matrix of rotation
R_inv = np.linalg.inv(R)   
b1_beta = [[1],[0],[0]]
b2_beta = [[0],[1],[0]]
b3_beta = [[0],[0],[1]]

#rotated matrix's bases from beta perspective
b1_pr_beta = R[:,0]
b2_pr_beta = R[:,1]
b3_pr_beta = R[:,2]

b1_beta_pr = np.dot(R_inv, b1_beta)
b2_beta_pr = np.dot(R_inv, b2_beta)
b3_beta_pr = np.dot(R_inv, b3_beta)


o_pr_o_beta_pr = [[1],[1],[1]]  # for a1
o_pr_beta = - np.dot(R, o_pr_o_beta_pr)

print("o_pr_beta="+ str(o_pr_beta))
#for testing
# o_pr_beta = [[1],[0],[1]] 

o_beta = np.array([0, 0, 0]) # origin point


#plot settings
ax = plt.axes(projection = '3d')
ax.set_xlim([-2,4])
ax.set_ylim([-2,4])
ax.set_zlim([-2,4])
ax.set_xlabel('x')
ax.set_ylabel('y')
ax.set_zlabel('z')
ax.set_xticks([-2,-1,0,1,2,3,4])
ax.set_yticks([-2,-1,0,1,2,3,4])
ax.set_zticks([-2,-1,0,1,2,3,4])


#plotting vectors
ax.quiver(o_beta[0],o_beta[1],o_beta[2], b1_beta[0],b1_beta[1],b1_beta[2], color= 'r') #b1
ax.quiver(o_beta[0],o_beta[1],o_beta[2], b2_beta[0],b2_beta[1],b2_beta[2], color= 'g') #b2
ax.quiver(o_beta[0],o_beta[1],o_beta[2], b3_beta[0],b3_beta[1],b3_beta[2], color= 'b') #b3

ax.quiver(o_pr_beta[0],o_pr_beta[1],o_pr_beta[2], b1_pr_beta[0],b1_pr_beta[1],b1_pr_beta[2], color= 'r') #b1_pr_beta
ax.quiver(o_pr_beta[0],o_pr_beta[1],o_pr_beta[2], b2_pr_beta[0],b2_pr_beta[1],b2_pr_beta[2], color= 'g') #b2_pr_beta
ax.quiver(o_pr_beta[0],o_pr_beta[1],o_pr_beta[2], b3_pr_beta[0],b3_pr_beta[1],b3_pr_beta[2], color= 'b') #b3_pr_beta


#finding axis of rotation

r = (sp.Matrix(R-np.identity(3))).nullspace()
print("eigenvectors= "+str(r))


#plot of axis of rotation 
ax.quiver(o_beta[0],o_beta[1],o_beta[2], r[0][0],r[0][1],r[0][2], color= 'k', label='axis of rotation')
plt.legend()

#########


# finding axis of motion
I = np.identity(3)

A =  np.dot((R-I),(R-I))
B = -np.dot((R-I),o_pr_beta)
# A = sp.Matrix(A)
# B = sp.Matrix(B)



point = np.linalg.lstsq(A,B, rcond=None)[0]
direction = r

print("point"+ str(point))
print("direction"+ str(direction))



ax.quiver(point[0], point[1], point[2],direction[0][0],direction[0][1],direction[0][2], color= 'y', label='axis of motion')
plt.legend()

############

#GENERATOR
g1 = ((R-I)[:,0])
g2 = ((R-I)[:,1])
g3 = ((R-I)[:,2])



print("g1= "+ str(g1))
print("g2= "+ str(g2))
print("g3= "+ str(g3))
# print("g1[0]= "+ str(g1[0]))
# print("g1[1]= "+ str(g1[1]))
# print("g1[2]= "+ str(g1[2]))

print("R-I=" + str(R-I))

ax.quiver(0, 0, 0,g1[0],g1[0],g1[0], label='sigma1')
ax.quiver(0, 0, 0,g3[0],g3[0],g3[0], label='sigma2')


plt.show()


#point of intersection of a1 and plane signma
P = point
print("P= "+str(P))

P_pr = np.dot(R, P)
print("P_pr=" + str(P_pr))

P_pr_pr = P_pr + o_pr_beta*direction
print("P_pr_pr=" + str(P_pr_pr))

# x = np.linspace(-5, 5, 1)
# y = np.linspace(-5, 5, 1)

# z = -x + y + point[0] - point[1] + point[2]

# fig = plt.figure()
# ax = fig.gca(projection='3d')

# surf = ax.plot_surface(x,y,z)
# plt.show()

