# print perfect number list
# ref. stackoverflow.com
#
# 2019.01.12 by jskim, neibc96@gmail.com

import math
from datetime import datetime
import sys
import platform

#global variables
ispause = 0

def is_perfect_number(n):
    sum = 0
    for x in range(1, n):
        if n % x == 0:
            sum += x
    return sum == n


argcnt = len(sys.argv)

print('usage : ex> python printperfectnum.py [ispause]\n')
if argcnt > 1:
    ispause = 1
	
print('environment_uname : ', end='')
print(platform.platform())
number = int(input("input value(>1) ex> 3212321223 : "))
print('-------------------------------------------------------')
print('start time : ' + datetime.utcnow().strftime('%Y/%m/%d_%H:%M:%S.%f'))
starta = datetime.now()

print('\nperfect number list from 2 to '+str(number))
for i in range(2, number):
    if is_perfect_number(i) == True:
        print(i)

startb = datetime.now()
print('\nend time   : ' + datetime.utcnow().strftime('%Y/%m/%d_%H:%M:%S.%f'))
print('-------------------------------------------------------')
print('time diff  : ', end='')
print(startb-starta)

if ispause > 0:
    input('enter key to end')
