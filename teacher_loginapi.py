from tracemalloc import stop
import requests
from requests.auth import HTTPBasicAuth

response=requests.post('https://api.opayl.com/api/admin/login',headers={"Accept":"application/json"},data={'email': 'amrindermishra05551@gmail.com',"password":"123456"})
code=response.status_code
assert code==200 , "code doesn't match"
pass
print(response.json())