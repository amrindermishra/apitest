import requests

resp =requests.get('https://api.opayl.com/api/mentor/detail/86', headers={"Accept":"application/json"})


print(resp)
print(resp.text)
