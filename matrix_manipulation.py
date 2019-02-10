## program to manipulate two matrices ##

import numpy as np

first_rows = int(input('Enter no.of rows for A matrix:'))
first_cols = int(input('Enter no.of cols for A matrix:'))
first= [[0 for c in range(first_cols)] for r in range(first_rows)]

## takes elemnts for matrix ##
for i in range(first_rows):
	for j in range(first_cols):
		ip = int(input('Enter number for A matrix:'))
		first[i][j] = ip

second_rows = int(input('Enter no.of rows for B matrix:'))
second_cols = int(input('Enter no.of cols for B matrix:'))
second = [[0 for c in range(second_cols)] for r in range(second_rows)]
if first_rows == second_rows and first_cols == second_cols:
	## takes elemnts for second matrix ##
	for i in range(second_rows):
		for j in range(second_cols):
			ip = int(input('Enter number for B matrix:'))
			second[i][j] = ip

	first = np.array(first)
	second = np.array(second)
	print(first)
	print(second)
	print('Sum of A+B is:')
	print(first+second)

else:
	print('please enter two matrices order in equally')