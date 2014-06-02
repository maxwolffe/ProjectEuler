import math 

def Sieve_of_Eratsthenes(limit):
	primes = range(2, limit)

	for i in primes:
		not_primes = range(i*i, limit + 1 , i)
		for item in not_primes:
			if item in primes:
				primes.remove(item)
	return primes

def nth_prime_with_Eratsthenes(n):
	primes = Sieve_of_Eratsthenes(200000)
	return primes[n]

def nth_prime_normal(n):
	primes = [2,]
	inspect = 3
	n -= 1
	while n > 0:
		prime_test = True
		for prime in primes:
			if inspect % prime == 0:
				prime_test = False
			elif prime >= inspect / math.sqrt(2):
				break
		if prime_test:
			n -= 1
			primes.append(inspect)
			if n == 0:
				return inspect
		inspect += 2
	



