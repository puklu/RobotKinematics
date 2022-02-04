########### TASK 3a #######################################################################################
## This is the soultion to task 3a to implement the forward kinematic task for a general 6R manipulator. ## 


######## mechanism and joints values for testing Motoman MA1400 manipulator (that was used in the previous homework)

# mechanism = {} 

# mechanism["theta1 offset"] = "0"
# mechanism["theta2 offset"] = "-1.57"
# mechanism["theta3 offset"] = "0"
# mechanism["theta4 offset"] = "0"
# mechanism["theta5 offset"] = "1.57"
# mechanism["theta6 offset"] = "0"

# mechanism["d1"] = "0.450"
# mechanism["d2"] = "0"
# mechanism["d3"] = "0"
# mechanism["d4"] = "0.640"
# mechanism["d5"] = "0"
# mechanism["d6"] = "0.200"

# mechanism["a1"] = "0.150"
# mechanism["a2"] = "0.614"
# mechanism["a3"] = "0.200"
# mechanism["a4"] = "0"
# mechanism["a5"] = "0.030"
# mechanism["a6"] = "0"

# mechanism["alpha1"] = "-1.57"
# mechanism["alpha2"] = "0"
# mechanism["alpha3"] = "-1.57"
# mechanism["alpha4"] = "1.57"
# mechanism["alpha5"] = "-1.57"
# mechanism["alpha6"] = "0"

# joints = {"theta1": "0", "theta2": "0","theta3": "0","theta4": "0","theta5": "0","theta6": "0", } 





####################################################################################################

