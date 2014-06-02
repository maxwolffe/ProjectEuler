def Collatz(number):
	count = 1
	while number != 1:
		count += 1
		if number % 2 == 0:
			number = number / 2
		else:
			number = 3 * number + 1
	return count

#finds the number with the longest collatz chain between 1 and num
def longest_under(num):
	longest_chain = 0
	longest_number = 0
	for i in range(1, num):
		chain = Collatz(i)
		if chain > longest_chain:
			longest_chain = chain
			longest_number = i
	return longest_number
