import requests

# headers ={'Authorization': 'Bearer c71ba4d05a1f9cd9aa88146d2ac729361b6ef378'}

endpoint = "http://localhost:8000/apis/product/" #http://127.0.0.1:8000/ 

get_response = requests.post(endpoint,json={'title':"This is title with tokens",'price':500})#,headers=headers) # HTTP Request

# print(get_response.text)
print(get_response.status_code)

print(get_response.json())