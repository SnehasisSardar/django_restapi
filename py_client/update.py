import requests

endpoint = "http://localhost:8000/apis/product/11/update/" #http://127.0.0.1:8000/ 

data = {
    'title': 'Playing free fire',
    'price': 100
}

get_response = requests.put(endpoint, json=data) # HTTP Request

# print(get_response.text)
print(get_response.status_code)

print(get_response.json())