#https://projecteuler.net/problem=127

import math
import time

def abcHit(a,b,c):
	if math.gcd(a,b) == math.gcd(a,c) == math.gcd(b,c) == 1:
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
m = 120000

start = time.time()
for a in range(m):
	print(f" {a}/{m}", end="\r")
	aStart = time.time()
	for b in range(a,m):
		if math.gcd(a,b) != 1:
			continue
		c = a+b
		if c >= m:
			break
		if abcHit(a,b,c):
			Cs.append(c)
			ABCs.append((a,b,c))
	print(f"took {time.time() - aStart} seconds")

print(f"Whole operation took {time.time() - start} seconds")
print(sum(Cs))
print(ABCs)