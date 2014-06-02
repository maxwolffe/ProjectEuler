import math

def special_pythag(sums_to):
	print(sums_to)
	for a in range(1, sums_to):
		for b in range(a,sums_to):
			c = math.sqrt(a ** 2 + b ** 2)
			if (a + b + c) == sums_to:
				return a * b * c

print(special_pythag(1000))
