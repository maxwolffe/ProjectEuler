fibonaci_numbers = {}

def fibonaci_num(index):
	if index < 2:
		return index
	if index in fibonaci_numbers.keys():
		return fibonaci_numbers[index]
	number = fibonaci_num(index - 1) + fibonaci_num(index - 2)
	fibonaci_numbers[index] = number
	return number

def fast_fibonaci_sum(less_than):
	index = 1
	fib_item = fibonaci_num(1)
	fib_sum = 0

	while fib_item < less_than:
		fib_item = fibonaci_num(index)
		if fib_item % 2 == 0:
			fib_sum += fib_item
		index += 1

	return fib_sum
