import requests

url = "https://app.ninjarmm.com/api/v2/organizations"
headers = {"Authorization": "Bearer YOUR_API_TOKEN"}

response = requests.get(url, headers=headers)
data = response.json()

# Verarbeite die Daten hier weiter...
