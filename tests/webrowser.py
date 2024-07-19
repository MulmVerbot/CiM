from tkinterweb import HtmlFrame #import the HTML browser
import tkinter as tk #python3
import ssl


root = tk.Tk() #create the tkinter window
frame = HtmlFrame(root) #create HTML browser
ssl._create_default_https_context = ssl._create_unverified_context
frame.load_website("www.beese-computer.de") #load a website
frame.pack(fill="both", expand=True) #attach the HtmlFrame widget to the parent window
root.mainloop()