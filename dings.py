import csv

# Benutzereingabe für Kunde, Problem, Lösung und Uhrzeit
kunde = input("Kunde: ")
problem = input("Problem: ")
loesung = input("Lösung: ")
uhrzeit = input("Uhrzeit: ")

# Pfad zur CSV-Datei
csv_datei = 'daten.csv'

# Überprüfen, ob die Datei bereits existiert, und ggf. einen Header schreiben
datei_existiert = True
try:
    with open(csv_datei, 'r', newline='') as datei:
        reader = csv.reader(datei)
        if not list(reader):
            datei_existiert = False
except FileNotFoundError:
    datei_existiert = False

# Daten in die CSV-Datei schreiben
with open(csv_datei, 'a', newline='') as datei:
    schreiber = csv.writer(datei)

    # Wenn die Datei neu ist, schreiben Sie den Header
    if not datei_existiert:
        schreiber.writerow(["Kunde", "Problem", "Lösung", "Uhrzeit"])

    # Schreiben Sie die Benutzereingaben in die Datei
    schreiber.writerow([kunde, problem, loesung, uhrzeit])

print("Daten wurden in die CSV-Datei gespeichert.")
