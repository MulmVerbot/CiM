import os
import re
import matplotlib.pyplot as plt

# Muster, um die Uhrzeit zu extrahieren
uhrzeit_muster = re.compile(r'bis (\d{2}:\d{2}:\d{2})')

# Funktion zum Durchsuchen eines Verzeichnisses und seiner Unterverzeichnisse
def durchsuche_ordner(pfad):
    ergebnisse = {}
    
    # Durchlaufe alle Dateien und Unterordner
    for root, dirs, files in os.walk(pfad):
        uhrzeiten = []
        for file in files:
            dateipfad = os.path.join(root, file)
            # Nur Textdateien durchsuchen
            if file.endswith('.txt'):
                with open(dateipfad, 'r') as datei:
                    for zeile in datei:
                        uhrzeit_match = uhrzeit_muster.search(zeile)
                        if uhrzeit_match:
                            uhrzeit = uhrzeit_match.group(1)
                            uhrzeiten.append(uhrzeit)
        
        # Speichere die Anzahl der gefundenen Uhrzeiten für diesen Ordner
        if uhrzeiten:
            ordnername = os.path.basename(root)
            ergebnisse[ordnername] = len(uhrzeiten)
    
    return ergebnisse

# Hauptverzeichnis, das durchsucht werden soll
hauptverzeichnis = 'C:\\Users\\MulmVerbot\\CiM\\Listen'

# Durchsuche das Hauptverzeichnis und Unterordner
ergebnisse = durchsuche_ordner(hauptverzeichnis)

# Bereite Daten für das Diagramm vor
ordner = list(ergebnisse.keys())
anzahl = list(ergebnisse.values())

# Erstelle ein Diagramm mit matplotlib
plt.figure(figsize=(12, 8))
plt.barh(ordner, anzahl, color='blue')
plt.xlabel('Anzahl gefundener Uhrzeiten')
plt.ylabel('Monat')
plt.title('Anzahl gefundener Anrufe pro Monat')
plt.grid(True, axis='x')

# Zeige das Diagramm an
plt.tight_layout()  # Optimiere das Layout
plt.show()
