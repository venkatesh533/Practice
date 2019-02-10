
import csv

# ## writing to a csv file ##
# with open('sample.csv','w') as cf:
# 	writer = csv.writer(cf)
# 	writer.writerow(['Column1','Column2'])
# 	for i in range(1,11):
# 		writer.writerow(['H{}'.format(i),'H{}'.format(i+1)])

filepath = input('Enter Your filename: ')
with open(filepath,'r') as fp:
	reader = csv.reader(fp)
	for r in reader:
		print(r)
