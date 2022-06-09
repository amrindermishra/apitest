import email
import requests
from config  import TEACHER_LOGIN_API
from  config import FAQ_API,API_LOGIN_URL,STUDENT_SIGN,WALKTHROW_API


class ApiTesting:
    
    def code_check(code):
        if code == 200:
            print("====================> Pass <===================="'\n')
        else:
            print("====================> Fail <===================="'\n')
    
    

    # CONTACT US API
    def contact_us(apilink,head,):
        print("Enter Details for Contact US ")
        subject = input("Subject : ")
        name = input("Name : ")
        attachment = input("Attachment : ")
        email = input("Email : ")
        msg = input("Message : ")
        phone = int(input("Phone : "))
     
        resp = requests.post(apilink,headers=head, data={
            "subject":subject,
            "email":email,
            "name":name,
            "attachment" : attachment,
            "phone": phone,
            "department" : "65968000000010772",
            "description":msg,
        })

        code=resp.status_code
        print("====================> CONTACT US Api <====================")
        api = ApiTesting
        api.code_check(code)
    
    
    def testing(random, head):

        resp =requests.get(random, headers=head)

        code=resp.status_code
        print("====================> FAQ Api <====================")
        api = ApiTesting
        api.code_check(code)


    def test(random, head):

        resp =requests.get(random, headers=head, )
        
        code=resp.status_code
        print("====================> HOME Api <====================")
        api = ApiTesting
        api.code_check(code)
        
     
    def mentor(teacher , head):
        resp =requests.get('https://api.opayl.com/api/mentor/detail/86', headers=head)
        code=resp.status_code
        print("====================> Mentor Details Api <====================")
        api = ApiTesting
        api.code_check(code)
        
        
    def profile(url, hed):
        response = requests.get(url, headers=hed)
        code=response.status_code
        print("====================> Profile Details Api <====================")
        api = ApiTesting
        api.code_check(code)


    # STUDENT LOGIN API amrindermishra@mailinator.com 12345678
    def std_Login(student,head):
        print("Enter Details for STUDENT Login ")
        email = input("Enter Email : ")
        password = input("Enter Password : ")
        response=requests.post(student,headers=head,data={'email': email,"password":password})
        code=response.status_code
        
        if code==200:
         print("====================>  Student Login Api <====================")  
         print("====================> Pass <===================="'\n')
            # print(response.json())
        else:
            print("====================>  Student Login Api <====================")
            print("====================> Fail <===================="'\n')

    def student_sign(run,head):
        print("Student signup Detail")
        name = input("Enter Name : ")
        email = input("Enter email : ")
        password = int(input("Enter Password : "))
        contact_num = int(input("Enter Mob NUM : "))

        head = {"Accept":"application/json"}
        resp = requests.post(run,headers=head,data={"id":"","name":name,"user_category":"2","course_level":"2",'email': email,"password":password,"user_category":"1","course_level":"1","services":[
        "1",
        "2"
        ],"timezone":"Asia/Kolkata",
        "country_id":"103",
        "timezone_id":"192",
        "contact_number":contact_num})
        code=resp.status_code
        print("====================> Student Sign Api <====================")
        api = ApiTesting
        api.code_check(code)
        

    def teacher_login(teacher, head):
        print("Teacher Login Enter Details")
        email = input("Enter Your email : ")
        password = input("Enter Your password : ")

        response=requests.post(teacher,headers=head,data={'email': email,"password":password})
        code=response.status_code
        print("====================> Teacher Login Api <====================")
        api = ApiTesting
        api.code_check(code)


    def walkthrow(walk,head):
        resp = requests.get(walk, headers=head)
        code=resp.status_code
        print("====================> Walkthrow Api <====================")
        api = ApiTesting
        api.code_check(code)


head = {"Accept":"application/json"}

auth_token='eyJ0eXAiOiJKV1QiLCJhbGciOiJSUzI1NiJ9.eyJhdWQiOiIxIiwianRpIjoiOTdhYWM0MjlkMTJmY2VjYzhlNmIxZmJmMjYxZDYzODI0YWQwYWNkYjU0YjM5YTExMjRiYmZlZmIyMDliNWM2YTZiYjAwOWI4NDdhYzQ2MWIiLCJpYXQiOjE2NTQyNTU4NTQuNzkwODIyLCJuYmYiOjE2NTQyNTU4NTQuNzkwODI2LCJleHAiOjE2ODU3OTE4NTQuNzc3MTUxLCJzdWIiOiIxNDciLCJzY29wZXMiOltdfQ.K8R8kbLraayaa40itZUpMai6O1MhHjseeVOUiYlJ5s6pcW_B4xuVnSfqtVXp_doopE0OVf-rI5g9_0oJB64Z_ICuCrg40p9wjkBqxxfDnBIWN34kxym0uip0JNrTPbBB6gl7prBjb1sh5GJbTWbVkiG-ENytH0LWbS7organxBHa-bcRcnU-HezKYCx8KwiYZh2NCyZ_Pj-VcpvAFcwdr1c-v6TUhqKSHI-ur8AKvcyA360ifBhKFkvMpKlQU5KyMLEnzXgRqbNYbGl2oZ48yin1As0aechZJ8G-vYsc4p2gUdmTTsw54ktWO-VEHFIX8SGBvqMUCAV_aAnemo_diOGSFf46pKmGXFH5rwzLkZH1buSTxZP0yN0oSMgl8corBVzQ8WdHRmNCN0eNHCTrILmOBrsQcgiN0vZbx0H_ACwHrVppg2LfonQsYAx0-b6nz8yrBOR9--3nHU4c-J45WeRzzOUdNAfQobxyvQzH4vpqYSWyNvJr97Vq8OsH4Tf1d07RuQh3M5qGDHGEOEVRsYHZfJquArX53b-edGd2UKp1c4K4DYDaP6SI9Y-mvqQTp34MlOeDgK_6GZAQw1R6G_pqzBqeMuuZgKbMY8_Kb1ETVs-cGk4IjfgKRHOvDyyO-G2mqrMZbqwMjAeDQmVwayNdbeIB9NnERRsnH3y_Kus'
hed = {'Accept':'application/json', 'Authorization': 'Bearer ' + auth_token}

api = ApiTesting
api.contact_us('http://staging-api.opayl.com/api/ticket',head)

api.testing(FAQ_API,head)

api.test('https://api.opayl.com/api/home',head,)

api.mentor('https://api.opayl.com/api/mentor/detail/86',head)

api.profile('http://staging-api.opayl.com/api/dashboard',hed)

api.std_Login(API_LOGIN_URL,head)

api.student_sign(STUDENT_SIGN,head)

api.teacher_login(TEACHER_LOGIN_API,head)

api.walkthrow(WALKTHROW_API,head)