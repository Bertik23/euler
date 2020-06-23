#https://projecteuler.net/problem=127

import math

def abcHit(a,b,c):
    if math.gcd(a,b) == math.gcd(a,c) == math.gcd(b,c) == 1:
        if a < b:
            if a+b == c:
                if rad(a*b*c) < c:
                    return True
    return False

#list(set(prime_factors(504)))

def prime_factors(n):
    i = 2
    factors = []
    while i * i <= n:
        if n % i:
            i += 1
        else:
            n //= i
            factors.append(i)
    if n > 1:
        factors.append(n)
    return factors

def rad(number: int) -> int:
    factors = list(set(prime_factors(number)))
    r = 1
    for i in factors:
        r*=i
    return r

#print(abcHit(5,27,32))

Cs = []
ABCs = []
m = 100

for a in range(m):
    print(f" {a}/{m}", end="\r")
    for b in range(a,m):
        for c in range(b,m):
            if a+b == c:
                if abcHit(a,b,c):
                    Cs.append(c)
                    ABCs.append((a,b,c))

print(sum(Cs))
print(ABCs)