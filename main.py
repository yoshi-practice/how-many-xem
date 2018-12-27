import requests
import json

node = 'http://104.128.226.60:7890'    # Test
api = '/account/get'
parameter = 'address=TCJC5VFBIYF5TKEUS273XS7IXUKJ36I3JCJQ7WOH'
url = str(node + api + '?' + parameter)

r = requests.get(url).json()

print(r['account']['balance'])
