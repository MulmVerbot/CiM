import tkinter as tk

def increase_window_size():
    global window_width, window_height
    window_width += 1
    window_height += 1
    window.geometry(f"{window_width}x{window_height}")
    window.after(1, increase_window_size)

window_width = 10
window_height = 10

window = tk.Tk()
window.geometry(f"{window_width}x{window_height}")

window.after(100, increase_window_size)

window.mainloop()
# hahahah das sieht lustig aus