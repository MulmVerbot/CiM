import requests
import json

# Zammad API URL und Token
zammad_api_url = 'http://ticketsystem.beese-computer.local/'
api_token = 'cefIGcJUaxE-ewjmVvsS-OZzmLJyulSbAGFo6roQcvJXEZPmZckp6KH-8paZtrck'

# Header für die Authentifizierung
headers = {
    'Authorization': f'Token token={api_token}',
    'Content-Type': 'application/json'
}

# Daten für das neue Ticket
ticket_data = {
    'title': 'Test Ticket',
    'group': 'Users',
    'customer': 'customer@example.com',
    'article': {
        'subject': 'Test Ticket',
        'body': 'Dies ist ein Test-Ticket',
        'type': 'note',
        'internal': False
    },
    'note': 'Dies ist eine Notiz für das Test-Ticket',
    'priority_id': 2,
    'state_id': 1
}

# HTTP POST Anfrage zum Erstellen des Tickets
response = requests.post(zammad_api_url, headers=headers, data=json.dumps(ticket_data))

# Antwort prüfen
if response.status_code == 201:
    print('Ticket erfolgreich erstellt:', response.json())
else:
    print('Fehler beim Erstellen des Tickets:', response.status_code, response.text)
