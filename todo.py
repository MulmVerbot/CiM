import requests

# Konfiguration
client_id = 'DEINE_CLIENT_ID'
client_secret = 'DEIN_CLIENT_SECRET'
username = 'maximilianbecker10@gmail.com'
password = '24022004mB'

# Token abrufen
token_url = 'https://login.microsoftonline.com/common/oauth2/token'
token_data = {
    'grant_type': 'password',
    'client_id': client_id,
    'client_secret': client_secret,
    'resource': 'https://graph.microsoft.com',
    'username': username,
    'password': password,
}
token_response = requests.post(token_url, data=token_data)
token = token_response.json().get('access_token')

# Aufgabe erstellen
todo_url = 'https://graph.microsoft.com/v1.0/me/todo/lists/DEFAULT_LIST_ID/tasks'
headers = {
    'Authorization': f'Bearer {token}',
    'Content-Type': 'application/json'
}
task_data = {
    'title': 'Deine neue Aufgabe',
    'dueDateTime': '2024-01-31T12:00:00.000Z'  # Füge das gewünschte Datum hinzu
}

task_response = requests.post(todo_url, headers=headers, json=task_data)

if task_response.status_code == 201:
    print('Aufgabe erfolgreich erstellt!')
else:
    print(f'Fehler beim Erstellen der Aufgabe: {task_response.text}')
