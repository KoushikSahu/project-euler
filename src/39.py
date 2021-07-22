import time, math, statistics, collections

"""
    Author: Koushik Sahu
    Created: 22 July 2021 Thu 22:08:53
"""

if __name__ == '__main__':
    start_time = time.time()
    prmtr = collections.defaultdict(lambda: 0)

    for hyp in range(5, 1001):
        for bs in range(1, hyp):
            prpd_sqrd = hyp**2 - bs**2
            prpd = int(math.sqrt(prpd_sqrd))
            if prpd**2 == prpd_sqrd and bs<=prpd:
                peri = bs + prpd + hyp
                prmtr[peri] = prmtr[peri] + 1

    ans_frq = 0
    ans = -1
    for key in prmtr:
        if key <= 1000 and prmtr[key] > ans_frq:
            ans_frq = prmtr[key]
            ans = key

    print(f'ans: {ans} ans_frq: {ans_frq}')
    print(f'Exection time: {time.time() - start_time} seconds')
