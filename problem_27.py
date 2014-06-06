import math

def new_quadratic(a, b):
	return lambda x: x ** 2 + a * x + b

def efficient_Sieve(limit):
	primes = [True] * limit
	for i in range(2, int(math.sqrt(limit))):
		if primes[i]:
			j = i * i
			while j < limit:
				primes[j] = False
				j += i
	index = 0
	list_of_primes = []
	while index < limit: 
		if primes[index]:
			list_of_primes.append(index)
		index += 1
	return list_of_primes

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

primes_to_10000 = Sieve_of_Eratsthenes(10000)

def is_prime(number):
	if number in primes_to_10000:
		return True
	for poss in primes_to_10000:
		if number % poss == 0:
			return False
	return True

def most_primes(a_limit, b_limit):
	most_primes = 0
	highest_a, test_a = -a_limit, -a_limit
	highest_b, test_b = 0, 0

	while test_a < a_limit:
		print("testing: " + str(test_a))
		print("highest so far: " + str((test_a, test_b)))
		print("Number of Primes = " + str(most_primes))
		for test_b in range(41, b_limit + 1):
			test_in = 1
			num_primes = 0
			quad_test = new_quadratic(test_a, test_b)
			while test_in <= b_limit and is_prime(quad_test(test_in)):
				test_in += 1
				num_primes += 1
			if num_primes > most_primes:
				highest_a = test_a
				highest_b = test_b
				most_primes = num_primes
		test_a += 1

	return highest_a, highest_b

#best = most_primes(1000, 1000)


