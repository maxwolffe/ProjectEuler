first_days_leap = [1,32, 32 + 29 , 32 + 29 + 31, 32 + 29 + 31 + 30, 32 + 29 + 31 + 30 + 31, 32 + 29 + 31 + 30 + 31 + 30, + 32 + 29 + 31 + 30 + 31 + 30 + 31, 32 + 29 + 31 + 30 + 31 + 30 + 31 + 31, 32 + 29 + 31 + 30 + 31 + 30 + 31 + 31 + 30, 32 + 29 + 31 + 30 + 31 + 30 + 31 + 31 + 30 + 31, 32 + 29 + 31 + 30 + 31 + 30 + 31 + 31 + 30 + 31 + 30]

first_days = [1,32, 32 + 28 , 32 + 28 + 31, 32 + 28 + 31 + 30, 32 + 28 + 31 + 30 + 31, 32 + 28 + 31 + 30 + 31 + 30, + 32 + 28 + 31 + 30 + 31 + 30 + 31, 32 + 28 + 31 + 30 + 31 + 30 + 31 + 31, 32 + 28 + 31 + 30 + 31 + 30 + 31 + 31 + 30, 32 + 28 + 31 + 30 + 31 + 30 + 31 + 31 + 30 + 31, 32 + 28 + 31 + 30 + 31 + 30 + 31 + 31 + 30 + 31 + 30]

def Counting_Sundays():
	first_Sunday = 0
	day = 1
	week_day = 2
	year = 1901
	while year <= 2000:
		print(year)
		day = 1
		if year % 4 == 0:
			print("Day of Week: " + str(week_day) + "Day of Year: " + str(day))
			while day <= 366:
				if day in first_days_leap and week_day == 0:
					first_Sunday += 1
				day += 1
				if week_day == 6:
					week_day = 0
				else:
					week_day += 1
		else:
			while day <= 365:
				if day in first_days and week_day == 0:
					first_Sunday += 1
				day += 1
				if week_day == 6:
					week_day = 0
				else:
					week_day += 1
		year += 1
	return first_Sunday

print(Counting_Sundays())

