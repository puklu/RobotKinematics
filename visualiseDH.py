## VISUALISING THE X-Y PROJECTION OF END EFFECTOR ##



import numpy as np
from matplotlib import pyplot as plt



# print(samplesTheta)
###################################################################################################
mechanism = {} 

mechanism["theta1 offset"] = "0"
mechanism["theta2 offset"] = "-1.57"
mechanism["theta3 offset"] = "0"
mechanism["theta4 offset"] = "0"
mechanism["theta5 offset"] = "1.57"
mechanism["theta6 offset"] = "0"

mechanism["d1"] = "0.450"
mechanism["d2"] = "0"
mechanism["d3"] = "0"
mechanism["d4"] = "0.640"
mechanism["d5"] = "0"
mechanism["d6"] = "0.200"

mechanism["a1"] = "0.150"
mechanism["a2"] = "0.614"
mechanism["a3"] = "0.200"
mechanism["a4"] = "0"
mechanism["a5"] = "0.030"
mechanism["a6"] = "0"

mechanism["alpha1"] = "-1.57"
mechanism["alpha2"] = "0"
mechanism["alpha3"] = "-1.57"
mechanism["alpha4"] = "1.57"
mechanism["alpha5"] = "-1.57"
mechanism["alpha6"] = "0"

joints = {"theta1": "0", "theta2": "0","theta3": "0","theta4": "0","theta5": "0","theta6": "0", } 

###################################################################################################


