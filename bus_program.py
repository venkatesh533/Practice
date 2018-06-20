
## Program for bus algorithm ##

'''
Sample i/p
2
4
6 5 9 4
3
8 6 2
'''
from collections import OrderedDict

status = False
val = 1
t = int(input(''))
d1 = mc = {}
ord_dic = {}
for i in range(0,t):
	bn = int(input(('')))
	cb = raw_input('')
	d1[bn] = cb
	ord_dic[val] = bn
	val = val + 1

for k,v in d1.items():
	v = [int(i) for i in v.split(' ')]
	if len(v) != k:
		print('Please enter costs for %d buses' %(k))
		status = False
		break
	d1[k] = v
	status = True

if status:
	for k,v in d1.items():
	    c,s = 0, [];
	    li = sorted(v)
	    for i in range(len(v)):
	        if i == 0:
	            a,b = li[i],li[i+1]
	            c = c + (a+b)
	        else:
	            if i == len(li) - 1:
	                break
	            a,b = c,li[i+1]
	            c = a+b
	        s.append(c)
	    mc[k] = sum(s)
	# print mc
	# descending = OrderedDict(sorted(mc.items(), key=lambda kv: kv[1], reverse=True))
	for j in ord_dic.keys():
		ord_dic[j] = mc.get(ord_dic.get(j))
	for i in ord_dic.keys():
		print(ord_dic.get(i))