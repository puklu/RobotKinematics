#### Funtion to perform division of polynomials ####


# Input/Output specifications for poly_div:

# f : Poly object
# divs : list of Poly objects
# mo : String. It can take the following values (according to SymPy documentation):
#     “lex” - lexicographic order
#     “grlex” - graded lexicographic order
#     “grevlex” - graded reversed lexicographic order
# Return value : dictionary with 2 keys “q” and “r”, whose values are the list of 
#                quotient polynomials (list of Poly objects) and the remainder of 
#                the division (Poly object), respectively. 


def poly_div(f, divs, mo):

        from sympy import Poly
        from sympy import rem, ZZ, QQ
        from sympy import quo
        from sympy import LT
        from sympy.core.symbol import symbols
        from sympy.abc import x, y, z, t
        x, y, z, t = symbols('x y z t')

        numOfDivs = len(divs)

        my_quotient = [Poly(0,x,y,z) for k in range(0,numOfDivs)]
        
        # print("q= "+ str(my_quotient))

        my_remainder = Poly(0,x,y,z)
        p = f

        while p!= 0:
            # print('processing...')
            i = 0
            divisionOccured = False
            while i<numOfDivs and divisionOccured == False:
                # print("i= " + str(i))
                # print("remainder= "+ str(rem(LT(p, order=mo),(LT(divs[i], order=mo)))))
                if(rem(LT(p, order=mo),(LT(divs[i], order=mo)))==0): 
                    
                    # print("LT(p)= " + str(LT(p, order=mo)))
                    # print("LT(f)= " + str(LT(divs[i], order=mo)))
                    # print("f= "+str(divs[i]))
                    # print("quo= "+ str((quo(LT(p, order=mo),(LT(divs[i], order=mo))))))
                    
                    my_quotient[i] = my_quotient[i] + (quo(LT(p, order=mo),(LT(divs[i], order=mo))))
                    
                    # print("q[%i]= " %i+str(my_quotient[i]))
                    # print("p= "+str(p))
                    # print("minus p term= "+str(divs[i]*(quo(LT(p, order=mo),(LT(divs[i], order=mo))))))
                    
                    p = p - divs[i]*(quo(LT(p, order=mo),(LT(divs[i], order=mo))))
                    
                    # print("p= "+str(p))
                    
                    divisionOccured = True
                else:
                    i = i+1

            if divisionOccured == False:
                my_remainder = my_remainder + LT(p, order=mo)
                # print("r= "+str(my_remainder))
                p = p - LT(p, order=mo)
                # print("p= "+str(p))
                
        

        result = dict(q = my_quotient, r= my_remainder)

        # print(result)

        return(result)