def fkt(mechanism, joints):
    
        import math  
        import numpy as np

        #dictionary to store results
        result = {}

        
        #H(0_1)
        h1    =[[math.cos((float(joints.get('theta1'))+float(mechanism.get('theta1 offset')))),   -math.sin((float(joints.get('theta1'))+float(mechanism.get('theta1 offset'))))*math.cos((float(mechanism.get('alpha1')))), math.sin((float(joints.get('theta1'))+float(mechanism.get('theta1 offset'))))*math.sin((float(mechanism.get('alpha1')))), float(mechanism.get('a1'))*math.cos((float(joints.get('theta1'))+float(mechanism.get('theta1 offset'))))],
                [math.sin((float(joints.get('theta1'))+float(mechanism.get('theta1 offset')))),    math.cos((float(joints.get('theta1'))+float(mechanism.get('theta1 offset'))))*math.cos((float(mechanism.get('alpha1')))),-math.cos((float(joints.get('theta1'))+float(mechanism.get('theta1 offset'))))*math.sin((float(mechanism.get('alpha1')))), float(mechanism.get('a1'))*math.sin((float(joints.get('theta1'))+float(mechanism.get('theta1 offset'))))],
                [0,                                                                                math.sin(float(mechanism.get('alpha1'))),                                                                                 math.cos(float(mechanism.get('alpha1'))),                                                                                 float(mechanism.get('d1'))                                                                              ],
                [0,                                                                                0,                                                                                                                        0,                                                                                                                        1                                                                                                       ]]

        #H(1_2)
        h2    =[[math.cos((float(joints.get('theta2'))+float(mechanism.get('theta2 offset')))),   -math.sin((float(joints.get('theta2'))+float(mechanism.get('theta2 offset'))))*math.cos((float(mechanism.get('alpha2')))), math.sin((float(joints.get('theta2'))+float(mechanism.get('theta2 offset'))))*math.sin((float(mechanism.get('alpha2')))), float(mechanism.get('a2'))*math.cos((float(joints.get('theta2'))+float(mechanism.get('theta2 offset'))))],
                [math.sin((float(joints.get('theta2'))+float(mechanism.get('theta2 offset')))),    math.cos((float(joints.get('theta2'))+float(mechanism.get('theta2 offset'))))*math.cos((float(mechanism.get('alpha2')))),-math.cos((float(joints.get('theta2'))+float(mechanism.get('theta2 offset'))))*math.sin((float(mechanism.get('alpha2')))), float(mechanism.get('a2'))*math.sin((float(joints.get('theta2'))+float(mechanism.get('theta2 offset'))))],
                [0,                                                                                math.sin(float(mechanism.get('alpha2'))),                                                                                 math.cos(float(mechanism.get('alpha2'))),                                                                                 float(mechanism.get('d2'))                                                                              ],
                [0,                                                                                0,                                                                                                                        0,                                                                                                                        1                                                                                                       ]]

        #H(2_3)
        h3    =[[math.cos((float(joints.get('theta3'))+float(mechanism.get('theta3 offset')))),   -math.sin((float(joints.get('theta3'))+float(mechanism.get('theta3 offset'))))*math.cos((float(mechanism.get('alpha3')))), math.sin((float(joints.get('theta3'))+float(mechanism.get('theta3 offset'))))*math.sin((float(mechanism.get('alpha3')))), float(mechanism.get('a3'))*math.cos((float(joints.get('theta3'))+float(mechanism.get('theta3 offset'))))],
                [math.sin((float(joints.get('theta3'))+float(mechanism.get('theta3 offset')))),    math.cos((float(joints.get('theta3'))+float(mechanism.get('theta3 offset'))))*math.cos((float(mechanism.get('alpha3')))),-math.cos((float(joints.get('theta3'))+float(mechanism.get('theta3 offset'))))*math.sin((float(mechanism.get('alpha3')))), float(mechanism.get('a3'))*math.sin((float(joints.get('theta3'))+float(mechanism.get('theta3 offset'))))],
                [0,                                                                                math.sin(float(mechanism.get('alpha3'))),                                                                                 math.cos(float(mechanism.get('alpha3'))),                                                                                 float(mechanism.get('d3'))                                                                              ],
                [0,                                                                                0,                                                                                                                        0,                                                                                                                        1                                                                                                       ]]


        #H(3_4)
        h4    =[[math.cos((float(joints.get('theta4'))+float(mechanism.get('theta4 offset')))),   -math.sin((float(joints.get('theta4'))+float(mechanism.get('theta4 offset'))))*math.cos((float(mechanism.get('alpha4')))), math.sin((float(joints.get('theta4'))+float(mechanism.get('theta4 offset'))))*math.sin((float(mechanism.get('alpha4')))), float(mechanism.get('a4'))*math.cos((float(joints.get('theta4'))+float(mechanism.get('theta4 offset'))))],
                [math.sin((float(joints.get('theta4'))+float(mechanism.get('theta4 offset')))),    math.cos((float(joints.get('theta4'))+float(mechanism.get('theta4 offset'))))*math.cos((float(mechanism.get('alpha4')))),-math.cos((float(joints.get('theta4'))+float(mechanism.get('theta4 offset'))))*math.sin((float(mechanism.get('alpha4')))), float(mechanism.get('a4'))*math.sin((float(joints.get('theta4'))+float(mechanism.get('theta4 offset'))))],
                [0,                                                                                math.sin(float(mechanism.get('alpha4'))),                                                                                 math.cos(float(mechanism.get('alpha4'))),                                                                                 float(mechanism.get('d4'))                                                                              ],
                [0,                                                                                0,                                                                                                                        0,                                                                                                                        1                                                                                                       ]]

        #H(4_5)
        h5    =[[math.cos((float(joints.get('theta5'))+float(mechanism.get('theta5 offset')))),   -math.sin((float(joints.get('theta5'))+float(mechanism.get('theta5 offset'))))*math.cos((float(mechanism.get('alpha5')))), math.sin((float(joints.get('theta5'))+float(mechanism.get('theta5 offset'))))*math.sin((float(mechanism.get('alpha5')))), float(mechanism.get('a5'))*math.cos((float(joints.get('theta5'))+float(mechanism.get('theta5 offset'))))],
                [math.sin((float(joints.get('theta5'))+float(mechanism.get('theta5 offset')))),    math.cos((float(joints.get('theta5'))+float(mechanism.get('theta5 offset'))))*math.cos((float(mechanism.get('alpha5')))),-math.cos((float(joints.get('theta5'))+float(mechanism.get('theta5 offset'))))*math.sin((float(mechanism.get('alpha5')))), float(mechanism.get('a5'))*math.sin((float(joints.get('theta5'))+float(mechanism.get('theta5 offset'))))],
                [0,                                                                                math.sin(float(mechanism.get('alpha5'))),                                                                                 math.cos(float(mechanism.get('alpha5'))),                                                                                 float(mechanism.get('d5'))                                                                              ],
                [0,                                                                                0,                                                                                                                        0,                                                                                                                        1                                                                                                       ]]

        #H(5_6)
        h6    =[[math.cos((float(joints.get('theta6'))+float(mechanism.get('theta6 offset')))),   -math.sin((float(joints.get('theta6'))+float(mechanism.get('theta6 offset'))))*math.cos((float(mechanism.get('alpha6')))), math.sin((float(joints.get('theta6'))+float(mechanism.get('theta6 offset'))))*math.sin((float(mechanism.get('alpha6')))), float(mechanism.get('a6'))*math.cos((float(joints.get('theta6'))+float(mechanism.get('theta6 offset'))))],
                [math.sin((float(joints.get('theta6'))+float(mechanism.get('theta6 offset')))),    math.cos((float(joints.get('theta6'))+float(mechanism.get('theta6 offset'))))*math.cos((float(mechanism.get('alpha6')))),-math.cos((float(joints.get('theta6'))+float(mechanism.get('theta6 offset'))))*math.sin((float(mechanism.get('alpha6')))), float(mechanism.get('a6'))*math.sin((float(joints.get('theta6'))+float(mechanism.get('theta6 offset'))))],
                [0,                                                                                math.sin(float(mechanism.get('alpha6'))),                                                                                 math.cos(float(mechanism.get('alpha6'))),                                                                                 float(mechanism.get('d6'))                                                                              ],
                [0,                                                                                0,                                                                                                                        0,                                                                                                                        1                                                                                                       ]]

        #H(0_6) = H(0_1).H(1_2).H(2_3).H(3_4).H(4_5).H(5_6)
        h = np.dot(h1,h2)
        h = np.dot(h,h3)
        h = np.dot(h,h4)
        h = np.dot(h,h5)
        h = np.dot(h,h6)

        #print(h)

        r = h[0:3, 0:3]
        t = h[0:3, 3]

        #rotation matrix
        result["r"] = r

        #translation vector
        result["t"] = t

        return result


