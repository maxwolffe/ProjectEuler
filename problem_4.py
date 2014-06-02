def is_palendrome(number):
	digits = []
	while number > 0:
		digits.append(number % 10)
		number = number // 10
	for i in range(0, (len(digits) // 2)):
		if digits[i] != digits[len(digits) - i - 1]:
			return False
	return True

def largest_three():
	largest_product = None
	for i in range (999):
		for j in range(999):

			product = (999-i) * (999-j)
			if is_palendrome(product) and (not largest_product or product > largest_product):
				largest_product = product
	return largest_product