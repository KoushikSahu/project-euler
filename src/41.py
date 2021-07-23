import math, statistics, collections
from itertools import permutations

"""
    Author: Koushik Sahu
    Created: 23 July 2021 Fri 22:10:37
"""

def is_prime(n: str) -> bool:
    n = int(n)

    for i in range(2, int(math.ceil(math.sqrt(n)))):
        if n%i == 0:
            return False
    
    return True


if __name__ == '__main__':
    curr = ''
    ans = 0

    for val in range(1, 10):
        curr += str(val)
        for perm in list(permutations(curr)):
            val = "".join(perm)
            if is_prime(val):
                ans = max(ans, int(val))

    print(f'ans: {ans}')
