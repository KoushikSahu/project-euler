import math, statistics, collections, time

"""
    Author: Koushik Sahu
    Created: 21 August 2021 Sat 11:45:22
"""

def binary_search(a, val):
    l = 0
    h = len(a)-1
    
    while l<=h:
        mid = l + (h-l)//2
        if a[mid] == val:
            return True
        elif a[mid] > val:
            h = mid-1
        else:
            l = mid+1

    return False

if __name__ == '__main__':
    t_start = time.time()
    n = 10000
    pent = [int((i*(3*i-1))/2) for i in range(n*10)]
    ans = (-1, -1)
    mn = int(1e9+5)

    for i in range(1, n):
        for j in range(i+1, n):
            a = pent[i]
            b = pent[j]

            if binary_search(pent, a+b) and binary_search(pent, abs(a-b)):
                if b-a < mn:
                    ans = (a, b)
                    mn = b-a

    print(f'ans: {ans} min_diff: {mn}')
    t_end = time.time()
    print(f'Time taken: {t_end-t_start}')
