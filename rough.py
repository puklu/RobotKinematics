# ####################### HW04 ################################################
# ############################################################################
# import sys
# import scipy.linalg as linalg 
# from sympy import Matrix
# import numpy as np
# import matplotlib.pyplot as plt
# from numpy.core.numeric import identity
# from sympy import Matrix
# from sympy.matrices.expressions.special import Identity
# from sympy.matrices.subspaces import _nullspace


# # approximate rotation
# R = np.array([[0.8047,   -0.5059,   -0.3106],
#               [0.3106,    0.8047,   -0.5059],
#               [0.5059,    0.3106,    0.8047]])

# #inverse matrix of rotation
# R_inv = np.linalg.inv(R)     

# b1_beta = [[1],[0],[0]]
# b2_beta = [[0],[1],[0]]
# b3_beta = [[0],[0],[1]]


# #rotated matrix's bases from beta perspective
# b1_pr_beta = R[:,0]
# print("b1_pr_beta= "+ str(b1_pr_beta))
# b2_pr_beta = R[:,1]
# print("b2_pr_beta= "+ str(b2_pr_beta))
# b3_pr_beta = R[:,2]
# print("b3_pr_beta= "+ str(b3_pr_beta))

# b1_beta_pr = np.dot(R_inv, b1_beta)
# print("b1_beta_pr= "+ str(b1_beta_pr))
# b2_beta_pr = np.dot(R_inv, b2_beta)
# print("b2_beta_pr= "+ str(b2_beta_pr))
# b3_beta_pr = np.dot(R_inv, b3_beta)
# print("b3_beta_pr= "+ str(b3_beta_pr))


# # print(R)

# #given data
# o_pr_o_beta_pr = [[1],[1],[1]]
# o_pr_beta = - np.dot(R, o_pr_o_beta_pr)
# y_pr_beta_pr = [[1],[2],[3]]
# x_beta = [[1],[2],[3]]
# y_pr_beta = np.dot(R, y_pr_beta_pr)



# o_beta = np.array([0, 0, 0]) # origin point

# #plot settings
# ax = plt.axes(projection = '3d')
# ax.set_xlim([-2,4])
# ax.set_ylim([-2,4])
# ax.set_zlim([-2,4])
# ax.set_xlabel('x')
# ax.set_ylabel('y')
# ax.set_zlabel('z')
# ax.set_xticks([-2,-1,0,1,2,3,4])
# ax.set_yticks([-2,-1,0,1,2,3,4])
# ax.set_zticks([-2,-1,0,1,2,3,4])


# #plotting vectors
# ax.quiver(o_beta[0],o_beta[1],o_beta[2], b1_beta[0],b1_beta[1],b1_beta[2], color= 'r') #b1
# ax.quiver(o_beta[0],o_beta[1],o_beta[2], b2_beta[0],b2_beta[1],b2_beta[2], color= 'g') #b2
# ax.quiver(o_beta[0],o_beta[1],o_beta[2], b3_beta[0],b3_beta[1],b3_beta[2], color= 'b') #b3



# ax.quiver(o_pr_beta[0],o_pr_beta[1],o_pr_beta[2], b1_pr_beta[0],b1_pr_beta[1],b1_pr_beta[2], color= 'r') #b1_pr_beta
# ax.quiver(o_pr_beta[0],o_pr_beta[1],o_pr_beta[2], b2_pr_beta[0],b2_pr_beta[1],b2_pr_beta[2], color= 'g') #b2_pr_beta
# ax.quiver(o_pr_beta[0],o_pr_beta[1],o_pr_beta[2], b3_pr_beta[0],b3_pr_beta[1],b3_pr_beta[2], color= 'b') #b3_pr_beta




# #plot of vector x in beta basis
# ax.quiver(o_beta[0],o_beta[1],o_beta[2], x_beta[0],x_beta[1],x_beta[2], color= 'y')

# #plot of vector y in beta prime basis
# ax.quiver(o_pr_beta[0],o_pr_beta[1],o_pr_beta[2], y_pr_beta[0],y_pr_beta[1],y_pr_beta[2], color= 'y')


# # #axis of rotation
# # r = _nullspace(Matrix(R-Identity(3)))
# # ax.quiver(o_beta[0],o_beta[1],o_beta[2], r[0][0],r[0][1],r[0][2], color= 'k')

# #axis of motion
# a1 = -np.linalg.inv(R-Identity(3))*o_pr_beta

# print("a1= " + str(a1))

# print("r= " + str(r))

# # a1 = np.dot((np.linalg.inv(R-identity(3))), o_pr_beta)
# # print("a1= " + str(a1))


# plt.title('Frames in standard and rotated basis')
# plt.show()



# A = np.array([[1, -2, 1], 
#               [1, 1, -2], 
#               [-2, 1, 1]])

# B = np.array([[1],[1],[-2]])

# r = [[1],[1],[1]]



# X =Matrix(np.concatenate((A,B), axis=1)).rref()[0]                                                                                                        


# # X = np.linalg.pinv(A).dot(B)
# Y = np.linalg.lstsq(A,B, rcond=None)[0]

# # # X = np.linalg.solve(A,B)

# point = X[:,3]
# print(point)
# print(Y-point))



import sympy
from sympy import *
import numpy as np


I = eye(3)


# theta1_half = symbol('theta1_half')
theta1_half = pi/18
# theta2_half = symbol('theta2_half')
theta2_half = -pi/20
# v_theta = symbol('v_theta')
v_theta = pi/8
# v_phi = symbol('v_phi')
v_phi = pi/9
# u_theta = symbol('u_theta')
u_theta =-pi/6
# u_phi = symbol('u_phi')
u_phi = -pi/7

# def check_7112(theta1_half, theta2_half, v_theta, v_phi, u_theta, u_phi):

s1 = sympy.sin(theta1_half)
c1 = sympy.cos(theta1_half)
s2 = sympy.sin(theta2_half)
c2 = sympy.cos(theta2_half)

v1 = sympy.cos(v_theta) * sympy.sin(v_phi)
v2 = sympy.sin(v_theta) * sympy.sin(v_phi)
v3 = sympy.cos(v_phi)
u1 = sympy.cos(u_theta) * sympy.sin(u_phi)
u2 = sympy.sin(u_theta) * sympy.sin(u_phi)
u3 = sympy.cos(u_phi)
    
v = sympy.Matrix([v1, v2, v3])
u = sympy.Matrix([u1, u2, u3])


def crossV(vect):
    return sympy.Matrix([[ 0,       -vect[2],  vect[1]],
                         [ vect[2],  0,       -vect[0]],  
                         [-vect[1],  vect[0],  0     ]])

pprint("v= " +str(v))
pprint("u= " +str(u))


R1 =(2*(s1*v))*(Transpose(s1*v))+(2*c1**2-1)*I+2*c1*s1*crossV(v)
R2 =(2*(s2*u))*(Transpose(s2*u))+(2*c2**2-1)*I+2*c2*s2*crossV(u)

R21 = R2*R1


# print("R1= "+ str(R1))
# print("R2= "+ str(R2))



# pprint("R21= "+ str(R21))


c21=Matrix([c2*c1])-(Transpose(s2*u) *(s1*v))
c21=c21[0]


s21v21=c2*s1*v+s2*c1*u+(s2*u).cross(s1*v)


pprint("s21v21= "+ str(s21v21))

RR21=2*s21v21*(Transpose(s21v21))+(2*c21**2-1)*I+2*c21*crossV(s21v21)

# pprint("RR21= "+ str(RR21))

result = N(RR21-R21)

pprint(result)





