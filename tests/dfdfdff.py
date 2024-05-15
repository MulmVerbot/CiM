import customtkinter
from tkinterdnd2 import DND_FILES

def drop(event):
    # do operations with event.data file
    label.configure(text=event.data)
                    
root = customtkinter.CTk()
root.geometry("500x200")

label = customtkinter.CTkLabel(root, text="➕ \nDrag & Drop Here", corner_radius=10, fg_color="blue", wraplength=300)
label.pack(expand=True, fill="both", padx=40, pady=40)

# Add this 2 lines to make it a dnd widget
label.drop_target_register(DND_FILES)
label.dnd_bind('<<Drop>>', drop)

root.mainloop()