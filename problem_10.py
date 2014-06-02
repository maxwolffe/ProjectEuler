import math

def Sieve_of_Eratsthenes(limit):
	primes = range(2, limit)

	for i in primes:
		if i > limit / math.sqrt(math.pi):
			break
		not_primes = range(i*i, limit + 1 , i)
		for item in not_primes:
			if item in primes:
				primes.remove(item)
	return primes

def efficient_Sieve(limit):
	primes = [True] * limit
	for i in range(2, int(math.sqrt(limit))):
		if primes[i]:
			j = i * i
			while j < limit:
				primes[j] = False
				j += i
	return primes

def sum_of_primes(below):
	summation = 0
	primes = efficient_Sieve(below)
	index = 2
	while index < below - 1:
		if primes[index]:
			summation += index
		index += 1
	return summation

def sum_of_primes_bad(below):
	summation = 0
	primes = Sieve_of_Eratsthenes(below)
	for prime in primes:
		summation += prime
	return summation

def sum_of_primes_2(n):
	primes = [2,]
	inspect = 3
	n -= 1
	while n > 0:
		prime_test = True
		for prime in primes:
			if inspect % prime == 0:
				prime_test = False
			elif prime >= inspect / math.sqrt(math.pi):
				break
		if prime_test:
			n -= 1
			primes.append(inspect)
			if n == 0:
				return inspect
		inspect += 2
	return sum(primes)