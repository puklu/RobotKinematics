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

#rotated matrix's bases from beta perspective
b1_pr_beta = R[:,0]
b2_pr_beta = R[:,1]
b3_pr_beta = R[:,2]

#original matrix's bases from rotated matrix's perspective
b1_beta_pr = R_inv[:,0]
b2_beta_pr = R_inv[:,1]
b3_beta_pr = R_inv[:,2]

print(R)

#given data
o_pr_beta = [[1], [1], [1]]
y_pr_beta_pr = [[1],[2],[3]]
x_beta = [[1],[2],[3]]
y_pr_beta_pr = [[1],[2],[3]]

y_beta = np.dot(R, y_pr_beta_pr) + o_pr_beta

o_beta = np.array([0, 0, 0]) # origin point

#plot settings
ax = plt.axes(projection = '3d')
ax.set_xlim([-2,5])
ax.set_ylim([-1,5])
ax.set_zlim([0,5])
ax.set_xlabel('x')
ax.set_ylabel('y')
ax.set_zlabel('z')
ax.set_xticks([-2,-1,0,1,2,3,4,5])
ax.set_yticks([-1,0,1,2,3,4,5])
ax.set_zticks([0,1,2,3,4,5])


#plotting vectors
ax.quiver(o_beta[0],o_beta[1],o_beta[2], R[0,0],R[1,0],R[2,0], color= 'r') #b1
ax.quiver(o_beta[0],o_beta[1],o_beta[2], R[0,1],R[1,1],R[2,1], color= 'g') #b2
ax.quiver(o_beta[0],o_beta[1],o_beta[2], R[0,2],R[1,2],R[2,2], color= 'b') #b3

ax.quiver(o_pr_beta[0],o_pr_beta[1],o_pr_beta[2], R_inv[0,0],R_inv[1,0],R_inv[2,0], color= 'r') #b1_pr
ax.quiver(o_pr_beta[0],o_pr_beta[1],o_pr_beta[2], R_inv[0,1],R_inv[1,1],R_inv[2,1], color= 'g') #b2_pr
ax.quiver(o_pr_beta[0],o_pr_beta[1],o_pr_beta[2], R_inv[0,2],R_inv[1,2],R_inv[2,2], color= 'b') #b3_pr


x_beta = np.dot(R, x_beta)
y_pr_beta_pr = np.dot(R_inv, y_pr_beta_pr)

#plot of vector x in beta basis
ax.quiver(o_beta[0],o_beta[1],o_beta[2], x_beta[0,0],x_beta[1,0],x_beta[2,0], color= 'y')

#plot of vector y in beta prime basis
ax.quiver(o_pr_beta[0],o_pr_beta[1],o_pr_beta[2], y_pr_beta_pr[0,0],y_pr_beta_pr[1,0],y_pr_beta_pr[2,0], color= 'y')

plt.title('beta and beta prime coordinate frames')
plt.show()

