####################### HW04 ################################################
############################################################################

import numpy as np
import matplotlib.pyplot as plt


# approximate rotation
R = np.array([[0.8047,   -0.5059,   -0.3106],
              [0.3106,    0.8047,   -0.5059],
              [0.5059,    0.3106,    0.8047]])

#inverse matrix of rotation
R_inv = np.linalg.inv(R)     

b1_beta = [[1],[0],[0]]
b2_beta = [[0],[1],[0]]
b3_beta = [[0],[0],[1]]


#rotated matrix's bases from beta perspective
b1_pr_beta = R[:,0]
print("b1_pr_beta= "+ str(b1_pr_beta))
b2_pr_beta = R[:,1]
print("b2_pr_beta= "+ str(b2_pr_beta))
b3_pr_beta = R[:,2]
print("b3_pr_beta= "+ str(b3_pr_beta))

b1_beta_pr = np.dot(R_inv, b1_beta)
print("b1_beta_pr= "+ str(b1_beta_pr))
b2_beta_pr = np.dot(R_inv, b2_beta)
print("b2_beta_pr= "+ str(b2_beta_pr))
b3_beta_pr = np.dot(R_inv, b3_beta)
print("b3_beta_pr= "+ str(b3_beta_pr))


# print(R)

#given data
# o_pr_beta = [[1], [1], [1]]

o_pr_o_beta_pr = [[1],[1],[1]]
o_pr_beta = - np.dot(R, o_pr_o_beta_pr)

y_pr_beta_pr = [[1],[2],[3]]
x_beta = [[1],[2],[3]]
y_pr_beta = np.dot(R, y_pr_beta_pr)



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




#plot of vector x in beta basis
# ax.quiver(o_beta[0],o_beta[1],o_beta[2], x_beta[0],x_beta[1],x_beta[2], color= 'y')

#plot of vector y in beta prime basis
# ax.quiver(o_pr_beta[0],o_pr_beta[1],o_pr_beta[2], y_pr_beta[0],y_pr_beta[1],y_pr_beta[2], color= 'y')

# plotting oz_beta
# y_beta = np.dot(R,y_pr_beta_pr ) + o_pr_beta
# ax.quiver(o_beta[0],o_beta[1],o_beta[2], y_beta[0],y_beta[1],y_beta[2], color= 'k')
# print("oz_beta= "+ str(y_beta))



plt.title('Frames in standard and rotated basis')
plt.show()






