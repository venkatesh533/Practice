
## program to print prime numbers between two numbers ##
a = int(input("Enter first number:"))
b = int(input("Enter second number:"))

for i in range(a,b+1):
	for j in range(2,i):
		if i%j == 0:
			break
	else:
		print(i)
