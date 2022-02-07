
from fractions import Fraction as frac
from math import atan2, floor
import math
import numpy as np
from sympy.core.symbol import symbols
import os
from sympy.core.sympify import sympify
from sympy.polys.polytools import Poly
from sympy import degree


def rat_approx(n, tol):

    if tol>= 1:
        f = floor(n)
        result = frac(f)
    
    elif tol<1:
        tol = "{:e}".format(tol)
        # print("tol= "+str(tol))
        epower = tol.split('e')       
        epower = int(epower[1])
        result = frac(floor(n * 10**(-epower)),(10**(-epower)))
        # print("result= "+str(result))

    return result



def exact_cs(th, tol):
    
    if (abs(th-math.pi)<tol) or (abs(th+math.pi)<tol):
        c = -1
        s = 0
        

    else:
        t = rat_approx(math.tan(th/2), tol)


        c = frac((1-t**2),(1+t**2))
        s = frac((2*t),(1+t**2))

        # print(c**2 + s**2)
    return [c, s]



def q2r(q):

    div = q[0]**2 +q[1]**2 + q[2]**2 + q[3]**2 

    div = np.array([
                    [1/div, 1/div, 1/div],
                    [1/div, 1/div, 1/div],
                    [1/div, 1/div, 1/div]
    ])
        
    qarray=  np.array([
                       [q[0]**2+q[1]**2-q[2]**2-q[3]**2,  2*(q[1]*q[2]-q[0]*q[3]),           2*(q[1]*q[3]+q[0]*q[2])],
                       [2*(q[1]*q[2]+q[0]*q[3]),           q[0]**2-q[1]**2+q[2]**2-q[3]**2,  2*(q[2]*q[3]-q[0]*q[1])],
                       [2*(q[1]*q[3]-q[0]*q[2]),           2*(q[2]*q[3]+q[0]*q[1]),           q[0]**2-q[1]**2-q[2]**2+q[3]**2  ]
    ])

    return (div*qarray)


def exact_rot(q, tol):

    tolq = tol
    
    while True:
        qrat = [0, 0, 0, 0]

        for i in range(0,4):
            qrat[i] = rat_approx(q[i], tolq)

        r = q2r(qrat)
        
        if(np.linalg.norm(r-q2r(q),'fro')<tol):
            # print(np.linalg.norm(r-q2r(q),'fro'))
            return r
        else:
            tolq = tolq/10
            # print("tolq="+str(tolq))




