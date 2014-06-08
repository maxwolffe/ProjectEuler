#finds the number of distinct terms in the sequence of A**b from 2 to a_limt and 2 to _blimt
def unique_exponents(a_limit, b_limit):
	term_set = set()
	a = 2
	while a <= a_limit:
		b = 2
		while b <= b_limit:
			term_set.add(a ** b)
			b += 1
		a += 1
	return len(term_set)
