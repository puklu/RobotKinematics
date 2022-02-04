

from sympy import *     
x, y, z, t = symbols('x y z t')   
mo = 'grlex'
div1 = poly(x**3 - 1)
div2 = poly(x**2 + 1)
div3 = poly(x**3 + 4)
divs = [div1, div2, div3]

f = poly(3*x**2 - x**2 + 2*x)




def poly_div(f, divs, mo):

        from sympy import poly
        from sympy.polys.polytools import LT, prem
        from sympy.core.symbol import symbols
        from sympy.abc import x, y, z, t
        x, y, z, t = symbols('x y z t')


        # f = poly(f, order = mo)
        
        numOfDivs = len(divs)

        q = [[0] for k in range(0,numOfDivs)]

        r = 0

        p = f

        while p!= 0:
            i = 0
            divisionOccured = False
            while i<numOfDivs and divisionOccured == False:
                # print("i= " + str(i))
                if(prem(LT(p, order=mo), LT(divs[i]))==0):
                    q[i].append(LT(p)/LT(divs[i]))
                    # print("q[%i]= " %i+str(q[i]))
                    p = p - divs[i]*(LT(p)/LT(divs[i]))
                    # print("p= "+str(p))
                    divisionOccured = True
                else:
                    i = i+1

            if divisionOccured == False:
                r = r + LT(p)
                # print("r= "+str(r))
                p = p - LT(p)
                # print("p= "+str(p))


        # print("q= " + str(q))
        return(q, r)

print(poly_div(f, divs, mo))