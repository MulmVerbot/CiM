import customtkinter as tk
import json
import os
import time
Benutzerordner = os.path.expanduser('~')
tasks_pfad = os.path.join(Benutzerordner, 'CiM', 'Db')
tasks_pfad_datei = os.path.join(tasks_pfad, 'tasks.json')

try:
    if not os.path.exists(tasks_pfad):
        print("[-INFO-] Der Db Ordner scheint nicht zu existieren. Erstelle ihn nun.")
        os.mkdir(tasks_pfad)
        print("[-INFO-] Der Db Ordner wurde erfolgreich erstellt.")
except Exception as ex_einst:
    print("[-ERR-] Fehler beim Erstellen des Db Ordners. Fehlercode:", ex_einst)
TASKS_FILE = tasks_pfad_datei

class TodoApp:
    def __init__(self, root):
        self.root = root
        self.root.title("TotDo Liste Alpha 1.1")
        self.Todo_offen = False
        
        self.Zeit = time.strftime("%H:%M:%S")
        self.todo_aufmachen()

    def todo_aufmachen(self):
        self.Todo_offen = True
        self.todo_frame = tk.CTkFrame(self.root, width=600, height=380)
        self.todo_frame.place(x=100, y=100)
        self.todo_frame_einz = tk.CTkScrollableFrame(self.root, width=300, height=220)
        self.todo_frame_einz.place(x=300, y=100)
        self.Aufgaben_name_e = tk.CTkEntry(self.todo_frame)
        self.Aufgaben_Beschreibung_e = tk.CTkEntry(self.todo_frame)
        self.Aufgaben_name_e.place(x=10, y=100)
        self.Aufgaben_Beschreibung_e.place(x=10, y=70)
        self.Aufgabe_hinzufuegen_Knopp = tk.CTkButton(self.todo_frame, text="Aufgabe erstellen", command=self.create_task_button_vor)
        self.Aufgabe_hinzufuegen_Knopp.place(x=10, y=10)
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
        self.button = tk.CTkButton(self.todo_frame_einz, text=task['name'], command=lambda t=task: self.show_task(t))
        self.button.pack(padx=10, pady=5)

    def l_ja(self):
        self.delete_task(self.task)
        self.top_show_f.destroy()

    def l_nein(self):
        self.top_show_f.destroy()

    def show_task(self, task):
        self.top_show_f = tk.CTkToplevel()
        self.task = task
        ja = tk.CTkButton(self.top_show_f, text="Ja", command=self.l_ja)
        ja.pack(pady=5,padx=5)
        nein = tk.CTkButton(self.top_show_f, text="Nein", command=self.l_nein)
        nein.pack(pady=5,padx=5)
        width = 250
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
        with open(TASKS_FILE, 'w') as file:
            json.dump(tasks, file, indent=4)

    def load_tasks(self):
        self.clear_tasks_frame()
        tasks = self.load_tasks_from_file()
        for task in tasks:
            self.create_task_button(task)

    def load_tasks_from_file(self):
        if os.path.exists(TASKS_FILE):
            with open(TASKS_FILE, 'r') as file:
                return json.load(file)
        return []

    def delete_task(self, task):
        tasks = self.load_tasks_from_file()
        tasks = [t for t in tasks if t['name'] != task['name']]
        with open(TASKS_FILE, 'w') as file:
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
