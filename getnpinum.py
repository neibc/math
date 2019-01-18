# get the value of Pi to n number of decimal places
# even number skipped and test it from 3 to sqrt(n)
# ref. w3resource.com
#
# 2019.01.12 by jskim, neibc96@gmail.com

import math
from datetime import datetime
import sys
import platform

#global variables
ispause = 0

#Prints out the digits of PI
#until it reaches the given limit
def calcPi(limit):  # Generator function
    q, r, t, k, n, l = 1, 0, 1, 1, 3, 3

    decimal = limit
    counter = 0

    while counter != decimal + 1:
        if 4 * q + r - t < n * t:
            # yield digit
            yield n
            # insert period after first digit
            if counter == 0:
                yield '.'
            # end
            if decimal == counter:
                print('')
                break
            counter += 1
            nr = 10 * (r - n * t)
            n = ((10 * (3 * q + r)) // t) - 10 * n
            q *= 10
            r = nr
        else:
            nr = (2 * q + r) * l
            nn = (q * (7 * k) + 2 + (r * l)) // (t * l)
            q *= k
            t *= l
            l += 2
            k += 1
            n = nn
            r = nr

def CalculatePi(roundVal):
    somepi = round(math.pi,roundVal);
    pi = str(somepi)
    someList = list(pi)
    return somepi;

argcnt = len(sys.argv)

print('usage : ex> python getnpinum.py [ispause]\n')
if argcnt > 1:
    ispause = 1
	
print('environment_uname : ', end='')
print(platform.platform())
number = int(input("input value(>1) ex> 1000 : "))
print('-------------------------------------------------------')
print('start time : ' + datetime.utcnow().strftime('%Y/%m/%d_%H:%M:%S.%f'))
starta = datetime.now()

print('\nresult     : ', end='')

pi_digits = calcPi(int(number))
i=0

for d in pi_digits:
    print(d, end='')
#    i += 1
#    if i == 80:
#        print('')
#        i=0

#try:
#    roundint = int(number)
#    print(CalculatePi(roundint))
#except:
#    print('integer value is needed')

startb = datetime.now()
print('\nend time   : ' + datetime.utcnow().strftime('%Y/%m/%d_%H:%M:%S.%f'))
print('-------------------------------------------------------')
print('time diff  : ', end='')
print(startb-starta)

if ispause > 0:
    input('enter key to end')
