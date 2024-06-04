import tkinter as tk
import pyautogui
import time

def move_window():
    d = tk.Toplevel()
    mouse_x, mouse_y = pyautogui.position()
    d.geometry(f"300x150+{mouse_x + 24}+{mouse_y + 24}")
    mouse_x, mouse_y = pyautogui.position()
    

window = tk.Tk()
window.title("Dings")
window.geometry("300x150")

mouse_label = tk.Label(window, text="")
mouse_label.pack()

for z in range(100):
    print("z")
    move_window()

window.mainloop()
