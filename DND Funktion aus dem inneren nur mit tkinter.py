import tkinter as tk

class DragAndDropApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Drag & Drop Dateipfad")
        self.root.geometry("500x200")

        self.label = tk.Label(root, text="➕ \nDrag & Drop Here", font=("Helvetica", 12), wraplength=300)
        self.label.pack(expand=True, fill="both", padx=40, pady=40)

        # Bind events for drag and drop
        self.label.bind("<Enter>", self.on_enter)
        self.label.bind("<Leave>", self.on_leave)
        self.label.bind("<Button-1>", self.start_drag)

        self.drag_data = {"x": 0, "y": 0}

    def on_enter(self, event):
        self.label.config(bg="lightblue")

    def on_leave(self, event):
        self.label.config(bg="white")

    def start_drag(self, event):
        self.drag_data["x"] = event.x
        self.drag_data["y"] = event.y

        self.label.bind("<B1-Motion>", self.on_drag)
        self.label.bind("<ButtonRelease-1>", self.end_drag)

    def on_drag(self, event):
        x, y = self.drag_data["x"], self.drag_data["y"]
        dx = event.x - x
        dy = event.y - y
        self.label.place(x=self.label.winfo_x() + dx, y=self.label.winfo_y() + dy)

    def end_drag(self, event):
        self.label.unbind("<B1-Motion>")
        self.label.unbind("<ButtonRelease-1>")

        # Get the final position
        final_x, final_y = self.label.winfo_x(), self.label.winfo_y()
        print(f"End position: ({final_x}, {final_y})")

if __name__ == "__main__":
    root = tk.Tk()
    app = DragAndDropApp(root)
    root.mainloop()
