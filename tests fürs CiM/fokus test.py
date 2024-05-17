import tkinter as tk
import customtkinter

class MyFrame(customtkinter.CTkFrame):
    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs)
        # Füge Widgets zum Frame hinzu, z. B.:
        self.label = customtkinter.CTkLabel(self)
        self.label.grid(row=0, column=0, padx=20)

        self.bind("<Button-1>", lambda event: print("Dings"))

class App(customtkinter.CTk):
    def __init__(self):
        super().__init__()
        self.geometry("400x200")
        self.grid_rowconfigure(0, weight=1)
        self.grid_columnconfigure(0, weight=1)
        self.my_frame = MyFrame(master=self)
        self.my_frame.grid(row=0, column=0, padx=20, pady=20, sticky="nsew")

app = App()
app.mainloop()
