import math, statistics, collections

nxm = int(1e6+5)


def sieve():
    p = [-1]*nxm
    p[0] = -1
    p[1] = -1
    for i in range(2, int(math.sqrt(nxm))):
        if p[i] == -1:
            for j in range(i*i, nxm, i):
                p[j] = i

    pf = [0]*nxm
    for i in range(2, nxm):
        pfs = set()
        j = i
        while p[j]!=-1:
            pfs.add(p[j])
            j = j // p[j];
        pfs.add(j)
        pf[i] = len(pfs)

    return pf


if __name__ == '__main__':
    pf = sieve()

    for i in range(2, nxm-3):
        val = True
        for j in range(4):
            if pf[i+j] != 4:
                val = False
        if val:
            print(i)
            break

