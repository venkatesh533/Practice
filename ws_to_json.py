
from bs4 import BeautifulSoup
import json

html_content = '''
</!DOCTYPE html>
<html>
<head>
	<title>Sample</title>
</head>
<body>
<p>
	Paragraph1
</p>
<p>
	Paragraph2
</p>
</body>
</html>
'''
dic = {}
soup = BeautifulSoup(html_content,'html.parser')
dic['a'] = [i.text.strip() for i in soup.find_all('p')]
d = json.dumps(dic)
dic = json.loads(d)
print(dic)