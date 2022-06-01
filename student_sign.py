import requests
from config import STUDENT_SIGN 



# signup URLS
 
head = {"Accept":"application/json"}
resp = requests.post(STUDENT_SIGN,headers=head,data={"id":"","name":"Rahul","user_category":"2","course_level":"2",'email': 'rrr123@mailinator.com',"password":"123456","user_category":"1","course_level":"1","services":[
        "1",
        "2"
    ],"timezone":"Asia/Kolkata",
    "country_id":"103",
    "timezone_id":"192",
    "contact_number":"+917888797621"})



print(resp)
print(resp.json())