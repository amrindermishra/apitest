import requests
from config import FAQ_API

resp =requests.get(FAQ_API, headers={"Accept":"application/json"})
code=resp.status_code

if code == 200:
    print(resp,'\n'"===>Pass<===")
else:
    print("===>Fail<===")





