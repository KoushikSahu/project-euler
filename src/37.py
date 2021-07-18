import math, statistics, collections, typing

"""
    Author: Koushik Sahu
    Created: 18 July 2021 Sun 21:59:03
"""

nxm = 1000005

def sieve() -> typing.List[bool]:
    global nxm
    prime = [True] * nxm
    prime[0] = prime[1] = False

    for i in range(2, int(math.sqrt(nxm))+1):
        if prime[i] == True:
            for j in range(i*i, nxm, i):
                prime[j] = False

    return prime

def remove_left(n: int) -> int:
    if n // 10 == 0:
        return 0
    return int(str(n)[1:])

if __name__ == '__main__':
    prime = sieve()

    left_dp = [False] * nxm
    right_dp = [False] * nxm
    dp = [False] * nxm
    for i in range(0, 10):
        left_dp[i] = prime[i]
        right_dp[i] = prime[i]
        dp[i] = prime[i]

    cnt = 0
    ans_list = list()
    for i in range(10, nxm):
        left_dp[i] = prime[i] and left_dp[remove_left(i)]
        right_dp[i] = prime[i] and right_dp[i//10]
        dp[i] = left_dp[i] and right_dp[i]
        if dp[i] == True:
            cnt += 1
            ans_list.append(i)

    print(cnt)
    print(ans_list)
    print(sum(ans_list))
