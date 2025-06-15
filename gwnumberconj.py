import math
from datetime import datetime
import sys
import platform

def is_prime(n):
    if n <= 1:
        return False
    if n % 2 == 0 and n > 2:
        return False
    return all(n % i for i in range(3, int(math.sqrt(n)) + 1, 2))


prevprime=2

for i in range(3,10000):
    if is_prime(i):
        print(prevprime, end='')
        print(' * ', end='')
        print(i, end='')
        print(' + 2 = ', end='')
        calval = prevprime*i + 2
        prevprime = i
        print(calval, end='')
        print(' : ', end='')
        print(is_prime(calval))

