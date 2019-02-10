
## Program to send POST(HTTP request method) data to an API ##

import requests

API_KEY = '4414941a84171e2227213cbb4f38ae4a'
API_ENDPOINT = 'https://pastebin.com/api/api_post.php'

## My source code ##
source_code = '''
print('Hello PasteBin,Im Venkatesh')
print('Thank you so much for your support')
'''
# data to be sent to api 
data = {'api_dev_key':API_KEY, 
        'api_option':'paste', 
        'api_paste_code':source_code, 
        'api_paste_format':'python'} 


resp = requests.post(url=API_ENDPOINT,data=data)
print('The PasteBin URL Is:{}'.format(resp.text))