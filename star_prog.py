
'''
program to print stars
'''

'''
*
**
***
****
*****
'''

j = 1
while j <= 5:
	k = 1
	while k <= j:
		print('*',end=' ')
		k += 1
	j += 1
	print(' ')

print(' ')

'''
*****
****
***
**
*
'''

j = 1
while j <= 5:
	k = 5
	while k >= j:
		print('*',end=' ')
		k -= 1
	j += 1
	print(' ')
