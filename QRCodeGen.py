import tkinter as tk
import qrcode
from PIL import Image
from tkinter import filedialog
from tkinter import messagebox
from tkinter import Menu
import sys
#            _ .-') _             .-') _                   
#           ( (  OO) )           ( OO ) )                  
#           \     .'_  .---.,--./ ,--,'   ,--.   .-----.  
#           ,`'--..._)/_   ||   \ |  |\  /  .'  / ,-.   \ 
#           |  |  \  ' |   ||    \|  | ).  / -. '-'  |  | 
#           |  |   ' | |   ||  .     |/ | .-.  '   .'  /  
#           |  |   / : |   ||  |\    |  ' \  |  |.'  /__  
#           |  '--'  / |   ||  | \   |  \  `'  /|       | 
#           `-------'  `---'`--'  `--'   `----' `-------'  <- 2025 ->
class QRDings:
    def __init__(self, master):
        self.master = master
        self.Programm_Name = "QR-Code Generator"
        self.Version = "1.0.1"
        print(f"[-VERSION-] {self.Version}")
        self.Zeit = "Die Zeit ist eine Illusion."
        master.title(self.Programm_Name + " " + self.Version)
        root.resizable(False, False)

        self.output_path = None
        self.data = None
        self.Bild_Pfad = None
        if sys.platform == "darwin":
            self.Windows = False
            print("[-Plattform-] Darwin")
        else:
            self.Windows = True
            print("[-Plattform-] Windows")

        self.Inhalt_l = tk.Label(root, text="Link oder Text des QR-Codes")
        self.Inhalt_l.place(x=10,y=70)
        if self.Windows == True:
            self.Inhalt_eingabe = tk.Entry(root, width=50)
            self.Bild_pfad_e = tk.Entry(root, width=50)
        else:
            self.Inhalt_eingabe = tk.Entry(root, width=20)
            self.Bild_pfad_e = tk.Entry(root, width=20)
        self.Inhalt_eingabe.place(x=10,y=100)


        self.Inhalt_l1 = tk.Label(root, text="Bild des QR-Codes (Optional)")
        self.Inhalt_l1.place(x=10,y=170)
        
        self.Bild_pfad_e.place(x=10,y=200)

        self.Erstellen_mit_Bild = tk.Button(root, text="QR-Code generieren...", command=self.Daten_vorbereiten)
        self.Erstellen_mit_Bild.place(x=100,y=290)

        self.Bild_einf_k = tk.Button(root, text="Bild einfügen...", command=self.Bild_einf_c)
        self.Bild_einf_k.place(x=10,y=230)

        ### Nur das Menu zeugs
        self.menu = Menu(root)
        root.configure(menu=self.menu)
        self.menudings = Menu(self.menu, tearoff=0)
        self.menu.add_cascade(label=self.Programm_Name  + " " + self.Version, menu=self.menudings)
        self.menudings.add_command(label="Info", command=self.info)
    ###

    def info(self):
        messagebox.showinfo(title=self.Programm_Name, message=self.Programm_Name + " " + self.Version + "\nProgrammiert von D1n62,\nhttps://dings.software für mehr Informationen")


    def Bild_einf_c(self):
        print("Bild_einf_c(def)")
        self.Bild_Pfad = filedialog.askopenfilename(defaultextension=".png",filetypes=[("Bild", "*.png")])
        if self.Bild_Pfad == "" or None:
            messagebox.showinfo(title=self.Programm_Name, message="Vorgang wurde abgebrochen.")
            return
        try:
            self.Bild_pfad_e.delete(0, tk.END)
        except:
            pass
        self.Bild_pfad_e.insert(0, self.Bild_Pfad)

    def Daten_vorbereiten(self):
        self.data = None
        self.data = self.Inhalt_eingabe.get()
        self.Bild_Pfad = self.Bild_pfad_e.get()
        
        if self.data == "" or None:
            messagebox.showerror(title=self.Programm_Name, message="Bitte geben Sie zuerst einen Inhalt an!")
            return
        else:
            self.data.strip()
        self.output_path = filedialog.asksaveasfilename(title="QR-Code speichern unter...", defaultextension=".png",filetypes=[("Bild", "*.png"), ("Alle Dateien", "*.*"),])
        if self.output_path and self.Bild_Pfad != "" or None:
            try:
                self.code_erstellen_mit_bild()
            except:
                messagebox.showerror(title=self.Programm_Name, message="Beim erstellen des QR-Codes ist ein Fehler aufgetreten, womöglich waren es zu viele Zeichen?")
        elif self.output_path:
            try:
                self.ohne_Bild()
            except:
                messagebox.showerror(title=self.Programm_Name, message="Beim erstellen des QR-Codes ist ein Fehler aufgetreten, womöglich waren es zu viele Zeichen?")
        else:
            messagebox.showinfo(title=self.Programm_Name, message="Vorgang wurde abgebrochen.")


    def code_erstellen_mit_bild(self):
        empty_center_ratio = 0.3
        qr_size = 500
        data = self.data
        output_path = self.output_path
        bild_pfad = self.Bild_Pfad  # Pfad zum Bild, das in die Mitte eingefügt werden soll
        qr = qrcode.QRCode(
            error_correction=qrcode.constants.ERROR_CORRECT_H  # Hoher Fehlerkorrekturgrad für das Bild in der Mitte
        )
        qr.add_data(data)
        qr.make(fit=True)
        hauptfarbe = (57, 147, 133, 255)  # #399385
        qr_img = qr.make_image(fill_color=hauptfarbe, back_color="white").convert("RGBA")
        qr_img = qr_img.resize((qr_size, qr_size), Image.LANCZOS)

        empty_center_size = int(qr_size * empty_center_ratio)
        center_x, center_y = (qr_size - empty_center_size) // 2, (qr_size - empty_center_size) // 2      
        try:
            center_img = Image.open(bild_pfad).convert("RGBA")
            center_img = center_img.resize((empty_center_size, empty_center_size), Image.LANCZOS)

            qr_img.paste(center_img, (center_x, center_y), center_img) 
        except FileNotFoundError:
            messagebox.showerror(title="Fehler", message="Das Bild für die Mitte wurde nicht gefunden.")
            return

        try:
            qr_img.save(output_path)
            messagebox.showinfo(title=self.Programm_Name, message="QR-Code gespeichert.")
        except PermissionError:
            messagebox.showerror(title="Fehler", message="Keine Schreibberechtigung für dieses Verzeichnis vorhanden.")

    
        self.output_path = None
        self.data = None
        self.Bild_Pfad = None
        self.Inhalt_eingabe.delete(0, tk.END)
        self.Bild_pfad_e.delete(0, tk.END)

    def ohne_Bild(self):
        qr_size = 500
        data = self.data
        output_path = self.output_path

        qr = qrcode.QRCode(
            error_correction=qrcode.constants.ERROR_CORRECT_H  # Hoher Fehlerkorrekturgrad
        )
        qr.add_data(data)
        qr.make(fit=True)

        hauptfarbe = (57, 147, 133, 255)  # #399385
        qr_img = qr.make_image(fill_color=hauptfarbe, back_color="white").convert("RGBA")
        qr_img = qr_img.resize((qr_size, qr_size), Image.LANCZOS)

        
        try:
            qr_img.save(output_path)
            messagebox.showinfo(title=self.Programm_Name, message="QR-Code gespeichert.")
        except PermissionError:
            messagebox.showerror(title="Fehler", message="Keine Schreibberechtigung für dieses Verzeichnis vorhanden.")

        self.output_path = None
        self.data = None

if __name__ == "__main__":
    root = tk.Tk()
    width = 420
    height = 420
    def mittig_fenster(root, width, height):
        root.update_idletasks()
        fenster_breite = root.winfo_screenwidth()
        fenster_höhe = root.winfo_screenheight()
        x = (fenster_breite - width) // 2
        y = (fenster_höhe - height) // 2
        root.geometry(f"{width}x{height}+{x}+{y}") # Das ist da um das Fenster mittig aufm Hauptmonitor zu spawnen, funktioniert in 30% der Fälle..
    mittig_fenster(root, width, height)
    QRDings = QRDings(root)
    root.mainloop()