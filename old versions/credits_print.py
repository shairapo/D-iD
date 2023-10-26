import requests

url = "https://api.d-id.com/credits"

headers = {
    "accept": "application/json",
    "authorization": "Basic xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx"
}

response = requests.get(url, headers=headers)

if response.status_code==200:
    data=response.json()
    print (data["remaining"])
else:
    print("request failed")