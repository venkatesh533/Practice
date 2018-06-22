
'''
program to give demo on generator
'''

def reverse(data):
	for i in range(len(data)-1,-1,-1):
		yield data[i]

for i in reverse([2,6,7]):
	print i,' '

for j in reverse('Venkatesh'):
	print(j)
