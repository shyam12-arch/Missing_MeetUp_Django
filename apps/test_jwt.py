import requests

BASE_URL = "http://127.0.0.1:8000"

# Register User
register_data = {"username": "shyam", "password": "qwerty"}
register_response = requests.post(f"{BASE_URL}/api/register/", json=register_data)

print("Register Response:", register_response.json(), '\n')



login_data = {"username": "shyam", "password": "qwerty"}
login_response = requests.post(f"{BASE_URL}/api/token/", json=login_data)
# login_response = requests.post(f"{BASE_URL}/api/token/refresh/", json=login_data)

print("Login Response:", login_response.json(), '\n')
access_token = login_response.json().get("access")


headers = {"Authorization": f"Bearer {access_token}"}
protected_response = requests.get(f"{BASE_URL}/api/protected/", headers=headers)
print("Protected API Response:", protected_response.json())


""" 🔥🔥🔥🔥🔥🔥 without postman 🔥🔥🔥🔥🔥🔥🔥"""
paylaod = {
        "name": "Amreesh pandey",
        "age": 12,
        "last_seen_location": "Russia"
}
requests.post(f"{BASE_URL}/find/", json=paylaod, headers=headers)
protected_response1 = requests.get(f"{BASE_URL}/find/", headers=headers)

print("Protected API Response1:", protected_response1.json())
print("******"*10, '\n\n')


## registration page---> login page(enter username & pwd)










