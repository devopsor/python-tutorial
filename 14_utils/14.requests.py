#pip install requests

import requests
r = requests.get('https://www.google.com/')
print(r.status_code) #200


r = requests.get('https://www.google.com/search', params={'q': 'python', 'cat': '1001'})

print(r.url) #https://www.google.com/search?q=python&cat=1001

