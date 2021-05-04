def prime_checker(a):
    i=2
    while i<=int(a**0.5):
        if a%i==0:
            return 0
        i+=1
    return 1

def gre(a,b):
    if a>=b:
        return a
    else:
        return b
    
inp=int(input())

if prime_checker(inp):
    print(inp)
    exit(0)
    
high=0
i=2
if inp%i==0:
    high=i
    x=inp/i
    if prime_checker(x):
        high=gre(high,x)
i=3
while i<=int(inp**0.5):
    if inp%i==0:
        if prime_checker(i):
            high=gre(high,i)
        x=inp/i
        if prime_checker(x):
            high=gre(high,x)
    i+=2
    
print(int(high))