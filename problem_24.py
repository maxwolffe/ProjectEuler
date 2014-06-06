def lexographical_permutations(num_list):
	permuations = set()

	for first in num_list:
		print(first)
		number1 = first
		for second in num_list:
			number2 = number1 + second
			for third in num_list:
				if second == first:
					break
				number3 = number2 + third
				for fourth in num_list:
					if third == second or third == first:
						break
					number4 = number3 + fourth
					for fifth in num_list:
						if fourth == third or fourth == second or fourth == first:
							break
						number5 = number4 + fifth
						for sixth in num_list:
							if fifth == fourth or fifth == third or fifth == second or fifth == first:
								break
							if len(permuations) >= 1000000:
								return list(permuations)
							number6 = number5 + sixth
							for seventh in num_list:
								if sixth == fourth or sixth == third or sixth == second or sixth == first or sixth == fifth:
									break
								number7 = number6 + seventh
								for eighth in num_list:
									if seventh == sixth or seventh == fifth or seventh == fourth or seventh == third or seventh == second or seventh == first:
										break
									number8 = number7 + eighth
									for nineth in num_list:
										if eighth == seventh or eighth == sixth or eighth == fifth or eighth == fourth or eighth == third or eighth == second or eighth == first:
											break
										number9 = number8 + nineth
										for tenth in num_list:
											if nineth == eighth or nineth == seventh or nineth == sixth or nineth == fifth or nineth == fourth or nineth == third or nineth == second or nineth == first:
												break
											final_number = number9 + tenth
											check_num = set([i for i in final_number])
											if len(final_number) == len(check_num):
												permuations.add(int(final_number))
	return list(permuations)

zero_through_nine = ['0','1','2','3','4','5','6','7','8','9']

set1 = lexographical_permutations(zero_through_nine)


