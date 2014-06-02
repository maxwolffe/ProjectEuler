def sum_diff(num_index):
	total_square = 0
	total = 0
	for i in range (1, num_index + 1):
		total_square += (i ** 2)
		total += i
	squared_total = total ** 2
	return squared_total - total_square