def fkt(mechanism, joints):
    
        
        import numpy as np

        #dictionary to store results
        result = {}

        
        #H(0_1)
        h0_1    =[[np.cos((float(joints.get('theta1'))+float(mechanism.get('theta1 offset')))),   -np.sin((float(joints.get('theta1'))+float(mechanism.get('theta1 offset'))))*np.cos((float(mechanism.get('alpha1')))), np.sin((float(joints.get('theta1'))+float(mechanism.get('theta1 offset'))))*np.sin((float(mechanism.get('alpha1')))), float(mechanism.get('a1'))*np.cos((float(joints.get('theta1'))+float(mechanism.get('theta1 offset'))))],
                [np.sin((float(joints.get('theta1'))+float(mechanism.get('theta1 offset')))),    np.cos((float(joints.get('theta1'))+float(mechanism.get('theta1 offset'))))*np.cos((float(mechanism.get('alpha1')))),-np.cos((float(joints.get('theta1'))+float(mechanism.get('theta1 offset'))))*np.sin((float(mechanism.get('alpha1')))), float(mechanism.get('a1'))*np.sin((float(joints.get('theta1'))+float(mechanism.get('theta1 offset'))))],
                [0,                                                                                np.sin(float(mechanism.get('alpha1'))),                                                                                 np.cos(float(mechanism.get('alpha1'))),                                                                                 float(mechanism.get('d1'))                                                                              ],
                [0,                                                                                0,                                                                                                                        0,                                                                                                                        1                                                                                                       ]]

        #H(1_2)
        h1_2    =[[np.cos((float(joints.get('theta2'))+float(mechanism.get('theta2 offset')))),   -np.sin((float(joints.get('theta2'))+float(mechanism.get('theta2 offset'))))*np.cos((float(mechanism.get('alpha2')))), np.sin((float(joints.get('theta2'))+float(mechanism.get('theta2 offset'))))*np.sin((float(mechanism.get('alpha2')))), float(mechanism.get('a2'))*np.cos((float(joints.get('theta2'))+float(mechanism.get('theta2 offset'))))],
                [np.sin((float(joints.get('theta2'))+float(mechanism.get('theta2 offset')))),    np.cos((float(joints.get('theta2'))+float(mechanism.get('theta2 offset'))))*np.cos((float(mechanism.get('alpha2')))),-np.cos((float(joints.get('theta2'))+float(mechanism.get('theta2 offset'))))*np.sin((float(mechanism.get('alpha2')))), float(mechanism.get('a2'))*np.sin((float(joints.get('theta2'))+float(mechanism.get('theta2 offset'))))],
                [0,                                                                                np.sin(float(mechanism.get('alpha2'))),                                                                                 np.cos(float(mechanism.get('alpha2'))),                                                                                 float(mechanism.get('d2'))                                                                              ],
                [0,                                                                                0,                                                                                                                        0,                                                                                                                        1                                                                                                       ]]

        #H(2_3)
        h2_3    =[[np.cos((float(joints.get('theta3'))+float(mechanism.get('theta3 offset')))),   -np.sin((float(joints.get('theta3'))+float(mechanism.get('theta3 offset'))))*np.cos((float(mechanism.get('alpha3')))), np.sin((float(joints.get('theta3'))+float(mechanism.get('theta3 offset'))))*np.sin((float(mechanism.get('alpha3')))), float(mechanism.get('a3'))*np.cos((float(joints.get('theta3'))+float(mechanism.get('theta3 offset'))))],
                [np.sin((float(joints.get('theta3'))+float(mechanism.get('theta3 offset')))),    np.cos((float(joints.get('theta3'))+float(mechanism.get('theta3 offset'))))*np.cos((float(mechanism.get('alpha3')))),-np.cos((float(joints.get('theta3'))+float(mechanism.get('theta3 offset'))))*np.sin((float(mechanism.get('alpha3')))), float(mechanism.get('a3'))*np.sin((float(joints.get('theta3'))+float(mechanism.get('theta3 offset'))))],
                [0,                                                                                np.sin(float(mechanism.get('alpha3'))),                                                                                 np.cos(float(mechanism.get('alpha3'))),                                                                                 float(mechanism.get('d3'))                                                                              ],
                [0,                                                                                0,                                                                                                                        0,                                                                                                                        1                                                                                                       ]]


        #H(3_4)
        h3_4    =[[np.cos((float(joints.get('theta4'))+float(mechanism.get('theta4 offset')))),   -np.sin((float(joints.get('theta4'))+float(mechanism.get('theta4 offset'))))*np.cos((float(mechanism.get('alpha4')))), np.sin((float(joints.get('theta4'))+float(mechanism.get('theta4 offset'))))*np.sin((float(mechanism.get('alpha4')))), float(mechanism.get('a4'))*np.cos((float(joints.get('theta4'))+float(mechanism.get('theta4 offset'))))],
                [np.sin((float(joints.get('theta4'))+float(mechanism.get('theta4 offset')))),    np.cos((float(joints.get('theta4'))+float(mechanism.get('theta4 offset'))))*np.cos((float(mechanism.get('alpha4')))),-np.cos((float(joints.get('theta4'))+float(mechanism.get('theta4 offset'))))*np.sin((float(mechanism.get('alpha4')))), float(mechanism.get('a4'))*np.sin((float(joints.get('theta4'))+float(mechanism.get('theta4 offset'))))],
                [0,                                                                                np.sin(float(mechanism.get('alpha4'))),                                                                                 np.cos(float(mechanism.get('alpha4'))),                                                                                 float(mechanism.get('d4'))                                                                              ],
                [0,                                                                                0,                                                                                                                        0,                                                                                                                        1                                                                                                       ]]

        #H(4_5)
        h4_5    =[[np.cos((float(joints.get('theta5'))+float(mechanism.get('theta5 offset')))),   -np.sin((float(joints.get('theta5'))+float(mechanism.get('theta5 offset'))))*np.cos((float(mechanism.get('alpha5')))), np.sin((float(joints.get('theta5'))+float(mechanism.get('theta5 offset'))))*np.sin((float(mechanism.get('alpha5')))), float(mechanism.get('a5'))*np.cos((float(joints.get('theta5'))+float(mechanism.get('theta5 offset'))))],
                [np.sin((float(joints.get('theta5'))+float(mechanism.get('theta5 offset')))),    np.cos((float(joints.get('theta5'))+float(mechanism.get('theta5 offset'))))*np.cos((float(mechanism.get('alpha5')))),-np.cos((float(joints.get('theta5'))+float(mechanism.get('theta5 offset'))))*np.sin((float(mechanism.get('alpha5')))), float(mechanism.get('a5'))*np.sin((float(joints.get('theta5'))+float(mechanism.get('theta5 offset'))))],
                [0,                                                                                np.sin(float(mechanism.get('alpha5'))),                                                                                 np.cos(float(mechanism.get('alpha5'))),                                                                                 float(mechanism.get('d5'))                                                                              ],
                [0,                                                                                0,                                                                                                                        0,                                                                                                                        1                                                                                                       ]]

        #H(5_6)
        h5_6    =[[np.cos((float(joints.get('theta6'))+float(mechanism.get('theta6 offset')))),   -np.sin((float(joints.get('theta6'))+float(mechanism.get('theta6 offset'))))*np.cos((float(mechanism.get('alpha6')))), np.sin((float(joints.get('theta6'))+float(mechanism.get('theta6 offset'))))*np.sin((float(mechanism.get('alpha6')))), float(mechanism.get('a6'))*np.cos((float(joints.get('theta6'))+float(mechanism.get('theta6 offset'))))],
                [np.sin((float(joints.get('theta6'))+float(mechanism.get('theta6 offset')))),    np.cos((float(joints.get('theta6'))+float(mechanism.get('theta6 offset'))))*np.cos((float(mechanism.get('alpha6')))),-np.cos((float(joints.get('theta6'))+float(mechanism.get('theta6 offset'))))*np.sin((float(mechanism.get('alpha6')))), float(mechanism.get('a6'))*np.sin((float(joints.get('theta6'))+float(mechanism.get('theta6 offset'))))],
                [0,                                                                                np.sin(float(mechanism.get('alpha6'))),                                                                                 np.cos(float(mechanism.get('alpha6'))),                                                                                 float(mechanism.get('d6'))                                                                              ],
                [0,                                                                                0,                                                                                                                        0,                                                                                                                        1                                                                                                       ]]

        #H(0_6) = H(0_1).H(1_2).H(2_3).H(3_4).H(4_5).H(5_6)
        h0_2 = np.dot(h0_1,h1_2)
        h0_3 = np.dot(h0_2,h2_3)
        h0_4 = np.dot(h0_3,h3_4)
        h0_5 = np.dot(h0_4,h4_5)
        h0_6 = np.dot(h0_5,h5_6)

        #print(h)

        r = h0_6[0:3, 0:3]
        t = h0_6[0:3, 3]

        #rotation matrix
        result["r"] = r

        #translation vector
        result["t"] = t

        return result


####################################################################################################


# print(fkt(mechanism, joints))
