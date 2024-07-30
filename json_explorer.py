import json
import tkinter as Atk
from tkinter import ttk, filedialog, messagebox
import os

class JSONTreeView:
    def __init__(self, root):
        self.root = root
        self.Version = "1.0.1"
        self.root.title("JSON Datei betracher " + self.Version)
        
        self.tree = ttk.Treeview(root)
        self.tree.pack(expand=True, fill='both')
        scrollbar = Atk.Scrollbar(self.tree, orient=Atk.VERTICAL)
        scrollbar.pack(side=Atk.RIGHT, fill=Atk.Y)
        self.tree.config(yscrollcommand=scrollbar.set)
        scrollbar.config(command=self.tree.yview)

        laden = Atk.Button(root, text="JSON Datei laden...", command=self.load_json_file)
        laden.pack()
        speichern = Atk.Button(root, text="JSON Datei Speichern")
        speichern.pack()
        DB_laden = Atk.Button(root, text="DB öffnen", command=self.load_json_file_standard)
        DB_laden.pack()

    def load_json_file_standard(self):
        self.Benutzerordner = os.path.expanduser('~')
        self.Db_Ordner_pfad = os.path.join(self.Benutzerordner, 'CiM', 'Db')
        self.Json_pfad = os.path.join(self.Db_Ordner_pfad, 'Db.json')
        file_path = self.Json_pfad
        with open(file_path, 'r+') as f:
            self.json_data = json.load(f)
            self.populate_tree(self.json_data)

    def load_json_file(self):
        file_path = filedialog.askopenfilename(filetypes=[("JSON files", "*.json")])
        if file_path:
            with open(file_path, 'r') as f:
                self.json_data = json.load(f)
            self.populate_tree(self.json_data)

    def save_json_file(self):
        file_path = filedialog.asksaveasfilename(defaultextension=".json", filetypes=[("JSON files", "*.")])
        if file_path:
            self.json_data = self.tree_to_dict(self.tree.get_children())
            with open(file_path, 'w') as f:
                json.dump(self.json_data, f, indent=4)
            messagebox.showinfo("Info", "File saved successfully")

    def populate_tree(self, data, parent=''):
        if isinstance(data, dict):
            for key, value in data.items():
                node_id = self.tree.insert(parent, 'end', text=key, values=(self.get_display_value(value),))
                self.tree.item(node_id, open=True)  # Knoten sofort ausklappen
                self.populate_tree(value, node_id)
        elif isinstance(data, list):
            for index, item in enumerate(data):
                node_id = self.tree.insert(parent, 'end', text=f"[{index}]", values=(self.get_display_value(item),))
                self.tree.item(node_id, open=True)  # Knoten sofort ausklappen
                self.populate_tree(item, node_id)
        else:
            self.tree.insert(parent, 'end', text=data)

    def get_display_value(self, value):
        if isinstance(value, (dict, list)):
            return type(value).__name__
        return str(value)

    def tree_to_dict(self, children):
        result = {}
        for child in children:
            item = self.tree.item(child)
            key = item['text']
            values = self.tree.item(child, 'values')
            children = self.tree.get_children(child)
            if children:
                result[key] = self.tree_to_dict(children)
            else:
                value = values[0]
                result[key] = self.convert_value(value)
        return result

    def convert_value(self, value):
        try:
            return json.loads(value)
        except json.JSONDecodeError:
            return value

root = Atk.Tk()
app = JSONTreeView(root)
root.mainloop()
