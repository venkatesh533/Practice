
'''
A number is called amazing if it has exactly three distinct divisors.

'''

t = int(input())
li = [int(input()) for i in range(1,t+1)]
for i in li:
	c = 0
	for j in range(1,i+1):
		if i%j == 0:
			c += 1
	if c == 3:
		print("1")
	else:
		print("0")
