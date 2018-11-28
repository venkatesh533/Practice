
'''
Program to check whether particular string is suitable
for good Password or not
#########
Password should be :
1) Be a minimum of eight (8) characters in length
2) it should contains:
	a)Uppercase letter (A-Z)
	b)Lowercase letter (a-z)
	c)Digit (0-9)
3) Special character (~`!@#$%^&*()+=_-{}[]|:;”’?/<>,.)
'''

import re

password = input('Please Enter Password:')
flag = 0
while True:
	if len(password) < 8:
		flag = -1
		print('Password length should be more than 8 characters')
		break
	elif not re.search('[a-z]',password):
		flag = -1
		break
	elif not re.search('[A-Z]',password):
		flag = -1
		break
	elif not re.search('[0-9]',password):
		flag = -1
		break
	elif not re.search('[_@$]',password):
		flag = -1
		break
	elif re.search('\s',password):
		flag = -1
		break
	else:
		flag = 0
		print('Valid Password')
		break

if flag == -1:
	print('Invalid Password')