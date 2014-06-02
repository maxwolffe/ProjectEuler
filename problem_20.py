def digit_summation(digit):
	digit_string = str(digit)
	total = 0
	for str_digit in digit_string:
		total += int(str_digit)
	return total 

def factorial(digit):
	if digit == 1:
		return 1
	return digit * factorial(digit - 1)
