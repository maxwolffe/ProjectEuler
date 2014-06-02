import num2word

#returns the sum of the letters used to spell out all the numbers up to num
def sum_of_letters(num):
	summation = 0
	for number in range(1, num + 1):
		for letter in num2word.to_card(number):
			if letter != " " and letter != "-":
				summation += 1
	return summation

one = 3 * (100 + 9 * 10) + 3
two = 3 * (100 + 9 * 10)
three = 5 * (100 + 9 * 10)
four = 4 * (100 + 9 * 10)
five = 4 * (100 + 9 * 10)
six = 3 * (100 + 9 * 10)
seven = 5 * (100 + 9 * 10)
eight = 5 * (100 + 9 * 10)
nine = 4 * (100 + 9 * 10)
ten = 3 * 10 
eleven = 6 * 10 
twelve = 6 * 10 
thirteen = 8 * 10 
fourteen = 8 * 10
fifteen = 7 * 10
sixteen = 7 * 10
seventeen = 9 * 10 
eighteen = 8 * 10
nineteen = 8 * 10
twenty = 6 * (100)
thirty = 6 * (100)
fourty = 6 * (100)
fifty = 5 * (100)
sixty = 5 * (100)
seventy = 7 * 100
ninety = 6 * 100
hundred = 7 * 900
thousand = 8
andi = 891 * 3

print(one +
two + 
three +
four +
five +
six +
seven + 
eight +
nine +
ten +
eleven +
twelve +
thirteen +
fourteen +
fifteen +
sixteen +
seventeen + 
eighteen +
nineteen +
twenty +
thirty +
fourty +
fifty +
sixty +
seventy +
ninety +
hundred +
thousand +
andi )