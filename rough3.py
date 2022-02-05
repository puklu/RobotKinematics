from fractions import Fraction as frac
from math import atan2, floor
import math
import numpy as np
from sympy.core.symbol import symbols
import os
from sympy.core.sympify import sympify
from sympy.polys.polytools import Poly



# def get_ikt_gb_lex(eqs):
#     file = open("compute_gb.txt", "r")
#     lines = file.readlines()
#     lines[5] = "eqX := " + str([eq.as_expr() for eq in eqs]) + ";\n"  # put eqs into the 6th line of compute_gb.txt
#     file = open("compute_gb.txt", "w")
#     file.writelines(lines)
#     file.close()
#     os.system('maple compute_gb.txt')
#     with open("gb.txt") as file:
#         basis = file.readline()
#     return [Poly(eq) for eq in sympify(basis.replace('^', '**'))]




# c1, s6 = symbols('c1, s6')
# eqs = [Poly(q6**2 + p1 + 1), Poly(q6 + p1 + 1)]
# gb = get_ikt_gb_lex(eqs)
# print(gb)

# gb = [Poly(1.0*s6**2 - 1.0*s6, s6, domain='RR'), Poly(1.0*s6 + 1.0*c1 + 1.0, s6, c1, domain='RR')]

li = [1, 2, 3, 4]
numpyArr = np.array(li)
print((np.transpose(numpyArr)))
