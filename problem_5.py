def multiple(highest_factor):
	product = highest_factor
	is_product = False
	product_of = 0
	if highest_factor > 17: 
		product = 12252240
	elif highest_factor > 18:
		product = 232792560
	while not is_product:
		for i in range(1, highest_factor + 1):
			if product % i == 0:
				product_of += 1
			else:
				break
		if product_of == highest_factor:
			is_product = True
			return product
		else:
			product_of = 0
			product += 1

