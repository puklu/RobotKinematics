from fractions import Fraction as frac
from math import atan2, floor
import numpy as np
from sympy import degree
from sympy import *
from sympy.core.symbol import symbols
import os
from sympy.core.sympify import sympify
from sympy.polys.polytools import Poly


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
eqs = [Poly(s6**3 - 2*s6*c1), Poly(s6**2 - 2*c1**2 + s6)]

print(eqs)
gb = get_ikt_gb_lex(eqs)

print("gb= "+str(gb))

#empty dictionary to store the solutions
solution = {"s6": [],"c6": [],"s5": [],"c5": [],"s4": [],"c4": [],"s3": [],"c3": [],"s2": [],"c2": [],"s1": [],"c1": []}



def findRoots(eq):
    #an empty array to contains the coefficients of a Poly
    coefficients = np.array([0]*(degree(eq)+1), dtype=float)   
    # storing the coefficeints of the Poly 
    coefficients = np.asarray(Poly.all_coeffs(eq))
    #the rooots of the Poly
    myRoots = np.roots(coefficients)
    
    return myRoots

def substitute(eq, value, variable):
    eq_new = [Poly(0, s6, c1)]
    
    # for i in range(0,len(values)):
    if (np.isreal(value)):
        print(value)
        print("eq="+ str(eq))
        eq_new = eq.subs(variable, value)
        print("eq_new="+str(eq_new))

    return eq_new

def saveToSolution(sol, variable):
    for ele in enumerate(sol):
        # print("ele= "+str(ele[1]))
        if (np.isreal(ele[1])):
           solution[variable].append(ele[1])


gb_new= gb

sol = findRoots(gb_new[0])
saveToSolution(sol, "s6")



for i in range(1,len(gb)):
    print(gb_new[i])

    
    
    # for j in range(0,len(sol)):
    newEq = substitute(gb_new[i], solution.get("s6")[i], "s6")
    print("newEq= "+str(newEq))
    # gb_new[i+1] = newEq

    sol = findRoots(newEq)
    print("sol= "+str((sol)))

    saveToSolution(sol, "s6")
        
