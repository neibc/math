# check whether the input number is a prime number or not
# even number skipped and test it from 3 to sqrt(n)
# ref. stackoverflow.com
#
# 2019.01.12 by jskim, neibc96@gmail.com

import math
from datetime import datetime
import sys
import platform

#global variables
ispause = 0

def is_prime(n):
    if n % 2 == 0 and n > 2: 
        return False
    return all(n % i for i in range(3, int(math.sqrt(n)) + 1, 2))
        
def divisorGenerator(n):
    large_divisors = []
    for i in range(1, int(math.sqrt(n) + 1)):
        if n % i == 0:
            yield i
            if i*i != n:
                large_divisors.append(n / i)
    for divisor in reversed(large_divisors):
        yield divisor

argcnt = len(sys.argv)

print('usage : ex> python checkprimenum.py [ispause]\n')
if argcnt > 1:
    ispause = 1
        
print('environment_uname : ', end='')
print(platform.platform())
number = 1
while number > 0:
    number = int(input("input value(>1, 0 to end) ex> 2020123212321223 : "))
    print('-------------------------------------------------------')
    print('start time : ' + datetime.utcnow().strftime('%Y/%m/%d_%H:%M:%S.%f'))
    starta = datetime.now()

    print('\nresult     : ', end='')
    print(is_prime(number))

    print('\nresult     : ', end='')
    print(list(divisorGenerator(number)))

    startb = datetime.now()
    print('\nend time   : ' + datetime.utcnow().strftime('%Y/%m/%d_%H:%M:%S.%f'))
    print('-------------------------------------------------------')
    print('time diff  : ', end='')
    print(startb-starta)

if ispause > 0:
    input('enter key to end')
