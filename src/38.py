import math, statistics, collections

"""
    Author: Koushik Sahu
    Created: 20 July 2021 Tue 11:41:15
"""

def is_pandigital(s: str) -> bool:
    if len(s) == 9:
        seen = [False]*10
        for i in s:
            seen[int(i)] = True
        ans = True
        for i in range(1, 10):
            ans = ans and seen[i]
        return ans
    return False

if __name__ == '__main__':
    ans = 0
    for i in range(10000):
        multiplier = 1
        s = ''

        while len(s)<9:
            s += str(i*multiplier)
            multiplier += 1

        is_valid = is_pandigital(s)
        if is_valid:
            ans = max(ans, int(s))
        
    print(ans)