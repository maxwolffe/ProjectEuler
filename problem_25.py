memo = dict()

def memoized_fib(term):
	if term == 1 or term == 2:
		return 1 
	if term in memo:
		return memo[term]
	memo[term] = memoized_fib(term - 1) + memoized_fib(term - 2)
	return memo[term]

def first_fib_of_length(length):
	fib_term = memoized_fib(1)
	term_number = 1
	while len(str(fib_term)) < length:
		fib_term = memoized_fib(term_number)
		term_number += 1
	print("Number: " + str(fib_term - 1))
	print("Term Number: " + str(term_number))
	return term_number - 1

