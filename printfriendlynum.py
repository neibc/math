# print friendly number list
# ref. stackoverflow.com
#
# 2019.01.12 by jskim, neibc96@gmail.com

import math
from datetime import datetime
import sys
import platform

#global variables
ispause = 0

def sum_factors(n):  
     result = []
     for i in range(1, int(n**0.5) + 1):
         if n % i == 0:
             result.extend([i, n//i])
     return sum(set(result)-set([n]))

def amicable_pair(number):
    result = []
    for x in range(1,number+1):
        y = sum_factors(x)
        if sum_factors(y) == x and x != y:
            result.append(tuple(sorted((x,y))))
    return set(result)

argcnt = len(sys.argv)

print('usage : ex> python printfriendlynum.py [ispause]\n')
if argcnt > 1:
    ispause = 1
	
print('environment_uname : ', end='')
print(platform.platform())
number = int(input("input value(>1) ex> 3212321223 : "))
print('-------------------------------------------------------')
print('start time : ' + datetime.utcnow().strftime('%Y/%m/%d_%H:%M:%S.%f'))
starta = datetime.now()

print('\nfriendly number list from 2 to '+str(number))
print(amicable_pair(number))

startb = datetime.now()
print('\nend time   : ' + datetime.utcnow().strftime('%Y/%m/%d_%H:%M:%S.%f'))
print('-------------------------------------------------------')
print('time diff  : ', end='')
print(startb-starta)

if ispause > 0:
    input('enter key to end')
