import tkinter as tk

def update_text():
    text = text_widget.get("1.0", "end-1c")
    

root = tk.Tk()
text_var = tk.StringVar()

text_widget = tk.Text(root)
text_widget.pack()

update_button = tk.Button(root, text="Text aktualisieren", command=update_text)
update_button.pack()

root.mainloop()