import requests

resp =requests.get('https://api.opayl.com/api/home', headers={"Accept":"application/json"})


print(resp)