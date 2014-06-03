def sum_of_divisors(number):
	total = 0
	for divisor in range(1, (number / 2) + 1):
		if number % divisor == 0:
			total += divisor
	return total

#returns the summ of all amicable numbers under the number 'under'
def sum_of_amicable(under):
	total = 0
	for number in range(1, under):
		poss_pair = sum_of_divisors(number)
		if poss_pair != number and sum_of_divisors(poss_pair) == number:
			total += number

	return total

