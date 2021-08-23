import math, statistics, collections
from typing import List

"""
    Author: Koushik Sahu
    Created: 23 August 2021 Mon 10:23:06
"""

nxm = int(1e7+5)

def sieve() -> List[bool]:
    global nxm
    primes = [True]*nxm
    primes[0] = primes[1] = False

    for i in range(2, int(math.sqrt(nxm))):
        if primes[i]:
            for j in range(i*i, nxm, i):
                primes[j] = False

    return primes

def valid(num: int, primes: List[bool]) -> bool:
    for i in range(0, num):
        if primes[i]:
            rem = num - i
            sqrd = rem // 2
            sr = int(math.sqrt(sqrd))
            if rem%2 == 0 and sr*sr == sqrd:
                return True
    return False

if __name__ == '__main__':
    primes = sieve()
    i = 9
    while True:
        if not primes[i] and not valid(i, primes):
            print(i)
            break
        i += 2
