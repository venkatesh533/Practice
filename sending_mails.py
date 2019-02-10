
'''
Program to send email using smtplib module
'''

import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

sender = 'venkatesh.savith@gmail.com'
receiver = 'venkatesh.vanapalli@zebi.co'
header = 'To:' + receiver + '\n' + 'From: ' + sender + '\n' + 'Subject:Testing of email in python \n'
message = 'Hii\n\nThis is a sample email using Python'
message = header + message

try:
	server = smtplib.SMTP('smtp.sendgrid.net', 587)
	server.starttls()
	server.login('sudhir_suresh','sudhir1234')
	server.sendmail(sender,receiver,message)
	print('Successfully email sent')
except:
	print('Sorry!Unable to send email')