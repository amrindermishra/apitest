import requests


# class details 
resp = requests.get('http://staging-api.opayl.com/class/detail/106',headers={"Accept":"application/json"})

print(resp)
