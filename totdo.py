import customtkinter as tk
import json
import os
import time


class TodoApp:
    def __init__(self, root):
        self.root = root
        self.root.title("TotDo Liste Alpha 1.2")
        self.Todo_offen = False
        Benutzerordner = os.path.expanduser('~')
        tasks_pfad = os.path.join(Benutzerordner, 'CiM', 'Db')
        tasks_pfad_datei = os.path.join(tasks_pfad, 'tasks.json')

        #### Farben #### , fg_color="White", border_color=self.Border_Farbe, border_width=2, text_color="Black", hover_color="pink"
        #self.Hintergrund_farbe = "SlateGrey"
        self.Hintergrund_farbe = "AntiqueWhite2"
        self.Hintergrund_farbe_Text_Widget = "AntiqueWhite2" #"AntiqueWhite" #"AntiqueWhite2"
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
        self.todo_aufmachen()

    def todo_aufmachen(self):
        self.Todo_offen = True
        self.todo_frame_links = tk.CTkFrame(self.root, width=200, height=1000, fg_color=self.Hintergrund_farbe, border_color=self.Border_Farbe, border_width=3, corner_radius=5)
        self.todo_frame_links.place(x=0, y=0)
        self.todo_frame_rechts = tk.CTkFrame(self.root, width=200, height=1000, fg_color=self.Hintergrund_farbe, border_color=self.Border_Farbe, border_width=3, corner_radius=5)
        self.todo_frame_rechts.place(x=1720, y=0)
        self.todo_frame_einz = tk.CTkScrollableFrame(self.root, width=820, height=800, fg_color=self.Hintergrund_farbe, border_color=self.Border_Farbe, border_width=3, corner_radius=5)
        self.todo_frame_einz.place(x=200, y=100)
        self.Aufgaben_name_e = tk.CTkEntry(self.root, placeholder_text="Titel", width=300, fg_color=self.Entry_Farbe, text_color="Black", placeholder_text_color="FloralWhite")
        self.Aufgaben_Beschreibung_e = tk.CTkEntry(self.root, placeholder_text="Beschreibung", width=300, fg_color=self.Entry_Farbe, text_color="Black", placeholder_text_color="FloralWhite")
        self.Aufgaben_name_e.place(x=1060, y=110)
        self.Aufgaben_Beschreibung_e.place(x=1060, y=150)
        self.Aufgabe_hinzufuegen_Knopp = tk.CTkButton(self.root, text="Aufgabe erstellen", command=self.create_task_button_vor, fg_color="White", border_color=self.Border_Farbe, border_width=2, text_color="Black", hover_color="pink")
        self.Aufgabe_hinzufuegen_Knopp.place(x=1120, y=240)
        self.load_tasks()

    def todo_zumachen(self):
        print("todo_zumachen(def)")
        try:
            self.button.pack_forget()
        except:
            print("button ist noch da.")
        self.todo_frame.place_forget()
        self.todo_frame_einz.place_forget()
        self.Aufgaben_name_e.place_forget()
        self.Aufgaben_Beschreibung_e.place_forget()
        self.Aufgabe_hinzufuegen_Knopp.place_forget()
        self.Todo_offen = False

    def create_task_button_vor(self):
        task_name = self.Aufgaben_name_e.get()
        self.Zeit = time.strftime("%H:%M:%S")
        
        if task_name:
            task_description = self.Aufgaben_Beschreibung_e.get()
            if task_description:
                task_name = f"{self.Zeit}\n{task_name}\nBeschreibung: {task_description}"
                self.task = {'name': task_name, 'description': task_description}
                self.save_task(self.task)
                self.create_task_button(self.task)

    def create_task_button(self, task):
        self.button = tk.CTkButton(self.todo_frame_einz, text=task['name'], command=lambda t=task: self.show_task(t), fg_color="White", border_color=self.Border_Farbe, border_width=2, text_color="Black", hover_color="pink")
        self.button.pack(padx=10, pady=5)

    def l_ja(self):
        self.delete_task(self.task)
        self.top_show_f.destroy()

    def l_nein(self):
        self.top_show_f.destroy()

    def show_task(self, task):
        self.top_show_f = tk.CTkToplevel()
        self.task = task
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
        self.clear_tasks_frame()
        self.load_tasks()

    def clear_tasks_frame(self):
        for widget in self.todo_frame_einz.winfo_children():
            widget.destroy()

if __name__ == "__main__":
    root = tk.CTk()
    width = 720
    height = 420
    def mittig_fenster(root, width, height):
        fenster_breite = root.winfo_screenwidth()
        fenster_hoehe = root.winfo_screenheight()
        x = (fenster_breite - width) // 2
        y = (fenster_hoehe - height) // 2

        # Leg die Position des Fensters fest
        root.geometry(f"{width}x{height}+{x}+{y}")
    mittig_fenster(root, width, height)
    app = TodoApp(root)
    root.mainloop()
