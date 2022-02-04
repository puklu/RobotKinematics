

from sympy import *     
x, y, z, t = symbols('x y z t')   
mo = 'lex'
div1 = poly(x*y - 1)
div2 = poly(x**2 - y)

divs = [div1, div2]

f = poly(-x + y**2)


def poly_div(f, divs, mo):

        from sympy import poly
        from sympy.polys.polytools import LT, prem
        from sympy.core.symbol import symbols
        from sympy.abc import x, y, z, t
        x, y, z, t = symbols('x y z t')

        
        numOfDivs = len(divs)

        q = [[0] for k in range(0,numOfDivs)]

        r = 0

        p = f

        while p!= 0:
            i = 0
            divisionOccured = False
            while i<numOfDivs and divisionOccured == False:
                # print("i= " + str(i))
                print(rem(LT(p, order=mo),(LT(divs[i], order=mo))))
                print("prem="+str(prem(LT(p, order=mo), LT(divs[i], order=mo))))
                if(prem(LT(p, order=mo), LT(divs[i], order=mo))==0):
                    q[i].append(LT(p, order=mo)/LT(divs[i], order=mo))
                    print("LT(p)= " + str(LT(p, order=mo)))
                    print("LT(f)= " + str(LT(divs[i], order=mo)))
                    print("f= "+str(divs[i]))
                    p = p - divs[i]*(LT(p, order=mo)/LT(divs[i], order=mo))
                    print("p= "+str(p))
                    divisionOccured = True
                else:
                    i = i+1

            if divisionOccured == False:
                r = r + LT(p, order=mo)
                # print("r= "+str(r))
                p = p - LT(p, order=mo)
                # print("p= "+str(p))


        # print("q= " + str(q))
        return(q, r)


print(poly_div(f, divs, mo))