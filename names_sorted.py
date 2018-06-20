## Program to accept a names untill end is given and display those names in a reverse order ##
li = []
while True:
	st = str(input('Enter a name:'))
	if st == 'end':
		break
	li.append(st)
li.sort()
print 'Names in sorted order'
for i in li:
	print i