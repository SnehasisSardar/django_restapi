import requests

# endpoint = "https://httpbin.org/status/200/"
# endpoint = "https://httpbin.org/anything"
endpoint = "http://localhost:8000/apis/" #http://127.0.0.1:8000/ 

get_response = requests.post(endpoint,params={"abc":123}, json={"querry": "Hello World" }) # HTTP Request
# print(get_response.headers)
print(get_response.text)
print(get_response.status_code)
# HTTP Request -> HTML
# REST API HTTP Request -> JSON
# JavaScript Object Nototion ~ Python Dict
get_response = requests.get(endpoint)
print(get_response.json())
print(get_response.status_code)