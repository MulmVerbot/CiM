import customtkinter as tka
###import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
from tkinter import filedialog
from tkinter import Menu
import time
import os
import sys
import csv
import ctypes
import json
from csv2pdf import convert as c2p_convert
from threading import Thread
from http.server import BaseHTTPRequestHandler, HTTPServer
import urllib.parse
import threading
from customtkinter import ThemeManager
import datetime

root = tka.CTk()

def optionmenu_callback(choice):
    print("optionmenu dropdown clicked:", choice)

combobox = tka.CTkOptionMenu(root, values=["option 1", "option 2"], command=optionmenu_callback)
combobox.pack(padx=20, pady=10)
combobox.set("option 2")

root.mainloop()