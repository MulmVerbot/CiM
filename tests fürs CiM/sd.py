import os
import tkinter as tk
from tkinter import messagebox

def load_todo_list(filename):
    if os.path.exists(filename):
        with open(filename, 'r') as f:
            return [line.strip() for line in f.readlines()]
    else:
        return []

def save_todo_list(todo_list, filename):
    with open(filename, 'w') as f:
        for item in todo_list:
            f.write(item + '\n')

def add_todo_item(entry, listbox):
    item = entry.get()
    if item:
        todo_list.append(item)
        listbox.insert(tk.END, item)
        entry.delete(0, tk.END)
        save_todo_list(todo_list, todo_list_file)
    else:
        messagebox.showwarning("Warnung", "Bitte geben Sie einen Eintrag ein.")

def remove_todo_item(listbox):
    try:
        index = listbox.curselection()[0]
        item = listbox.get(index)
        listbox.delete(index)
        todo_list.remove(item)
        save_todo_list(todo_list, todo_list_file)
    except IndexError:
        messagebox.showwarning("Warnung", "Bitte wählen Sie einen Eintrag aus der Liste.")

def main():
    global todo_list
    global todo_list_file
    todo_list_file = "todo_list.txt"
    todo_list = load_todo_list(todo_list_file)

    root = tk.Tk()
    root.title("To-Do-Liste")

    frame = tk.Frame(root)
    frame.pack(padx=10, pady=10)

    label = tk.Label(frame, text="To-Do-Liste")
    label.grid(row=0, column=0, columnspan=2)

    listbox = tk.Listbox(frame, width=40, height=10)
    for item in todo_list:
        listbox.insert(tk.END, item)
    listbox.grid(row=1, column=0, columnspan=2, pady=5)

    entry = tk.Entry(frame, width=30)
    entry.grid(row=2, column=0, padx=5)

    add_button = tk.Button(frame, text="Hinzufügen", command=add_todo_item)
    add_button.grid(row=2, column=1)

    remove_button = tk.Button(frame, text="Entfernen", command=remove_todo_item)
    remove_button.grid(row=3, column=0, columnspan=2, pady=5)

    root.mainloop()

if __name__ == "__main__":
    main()
