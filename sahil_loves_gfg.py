
'''
Input : 
First line of input contains "T" testcases. Next "T" lines contains Strings with lowercase characters.

Output : 
For each testcase, output the count the ccurrences of "gfg"(continuous) present in string.
'''

n = int(input(''))
li = []
for i in range(n):
	st = input('')
	li.append(st)

for i in li:
	if i.count('gfg') == 0:
		print('-1')
	else:
		print(str(i.count('gfg')))
