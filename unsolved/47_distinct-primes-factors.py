#https://projecteuler.net/problem=47

import math

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

nums = []
i = 9000000
#for i in range(10000):
while True:
	i += 1
	if i%100000 == 0:
		print(f" {i}/{math.inf}", end="\r")
	if len(list(set(prime_factors(i)))) == 4:
		try:
			if nums[-1] == i-1:
				nums.append(i)
				#if len(nums) > 2:
				print(nums)
		except IndexError:
			if nums == []:
				nums.append(i)
		else:
			nums = []

		if len(nums) == 4:
			break

print(nums)