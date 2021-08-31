import math, statistics, collections


if __name__ == '__main__':
    MOD = int(1e10)

    rem = 0
    for i in range(1, 1001):
        rem += pow(i, i, MOD)
        rem %= MOD
    print(rem)

