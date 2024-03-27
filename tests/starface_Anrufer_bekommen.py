import requests

base_url = "https://192.168.60.240:80/rest"
auth_token = "0003:b7148d6f23c05378f6f826e09f38f5e7deddc33a33d0b52e92643c76ad6041a3419b018fa1c210707c0017d4f75ef515587b2ba8ed959ad32241f0d8017e9748"

def get_current_call():
    url = f"{base_url}/CallServices"
    headers = {"Authorization": f"Bearer {auth_token}"}
    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        call_data = response.json()
        if "currentCall" in call_data:
            current_call = call_data["currentCall"]
            return current_call
        else:
            print("Kein aktueller Anruf.")
            return None
    else:
        print(f"Fehler beim Abrufen der Anrufdaten. Statuscode: {response.status_code}")
        return None

current_call_info = get_current_call()
if current_call_info:
    print("Details zum aktuellen eingehenden Anruf:")
    print(f"Anrufer-ID: {current_call_info.get('callerId', 'N/A')}")
    print(f"Anrufstatus: {current_call_info.get('state', 'N/A')}")
else:
    print("Fehler beim Abrufen der Anrufdaten.")
