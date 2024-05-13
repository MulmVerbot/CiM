from pypresence import Presence
import time

client_id = '807247545780273224'  # Ersetzen Sie dies durch Ihre Client-ID
RPC = Presence(client_id)  
RPC.connect()

# Die Rich Presence wird angezeigt
RPC.update(details="Details hier", state="Status hier", large_image="großes_bild", small_image="kleines_bild", large_text="Großer Text", small_text="Kleiner Text")

while True:  # Während die Schleife läuft, bleibt die Rich Presence aktiv
    print("läuft")
    time.sleep(15)  # Kann jede 15 Sekunden aktualisiert werden
