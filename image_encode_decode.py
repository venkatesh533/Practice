## program to encode,decode image to a string ##

import base64

file_path = str(input('Enter image file name with path:'))
with open(file_path,'rb') as fp:
	st = base64.b64encode(fp.read())
	print('Encoded string is:{}'.format(st))
imgfile = open('demo.png','wb')
imgfile.write(base64.b64decode(st))
imgfile.close()
