# check whether the result of prime_number * next_prime_number + 2 is prime number or not
# ref. stackoverflow.com
#
# pip3 install sympy!
#
# 2022.07.17 by neibc96@gmail.com & GD

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

#startnum = 3 

while maxnum > 0:
    pnum1 = 2
    pnum2 = 3
    noftrue = 0
    noffalse = 0

    maxnum = int(input("input max target investigation value(>1, 0 to end) ex> 2020123212321223 : "))
    print('-------------------------------------------------------')
    print('start time : ' + datetime.utcnow().strftime('%Y/%m/%d_%H:%M:%S.%f'))
    starta = datetime.now()

    for i in range(3, maxnum):
#        if is_prime(i) == True:
        if sympy.isprime(i) == True:
            pnum2 = i
            
            tval = pnum1 * pnum2 + 2
#            pcheckresult = is_prime(tval)
            pcheckresult = sympy.isprime(tval)
            if pcheckresult == True:
                noftrue=noftrue+1
            else: 
                noffalse=noffalse+1
            print('%d * %d + 2 = %d and %s' %(pnum1, pnum2, tval, pcheckresult))
            pnum1 = pnum2
    startb = datetime.now()
    print('\nend time   : ' + datetime.utcnow().strftime('%Y/%m/%d_%H:%M:%S.%f'))
    print('-------------------------------------------------------')
    print('time diff  : ', end='')
    print(startb-starta)
    print('max number : %d' %maxnum)
    print('number of total prime numbers within maxnum : %d' %(noftrue+noffalse))
    print('ratio of prime numbers within maxnum : %f ' %((noftrue+noffalse)/maxnum))
    print('\nnumber of true samples : %d' %noftrue)
    print('number of false samples : %d' %noffalse)
    print('ratio of true samples : %f' %(noftrue/(noftrue+noffalse)))

if ispause > 0:
    input('enter key to end')
