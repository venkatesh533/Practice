
import xmltodict
import json
import requests

resp = requests.get('http://dataquestio.github.io/web-scraping-pages/simple.html')
pv = json.dumps(xmltodict.parse(resp.content))
pv = json.loads(pv)
print(pv)