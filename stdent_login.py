from tracemalloc import stop
import requests
from requests.auth import HTTPBasicAuth
from config import API_LOGIN_URL


response=requests.post(API_LOGIN_URL,headers={"Accept":"application/json"},data={'email': 'amrinder.rabblesoft@gmail.com',"password":"123456"})
code=response.status_code
assert code==200 , "code doesn't match"
pass
print(response.json())