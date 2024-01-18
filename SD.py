import tkinter as tk
from tkinter import ttk
from datetime import datetime

class Eintrag:
    def __init__(self, kunde, problem, loesung, info, erledigt=False):
        self.kunde = kunde
        self.problem = problem
        self.loesung = loesung
        self.info = info
        self.erledigt = erledigt
        self.datum = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

class EintragsAnwendung:
    def __init__(self, root):
        self.root = root
        self.root.title("Eintragsanwendung")

        self.eintraege = []

        # Eingabefelder
        self.kunde_entry = tk.Entry(root)
        self.problem_entry = tk.Entry(root)
        self.loesung_entry = tk.Entry(root)
        self.info_entry = tk.Entry(root)

        # Buttons
        self.senden_button = tk.Button(root, text="Senden", command=self.senden)
        self.erledigt_button = tk.Button(root, text="Als erledigt markieren", command=self.erledigt_markieren)

        # Treeview für Anzeige der Einträge
        self.treeview = ttk.Treeview(root, columns=('Kunde', 'Problem', 'Lösung', 'Info', 'Erledigt', 'Datum'))
        self.treeview.heading('#0', text='ID')
        self.treeview.heading('Kunde', text='Kunde')
        self.treeview.heading('Problem', text='Problem')
        self.treeview.heading('Lösung', text='Lösung')
        self.treeview.heading('Info', text='Info')
        self.treeview.heading('Erledigt', text='Erledigt')
        self.treeview.heading('Datum', text='Datum')

        # Platzierung der Widgets
        self.kunde_entry.grid(row=0, column=1)
        self.problem_entry.grid(row=1, column=1)
        self.loesung_entry.grid(row=2, column=1)
        self.info_entry.grid(row=3, column=1)

        self.senden_button.grid(row=4, column=0, columnspan=2, pady=10)
        self.erledigt_button.grid(row=5, column=0, columnspan=2, pady=10)

        self.treeview.grid(row=0, column=2, rowspan=6, padx=10)

    def senden(self):
        kunde = self.kunde_entry.get()
        problem = self.problem_entry.get()
        loesung = self.loesung_entry.get()
        info = self.info_entry.get()

        eintrag = Eintrag(kunde, problem, loesung, info)
        self.eintraege.append(eintrag)

        # Eintrag zur Treeview hinzufügen
        self.treeview.insert('', 'end', values=(kunde, problem, loesung, info, '', eintrag.datum))

        # Eingabefelder leeren
        self.kunde_entry.delete(0, 'end')
        self.problem_entry.delete(0, 'end')
        self.loesung_entry.delete(0, 'end')
        self.info_entry.delete(0, 'end')

    def erledigt_markieren(self):
        # Überprüfen, ob ein Eintrag ausgewählt ist
        selected_item = self.treeview.selection()
        if selected_item:
            # Den Eintrag als erledigt markieren und Treeview aktualisieren
            item = self.treeview.item(selected_item)
            index = int(item['text'])
            self.eintraege[index].erledigt = True
            self.treeview.item(selected_item, values=(item['values'][0], item['values'][1], item['values'][2], item['values'][3], '✔', item['values'][5]))

if __name__ == "__main__":
    root = tk.Tk()
    app = EintragsAnwendung(root)
    root.mainloop()
