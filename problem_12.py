import math

def triangle(index):
	number = 0
	for i in range(index + 1):
		number += i
	return number

def num_factors(number):
	factor = 1
	count = 0
	while factor <= math.sqrt(number):
		if number % factor == 0:
			count += 1
		factor += 1
	return count * 2

#generates a list of the first n triangle numbers
def generate_triangle_list(n):
	print("generating list of triangle numbers")
	number = 0
	triangle_list = []
	for i in range(1, n + 1):
		number += i
		triangle_list.append(number)
	print("done")
	return triangle_list

def generate_triangle_list_by(n, factor):
	print("generating list of triangle numbers")
	number = 0
	triangle_list = []
	for i in range(1, n + 1):
		number += i
		if number % factor == 0:
			triangle_list.append(number)
	print("done")
	return triangle_list

def factor_printer(product_list):
	for product in product_list:
		print(str(product) + " : " + str(num_factors(product)))

check10 = generate_triangle_list_by(500 * 100000, 10)
check = generate_triangle_list(500 * 100000)

def first_over_by_10(number_factors):
	#check = generate_triangle_list_by(number_factors * 100000, 10)
	highest_factor = 0
	print("checking over list of triangle numbers by 10s")
	for triangle in check10:
		if num_factors(triangle) > number_factors:
			return triangle


def first_over(number_factors):
	#check = generate_triangle_list(number_factors * 100000)
	highest_factor = 0
	print("checking over list of triangle numbers")
	for triangle in check:
		if num_factors(triangle) > number_factors:
			return triangle




