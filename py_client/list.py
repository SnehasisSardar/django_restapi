import requests

from getpass import getpass
auth_endpoint = "http://localhost:8000/apis/auth/" #http://127.0.0.1:8000/ 
username=input("Enter Username: ")
password= getpass("Enter password: ")
auth_response = requests.post(auth_endpoint, json={'username':username,'password':password}) # HTTP Request

# print(get_response.text)
print(auth_response.status_code)

print(auth_response.json())

if auth_response.status_code==200:
    token = auth_response.json()['token']
    headers={
        "Authorization":f"Bearer {token}"
    }
    endpoint = "http://localhost:8000/apis/product/" #http://127.0.0.1:8000/ 

    get_response = requests.get(endpoint,headers=headers) # HTTP Request

    # print(get_response.text)
    print(get_response.status_code)

    print(get_response.json())