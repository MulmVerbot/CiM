import requests

base_url = "http://192.168.60.240:80/rest"
auth_token = "your_auth_token_here"

def get_users():
    url = f"{base_url}/Users"
    headers = {"Authorization": f"Bearer {auth_token}"}
    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        users = response.json()
        return users
    else:
        print(f"Error fetching user data. Status code: {response.status_code}")
        return None

users_data = get_users()
if users_data:
    print("List of users:")
    for user in users_data:
        print(f"User ID: {user['id']}, Name: {user['name']}, Email: {user['email']}")
else:
    print("Failed to fetch user data.")
