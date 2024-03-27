import requests

base_url = "http://192.168.60.240:80/rest"
auth_token = "ICH HAB KEINEN AUTH TOKEN"

def get_users():
    url = f"{base_url}/Users"
    headers = {"Authorization": f"Bearer {auth_token}"}
    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        users = response.json()
        return users
    else:
        print(f"Konnte die Daten nicht anfordern: {response.status_code}")
        return None

users_data = get_users()
if users_data:
    print("Liste an Nutzern:")
    for user in users_data:
        print(f"User ID: {user['id']}, Name: {user['name']}, Email: {user['email']}")
else:
    print("Konnte mir die Daten nicht ziehen")
