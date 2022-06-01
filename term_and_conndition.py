import requests
from config import T_AND_C




head = {"Accept":"application/json"}
resp = requests.get(T_AND_C,headers=head)


print(resp)
print(resp.json())