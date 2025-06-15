# check whether the input number is a prime number or not
# even number skipped and test it from 3 to sqrt(n)
# ref. stackoverflow.com
#
# 2019.01.12 by jskim, neibc96@gmail.com

import math
from datetime import datetime
import sys
import platform


def is_prime(n):
    """Return True if *n* is a prime number."""
    if n % 2 == 0 and n > 2:
        return False
    return all(n % i for i in range(3, int(math.sqrt(n)) + 1, 2))

def main():
    """Run a simple command line interface for checking primality."""
    argcnt = len(sys.argv)
    ispause = 0

    print('usage : ex> python checkprimenum.py [ispause]\n')
    if argcnt > 1:
        ispause = 1

    print('environment_uname : ', end='')
    print(platform.platform())
    number = int(input("input value(>1) ex> 2020123212321223 : "))
    print('-------------------------------------------------------')
    print('start time : ' + datetime.utcnow().strftime('%Y/%m/%d_%H:%M:%S.%f'))
    starta = datetime.now()

    print('\nresult     : ', end='')
    print(is_prime(number))

    startb = datetime.now()
    print('\nend time   : ' + datetime.utcnow().strftime('%Y/%m/%d_%H:%M:%S.%f'))
    print('-------------------------------------------------------')
    print('time diff  : ', end='')
    print(startb-starta)

    if ispause > 0:
        input('enter key to end')


if __name__ == '__main__':
    main()