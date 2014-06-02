def multiple_sum(first, second, position = 0, end = 1000):
	total = 0
	while position < end:
		if position % first == 0 or position % second == 0:
			print(position)
			total += position
		position += 1
	return total

