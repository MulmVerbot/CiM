try:
    import tkinter as tk
    from tkinter import ttk
    from tkinter import messagebox
    from tkinter import filedialog
    from tkinter import Menu
    import time
    import os
    import sys
except:
    print("(FATAL) Konnte die wichtigen Bilbioteken nicht Laden!")
    messagebox.showerror(title="Kritischer Fehler", message="(FATAL) Konnte die wichtigen Bilbioteken nicht Laden! Das Programm wird nun Beendet.")
    sys.extit

root = tk.Tk()

class FeedbackForm:
    def __init__(self, master):
        self.master = master
        
        self.zeit_string = time.strftime("%H:%M:%S")
        self.tag_string = str(time.strftime("%d %m %Y"))
        print(self.tag_string)

        self.Programm_Name = "ListenDings"
        self.Version = "Alpha 0.1.1"
        master.title(self.Programm_Name + " " + self.Version)

        # Labels für Textfelder
        self.kunde_label = tk.Label(master, text="Kunde:")
        self.problem_label = tk.Label(master, text="Problem:")
        self.loesung_label = tk.Label(master, text="Lösung:")        

        # Textfelder
        self.kunde_entry = tk.Entry(master)
        self.problem_entry = tk.Entry(master)
        self.loesung_entry = tk.Entry(master)
        

        # "Senden" Knopf
        self.senden_button = tk.Button(master, text="Senden", command="")
        self.senden_button.bind('<Button-1>', self.senden)
        root.bind('<Return>', self.senden)

        # Ausgabe-Textfeld
        self.ausgabe_text = tk.Text(master)
        self.ausgabe_text.config(highlightthickness=0)
        self.ausgabe_text.config(state='disabled')

        # Positionierung von Labels und Textfeldern
        self.kunde_label.grid(row=0, column=0)
        self.problem_label.grid(row=1, column=0)
        self.loesung_label.grid(row=2, column=0)

        self.kunde_entry.grid(row=0, column=1)
        self.problem_entry.grid(row=1, column=1)
        self.loesung_entry.grid(row=2, column=1)
        self.senden_button.grid(row=3, column=1)
        self.ausgabe_text.grid(row=4, column=0, columnspan=2)

        self.menu = Menu(root)
        root.config(menu=self.menu)
        self.menudings = Menu(self.menu, tearoff=0)
        self.menu.add_cascade(label=self.Programm_Name + self.Version, menu=self.menudings)
        self.menudings.add_command(label="Info", command=self.info)

        try:
            # Ausgabe-Textfeld aktualisieren
            print("(INFO) versuche die alten Aufzeichenungen zu Laden")
            self.ausgabe_text.config(state='normal')
            with open("liste.txt", "r") as f:
                feedback_text = f.read()
                self.ausgabe_text.delete("1.0", tk.END)
                self.ausgabe_text.insert(tk.END, feedback_text)
                self.ausgabe_text.config(state='disabled')
                print("-----------------------------------------")
                print("(DEV) Hier ist nun das geladene aus der bisherigen Liste:")
                print(feedback_text)
                print("(DEV) Das War das geladene aus der bisherigen Liste.")
                print("-----------------------------------------")
        except FileNotFoundError:
            print("(INFO) Die Datei Liste.txt gibts net")
            self.ausgabe_text.config(state='disabled')
        except:
            messagebox.showinfo(title="Fehler", message="Ein Unbekannter Fehler ist aufgetreten beim Versuch während des Programmstarts die bisherigen aufzeichnungen zu laden, es könnte sein dass das Programm trotzdem fehlerfrei funktioniert.")
            self.ausgabe_text.config(state='disabled')

    def info(self):
        print("(INFO) Info(def)")
        messagebox.showinfo(title="Info", message=self.Programm_Name + " " + self.Version + "\n Programmiert von Maximilian Becker, \n https://dings.systems für mehr Informationen")
    def senden(self, event):
        print("(DEV) senden(def)")
        # Textfeld-Inhalte lesen
        kunde = self.kunde_entry.get()
        problem = self.problem_entry.get()
        loesung = self.loesung_entry.get()
        self.ausgabe_text.config(state='normal')
        
        if kunde or problem or loesung != "":
            print("(INFO) Enter gedrückt obwohl etwas geschrieben wurde.")

            # Inhalte in Textdatei speichern
            if os.path.exists("liste.txt"):
                with open("liste.txt", "a") as f:
                    f.write(f"=============================\n")
                    f.write(self.zeit_string)
                    
                    f.write("\n")
                    f.write(f"Kunde: {kunde}\n----------------\nProblem: {problem}\n----------------\nLösung: {loesung}\n\n")
                    print("----------------\n")
                    # Ausgabe-Textfeld aktualisieren
                with open("liste.txt", "r") as f:
                    feedback_text = f.read()
                    self.ausgabe_text.delete("1.0", tk.END)
                    self.ausgabe_text.insert(tk.END, feedback_text)
                self.ausgabe_text.config(state='disabled')
            else:
                print("(INFO) Liste zum beschreiben existiert bereits.")
                with open("liste.txt", "w+") as f:
                    f.write(f"=============================\n")
                    f.write(self.zeit_string)
                    f.write("\n")
                    f.write(f"Kunde: {kunde}\nProblem: {problem}\nLösung: {loesung}\n\n")
                    # Ausgabe-Textfeld aktualisieren
                with open("liste.txt", "r") as f:
                    feedback_text = f.read()
                    self.ausgabe_text.delete("1.0", tk.END)
                    self.ausgabe_text.insert(tk.END, feedback_text)
                    self.ausgabe_text.config(state='disabled')
        else:
            print("(ERR) Da hat wer Enter gedrückt obwohl noch nicht geschrieben war.")
            messagebox.showinfo(title="Fehler", message="Bitte geben Sie zuerst in wenigsten eine Spalte etwas ein.")
            self.ausgabe_text.config(state='disabled')
            return
        
        self.kunde_entry.delete(0, tk.END)
        self.problem_entry.delete(0, tk.END)
        self.loesung_entry.delete(0, tk.END)
       

        

def bye():
    print("(ENDE) Das Programm wurde Beendet, auf wiedersehen! \^_^/ ")
    zeit_string = time.strftime("%H:%M:%S")
    tag_string = str(time.strftime("%d %m %Y"))
    print(zeit_string , tag_string)
    print("/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/")
    sys.exit()

# Hauptprogramm
root.resizable(False,False)
feedback_form = FeedbackForm(root)
root.protocol("WM_DELETE_WINDOW", bye)
root.mainloop()