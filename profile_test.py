from email import header
from lib2to3.pgen2 import token
from wsgiref import headers
import requests

auth_token='eyJ0eXAiOiJKV1QiLCJhbGciOiJSUzI1NiJ9.eyJhdWQiOiIxIiwianRpIjoiZDM0MTNlNTVhMjdhOGI5ZWYzMzBkNGYyOGY1MzdkODBiOWNmOWVhYjljZDhjZmE3NzlmMGViNmY2MzBiYmIzYTcxOTJjYzdhYWRhZWQ3MzAiLCJpYXQiOjE2NTM1NTUwNjguNjQ5MzY1LCJuYmYiOjE2NTM1NTUwNjguNjQ5MzY5LCJleHAiOjE2ODUwOTEwNjguNjM3MTU0LCJzdWIiOiIyMTIiLCJzY29wZXMiOltdfQ.DusSYC8Jp26Jk4rvA8RLQCcH9jYvyjdl0bBr9kDFUiPeW5Go5_IpWVQZDMVtkPpg5An0tLNQkNjuH88XVVokQ3BOYmt5pxl_6o9pWpaIbN-p4INZ_boTp84os9nx9T-jOpHLSDjY8ui3lJwri7E1h0UpIILcrmQZcK1xfXS38k9WevvjRkmDydJLRwdeF5efgB812AAgmZ81JocVkP5hkX9J3o1jhYpAv26FmJnoYbwiQpYz1HutAg2DkhWYELb_0nVsXtXMfCVl47CaFmuUDDvwYv-f5VCnmEZeM05rBPMkMUbz2ockSLh_QKOBdDGkwUjLXej82QpTxC0Jff2eHuMnzZ2fvaEhpBcDhUYLLot_u4trghj9Nv5NM2DjEyIp6k0XBj1H7I6EIoqZlw6jSFuInokxGuCKJthL1R8RfT9Siyu5BgVR6YoInqEP__8xE6RASFPKiPonBpCzSAPChR8UvAHroTbkOolqcY7ANRPI1WjalGEr38Bu9nPMPJe2aKPrMmquz_na0wAcajS3tanHQQP2keTrGZ9p4pY7COq-XESpyKUg-AZAgAJLdyhSc9VKYnDxIRvsBf1IuSuecm8cOqL-i0gPpYKyERrN8iWfg_aDh4SdmnCKxy9MAX7xTWzrYkdP2bbateFmygeRHf7eiZtPQvKkHo8piLiNQc0'
hed = {'Accept':'application/json', 'Authorization': 'Bearer ' + auth_token}
url = 'http://staging-api.opayl.com/api/dashboard'
response = requests.get(url, headers=hed)
print(response)
print(response.json())
