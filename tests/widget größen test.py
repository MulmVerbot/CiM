import tkinter as tk

def update_text(text_widget):
    text = text_widget.get("1.0", "end-1c")
    text_widget.pack_forget()
    text_widget.pack()

root = tk.Tk()



text_widget = tk.Text(root, text="Dings")
text_widget.pack()

update_button = tk.Button(root, text="Text aktualisieren", command=update_text)
update_button.pack()

root.mainloop()
