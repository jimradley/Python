#http://docs.python-requests.org/en/latest/user/quickstart/#make-a-request


import requests
from bs4 import BeautifulSoup

html_doc = requests.get('http://ojp.nationalrail.co.uk/service/timesandfares/MLY/LDS/today/0700/dep')

# print(html_doc.text)

soup = BeautifulSoup(html_doc.text, 'html.parser')

# print(soup.select('.first .journey-breakdown input[type$="hidden"]'))

try:
    values = soup.find_all('input', {'id': '' })
except:
    pass
    

if "GREEN" not in values[1]['value']:
    print("Delay 1")

if "GREEN" not  in values[4]['value']:
    print("Delay 2")
    
if "GREEN" not  in values[6]['value']:
    print("Delay 3")
    
if "GREEN" not  in values[9]['value']:
    print("Delay 4")
 
if "GREEN" not in values[11]['value']   :
    print("Delay 5")

print(values[1]['value'])
print(values[4]['value'])
print(values[6]['value'])
print(values[9]['value'])
print(values[11]['value'])

# print(soup.select('.first .journey-breakdown input[type$="hidden"]'))

# txt = soup.select('.first .journey-breakdown input[type$="hidden"]')
# print(txt)

# print(str(holding))

# if str(holding).find("delayed") == -1:
#     print ("No")
# else:
#     print ("DELAYED")
# print(str(holding).find("Morlfey"))

# print(soup.body.td)
