import sympy
from sympy import *
import numpy as np
import math

I = eye(3)


#### 6a #########
def check_7112(theta1_half, theta2_half, v_theta, v_phi, u_theta, u_phi):

    I = eye(3)

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

    # print("v= " +str(v))
    # print("u= " +str(u))


    R1 =(2*(s1*v))*(Transpose(s1*v))+(2*c1**2-1)*I+2*c1*s1*crossV(v)
    R2 =(2*(s2*u))*(Transpose(s2*u))+(2*c2**2-1)*I+2*c2*s2*crossV(u)

    R21 = R2*R1

    # print("R1= "+ str(R1))
    # print("R2= "+ str(R2))

    print("R21= "+ str(R21))

    c21=Matrix([c2*c1])-(Transpose(s2*u) *(s1*v))
    c21=c21[0]

    # print("c21= "+ str(c21))

    s21v21=c2*s1*v+s2*c1*u+(s2*u).cross(s1*v)

    # print("s21v21= "+ str(s21v21))

    RR21=2*s21v21*(Transpose(s21v21))+(2*c21**2-1)*I+2*c21*crossV(s21v21)

    # print("RR21= "+ str(RR21))

    return N(RR21-R21)

    # pprint("7.112verify = "+str(result))


def R_from_theta_half_axis(theta_half,v):
    
    I = eye(3)
    s1 = sympy.sin(theta_half)
    c1 = sympy.cos(theta_half)

    def crossV(vect):
        return sympy.Matrix([[ 0,       -vect[2],  vect[1]],
                            [ vect[2],  0,       -vect[0]],  
                            [-vect[1],  vect[0],  0     ]])


    R =(2*(s1*v))*(Transpose(s1*v))+(2*c1**2-1)*I+2*c1*s1*crossV(v)

    return R



#### 6b #########
def check_7116(theta1_half, theta2_half, v_theta, v_phi, u_theta, u_phi):

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

    c21=Matrix([c2*c1])-(Transpose(s2*u) *(s1*v))
    c21= c21[0]
    s21v21=c2*s1*v+s2*c1*u+(s2*u).cross(s1*v)

    q1 = sympy.Matrix([[c1],[s1*v]])
    q2 = sympy.Matrix([[c2],[s2*u]])
    q21 = sympy.Matrix([[c21],[s21v21]])

    # pprint("q1= "+ str(q1))
    # pprint("q2= "+ str(q2))
    # pprint("q21= "+ str(q21))

    q2Mat =sympy.Matrix([[q2[0],-q2[1],-q2[2], -q2[3]],
                        [q2[1], q2[0],-q2[3],  q2[2]],  
                        [q2[2], q2[3], q2[0], -q2[1]], 
                        [q2[3],-q2[2], q2[1],  q2[0]]])

    q1Mat =sympy.Matrix([[q1[0]],[q1[1]],[q1[2]],[q1[3]]])

    q2q1 = q2Mat*q1Mat

    # pprint(str(q2q1-q21))

    return N(q2q1-q21)

    
        

def R_from_q(q):
    return sympy.Matrix([
                       [q[0]**2+q[1]**2-q[2]**2-q[3]**2,  2*(q[1]*q[2]-q[0]*q[3]),           2*(q[1]*q[3]+q[0]*q[2])],
                       [2*(q[1]*q[2]+q[0]*q[3]),           q[0]**2-q[1]**2+q[2]**2-q[3]**2,  2*(q[2]*q[3]-q[0]*q[1])],
                       [2*(q[1]*q[3]-q[0]*q[2]),           2*(q[2]*q[3]+q[0]*q[1]),           q[0]**2-q[1]**2-q[2]**2+q[3]**2  ]
    ])

def q_from_R(R):

    traceR = sympy.trace(R)

    matr = sympy.Matrix([
                         [traceR+1],
                         [R[7]-R[5]],
                         [R[2]-R[6]],
                         [R[3]-R[1]]
    ])

    return matr/(2*(sympy.sqrt(traceR+1)))


#### 6c #########

def findR(theta1_half,v_theta,v_phi):
    I = eye(3)
    s1 = sympy.sin(theta1_half)
    c1 = sympy.cos(theta1_half)
    v1 = sympy.cos(v_theta) * sympy.sin(v_phi)
    v2 = sympy.sin(v_theta) * sympy.sin(v_phi)
    v3 = sympy.cos(v_phi)    
    v = sympy.Matrix([v1, v2, v3])

    def crossV(vect):
        return sympy.Matrix([[ 0,       -vect[2],  vect[1]],
                            [ vect[2],  0,       -vect[0]],  
                            [-vect[1],  vect[0],  0     ]])


    R =(2*(s1*v))*(Transpose(s1*v))+(2*c1**2-1)*I+2*c1*s1*crossV(v)

    return R
    

def findQ(theta1_half,v_theta,v_phi):  
    R = findR(theta1_half,v_theta,v_phi)
    q = q_from_R(R)
    return q



### 6c1 ####
theta1_half = pi/4
v_theta = 0
v_phi = pi/2

R1 = findR(theta1_half,v_theta,v_phi)
q1 = findQ(theta1_half,v_theta,v_phi)
print("R1= ")
pprint(N(R1))
print("q1= ")
pprint(N(q1))


#### 6c2 #####

theta1_half = pi/4
v_theta = pi/2
v_phi = pi/2

R2 = findR(theta1_half,v_theta,v_phi)
q2 = findQ(theta1_half,v_theta,v_phi)
print("R2= ")
pprint(N(R2))
print("q2= ")
pprint(N(q2))


#### 6c3 ######
def q21FROMq2q1(q1, q2):

    q2Mat =sympy.Matrix([[q2[0],-q2[1],-q2[2], -q2[3]],
                        [q2[1], q2[0],-q2[3],  q2[2]],  
                        [q2[2], q2[3], q2[0], -q2[1]], 
                        [q2[3],-q2[2], q2[1],  q2[0]]])

    q1Mat =sympy.Matrix([[q1[0]],[q1[1]],[q1[2]],[q1[3]]])

    q2q1 = q2Mat*q1Mat

    return N(q2q1)

q21 = q21FROMq2q1(q1, q2)
print("q21= ")
pprint(N(q21))

#### 6c4 ####

R21 = R2*R1
print("R21= ")
pprint(N(R21))

##### 6c5 ####

R21fromq21 = R_from_q(q21)
print("R21fromq21= ")
pprint(N(R21fromq21))

##### 6c6 ####

q21fromR21 = q_from_R(R21)
print("q21fromR21= ")
pprint(N(q21fromR21))


# theta1_half = pi/18
# v_theta = pi/9
# v_phi = pi/9

# theta2_half = -pi/20
# u_theta = -pi/6
# u_phi = -pi/7

# pprint(check_7112(theta1_half, theta2_half, v_theta, v_phi, u_theta, u_phi))