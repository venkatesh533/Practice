
'''
i/p:aaaccbdd
o/p:a3b1c2d2
'''
from collections import Counter

li = []
st = input('Enter String:')
di = dict(Counter(st))
di = sorted(di.items(),key=lambda s:s[0])
for i in di:
	if i[0]:
		s = str(i[0])
		li.append(s)
	if i[1]:
		s = str(i[1])
		li.append(s)
print(''.join(li))