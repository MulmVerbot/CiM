import tkinter as tk
from tkinter import ttk
from tkcalendar import Calendar

class CalendarApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Kalender-App")

        # Erstelle einen Kalender und passe die Schriftgröße an
        self.cal = Calendar(self.root, selectmode="day", font=("Arial", 14), background="white", foreground="black", bordercolor="gray", headersbackground="gray", normalbackground="white", weekendbackground="lightgray")
        self.cal.pack(padx=10, pady=10)

        # Erstelle Buttons für Aktionen
        self.add_button = ttk.Button(self.root, text="Termin hinzufügen", command=self.add_event)
        self.add_button.pack(pady=5)

        self.delete_button = ttk.Button(self.root, text="Termin löschen", command=self.delete_event)
        self.delete_button.pack(pady=5)

    def add_event(self):
        selected_date = self.cal.get_date()
        # Hier kannst du die Logik zum Hinzufügen eines Termins implementieren
        print(f"Termin hinzugefügt für {selected_date}")

    def delete_event(self):
        selected_date = self.cal.get_date()
        # Hier kannst du die Logik zum Löschen eines Termins implementieren
        print(f"Termin gelöscht für {selected_date}")

if __name__ == "__main__":
    root = tk.Tk()
    app = CalendarApp(root)
    root.mainloop()
