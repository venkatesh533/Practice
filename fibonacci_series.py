
'''
Program to print fibonacci series
'''

n = int(input('Enter a number:'))
a,b = 0,1
if n <= 0:
	print('Please enter positive number')
elif n == 1:
	print('Fibonacci series upto {}:'.format(n))
	print(a)
else:
	print('Fibonacci series upto {}:'.format(n))
	n -= 1
	print(a, end=',')
	print(b, end=',')
	while n != 0:
		c = a+b
		a,b = b,c
		n -= 1
		print(c, end=',')