# print(fkt(mechanism,joints))

##################################################################################################

# an array from 0 to 2pi with 1000 samples to take samples of theta1
samplesTheta = np.linspace(0,2*(np.pi),1000)

#arrays to record the x and y coordinate of the end effector as theta1 changes
x = []
y = []


for sampleTh in samplesTheta:
   #updating theta1 with the sample values of theta1  
   joints["theta1"] = sampleTh
   #print(fkt(mechanism,joints))
   #recording the values of x and y coordinates of the end effector
   x.append(fkt(mechanism, joints)["t"][0:1])
   y.append(fkt(mechanism, joints)["t"][1:2]) 
   #print(joints)

# print (x) 
# print (y)  

#plotting the projection of the end effector on xy plane
# plt.scatter(x,y)
# plt.xlabel('x-axis (in metres)')
# plt.ylabel('y-axis (in metres)')
# plt.title('Projection of end-effector on x-y plane')
# plt.axis('square')
# plt.grid()
# plt.xticks([i/10 for i in range(-9,10)])
# plt.yticks([i/10 for i in range(-9,10)])
# plt.show()

# plt.imshow([x,y])
# plt.show()

print([x,y])


plt.hexbin(x,y,bins=500, gridsize=100, cmap=plt.cm.jet)
plt.axis('square')
plt.xticks([i/10 for i in range(-9,10)])
plt.yticks([i/10 for i in range(-9,10)])
plt.show()
