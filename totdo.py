import customtkinter as tk
from tkinter import Menu
from tkinter import font
import json
import os
import time


class TodoApp:
    def __init__(self, root):
        self.root = root
        
        self.Version = "Alpha 1.2.1"
        self.Programm_Name = "TotDo Liste"
        self.root.title(self.Programm_Name + " " + self.Version)
        self.Todo_offen = False
        Benutzerordner = os.path.expanduser('~')
        tasks_pfad = os.path.join(Benutzerordner, 'CiM', 'Db')
        tasks_pfad_datei = os.path.join(tasks_pfad, 'tasks.json')
        self.Einstellungsordner_pfad = os.path.join(Benutzerordner, 'CiM', 'Einstellungen')
        self.Listenname_speicherort = os.path.join(self.Einstellungsordner_pfad, 'Listenname.txt')

        try:
            if not os.path.exists(self.Einstellungsordner_pfad):
                os.mkdir(self.Einstellungsordner_pfad)
        except Exception as ex1:
            print(f"konnte den Einstellungsordner nicht erstellen. Fehlercode: {ex1}")

        #### Farben #### , fg_color="White", border_color=self.Border_Farbe, border_width=2, text_color="Black", hover_color="pink"
        self.Hintergrund_farbe = "AntiqueWhite2"
        self.Hintergrund_farbe_Text_Widget = "AntiqueWhite2"
        self.Textfarbe = "Black"
        self.Border_Farbe = "AntiqueWhite4"
        self.Entry_Farbe = "AntiqueWhite3"
        self.Ereignislog_farbe = self.Hintergrund_farbe_Text_Widget
        self.aktiviert_farbe = "aquamarine2"
        self.deaktiviert_farbe = "White"
        self.dunkle_ui_farbe = "burlywood2"
        self.helle_ui_farbe = "burlywood1"
        self.ja_ui_fabe = "burlywood"
        self.das_hübsche_grau = "LightSlateGray"
        self.helle_farbe_für_knopfe = "LightSkyBlue"
    #### Farben Ende ####

        self.Schriftart = ("Helvetica", 20, "bold")
        self.Schriftart_k = ("Helvetica", 20, "normal")
        self.root.configure(fg_color=self.Hintergrund_farbe)

        try:
            if not os.path.exists(tasks_pfad):
                print("[-INFO-] Der Db Ordner scheint nicht zu existieren. Erstelle ihn nun.")
                os.mkdir(tasks_pfad)
                print("[-INFO-] Der Db Ordner wurde erfolgreich erstellt.")
        except Exception as ex_einst:
            print("[-ERR-] Fehler beim Erstellen des Db Ordners. Fehlercode:", ex_einst)
        self.TASK_FILE = tasks_pfad_datei
        
        self.Zeit = time.strftime("%H:%M:%S")
        self.Listennamen_laden()
        self.todo_aufmachen()


    def Listennamen_laden(self):
        try:
            self.Listenname_l.place_forget()
        except:
            pass
        try:
            with open(self.Listenname_speicherort, "r") as ln:
                self.Listenname = ln.read()
            self.Listenname_l = tk.CTkLabel(self.root, text=self.Listenname, font=self.Schriftart, text_color="Black")
            self.Listenname_l.place(x=220,y=50)
        except:
            print("konnte den Listennamen nicht lesen.")
            self.Listenname = "Dings"
    
    def Listennamen_speichern(self):
        try:
            with open(self.Listenname_speicherort, "w+") as ln:
                ln.write(self.Ln_beb_e.get())
                print("Listenname gespeichert.")
            self.top_ln_f.destroy()
            self.Listennamen_laden()
        except:
            print("konnte den Listennamen nicht speichern.")
            self.top_ln_f.destroy()

    def fake_laden(self):
        print("lade nun die ganzen Konzept Sachen")
        y1 = 100
        i = 1
        while i <= 10:
            l = tk.CTkLabel(self.todo_frame_links, text=f"{i}. Liste (zukünftig anclickbar)", text_color="Black")
            l.place(x=10,y=y1)
            y1 += 40
            i += 1
        print("Alle Fakes/ Konzepte wurden geladen")

    def todo_aufmachen(self):
        self.Todo_offen = True

        self.menu = Menu(root)
        root.configure(menu=self.menu)
        self.menudings = Menu(self.menu, tearoff=0)
        
        self.Einstellungen = Menu(self.menu, tearoff=0)
        self.Bearbeiten_Menu = Menu(self.menu, tearoff=0)
        self.menu.add_cascade(label=self.Programm_Name  + " " + self.Version, menu=self.menudings)
        self.menu.add_cascade(label="Einstellungen", menu=self.Einstellungen)
        self.menu.add_cascade(label="Bearbeiten", menu=self.Bearbeiten_Menu)
        self.menudings.add_command(label="Info", command=self.info)
        self.Bearbeiten_Menu.add_command(label="Listenmamen ändern", command=self.Listenname_change)

        self.todo_frame_links = tk.CTkFrame(self.root, width=200, height=1000, fg_color=self.Hintergrund_farbe, border_color=self.Border_Farbe, border_width=3, corner_radius=5)
        self.todo_frame_links.place(x=0, y=0)
        self.todo_frame_rechts = tk.CTkFrame(self.root, width=400, height=1000, fg_color=self.Hintergrund_farbe, border_color=self.Border_Farbe, border_width=3, corner_radius=5)
        self.todo_frame_rechts.place(x=1520, y=0)
        self.todo_frame_einz = tk.CTkScrollableFrame(self.root, width=820, height=800, fg_color=self.Hintergrund_farbe, border_color=self.Border_Farbe, border_width=3, corner_radius=5)
        self.todo_frame_einz.place(x=200, y=100)

        self.Aufgabe_hinzufuegen_Knopp = tk.CTkButton(self.root, text="Aufgabe erstellen", command="", fg_color="White", border_color=self.Border_Farbe, border_width=2, text_color="Black", hover_color="pink")
        self.Aufgabe_hinzufuegen_Knopp.bind('<Button-1>', self.create_task_button_vor)
        self.root.bind('<Return>', self.create_task_button_vor)
        self.Aufgabe_hinzufuegen_Knopp.place(x=1120, y=240)

        self.Aufgaben_name_e = tk.CTkEntry(self.root, placeholder_text="Titel", width=300, fg_color=self.Entry_Farbe, text_color="Black", placeholder_text_color="FloralWhite")
        self.Aufgaben_Beschreibung_e = tk.CTkEntry(self.root, placeholder_text="Beschreibung", width=300, fg_color=self.Entry_Farbe, text_color="Black", placeholder_text_color="FloralWhite")
        self.Aufgaben_name_e.place(x=1060, y=110)
        self.Aufgaben_Beschreibung_e.place(x=1060, y=150)

        

        self.fake_laden()
        self.load_tasks()

    def info(self):
        print("Programmiert von Maximilian Becker")

    def Listenname_change(self):
        print("Listenname_change (def)")
        self.top_ln_f = tk.CTkToplevel()
        self.top_ln_f.configure(resizeable=False)
        self.top_ln_f.title=("Den Namen der Liste bearbeiten")
        self.Ln_beb_e = tk.CTkEntry(self.top_ln_f)
        self.Ln_beb_e.pack()
        width = 100
        height = 100
        def mittig_fenster(width, height):
            fenster_breite = root.winfo_screenwidth()
            fenster_hoehe = root.winfo_screenheight()
            x = (fenster_breite - width) // 2
            y = (fenster_hoehe - height) // 2
            self.top_ln_f.geometry(f"{width}x{height}+{x}+{y}")
        mittig_fenster(width, height)
        self.sp_ln = tk.CTkButton(self.top_ln_f, text="Speichern", command=self.Listennamen_speichern)
        self.sp_ln.pack(pady=10,padx=10)
        #btn und dann die funktion

    def todo_zumachen(self):
        print("todo_zumachen(def)")
        try:
            self.button.pack_forget()
        except:
            print("button ist noch da.")
        self.todo_frame_links.place_forget()
        self.todo_frame_rechts.place_forget()
        self.todo_frame_einz.place_forget()
        self.Aufgaben_name_e.place_forget()
        self.Aufgaben_Beschreibung_e.place_forget()
        self.Aufgabe_hinzufuegen_Knopp.place_forget()
        self.Todo_offen = False

    def create_task_button_vor(self, event):
        task_name = self.Aufgaben_name_e.get()
        self.Zeit = time.strftime("%H:%M:%S")
        if task_name:
            task_description = self.Aufgaben_Beschreibung_e.get()
            if task_description:
                self.task = {'name': task_name, 'description': task_description, 'Uhrzeit': self.Zeit, 'Notizen': "-"}
                self.Aufgaben_name_e.delete(0, tk.END)
                self.Aufgaben_Beschreibung_e.delete(0, tk.END)
                self.save_task(self.task)
                self.create_task_button(self.task)
            else:
                task_description = "-"
                self.task = {'name': task_name, 'description': task_description, 'Uhrzeit': self.Zeit, 'Notizen': "-"}
                self.Aufgaben_name_e.delete(0, tk.END)
                self.Aufgaben_Beschreibung_e.delete(0, tk.END)
                self.save_task(self.task)
                self.create_task_button(self.task)

    def create_task_button(self, task):
        self.button = tk.CTkButton(self.todo_frame_einz, text=f"{task['name']}", command=lambda t=task: self.show_task(t), fg_color="White", border_color=self.Border_Farbe, border_width=2, text_color="Black", hover_color="pink", width=800)
        self.button.pack(padx=10, pady=5)

    def l_ja(self):
        self.delete_task(self.task)
        self.top_show_f.destroy()

    def l_nein(self):
        self.top_show_f.destroy()

    def todo_r_dispawn(self):
        try:
            self.Aufgaben_Titel.place_forget()
            self.Aufgabe_entfernen.place_forget()
            self.Aufgaben_Beschreibung_l.place_forget()
            self.Notizen_feld.place_forget()
        except:
            pass

    def show_task(self, task):
        print("Aufgabe anzeigen")
        self.task = task
        self.todo_r_dispawn()
        self.Aufgaben_Titel = tk.CTkLabel(self.todo_frame_rechts, text=f"Titel: {task['name']}", text_color="Black", justify="left", font=self.Schriftart)
        self.Aufgaben_Beschreibung_l = tk.CTkLabel(self.todo_frame_rechts, text=f"Uhrzeit: {task['Uhrzeit']}\nBeschreibung:\n{task['description']}", text_color="Black", justify="left", font=self.Schriftart_k)
        self.Aufgabe_entfernen = tk.CTkButton(self.todo_frame_rechts, text="Aufgabe entfernen", command=self.aufgabe_loeschen_frage, fg_color="White", border_color=self.Border_Farbe, border_width=2, text_color="Black", hover_color="pink")
        self.Notizen_feld = tk.CTkTextbox(self.todo_frame_rechts, width=320, height=440, text_color="Black", fg_color="azure", wrap="word", border_width=0)
        self.Aufgaben_Titel.place(x=20,y=20)
        self.Aufgaben_Beschreibung_l.place(x=20,y=100)
        self.Aufgabe_entfernen.place(x=20,y=930)
        self.Notizen_feld.place(x=20,y=300)
        self.Notizen_feld.insert(tk.END, f"{task['Notizen']}")

    def aufgabe_loeschen_frage(self):
        self.top_show_f = tk.CTkToplevel()
        self.top_show_f.configure(resizeable=False)
        self.top_show_f.title=("Diese Aufgabe löschen")
        ja = tk.CTkButton(self.top_show_f, text="Ja", command=self.l_ja, fg_color="White", border_color=self.Border_Farbe, border_width=2, text_color="Black", hover_color="pink")
        ja.pack(pady=5,padx=5)
        nein = tk.CTkButton(self.top_show_f, text="Nein", command=self.l_nein, fg_color="White", border_color=self.Border_Farbe, border_width=2, text_color="Black", hover_color="pink")
        nein.pack(pady=5,padx=5)
        width = 290
        height = 100
        def mittig_fenster(width, height):
            fenster_breite = root.winfo_screenwidth()
            fenster_hoehe = root.winfo_screenheight()
            x = (fenster_breite - width) // 2
            y = (fenster_hoehe - height) // 2

            # Leg die Position des Fensters fest
            self.top_show_f.geometry(f"{width}x{height}+{x}+{y}")
        mittig_fenster(width, height)
        

    def save_task(self, task):
        tasks = self.load_tasks_from_file()
        tasks.append(task)
        with open(self.TASK_FILE, 'w') as file:
            json.dump(tasks, file, indent=4)

    def load_tasks(self):
        self.clear_tasks_frame()
        tasks = self.load_tasks_from_file()
        for task in tasks:
            self.create_task_button(task)

    def load_tasks_from_file(self):
        if os.path.exists(self.TASK_FILE):
            with open(self.TASK_FILE, 'r') as file:
                return json.load(file)
        return []

    def delete_task(self, task):
        tasks = self.load_tasks_from_file()
        tasks = [t for t in tasks if t['name'] != task['name']]
        with open(self.TASK_FILE, 'w') as file:
            json.dump(tasks, file, indent=4)
        self.refresh_tasks()

    def refresh_tasks(self):
        self.todo_r_dispawn()
        self.clear_tasks_frame()
        self.load_tasks()

    def clear_tasks_frame(self):
        for widget in self.todo_frame_einz.winfo_children():
            widget.destroy()

if __name__ == "__main__":
    root = tk.CTk()
    width = 1920
    height = 1080
    def mittig_fenster(root, width, height):
        fenster_breite = root.winfo_screenwidth()
        fenster_hoehe = root.winfo_screenheight()
        x = (fenster_breite - width) // 2
        y = (fenster_hoehe - height) // 2
        root.geometry(f"{width}x{height}+{x}+{y}")
    mittig_fenster(root, width, height)
    app = TodoApp(root)
    root.mainloop()