def rational_mechanism(mechanism, tol):

    rat_mechanism = mechanism.copy()
    
    cos_alpha1 = exact_cs((mechanism["alpha1"]), tol)[0]
    sin_alpha1 = exact_cs((mechanism["alpha1"]), tol)[1]

    cos_alpha2 = exact_cs((mechanism["alpha2"]), tol)[0]
    sin_alpha2 = exact_cs((mechanism["alpha2"]), tol)[1]

    cos_alpha3 = exact_cs((mechanism["alpha3"]), tol)[0]
    sin_alpha3 = exact_cs((mechanism["alpha3"]), tol)[1]

    cos_alpha4 = exact_cs((mechanism["alpha4"]), tol)[0]
    sin_alpha4 = exact_cs((mechanism["alpha4"]), tol)[1]

    cos_alpha5 = exact_cs((mechanism["alpha5"]), tol)[0]
    sin_alpha5 = exact_cs((mechanism["alpha5"]), tol)[1]

    cos_alpha6 = exact_cs((mechanism["alpha6"]), tol)[0]
    sin_alpha6 = exact_cs((mechanism["alpha6"]), tol)[1]

    rat_mechanism["cos alpha1"] = rat_mechanism["alpha1"]
    del rat_mechanism["alpha1"]

    rat_mechanism["sin alpha1"] = sin_alpha1

    rat_mechanism["cos alpha2"] = rat_mechanism["alpha2"]
    del rat_mechanism["alpha2"]

    rat_mechanism["sin alpha2"] = sin_alpha2

    rat_mechanism["cos alpha3"] = rat_mechanism["alpha3"]
    del rat_mechanism["alpha3"]

    rat_mechanism["sin alpha3"] = sin_alpha3

    rat_mechanism["cos alpha4"] = rat_mechanism["alpha4"]
    del rat_mechanism["alpha4"]

    rat_mechanism["sin alpha4"] = sin_alpha4

    rat_mechanism["cos alpha5"] = rat_mechanism["alpha5"]
    del rat_mechanism["alpha5"]

    rat_mechanism["sin alpha5"] = sin_alpha5

    rat_mechanism["cos alpha6"] = rat_mechanism["alpha6"]
    del rat_mechanism["alpha6"]

    rat_mechanism["sin alpha6"] = sin_alpha6

    rat_mechanism["cos alpha1"] = cos_alpha1
    rat_mechanism["cos alpha2"] = cos_alpha2
    rat_mechanism["cos alpha3"] = cos_alpha3
    rat_mechanism["cos alpha4"] = cos_alpha4
    rat_mechanism["cos alpha5"] = cos_alpha5
    rat_mechanism["cos alpha6"] = cos_alpha6

    rat_mechanism["a1"] = rat_approx((mechanism["a1"]), tol)
    rat_mechanism["a2"] = rat_approx((mechanism["a2"]), tol)
    rat_mechanism["a3"] = rat_approx((mechanism["a3"]), tol)
    rat_mechanism["a4"] = rat_approx((mechanism["a4"]), tol)
    rat_mechanism["a5"] = rat_approx((mechanism["a5"]), tol)
    rat_mechanism["a6"] = rat_approx((mechanism["a6"]), tol)

    rat_mechanism["d1"] = rat_approx((mechanism["d1"]), tol)
    rat_mechanism["d2"] = rat_approx((mechanism["d2"]), tol)
    rat_mechanism["d3"] = rat_approx((mechanism["d3"]), tol)
    rat_mechanism["d4"] = rat_approx((mechanism["d4"]), tol)
    rat_mechanism["d5"] = rat_approx((mechanism["d5"]), tol)
    rat_mechanism["d6"] = rat_approx((mechanism["d6"]), tol)

    return rat_mechanism
    pass

def rational_pose(pose, tol):
    
    rotation = exact_rot(pose["q"], tol)
     
    # print("rotation= "+ str(rotation))

    trans = pose["t"]
    trans = np.array([trans])

    # converting translation into rational form
    transRational = [0, 0, 0]
    for i in range(0,3):
        transRational[i] = rat_approx(trans[0][i], tol)
        # print("transRational[i]= "+ str(transRational[i]))   
    transRational = np.array([transRational])

    lastRow = np.array([[frac(0), frac(0), frac(0), frac(1)]])

    # print("trans= "+ str(np.shape(transRational)))

    inter1 = np.hstack((rotation, np.transpose(transRational)))

    # print("RTR= "+ str(np.dot(np.transpose(rotation),rotation)))
    # print("detR= "+ str(np.linalg.det(rotation)))
    result = np.vstack((inter1, lastRow))

    # print("result= "+ str(result))

    return result   
    
    pass


def calculate_M(mechanism, k, tol):
        
        c, s = symbols(f'c{str(k)}, s{str(k)}')

        rat_mech = rational_mechanism(mechanism, tol)

        a = np.array([   
                   [c, -s, 0, 0],
                   [s,  c, 0, 0],
                   [0, 0, 1, rat_mech["d"+str(k)]  ],
                   [0, 0, 0, 1]
                      ])
        
        b = np.array([
                    [1, 0,                            0,                           rat_mech["a"+str(k)]   ],
                    [0, rat_mech["cos alpha"+str(k)], - rat_mech["sin alpha"+str(k)], 0],
                    [0, rat_mech["sin alpha"+str(k)], rat_mech["cos alpha"+str(k)], 0],
                    [0, 0,                      0,                      1]   
        ])

        return np.dot(a,b)


def convertToPoly(mat):
    for i in range(0,3):
        for j in range(0,4):
            # print("mat[i][j]= "+str(mat[i][j]))
            mat[i][j] = Poly(mat[i][j])

    return mat



