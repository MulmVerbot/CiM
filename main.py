import tkinter as tk
import time

class FeedbackForm:
    def __init__(self, master):
        self.master = master
        master.title("Feedback-Formular")
        self.zeit_string = time.strftime("%H:%M:%S")
        self.tag_string = str(time.strftime("%d %m %Y"))
        print(self.tag_string)

        # Labels für Textfelder
        self.kunde_label = tk.Label(master, text="Kunde:")
        self.problem_label = tk.Label(master, text="Problem:")
        self.loesung_label = tk.Label(master, text="Lösung:")
        

        # Textfelder
        self.kunde_entry = tk.Entry(master)
        self.problem_entry = tk.Entry(master)
        self.loesung_entry = tk.Entry(master)

        # "Senden" Knopf
        self.senden_button = tk.Button(master, text="Senden", command=self.senden)
        self.senden_button.bind('<Return>', self.senden)

        # Ausgabe-Textfeld
        self.ausgabe_text = tk.Text(master)

        # Positionierung von Labels und Textfeldern
        self.kunde_label.grid(row=0, column=0)
        self.problem_label.grid(row=1, column=0)
        self.loesung_label.grid(row=2, column=0)

        self.kunde_entry.grid(row=0, column=1)
        self.problem_entry.grid(row=1, column=1)
        self.loesung_entry.grid(row=2, column=1)

        self.senden_button.grid(row=3, column=1)

        self.ausgabe_text.grid(row=4, column=0, columnspan=2)

    def senden(self):
        # Textfeld-Inhalte lesen
        kunde = self.kunde_entry.get()
        problem = self.problem_entry.get()
        loesung = self.loesung_entry.get()
        self.kunde_entry.delete(0, tk.END)
        self.problem_entry.delete(0, tk.END)
        self.loesung_entry.delete(0, tk.END)

        # Inhalte in Textdatei speichern
        with open("feedback.txt", "a") as f:
            f.write(f"=============================\n")
            f.write(self.zeit_string)
            f.write("\n")
            f.write(f"Kunde: {kunde}\nProblem: {problem}\nLösung: {loesung}\n\n")

        # Ausgabe-Textfeld aktualisieren
        with open("feedback.txt", "r") as f:
            feedback_text = f.read()
            self.ausgabe_text.delete("1.0", tk.END)
            self.ausgabe_text.insert(tk.END, feedback_text)

        

# Hauptprogramm
root = tk.Tk()
feedback_form = FeedbackForm(root)
root.mainloop()
