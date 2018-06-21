
'''
Read an integer .
Without using any string methods, try to print the following:
Note that "" represents the values in between.
'''
n = int(input('Enter a number'))
li = [str(i) for i in range(1,n+1)]
li = ''.join(li)
print(li)
