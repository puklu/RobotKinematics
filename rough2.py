
from __future__ import division
from sympy import *

# from sympy.polys.groebnertools import s_poly     
x, y, z, t = symbols('x y z t')   
mo = 'lex'
div1 = Poly(x*y + x -y -1)
# print(monoms(div1))
div2 = Poly(x*z + x -z -1)
div4 = poly(x*y - x*z -y -z )
divs = [div1, div2, div4]

f = Poly(x*y + x*z**2 -y +z**2)


# print(f)




def poly_div(f, divs, mo):

        from sympy import poly
        from sympy.polys.polytools import LT, prem
        from sympy.core.symbol import symbols
        from sympy.abc import x, y, z, t
        x, y, z, t = symbols('x y z t')


        # f = poly(f, order = mo)
        
        numOfDivs = len(divs)

        q = [0 for k in range(0,numOfDivs)]

        print("q= "+ str(q))

        r = 0

        p = f

        while p!= 0:
            print('processing...')
            i = 0
            divisionOccured = False
            # print(divisionOccured)
            while i<numOfDivs and divisionOccured == False:
                print("i= " + str(i))
                print("remainder= "+ str(rem(LT(p, order=mo),(LT(divs[i], order=mo)))))
                if(rem(LT(p, order=mo),(LT(divs[i], order=mo)))==0): 
                    print("LT(p)= " + str(LT(p, order=mo)))
                    print("LT(f)= " + str(LT(divs[i], order=mo)))
                    print("f= "+str(divs[i]))
                    
                    # q[i].append(LT(p, order=mo)/LT(divs[i], order=mo))
                    # q[i].append(quo(LT(p, order=mo),(LT(divs[i], order=mo))))
                    print("quo= "+ str((quo(LT(p, order=mo),(LT(divs[i], order=mo))))))
                    q[i] = q[i] + (quo(LT(p, order=mo),(LT(divs[i], order=mo))))
                    print("q[%i]= " %i+str(q[i]))
                    print("p= "+str(p))
                    print("minus p term= "+str(divs[i]*(quo(LT(p, order=mo),(LT(divs[i], order=mo))))))
                    p = p - divs[i]*(quo(LT(p, order=mo),(LT(divs[i], order=mo))))
                    print("p= "+str(p))
                    divisionOccured = True
                else:
                    i = i+1

            if divisionOccured == False:
                r = r + LT(p, order=mo)
                print("r= "+str(r))
                p = p - LT(p, order=mo)
                print("p= "+str(p))


        # print("q= " + str(q))
        return(q, r)

print("result"+ str(poly_div(f, divs, mo)))