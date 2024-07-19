import tkinter as tk
from tkinter import messagebox
import datetime

class HabitTracker:
    def __init__(self, root):
        self.root = root
        self.habits = {}
        self.create_widgets()

    def create_widgets(self):
        self.habit_entry = tk.Entry(self.root)
        self.habit_entry.pack()

        self.add_button = tk.Button(self.root, text="Habit hinzufügen", command=self.add_habit)
        self.add_button.pack()

        self.track_button = tk.Button(self.root, text="Habit verfolgen", command=self.track_habit)
        self.track_button.pack()

        self.show_button = tk.Button(self.root, text="Gewohnheiten anzeigen", command=self.show_habits)
        self.show_button.pack()

    def add_habit(self):
        habit_name = self.habit_entry.get()
        if habit_name:
            self.habits[habit_name] = []
            messagebox.showinfo("Erfolg", f"Gewohnheit '{habit_name}' hinzugefügt.")
        else:
            messagebox.showerror("Fehler", "Bitte geben Sie einen Habit-Namen ein.")

    def track_habit(self):
        habit_name = self.habit_entry.get()
        if habit_name in self.habits:
            self.habits[habit_name].append(datetime.date.today())
            messagebox.showinfo("Erfolg", f"Gewohnheit '{habit_name}' verfolgt.")
        else:
            messagebox.showerror("Fehler", "Habit nicht gefunden. Bitte fügen Sie zuerst die Gewohnheit hinzu.")

    def show_habits(self):
        habits_str = ""
        for habit in self.habits:
            habits_str += f"Habit: {habit}\n"
            for date in self.habits[habit]:
                habits_str += f"  - Verfolgt am: {date}\n"
        messagebox.showinfo("Gewohnheiten", habits_str)

root = tk.Tk()
app = HabitTracker(root)
root.mainloop()
