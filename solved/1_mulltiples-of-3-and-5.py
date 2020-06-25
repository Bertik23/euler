#https://projecteuler.net/problem=1

multiples = []
for i in range(200):
    if i < 1000:
        multiples.append(5*i)

for i in range(334):
    if i < 1000:
        multiples.append(3*i)

print(multiples)

print(sum(list(set(multiples))))