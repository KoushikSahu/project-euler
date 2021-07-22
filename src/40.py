import math, statistics, collections

"""
    Author: Koushik Sahu
    Created: 22 July 2021 Thu 22:32:58
"""

if __name__ == '__main__':
    s = ''
    curr = 1

    while len(s) <= 1_000_000:
        s += str(curr)
        curr += 1

    ans = int(s[0]) * int(s[9]) * int(s[99]) * int(s[999]) * int(s[9999]) * int(s[99999])
    print(f'ans: {ans}')
        