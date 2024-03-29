import requests

base_url = "http://192.168.60.240:80/rest"
auth_token = "0003:f1b2da444dd4c03d93242a1f07b527fb7f4cddde8bbbd96a23d245aee20305b775e45ef620c8f233de4a2d1d2ad2c3cf814c9cbe7e1b1b87236610e7420ed886"

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
