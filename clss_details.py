from urllib import response
import requests
from requests.auth import HTTPBasicAuth

resp =requests.get('https://api.opayl.com/api/class', headers={"Accept":"application/json"})
# print(resp.json())
print(resp.text)