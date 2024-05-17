import requests

base_url = "http://192.168.60.240:80/rest"
auth_token = "your_auth_token_here"

def get_recent_calls():
    url = f"{base_url}/CallServices"
    headers = {"Authorization": f"Bearer {auth_token}"}
    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        call_data = response.json()
        recent_calls = call_data.get("recentCalls", [])
        return recent_calls
    else:
        print(f"Fehler beim Abrufen der Anrufdaten. Statuscode: {response.status_code}")
        return []

recent_call_list = get_recent_calls()
if recent_call_list:
    print("Liste der gerade beendeten Anrufe:")
    for call in recent_call_list:
        print(f"Anrufer-ID: {call.get('callerId', 'N/A')}, Dauer: {call.get('duration', 'N/A')} Sekunden")
else:
    print("Keine kürzlich beendeten Anrufe gefunden.")