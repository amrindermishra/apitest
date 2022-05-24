import requests
from requests.auth import HTTPBasicAuth

response=requests.get('https://api.opayl.com/api/dashboard', headers={"Accept":"application/json"})
# print (response.json())
print (response)
