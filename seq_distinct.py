
a = range(2,101)
b = range(2,101)
dic = dict(zip(a,b))
li = []
for i in dic.values():
	for j in dic.keys():
		n = j**i
		li.append(n)

li = list(set(li))
print(len(li))