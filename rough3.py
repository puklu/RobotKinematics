from fractions import Fraction as frac
from math import atan2, floor
import math
import numpy as np
import scipy
from sympy import degree
from sympy import Matrix
from sympy import *
from sympy.core.symbol import symbols
import os
from sympy.core.sympify import sympify
from sympy.polys.polytools import Poly
from scipy.linalg import companion



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
    return [Poly(eq) for eq in sympify(basis.replace('^', '**'))]


#equations being solved
c1, s6 = symbols('c1, s6')
# eqs = [Poly(s6**2 + c1 + 1), Poly(s6 + c1 + 1)]
eqs = [Poly(s6**3 - 2*s6), Poly(s6**2 - 2*c1 + s6)]

print(eqs)
gb = get_ikt_gb_lex(eqs)

print("gb= "+str(gb))

# solution = np.array([[0]*(degree(gb[0])), [0]*(degree(gb[0]))])

#empty dictionary to store the solutions
# solution = {"s6": [], "c1": []}
solution = {"s6": [],"c6": [],"s5": [],"c5": [],"s4": [],"c4": [],"s3": [],"c3": [],"s2": [],"c2": [],"s1": [],"c1": []}


coefficients = np.array([0]*(degree(gb[0])+1), dtype=float)       
coefficients = np.asarray(Poly.all_coeffs(gb[0]))
sol = np.roots(coefficients)

for ele in enumerate(sol):
    if (np.isreal(ele[1])):
        solution[list(solution.keys())[0]].append(ele[1])
    
    



# print(solution)

for i in range(0, len(solution.get("s6"))):
    for j in range(1,len(gb)):  

        coefficients = np.array([0]*(degree(gb[j])+1), dtype=float)
        #gb_new = [Poly(0, s6, c1)]
        gb_new = gb[j].subs({"s6":solution.get("s6")[i]})
    
        coefficients = np.asarray(Poly.all_coeffs(gb_new))

        sol = np.roots(coefficients)
        # print("sol= "+str(sol))

        # solution["c1"].append(sol[0])
        solution[list(solution.keys())[j]].append(sol[0])
    
        
print("solution= "+str(solution))

    


    
################3
# for i in range(1,len(gb)):
#     coefficients = np.array([0]*(degree(gb[i])+1), dtype=float)
    
#     # print("coeffsBefore= "+ str(coefficients))
#     # print("gb["+str(i)+"]= "+str(gb[i]))

#     # gb[i] = gb[i].subs({s6:solution.get("s6")[j]})
    
#     coefficients = np.asarray(Poly.all_coeffs(gb[i]))

#     sol = np.roots(coefficients)

#     for ele in enumerate(sol):
#         # print("ele= "+str(ele[1]))
#         if (np.isreal(ele[1])):
#            solution[list(solution.keys())[i]].append(ele[1])
    
    
#     print("sol= "+str(sol))
#     print("solution= "+str(solution))

#     for j in range(0, len(solution[list(solution.keys())[i]])):

#         # print("len(solution['s6'])="+str(len(solution["s6"])))
#         # gb_new = [Poly(0, s6, c1) for k in range(0,len(solution["s6"])+1)]
#         gb_new = [Poly(0, s6, c1)]


#         print("i="+str(i))
#         print("j="+str(j))
#         print("solution.get("+list(solution.keys())[i]+")["+str(j)+"]= "+ str(solution.get(list(solution.keys())[i])[j]))
    

#         # gb_new[j] = gb[i+1].subs({s6:solution.get("s6")[0][j]})
#         for k in range(i+1,len(gb)):
#             print("k="+str(k))
#             gb_new = gb[k].subs({list(solution.keys())[i]:solution.get(list(solution.keys())[i])[j]})
#             print("gb_new=" +str(gb_new))
#             coefficients = np.asarray(Poly.all_coeffs(gb_new))
#             sol = np.roots(coefficients)
#             print("sol= "+str(sol))
            
#             for ele in enumerate(sol):
#             # print("ele= "+str(ele[1]))
#                 if (np.isreal(ele[1])):
#                     solution[list(solution.keys())[i+1]].append(ele[1]) 
#                     print("solution= "+str(solution))

        
