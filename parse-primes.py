with open("primes10000.txt", 'r') as fp:
	primes_list = fp.readlines()

primes = []

for row in primes_list:
	if ':' in row:
		primes += row.split(":")[1].split()

#primes = list(map(int, primes)) # cast strings to ints

with open("primes.txt", 'w') as fp:
	for prime in primes:
		fp.write(prime + '\n')
	print(f"Saved {len(primes)} primes to 'primes.txt'")