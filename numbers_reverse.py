## Program to accept numbers untill 0 is given and display one by one in reverse order ##

li = []
while True:
	n = int(input('Enter a Number(0 to stop):'))
	if n == 0:
		break
	li.append(n)
li.reverse()
print li
for i in range(0,len(li)):
	# del li[i]
	print li[i]
	