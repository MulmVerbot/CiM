import tkinter as tk
import pyautogui

def create_window():
    root = tk.Tk()
    root.title("Mauszeiger-Fenster")

    # Startposition des Fensters
    start_x, start_y = 100, 100
    root.geometry(f"{start_x}x{start_y}+0+0")

    def move_window():
        # Hole die aktuelle Position des Mauszeigers
        x, y = pyautogui.position()

        # Berechne die Verschiebung
        dx, dy = 0, 0
        if x < dx:
            x += 10
        if y < dy:
            y += 10

        # Verschiebe das Fenster
        root.geometry(f"{start_x}x{start_y}+{x}+{y}")

        # Überwache die Mausbewegung alle 100 Millisekunden
        root.after(100, move_window)

    # Starte die Überwachung
    move_window()

    root.mainloop()

if __name__ == "__main__":
    create_window()
