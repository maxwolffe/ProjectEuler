
not_primes = []

def is_prime(number):
	if number in primes:
		return True
	for factor in range(2, number):
		if number % factor == 0:
			not_primes.append(number)
			return False
	primes.append(number)
	return True

def Sieve_of_Eratsthenes(limit):
	primes = range(2, limit)

	for i in primes:
		not_primes = range(i*i, limit + 1 , i)
		for item in not_primes:
			if item in primes:
				primes.remove(item)
	return primes

def try_by_divide(product):
	primes = Sieve_of_Eratsthenes(10000)
	index = -1
	divider = 2
	while divider < product / 2:
		if index < len(primes):
			index += 1
			divider = primes[index]
		else:
			divider += 1
		print(product)
		if product % divider == 0:
			product = product / divider
			index = -1
	return product

def largest_p_factor(product):
	primes = Sieve_of_Eratsthenes(product / 2)
	largest_prime = 0
	for prime in primes:
		print("currently considering: " + prime)
		if product % prime == 0:
			if prime > largest_prime:
				largest_prime = prime
	return largest_prime