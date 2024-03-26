import requests

base_url = "http://[IP/URL der Starface]:80/rest"
auth_token = "your_auth_token_here"

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
