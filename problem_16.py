huge_number = 2 ** 1000


def digit_summator(number):
	sum = 0
	for digit in str(number):
		sum += int(digit)

	return sum