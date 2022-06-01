from tracemalloc import stop
import requests
from requests.auth import HTTPBasicAuth
from config  import TEACHER_LOGIN_API

response=requests.post(TEACHER_LOGIN_API,headers={"Accept":"application/json"},data={'email': 'amrindermishra05551@gmail.com',"password":"123456"})
code=response.status_code

if code==200:
    print(response.text,'\n'"===>Pass<===")
else:
    print("===>FAIL<===")
    print(response.json())


# assert code==200 , "code doesn't match"
# pass
