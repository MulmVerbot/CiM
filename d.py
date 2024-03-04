import customtkinter as ctk
import tkinterweb
import tkinter as tk

class WebBrowser(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.title('Python WebBrowser')
        self.geometry('800x600')

        self.url_entry = ctk.CTkEntry(self, placeholder_text="Enter URL")
        self.url_entry.pack(fill=tk.X, padx=20, pady=20)

        self.go_button = ctk.CTkButton(self, text="Go", command=self.load_url)
        self.go_button.pack(pady=10)

        self.web_frame = tk.Frame(self)
        self.web_frame.pack(fill=tk.BOTH, expand=True)

        self.web_view = tkinterweb.HtmlFrame(self.web_frame)
        self.web_view.pack(fill=tk.BOTH, expand=True)

    def load_url(self):
        url = self.url_entry.get()
        self.web_view.load_website(url)

if __name__ == '__main__':
    app = WebBrowser()
    app.mainloop()