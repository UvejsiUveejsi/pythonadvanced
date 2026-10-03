import requests
api_url="http://127.0.0.1:8000/user"
from typing import Dict


user_data:Dict[str,str |int]={"id":1,"name":"Dren","age":23,"email":"ub@gmail.com","gender":"Female"}
# user_data:(id=1,name="John",age=21,emal="ub123@gmail.com",gender="Male")

response=requests.post(api_url,json=user_data)

print(response.status_code)#200,#201
