import math, statistics, collections

def common_digit(x, y):
    s1 = set()
    s2 = set()

    while x != 0:
        s1.add(x%10)
        x = x//10

    while y != 0:
        s2.add(y%10)
        y = y//10

    return s1 & s2

def remove_digit(x, d):
    ans = 0
    p = 1
    done = False

    while x != 0:
        dig = x%10
        x = x//10
        if dig == d and not done:
            done = True
        else:
            ans += dig*p
            p *= 10

    return ans

if __name__ == '__main__':
    pos = set()

    for i in range(1, 100):
        for j in range(i+1, 100):
            cd = common_digit(i, j)
            if len(cd) != 0:
                dig = list(cd)[0]
                if dig == 0 and i%10 == 0 and j%10 == 0:
                    continue
                else:
                    tmp1 = remove_digit(i, dig)
                    tmp2 = remove_digit(j, dig)
                    if tmp1*j == tmp2*i:
                        pos.add((min(tmp1, tmp2), max(tmp1, tmp2)))

    pos.remove((0, 0))

    num_prod = 1
    deno_prod = 1
    for i in pos:
        num_prod *= i[0]
        deno_prod *= i[1]

    hcf = math.gcd(num_prod, deno_prod)

    print("Ans: ", deno_prod // hcf)

