from zammad_py import ZammadAPI

# Initialisiere den Client mit der URL, dem Benutzernamen und dem Passwort
# Die Host-URL sollte in diesem Format sein: 'https://zammad.example.org/api/v1/'
client = ZammadAPI(url='http://ticketsystem.beese-computer.local', username='m.becker@beese-computer.de', password='1.Start2022!')

params = {
   "title": "Help me!",
   "group": "2nd Level",
   "customer": "david@example.com",
   "article": {
      "subject": "My subject",
      "body": "I am a message!",
      "type": "note",
      "internal": "false"
   }
}
new_ticket = client.ticket.create(params=params)
