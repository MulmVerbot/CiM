import os
from flashtext import KeywordProcessor
from tkinter import filedialog

# Ordnerpfad
ordner_pfad = filedialog.askdirectory(title="Wo?")

# Liste der Dateierweiterungen, die ignoriert werden sollen
ignorierte_erweiterungen = [".exe", ".jpg", ".pdf"]

# KeywordProcessor für die Schlüsselwortsuche
keyword_processor = KeywordProcessor()
keyword_processor.add_keyword("Dings", "Passwort")
#keyword_processor.add_keyword("suchwort2", "Ersatzwort2")

def analysiere_datei(datei_pfad):
    try:
        with open(datei_pfad, "r", encoding="utf-8") as datei:
            text = datei.read()
            matches = keyword_processor.extract_keywords(text)
            if matches:
                print(f"Gefundene Schlüsselwörter in {datei_pfad}: {matches}")
            else:
                print(f"Keine passenden Schlüsselwörter in {datei_pfad} gefunden.")
    except UnicodeDecodeError:
        #print(f"Datei {datei_pfad} kann nicht analysiert werden (nicht UTF-8).")
        pass

# Alle Dateien im Ordner und Unterordnern durchsuchen
for ordner_pfad, _, dateien in os.walk(ordner_pfad):
    for datei_name in dateien:
        datei_pfad = os.path.join(ordner_pfad, datei_name)
        if os.path.isfile(datei_pfad) and not any(datei_name.lower().endswith(ext) for ext in ignorierte_erweiterungen):
            analysiere_datei(datei_pfad)