def ikt_eqs(mechanism, pose, tol):

    c1, s1, c2, s2, c3, s3, c4, s4, c5, s5, c6, s6 = symbols('c1 s1 c2 s2 c3 s3 c4 s4 c5 s5 c6 s6')

    rat_mech = rational_mechanism(mechanism, tol)

    M3_4 = calculate_M(mechanism, 4, tol)
    M4_5 = calculate_M(mechanism, 5, tol)
    M5_6 = calculate_M(mechanism, 6, tol)

    M3_6 =  np.dot(M3_4 , np.dot(M4_5, M5_6))

    M0_1 = calculate_M(mechanism, 1, tol)

    M0_1_inv_a = np.array([
                          [1, 0, 0, -rat_mech["a1"] ],
                          [0, rat_mech["cos alpha1"], rat_mech["sin alpha1"], 0],
                          [0, -rat_mech["sin alpha1"], rat_mech["cos alpha1"], 0],
                          [0, 0, 0, 1]
    ])

    M0_1_inv_b = np.array([
                          [c1, s1, 0, 0],
                          [-s1, c1,0, 0],
                          [0, 0, 1, -rat_mech["d1"] ],
                          [0, 0, 0, 1]
    ])

    M0_1_inv = np.dot(M0_1_inv_a, M0_1_inv_b)



    M1_2 = calculate_M(mechanism, 2, tol)

    M1_2_inv_a = np.array([
                          [1, 0, 0, -rat_mech["a2"] ],
                          [0, rat_mech["cos alpha2"], rat_mech["sin alpha2"], 0],
                          [0, -rat_mech["sin alpha2"], rat_mech["cos alpha2"], 0],
                          [0, 0, 0, 1]
    ])

    M1_2_inv_b = np.array([
                          [c2, s2, 0, 0],
                          [-s2, c2,0, 0],
                          [0, 0, 1, -rat_mech["d2"] ],
                          [0, 0, 0, 1]
    ])

    M1_2_inv = np.dot(M1_2_inv_a, M1_2_inv_b)

    M2_3 = calculate_M(mechanism, 3, tol)

    M2_3_inv_a = np.array([
                          [1, 0, 0, -rat_mech["a3"] ],
                          [0, rat_mech["cos alpha3"], rat_mech["sin alpha3"], 0],
                          [0, -rat_mech["sin alpha3"], rat_mech["cos alpha3"], 0],
                          [0, 0, 0, 1]
    ])

    M2_3_inv_b = np.array([
                          [c3, s3, 0, 0],
                          [-s3, c3,0, 0],
                          [0, 0, 1, -rat_mech["d3"] ],
                          [0, 0, 0, 1]
    ])

    M2_3_inv = np.dot(M2_3_inv_a, M2_3_inv_b)


    # M0_3 =  np.dot(M0_1 , np.dot(M1_2, M2_3))

    # print((np.dot(np.dot(M2_3_inv, np.dot(M1_2_inv, M0_1_inv)), rational_pose(pose, tol))))
    res = M3_6  - np.dot(np.dot(M2_3_inv, np.dot(M1_2_inv, M0_1_inv)), rational_pose(pose, tol))

    # print(res)

    resPoly = convertToPoly(res)

    six1 = Poly(c1**2 + s1**2 -1, domain = 'QQ')
    six2 = Poly(c2**2 + s2**2 -1, domain = 'QQ')
    six3 = Poly(c3**2 + s3**2 -1, domain = 'QQ')
    six4 = Poly(c4**2 + s4**2 -1, domain = 'QQ')
    six5 = Poly(c5**2 + s5**2 -1, domain = 'QQ')
    six6 = Poly(c6**2 + s6**2 -1, domain = 'QQ')

    result =  [resPoly[0][0],resPoly[0][1], resPoly[0][2], resPoly[0][3], resPoly[1][0],resPoly[1][1],resPoly[1][2],resPoly[1][3],resPoly[2][0],resPoly[2][1], resPoly[2][2], resPoly[2][3], six1, six2, six3, six4, six5, six6 ]

    return result

    pass


def get_ikt_gb_lex(eqs):
    file = open("compute_gb.txt", "r")
    lines = file.readlines()
    lines[5] = "eqX := " + str([eq.as_expr() for eq in eqs]) + ";\n"  # put eqs into the 6th line of compute_gb.txt
    file = open("compute_gb.txt", "w")
    file.writelines(lines)
    file.close()
    os.system('maple compute_gb.txt')
    with open("gb.txt") as file:
        basis = file.readline()
    # print("test= "+str(sympify(basis.replace('^', '**')))  ) 
    basis = sympify(basis.replace('^', '**'))
    if basis == [1]:
        return [1]
    return [Poly(eq) for eq in basis]


