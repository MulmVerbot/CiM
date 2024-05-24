import tkinter as tk
einz = 0

def increase_window_size():
    global window_width, window_height, einz
    window_width = int(window_width + 1 / 2 + 1)
    if window_height <= 820 and einz == 0:
        window_height += 1
        print(f"IFFF einz ist: {einz} ; window_height ist: {window_height}")
    if window_height >=820:
        print("elif")
        print(f"einz ist: {einz} ; window_height ist: {window_height}")
        window_height -=1
        einz = 1
    if einz == 1:
        window_height -=100
    if window_height >= 0:
        einz = 0

    window.geometry(f"{window_width}x{window_height}")
    window.after(1, increase_window_size)

window_width = 10
window_height = 10

window = tk.Tk()
window.geometry(f"{window_width}x{window_height}")

window.after(100, increase_window_size)

window.mainloop()
# hahahah das sieht lustig aus