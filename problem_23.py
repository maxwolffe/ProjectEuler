def sum_of_divisors(number):
	total = 0
	for divisor in range(1, (number / 2) + 1):
		if number % divisor == 0:
			total += divisor
	return total

def is_abundant_number(number):
	if sum_of_divisors(number) > number:
		return True

abundant_list = [number for number in range(1, 28123) if is_abundant_number(number)]

abundant_set = set()

for number in range(1,28123):
	if is_abundant_number(number):
		abundant_set.add(number)

#return the sum of all non-abundant numbers under the number 'under'
def sum_of_non_abundants(under):
	total = 0
	for number in range(1, under):
		sumable = True
		for digit1 in abundant_list:
			if (number - digit1) in abundant_set:
				sumable = False
		if sumable:
			total += number
	return total


