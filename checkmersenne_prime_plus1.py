# check whether the result of 2^n+1 is prime number or not when n is a prime number
# ref. stackoverflow.com
#
# pip3 install sympy!
#
# 2022.09.15 by neibc96@gmail.com & GD

import math
from datetime import datetime
import sys
import platform
import sympy

#global variables
ispause = 0

def is_prime(n):
    if n % 2 == 0 and n > 2: 
        return False
    return all(n % i for i in range(3, int(math.sqrt(n)) + 1, 2))
        
print('environment_uname : ', end='')
print(platform.platform())

maxnum = 1000
maxsquarenum = 10000

#startnum = 3 

while maxnum > 0:
    pnum1 = 0
    noftrue = 0
    noffalse = 0

    maxnum = int(input("input max target investigation value(>1, 0 to end) ex> 2020123212321223 : "))
    print('-------------------------------------------------------')
    print('start time : ' + datetime.utcnow().strftime('%Y/%m/%d_%H:%M:%S.%f'))
    starta = datetime.now()

    for i in range(2, maxsquarenum):
         if sympy.isprime(i) == True:
            tval = pow(2, i) + 1
            if tval > maxnum:
               break
            pcheckresult = sympy.isprime(tval)
            if pcheckresult == True:
               noftrue=noftrue+1
            else: 
               noffalse=noffalse+1
            print('2^%d + 1 = %d : %s' %(i, tval, pcheckresult))

    startb = datetime.now()
    print('\nend time   : ' + datetime.utcnow().strftime('%Y/%m/%d_%H:%M:%S.%f'))
    print('-------------------------------------------------------')
    print('time diff  : ', end='')
    print(startb-starta)
    print('max number : %d' %maxnum)
    print('\nnumber of true samples : %d' %noftrue)
    print('number of false samples : %d' %noffalse)
    print('ratio of true samples : %f' %(noftrue/(noftrue+noffalse)))

if ispause > 0:
    input('enter key to end')
