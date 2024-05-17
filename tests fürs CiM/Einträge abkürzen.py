import tkinter as tk
from tkinter import messagebox
from tkinter import simpledialog

def extract_entries():
    # Text aus dem Textwidget extrahieren
    text = text_widget.get("1.0", tk.END)

    # Einträge aufteilen
    entries = text.split("\n\n")  # Annahme: Einträge sind durch zwei Zeilenumbrüche getrennt

    # Dialogfenster für die Auswahl des Eintrags anzeigen
    selected_entry = choose_entry(entries)

    if selected_entry:
        # Hier können Sie die gewünschte Aktion für den ausgewählten Eintrag ausführen (z. B. kopieren)
        print("Ausgewählter Eintrag:")
        print(selected_entry)
    else:
        print("Kein Eintrag ausgewählt.")

def choose_entry(entries):
    # Dialogfenster für die Auswahl des Eintrags anzeigen
    selected_index = tk.simpledialog.askinteger("Eintrag auswählen", "Geben Sie die Nummer des gewünschten Eintrags ein (1, 2, 3, ...):", minvalue=1, maxvalue=len(entries))

    if selected_index:
        return entries[selected_index - 1]  # Index in der Liste ist 0-basiert
    else:
        return None

# GUI erstellen
root = tk.Tk()
text_widget = tk.Text(root)
text_widget.pack()

# Button erstellen
extract_button = tk.Button(root, text="Einträge extrahieren", command=extract_entries)
extract_button.pack()

root.mainloop()
