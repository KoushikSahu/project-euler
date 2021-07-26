import math, statistics, collections
from itertools import permutations

"""
    Author: Koushik Sahu
    Created: 26 July 2021 Mon 11:53:41
"""

def valid(n: str) -> int:
    sz = len(n)
    i = 1
    primes = [2, 3, 5, 7, 11, 13, 17]
    ptr = 0

    while i+2 < sz:
        curr = int(n[i:i+3])
        if not curr%primes[ptr] == 0:
            return -1
        i += 1
        ptr += 1

    return int(n)


if __name__ == '__main__':
    pandigit = '0123456789'

    ans = 0
    for perm in permutations(pandigit):
        num = "".join(perm)
        if int(num) > 1_000_000_000:
            if (val := valid(num)) != -1:
                ans += val

    print(f'ans: {ans}')
