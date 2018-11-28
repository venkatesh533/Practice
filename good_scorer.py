
'''
Input : First line of Input contains testcase "T". For each testcase "T", there will be 3 lines of input, 
first line contains lengths of the columns, and next two lines contains the scores of students sitting in that column.

Input :
2
5 6
8 4 5 6 7
2 3 4 5 6 7
3 5
100 29 37
100 200 300 400 500
output:
C1
C2
'''

n = int(input(''))
li = []

for i in range(n):
	vi = {}
	## length of the columns ##
	lc = list(map(int, input().split()))
	C1 = list(map(int, input().split()))
	C2 = list(map(int, input().split()))
	vi['length'] = lc
	vi['C1'] = C1
	vi['C2'] = C2
	li.append(vi)

for j in li:
	a = sum(j.get('C1'))
	b = sum(j.get('C2'))
	if a == b:
		print('Both Columns Are Equal')
	elif a > b:
		print('C1')
	else:
		print('C2')