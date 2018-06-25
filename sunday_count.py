import datetime

year = range(1901,2001)
month = range(1,13)
day = range(1,32)
# year,month,day = [2017],[1],range(1,32)
li = []
for i in year:
	for j in month:
		for k in day:
			if j == 1:
				d = datetime.datetime.strptime('%d-%d-%d' %(k,j,i),'%d-%m-%Y')
				wd = datetime.datetime.weekday(d)
				if wd == 6:
					li.append(wd)

print(len(li))