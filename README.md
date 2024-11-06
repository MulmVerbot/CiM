# Multifunktionaler Unternehmens-Logbuch-Manager (M.U.L.M)
Der Multifunktionaler Unternehmens-Logbuch-Manager, 
zum aufschreiben von Dingen zum Beispiel wenn jemand in einer Firma anruft und irgendwas will

Hier kommt noch bissl Zeugs dazu.
## Features bis jetzt:
- Kundenname, Telefonnummer, Problem, Info und eventuelle Weiterleitung an Kollegen können aufgenommen und gespeichert werden
- Exportierung der Daten als csv oder Text Datei
- schnelles versenden von Tickets
- Bearbeitung eingetragener Daten
- Nach Configuration im Starface UCC Client: Automatische aufnahme der Telefonummer des Anrufenden Kunden sowie abspeicherung der Zeit dieser Anrufe
- Eine Uhr welche die Uhrzeit anzeigt und eine Meldung rausgibt sobald Feierabend ist
- Weiterleitungen können protokolliert werden
- Einstellung eines SMTP Server um Beispielsweise Tickets direkt aus dem Programm versendet werden können
- Es wird eine Liste mit Kontakten durchsucht um auch bereits angerufenene Nummern wieder zu erkennen, oder ggf. eine unbekannte hinzuzufügen. (diese Einstellung kann im Menü deaktiviert werden)
    Um die Redundanzfreiheit zu verbessern, wird auch wenn die Nummer bereits eingetragen wurde, der Name des Kontakts immer mit dem Inhalt der Zeile "Anrufer" Überschrieben.
- Es kann per Schnellmenü in der Kundenablage, in der Datenbank vorangehender "ListenDingse" oder in einem selbst gewählten Ordner/Laufwerk gesucht werden (klappt auch mit Netzlaufwerken)
- Es kann per Knopfdruck ein Fenster für eine Schnellnotiz geöffnet werden, diese wird nicht gespeichert und funktioniert ohne Ladezeiten oder irgendeinen anderen Schnickschnack
- Das JSON Adressbuch kann über ein inkludiertes, externes Script in einer grafischen Ansicht dargestellt werden(genauso wie alle anderen JSON Dateien, das Ding ist universal).
- Es gibt die möglichkeit eine Blacklist zu erstellen, um Nummern aus dem Starface Modul zu entfernen/ignorieren
- Das IHK Berichtsheft kann geöffnet werden
- Es gibt ein eigenes Todo Programm, "Totdo - jetzt kannst Du Dir sogar aufschreiben wie Du Dich totarbeitest". Es können aus vergangenen Anrufen mittels One-Click Aufgaben erstellt werden.
- Es kann eine Statistik zur Anrufhäufgigkeit als Diagram dargestellt werden.
- Demo zum neuen Checklisten System (Im Tab unter INFO -> Checklisten)
- anrufen von eingetragenen Nummern via webaufruf (Mit allen TK Programmen Kompatibel)


## Zukünftige Features:
- Das Totdo soll mit einstellbaren Timern und Erinnerungen ausgestattet werden:
- "DingsListen" verschlüsseln und ausschließlich schreibgeschützt im Programm auslesbar machen alternativ auch mit Passwort
- Ki gestützte Formulierung von texten um die Weiterleitung der Stichpunkte als Email zu erleichtern und zu verschnellern
- Der Such Algo wird noch verbessert und soll die möglichkeit bieten, mit Akronymen zu suchen (erste Alpha bereits vorhanden).
- Voll ausgebaute Checklisten Funktion mit eigenem Editor sowie Import/Export System
