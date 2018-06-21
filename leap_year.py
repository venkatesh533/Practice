
'''
program which will take the year and return the
status True:leap year , False:Non leap year
'''

def is_leap(year):
	status = False

	if (year in range(1900,(10**5+1))) and (year % 4 == 0):
		status = True

	return status


year = int(input('Enter a year'))
print(is_leap(year))