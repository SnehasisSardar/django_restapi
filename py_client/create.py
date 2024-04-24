import requests

headers ={'Authorization': 'Bearer 773580ea2677405cbebba95fb61fee22ca1f07b4'}

endpoint = "http://localhost:8000/apis/product/" #http://127.0.0.1:8000/ 

get_response = requests.post(endpoint,json={'title':"This is title with tokens",'price':500},headers=headers) # HTTP Request

# print(get_response.text)
print(get_response.status_code)

print(get_response.json())