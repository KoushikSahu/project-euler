import math, collections, itertools

"""
    Author: Koushik Sahu
    Created: 13 Sep 2020 14:03:34
"""

pandigital = "123456789"

if __name__ == '__main__':
    ans = 0
    ans_set = set()

    perms = itertools.permutations(pandigital)
    for perm in perms:
        for i in range(1, 9):
            for j in range(i+2, 8):
                a = int(''.join(perm[0:i]))
                b = int(''.join(perm[i:j]))
                c = int(''.join(perm[j:]))

                if a*b==c:
                    print(str(a)+' '+str(b)+' '+str(c))
                    if c not in ans_set:
                        ans_set.add(c)
                        ans += c
    
    print(ans)
