#return true if the number is the sum of the fifth power of it's digits
def is_sum_fifths(number):
	list_digits = str(number)
	sum_nums = 0
	for digit in list_digits:
		sum_nums += int(digit) ** 5
	return sum_nums == number

def find_all_fifth(under):
	i = 2
	list_of = []
	while i < under:
		if is_sum_fifths(i):
			list_of.append(i)
		i += 1
	return list_of