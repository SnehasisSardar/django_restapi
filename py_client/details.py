import requests

endpoint = "http://localhost:8000/apis/product/2/" #http://127.0.0.1:8000/ 

get_response = requests.get(endpoint) # HTTP Request

# print(get_response.text)
print(get_response.status_code)

print(get_response.json())