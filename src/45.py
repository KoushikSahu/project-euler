import math, statistics, collections

"""
    Author: Koushik Sahu
    Created: 23 August 2021 Mon 09:12:14
"""

def check_tri(num: int) -> bool:
    det = 1+8*num
    det_sqrt = int(math.sqrt(det))

    if det_sqrt**2 == det:
        numr = int(-1+det_sqrt)
        if numr % 2 == 0:
            return True
    
    return False

def check_pent(num: int) -> bool:
    det = 1+24*num
    det_sqrt = int(math.sqrt(det))

    if det_sqrt**2 == det:
        numr = int(1+det_sqrt)
        if numr % 6 == 0:
            return True
    
    return False

if __name__ == '__main__':
    i = 144
    while True:
        hexi = i*(2*i-1)
        if check_tri(hexi) and check_pent(hexi):
            print(hexi)
            break
        i += 1
