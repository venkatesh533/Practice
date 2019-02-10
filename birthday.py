
## Program to print the day based on date ##

import datetime

n = int(input('Enter no of dates:'))
li = []
status = False

if n in list(range(1,101)):
	for i in range(n):
		a = str(input('Enter date:'))
		li.append(a)

	day_dic = {0:'Monday',1:'Tuesday',2:'Wednesday',3:'Thursday',4:'Friday',5:'Saturday',6:'Sunday'}
	for i in li:
		dob = i.split(' ')
		dob = datetime.datetime.strptime('{}-{}-{}'.format(dob[0],dob[1],dob[2]),'%d-%m-%Y')
		print(day_dic.get(dob.weekday()))
		