def computeAtan(solutions):
    
    solution = {"theta6": [],"theta5": [],"theta4": [],"theta3": [],"theta2": [],"theta1": []}

    for i in range(0,len(solutions.get("s6"))):
        theta6 = solution["theta6"].append(atan2(solutions.get("s6")[i], solutions.get("c6")[i]) - mech.get("theta6 offset"))
        theta5 = solution["theta5"].append(atan2(solutions.get("s5")[i], solutions.get("c5")[i]) - mech.get("theta5 offset"))
        theta4 = solution["theta4"].append(atan2(solutions.get("s4")[i], solutions.get("c4")[i]) - mech.get("theta4 offset"))
        theta3 = solution["theta3"].append(atan2(solutions.get("s3")[i], solutions.get("c3")[i]) - mech.get("theta3 offset"))
        theta2 = solution["theta2"].append(atan2(solutions.get("s2")[i], solutions.get("c2")[i]) - mech.get("theta2 offset"))
        theta1 = solution["theta1"].append(atan2(solutions.get("s1")[i], solutions.get("c1")[i]) - mech.get("theta1 offset"))

    return solution    

def convertToList(solution):

    # print("runnningggg")
    result = []
    for r in range(0,len(solution[0])):
        result.append([])
    
    # print(result)
    # print(np.shape(solution)[0])
    for i in range(0,np.shape(solution)[0]):
        for j in range(0,len(solution[0])):
            # print("solution[j][i]= "+ str(solution[i][j]))
            result[j].append(solution[i][j])
    # print(result)
    return result           
    

def solve_ikt_gb_lex(gb):
    print("running solve ikt gb lex")

    solution = {"s6": [],"c6": [],"s5": [],"c5": [],"s4": [],"c4": [],"s3": [],"c3": [],"s2": [],"c2": [],"s1": [],"c1": []}

    # coefficients = np.array([0]*(degree(gb[0])+1), dtype=float)       
    coefficients = np.asarray(Poly.all_coeffs(gb[0]))
    sols = np.roots(coefficients)
    # print("sol= "+str(sols))

    for sol in sols:
        if (np.isreal(sol)):
            solution["s6"].append(float(sol))
    
    for i in range(0, len(solution.get("s6"))):
        for j in range(1,len(gb)):  

            coefficients = np.array([0]*(degree(gb[j])+1), dtype=float)
            gb_new = gb[j].subs({"s6":solution.get("s6")[i]})   
            coefficients = np.asarray(Poly.all_coeffs(gb_new))

            sol = np.roots(coefficients)
            # print("sol= "+str(sol))

            # solution["c1"].append(sol[0])
            solution[list(solution.keys())[j]].append(sol[0])
            # print("solution= " + str(solution))
        
    # solution = computeAtan(solution)
    solution = list(reversed(list(solution.values())))

    solution = convertToList(solution)

    return (solution)

    pass




# mech = {"theta1 offset": 0, "theta2 offset": -np.pi/2, "theta3 offset": 0, "theta4 offset": 0, "theta5 offset": np.pi/2, "theta6 offset": 0, "d1": 0.6, "d2": 0, "d3": 0, "d4": 0.64, "d5": 0, "d6": 0.2, "a1": 0.150, "a2": 0.614, "a3": 0.200, "a4": 0, "a5": 0.030, "a6": 0, "alpha1": -np.pi/2, "alpha2": 0, "alpha3": -np.pi/2, "alpha4": np.pi/2, "alpha5": -np.pi/2, "alpha6": 0}
# q = np.array([0.44649564413579207, -0.13032172899379538, 0.7871907450720678, 0.4049550809567836])
# t = np.array([0.5139524769370176, 0.9469829362775635, 1.3668413816672553])

# pose1 = {"q" : q, "t" : t}

# tol1 = 0.00001

# eqs1 = ikt_eqs(mech, pose1, tol1)


# # print((eqs1))
# gb = get_ikt_gb_lex(eqs1)



# # print(gb)

# print(solve_ikt_gb_lex(gb))



