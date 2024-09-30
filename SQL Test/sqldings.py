import sqlite3
from tkinter import *
from tkinter import messagebox
import datetime

# Funktion zum Erstellen der Datenbank und Einfügen von Daten
def save_to_db():
    # Verbindung zur SQLite-Datenbank herstellen (oder erstellen, falls sie noch nicht existiert)
    conn = sqlite3.connect('support_database.db')
    cursor = conn.cursor()

    # Heutiges Datum als Tabellenname (Format: logs_YYYY_MM_DD)
    table_name = f'logs_{datetime.date.today().strftime("%Y_%m_%d")}'

    # Tabelle erstellen, falls sie noch nicht existiert
    cursor.execute(f'''
    CREATE TABLE IF NOT EXISTS {table_name} (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        start_time TEXT,
        end_time TEXT,
        customer TEXT,
        problem TEXT,
        info TEXT,
        phone_number TEXT,
        specific_person TEXT,
        forwarded TEXT
    )
    ''')

    # Daten aus den Eingabefeldern erfassen
    start_time = entry_start_time.get()
    end_time = entry_end_time.get()
    customer = entry_customer.get()
    problem = entry_problem.get("1.0", END).strip()
    info = entry_info.get()
    phone_number = entry_phone_number.get()
    specific_person = entry_specific_person.get()
    forwarded = entry_forwarded.get()

    # Daten in die Tabelle einfügen
    cursor.execute(f'''
    INSERT INTO {table_name} (start_time, end_time, customer, problem, info, phone_number, specific_person, forwarded)
    VALUES (?, ?, ?, ?, ?, ?, ?, ?)
    ''', (start_time, end_time, customer, problem, info, phone_number, specific_person, forwarded))

    # Änderungen speichern und Verbindung zur Datenbank schließen
    conn.commit()
    conn.close()

    # Bestätigung anzeigen
    messagebox.showinfo("Erfolg", "Daten wurden erfolgreich gespeichert!")

    # Eingabefelder zurücksetzen
    reset_fields()

# Funktion zum Zurücksetzen der Eingabefelder
def reset_fields():
    entry_start_time.delete(0, END)
    entry_end_time.delete(0, END)
    entry_customer.delete(0, END)
    entry_problem.delete("1.0", END)
    entry_info.delete(0, END)
    entry_phone_number.delete(0, END)
    entry_specific_person.delete(0, END)
    entry_forwarded.delete(0, END)

# GUI erstellen
root = Tk()
root.title("Support-Log Eintrag")

# Labels und Eingabefelder
Label(root, text="Startzeit:").grid(row=0, column=0, padx=10, pady=5)
entry_start_time = Entry(root)
entry_start_time.grid(row=0, column=1, padx=10, pady=5)

Label(root, text="Endzeit:").grid(row=1, column=0, padx=10, pady=5)
entry_end_time = Entry(root)
entry_end_time.grid(row=1, column=1, padx=10, pady=5)

Label(root, text="Kunde:").grid(row=2, column=0, padx=10, pady=5)
entry_customer = Entry(root)
entry_customer.grid(row=2, column=1, padx=10, pady=5)

Label(root, text="Problem:").grid(row=3, column=0, padx=10, pady=5)
entry_problem = Text(root, height=5, width=30)
entry_problem.grid(row=3, column=1, padx=10, pady=5)

Label(root, text="Info:").grid(row=4, column=0, padx=10, pady=5)
entry_info = Entry(root)
entry_info.grid(row=4, column=1, padx=10, pady=5)

Label(root, text="Telefonnummer:").grid(row=5, column=0, padx=10, pady=5)
entry_phone_number = Entry(root)
entry_phone_number.grid(row=5, column=1, padx=10, pady=5)

Label(root, text="Bestimmte Person:").grid(row=6, column=0, padx=10, pady=5)
entry_specific_person = Entry(root)
entry_specific_person.grid(row=6, column=1, padx=10, pady=5)

Label(root, text="Weiterleitung:").grid(row=7, column=0, padx=10, pady=5)
entry_forwarded = Entry(root)
entry_forwarded.grid(row=7, column=1, padx=10, pady=5)

# Speichern-Button
save_button = Button(root, text="Speichern", command=save_to_db)
save_button.grid(row=8, column=0, columnspan=2, pady=10)

# Mainloop für die GUI
root.mainloop()