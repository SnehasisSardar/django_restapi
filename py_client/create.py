import requests

endpoint = "http://localhost:8000/apis/product/" #http://127.0.0.1:8000/ 

get_response = requests.post(endpoint,json={'title':"This is title",'price':50}) # HTTP Request

# print(get_response.text)
print(get_response.status_code)

print(get_response.json())