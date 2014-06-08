def coin_sum(list_of_coins, sum1):
	#print(list_of_coins)
	#print(sum1)
	if abs(sum1) <= 0.001:
		return 1
	if sum1 <= 0 or len(list_of_coins) == 0:
		return 0
	return coin_sum(list_of_coins, sum1 - list_of_coins[0]) + coin_sum(list_of_coins[1:], sum1)

uk_list = [2, 1, .5, .2, .1, .05, .02, .01]

test_list = [2, 1, .5, .2]