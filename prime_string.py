
'''
Input
3
13
geeksforgeeks
4
JiiT
5
India
##
Output
YES
NO
NO
'''

##code
def prime(num):
	c = 0
	for k in range(2,num//2+1):
		if num%k == 0:
			c = 1
			break
	if c == 1:
		return 0
	else:
		return 1

n = int(input())
for i in range(n):
	s = 0
	length = int(input())
	st = input()
	if len(st) == length:
		for j in st:
			s += ord(j)
		if prime(s):
			print("YES")
		else:
			print("NO")
	else:
		print("Please enter correct length")
	break

