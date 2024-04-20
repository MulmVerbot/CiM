import tkinter as tk
import json
import customtkinter as ctk
class ToDoApp:
    def __init__(self, root):
        self.root = root
        self.root.title("To-Do List")

        self.tasks = []

        # Menü erstellen
        self.menu = tk.Menu(self.root)
        self.root.config(menu=self.menu)
        self.task_menu = tk.Menu(self.menu, tearoff=0)
        self.menu.add_cascade(label="Tasks", menu=self.task_menu)
        self.load_tasks()

        # Button zum Hinzufügen einer neuen Aufgabe
        self.add_button = tk.Button(self.root, text="Add Task", command=self.add_task)
        self.add_button.pack()

    def load_tasks(self):
        try:
            with open("tasks.json", "r") as f:
                self.tasks = json.load(f)
                for task in self.tasks:
                    self.task_menu.add_checkbutton(label=task, onvalue=True, offvalue=False)
        except FileNotFoundError:
            pass

    def save_tasks(self):
        with open("tasks.json", "w") as f:
            json.dump(self.tasks, f)

    def add_task(self):
        task = ctk.CTkInputDialog()
        task = task.get_input()
        if task:
            self.tasks.append(task)
            self.task_menu.add_checkbutton(label=task, onvalue=True, offvalue=False)
            self.save_tasks()

if __name__ == "__main__":
    root = tk.Tk()
    app = ToDoApp(root)
    root.mainloop()
