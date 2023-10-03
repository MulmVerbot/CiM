###############################################################
## ________     _____   ________    ________   ________      ##
##|\   ___ \   / __  \ |\   ___  \ |\   ____\ |\   ____\     ##
##\ \  \_|\ \ |\/_|\  \\ \  \\ \  \\ \  \___| \ \  \___|_    ##
## \ \  \ \\ \\|/ \ \  \\ \  \\ \  \\ \  \  ___\ \_____  \   ##
##  \ \  \_\\ \    \ \  \\ \  \\ \  \\ \  \|\  \\|____|\  \  ##
##   \ \_______\    \ \__\\ \__\\ \__\\ \_______\ ____\_\  \ ##
##    \|_______|     \|__| \|__| \|__| \|_______||\_________\##
##                                               \|_________|##
##                            D1ng5                          ##
############################################################### 2022 - 2023
try:
    import tkinter as tk
    from tkinter import filedialog
    from tkinter import *
    from tkinter import ttk
    import zipfile
    import os
    import pyzipper
    import time
    from tkinter import messagebox
    import pyautogui
    import json as json
    from tkinterdnd2 import *
    from cryptography.fernet import Fernet
    import tkinter.font as tkFont
    import tkinter.ttk as ttk
    import sys
    #import webbrowser
    import PIL
    from PIL import ImageTk, Image
    from threading import Thread
    import subprocess
    import shutil
    #import shlex
    import ctypes
except:
    messagebox.showinfo(title='Information', message="Fehler 88: Schwerwiegemder Fehler, das Programm konnte nicht gestartet werden, Bitte wenden Sie sich an den Entwickler!")
    sys.exit()
try:
    #import pywin32_system32
    #import win32
    import win32com.client
    import winreg
    Windows = "1"
    print("[-INFO-] Nutzer scheint auf Windows zu sein, konnte die win32com.client und winreg laden.")
except:
    print("[-INFO-] Nutzer ist nicht auf Windows bzw konnte ich die libs win32com.client und winreg nicht finden")
    Windows = "0"
#    messagebox.showinfo(title='Information', message="Fehler 88.1: Sie scheinen sich nicht auf Windows zu befinden, die Email Funktion wird möglicher weise nicht richtig Funtkionieren.")
    pass


# +++++ HALT BEVOR DU HIER WEITERMACHST++++++++++
# gibt nix zu sagen.


def mittig_fenster(root, width, height):
    fenster_breite = root.winfo_screenwidth()
    screen_height = root.winfo_screenheight()
    x = (fenster_breite - width) // 2
    y = (screen_height - height) // 2

    # Leg die Position des Fensters fest
    root.geometry(f"{width}x{height}+{x}+{y}")


#root = tk.Tk()

root = TkinterDnD.Tk()
root.attributes('-toolwindow', True)
    #print("[FATAL] Fehler beim Laden der tkinterDnD2 lib, Nutzer ist wohl auf Apple Silicon Mac")
    #messagebox.showerror(title="Es ist ein schwerer Fehler aufgetren", message="Diese Software ist nicht für Arm86/M1/M2 Prozessoren konfiguriert, Wenn dieser Fehler dennoch bestehen bleibt wenden Sie sich an den Support, DND wurde deaktiviert und das Programm läuft weiter. ")


class App(tk.Frame):

    class Logger(object):

        def __init__(self): #eine init welche nur das "unwichtige" vorgeplänkel macht
            try:
                with open ("einstellungen/log_einst.json", "r") as Ei:
                    geladen_fuer_log = json.load(Ei)
                self.Neu_gewählterordner_für_logs = geladen_fuer_log["Log_pfad"]
                print('[-INFO-] ',geladen_fuer_log["Log_pfad"])#und jetzt hier der rest welcher sagt was von der json es ist
                self.log_ordner_speicherort = self.Neu_gewählterordner_für_logs
                print("[-INFO-] Das Laden des log Pfades aus der Datei hat geklappt.")
                print("[-INFO-] Entgüliger ort:" , self.log_ordner_speicherort)
                
            except:
                print("[-ERR-] hier ist was schiefgegangen, da war wohl kein log ordner gespeichert, nutze nun den standart ort")
                self.log_ordner_speicherort = "logs/"
            self.tag_und_zeit_string = time.strftime("%m/%d/%Y, %H:%M:%S")
            self.tag_string = str(time.strftime("%d %m %Y"))
            print("[-INFO-] ",self.tag_und_zeit_string)
            try:
                log_pfad = (self.log_ordner_speicherort + self.tag_string + ".log")
                self.terminal = sys.stdout
                self.log = open(log_pfad, "w")
                print("[-INFO-] Der zweite teil vom log hat direkt geklappt.")
            except:
                print("[-ERR-] Das mit den Logs hat nicht geklappt")
                self.log_ordner_speicherort = "logs/"
                try:
                    print("[-INFO-] neuer anlauf mit dem standart log verzeichnis")
                    log_pfad = (self.log_ordner_speicherort + self.tag_string + ".log")
                    self.terminal = sys.stdout
                    self.log = open(log_pfad, "a")
                    print("[-INFO-] der zweite teil vom log hat geklappt.")
                except:
                    print("[-FATAL-] Log Verzeichnis Laden ist abgetürzt ")

   
        def write(self, message):
            self.terminal.write(message)
            self.log.write(message)

        def flush(self):
            #für Python 3 wichtig wegen kompatibilität, hab aber keine wirkliche ahnung was das macht
            pass    
    sys.stdout = Logger()

    
    print("[-INFO-] gucke ob alle assets da sind...")
    if os.path.exists("assets/Bild11.png"):
        print("[-INFO-] Alle assets vorhanden.")
    else:
        print("[-FATAL-] Fehler, es sind NICHT alle assets vorhanden.")
        print("[-INFO-] assets/Bild11.png fehlt")
        messagebox.showerror(title="Fehler 8", message="Fehler bei der Überprüfung der assets, bitte wenden Sie sich an dem Support.")
        sys.exit()
    #except:
    #    messagebox.showerror(title="Fehler 8", message="Fehler bei der Überprüfung der assets, bitte wenden Sie sich an dem Support.")

    def __init__(self, master=None):
        super().__init__(master)
        #print(sys.path) # zeigt die Installieren libs
        
        self.master = master
        self.pack(fill="both", expand=True)
        self.Kontakt_Passwort = 0
        self.kontaktM = 0
        self.tree_iz_da = 0
        self.Kontakt_löschen_knopp_iz_da = 0
        self.kbe_k_iz_da = 0
        self.Passwort1 = ""
        self.Version = " 1.0.2.2"
        self.Hintergrund_farbe = "#e6edfa"
        self.speicherort = "output/"
        self.Dings = ""  #Kunden PW
        self.Bums = ""   #Passwort des ITler welcher ein paar mehr möglichkeiten zur Überwachung/den Support hat
        self.Ja = "" # Das Passwort für die einzig Wahren :)
        key = b'bymG7hj4Je81pMS-hRdzxRR6qn5ldSce6gsR-z-nydc='
        keyadm = b'1Zip_QLmN0lumCsBguydMSLLzcpjtgk9seV_x9p0wSw='
        keyMulm = b'fOGZ_MiCiXTWt-l4sRmTvJrYiv88PSiRRQu8ZZ7L9Os='
        self.fernet = Fernet(key)
        self.fernetadm = Fernet(keyadm)
        self.fernetdev = Fernet(keyMulm)
        self.Absturz_meldung = "Ein Schwerwiegender Fehler ist aufgetreten, Bitte starten sie das Programm Neu um Fortzufahren, wenn diese Meldung bestehen bleibt wenden sie sich bitte an den Support"
        self.entrydnd = tk.Entry(self)
        self.entry21_r1 = self.entrydnd.get()
        self.tag_und_zeit_string = time.strftime("%m/%d/%Y, %H:%M:%S")
        self.KTK_Speicherort = ""
        self.Datei_gezogen = 0
        self.dieser_komische_grünton = "#abf5bf"
        self.vnv = 1
        self.etwas_bereits_eingefügt = 0
       
        
        
        print("[-INFO-] ", self.tag_und_zeit_string)
        if Windows == "0":
            print("[-INFO-] Nutzer ist echt nicht auf Windows: 'Windows' var = " + Windows)
        
        #self.cfg = configparser.ConfigParser()
        #self.cfg.read("Einstellungen.ini")
        #try:
        with open ("einstellungen/outp_einst.json", "r") as g:
            self.geladene_einst_zip = json.load(g)
            print("[-INFO-] ",self.geladene_einst_zip)
        try:
            with open ("einstellungen/outp_einst.json", "r") as Eiz:
                geladen_fuer_zip = json.load(Eiz)
            #if geladen_fuer_log["Log_pfad"]:
            #    print("Die einstellung heißt: ")
            #    print(geladen_fuer_log)
            #    self.log_ordner_speicherort = geladen_fuer_log
            
            self.Neu_gewählterordner_für_zip = geladen_fuer_zip["Zip_pfad"]
            print('[-INFO-] geladen_fuer_zip["Zip_pfad"]: ', geladen_fuer_zip["Zip_pfad"])#und jetzt hier der rest welcher sagt was von der json es ist
            self.zip_ordner_speicherort = self.Neu_gewählterordner_für_zip
            print("[-INFO-] Das eine zip einst hat geklappt.")
            print("[-INFO-] self.zip_ordner_speicherort:", self.zip_ordner_speicherort)
        except:
            print("[-WARN-] hier ist was schiefgegangen, da war wohl kein zip ordner gespeichert. Nutze nun den Standard output ordner.")
            self.zip_ordner_speicherort = "output/"
        try:
            with open("usr.txt", "rb") as KPW:
                KndPW = KPW.read()
                print("[-INFO-] Das momentane Passwort lautet: ", KndPW)
                KnDPW_Entschlt = self.fernet.decrypt(KndPW)
                KnDPW_Entschlt = KnDPW_Entschlt.decode('utf-8')
                #print("[-INFO-]  Das entschlüsselte Kunden Passwort Lautet: ", KnDPW_Entschlt)
                self.Dings = KnDPW_Entschlt
        except:
                print("[-FATAL-] KundenPW: kann kein pw finden in der txt.")
                self.Dings = "89037599980345jth23hjjk2nglnvlsbnfgdsjglsfgjklsdgjdskgjkwlej45k634k634jk6l56kl4j6lö3j63k4j6kl45nggkdöjsgksjk"

        try:
            with open("admn.txt", "rb") as aPW:
                admPW = aPW.read()
                print("[-INFO-] Das momentane Passwort lautet: ", admPW)
                admPW_Entschlt = self.fernetadm.decrypt(admPW)
                admPW_Entschlt = admPW_Entschlt.decode('utf-8')
                #print("[-INFO-]  Das entschlüsselte Admin Passwort Lautet: ", admPW_Entschlt)
                self.Bums = admPW_Entschlt
        except:
                print("[-FATAL-] AdminPW: kann kein pw finden in der txt.")
                self.Bums = "JHKASFLAHAHAHAHHAHAHAHAHAHAHAHAHHAHAHAHAHAOROAC"

        try:
            with open("dev.txt", "rb") as dPW:
                devPW = dPW.read()
                print("[-INFO-] Das Momentane Dev PW lautet: ", devPW)
                dev_Entschlt = self.fernetdev.decrypt(devPW)
                dev_Entschlt = dev_Entschlt.decode('utf-8')
                #print("[-INFO-] Das entschlüsselte Dev PW lautet: ", dev_Entschlt)
                self.Ja = dev_Entschlt
        except:
                print("[-ERR-] DevPW: kann kein pw finden in der txt.")
                self.Ja = "CmsWsf14Mulm"

        self.configure(bg="#e6edfa")
    #    self.create_widgets()
        self.master.title("CMS Zipa" + self.Version)
        self.menu = Menu(root)
        root.config(menu=self.menu)
        self.filemenu = Menu(self.menu, tearoff=0)
        self.filemenu2 = Menu(self.menu, tearoff=0)
        #self.bind_event()
        
        
        try:
            with open("einstellungen/design.json", "r") as design_data:
                self.geladene_design_einst = json.load(design_data)
                if self.geladene_design_einst["Design_mode"] == "Windoof":
                    print("[-INFO-] Windoof Design wird genutzt.")
                elif self.geladene_design_einst["Design_mode"] == "Modern":
                    print("[-INFO-] Die Design einstellung scheint Modern zu sein.")
                else:
                    print("[-WARN-] Die Datei ist zwar vorhanden aber die Einstellung konnte nicht geladen(Design)")
                    self.geladene_design_einst = ""
        except:
            print("[-ERR-] Design Einstellungen konnten nicht geladen werden.")
            self.geladene_design_einst = ""

        try:
            with open("einstellungen/Kontaktliste_Speicherort.json" , "r") as KtkSpOt_data:
                self.Ktk_speichOt = json.load(KtkSpOt_data)
                print('[-INFO-] self.Ktk_speichOt["Kontaktliste_Speicherort"]: ', self.Ktk_speichOt["Kontaktliste_Speicherort"])
                self.KTK_Speicherort = (self.Ktk_speichOt["Kontaktliste_Speicherort"])
        except PermissionError:
                print("[-FATAL-] Die berechtigung zum Beschreiben fehlt.")
                messagebox.showerror(title="Fehlercode 20", message="Es Fehlt für diesen Ordner die nötige Berechtigung, Die Kontakliste konnte nicht aufgerufen werden.")
        except:
            print("[-FATAL-] Der für die KTK gewählte Ordner Existiert nicht.")
            messagebox.showerror(title="Fehlercode 19", message="Der Pfad konnte zwar gelesen werden, allerdings scheint der Ausgewählte Ordner nicht zu existieren.")

        try:
            with open ("einstellungen/Kontaktliste_Speicherort.json", "r") as ktk:
                geladen_fuer_ktk = json.load(ktk)
            self.Neu_gewählterordner_für_ktk = geladen_fuer_ktk["Kontaktliste_Speicherort"]
            print('[-INFO-] geladen_fuer_ktk["Kontaktliste_Speicherort"]: ', geladen_fuer_ktk["Kontaktliste_Speicherort"])
            self.ktk_ordner_speicherort = self.Neu_gewählterordner_für_ktk
            print("[-INFO-] Ort für Die KTK wurde geladen.")
            print("[-INFO-] Endgüliger ort der ktk: ", self.ktk_ordner_speicherort)
        except:
            print("[-ERR-] hier ist was schiefgegangen, da war wohl kein ktk ordner gespeichert, nutze nun den Standart Ort im Programmverzeichnis.")
            self.ktk_ordner_speicherort = "/"

        if (self.geladene_design_einst["Design_mode"] == "Windoof"):
            self.Anmelde_entry = tk.Entry(self, show="*")
            self.Anmelde_Knopp = tk.Button(self, text="Anmelden", highlightbackground=self.Hintergrund_farbe, bg=self.Hintergrund_farbe, command="")
            self.PW_F_Knopp = tk.Button(self, text="Passwort einstellen", command=self.PW_Check)
            self.KonvKnopp = tk.Button(self, text="Umwandeln", command=self.beides, background="#f59090", foreground="Black")
      
            self.Kontakte_AnzeigenMainMenu = tk.Button(self, text="Kontakte anzeigen", command= self.Krams)
            self.TauschenLBundEN = tk.Button(self, text="eigenes Passwort verwenden", command=self.TLBUEN)
            self.Thunderbird_anEmail_anfügen = tk.Button(self, text="an neue Email anfügen", highlightbackground="lightsteelblue", command=Thunderbird)
            self.Kontakte_Einfügen_Knopp_zeigen = tk.Button(self, text="Kontakt Erstellen", highlightbackground="lightsteelblue", command=self.NeuenKontaktHinzufügen, bg="#f5da90", fg="Black")
            self.Kontakt_löschen = tk.Button(self, text="Löschen", command= self.Kontakt_löschen_bst_c)
    
            self.KTLS = tk.Button(self, text="x", highlightbackground="lightsteelblue", command= self.KTLS_C)
            self.Beb_Knopp = tk.Button(self, text="Kontakt bearbeiten", command=self.kBe)
            self.Kontakt_löschen = tk.Button(self, text="löschen", command= self.Kontakt_löschen_bst_c)

        elif (self.geladene_design_einst["Design_mode"] == "Modern"):
            self.Anmelde_entry = tk.Entry(self, show="*")
            self.Anmelde_Knopp = tk.Button(self, text="Anmelden", highlightbackground=self.Hintergrund_farbe, command="",  relief=tk.RAISED, bd=3, compound=tk.CENTER,bg="#3366CC", fg="white", font=("Helvetica", 12), padx=10, pady=5, borderwidth=0, highlightthickness=0, activebackground="#6699FF")
            self.PW_F_Knopp = tk.Button(self, text="Passwort einstellen", highlightbackground="lightsteelblue" , command=self.PW_Check,  relief=tk.RAISED, bd=3, compound=tk.CENTER, bg="#3366CC", fg="white", font=("Helvetica", 12), padx=10, pady=5, borderwidth=0, highlightthickness=0, activebackground="#6699FF")
            self.KonvKnopp = tk.Button(self, text="Umwandeln", highlightbackground="lightsteelblue", command=self.beides,  relief=tk.RAISED, bd=3, compound=tk.CENTER, bg="#3366CC", fg="white", font=("Helvetica", 12), padx=10, pady=5, borderwidth=0, highlightthickness=0, activebackground="#6699FF")
         
            self.Kontakte_AnzeigenMainMenu = tk.Button(self, text="Kontakte anzeigen", command= self.Krams, relief=tk.RAISED, bd=3, compound=tk.CENTER, bg="#3366CC", fg="white", font=("Helvetica", 12), padx=10, pady=5, borderwidth=0, highlightthickness=0, activebackground="#6699FF")
            self.TauschenLBundEN = tk.Button(self, text="eigenes Passwort verwenden", command=self.TLBUEN,  relief=tk.RAISED, bd=3, compound=tk.CENTER, bg="#3366CC", fg="white", font=("Helvetica", 12), padx=10, pady=5, borderwidth=0, highlightthickness=0, activebackground="#6699FF")
           
            self.Thunderbird_anEmail_anfügen = tk.Button(self, text="an neue Email anfügen", highlightbackground="lightsteelblue", command=Thunderbird, relief=tk.RAISED, bd=3, compound=tk.CENTER, bg="#3366CC", fg="white", font=("Helvetica", 12), padx=10, pady=5, borderwidth=0, highlightthickness=0, activebackground="#6699FF" )
            self.Kontakte_Einfügen_Knopp_zeigen = tk.Button(self, text="+", highlightbackground="lightsteelblue", command=self.NeuenKontaktHinzufügen, relief=tk.RAISED, bd=3, compound=tk.CENTER, bg="#3366CC", fg="white", font=("Helvetica", 12), padx=10, pady=5, borderwidth=0, highlightthickness=0, activebackground="#6699FF")
            self.Kontakt_löschen = tk.Button(self, text="Löschen", command= self.Kontakt_löschen_bst_c, relief=tk.RAISED,border=10, bd=3, compound=tk.CENTER, bg="#3366CC", fg="white", font=("Helvetica", 12), padx=10, pady=5, borderwidth=0, highlightthickness=0, activebackground="#6699FF")
            self.KTLS = tk.Button(self, text="x", highlightbackground="lightsteelblue", command= self.KTLS_C,  relief=tk.RAISED,border=10, bd=3, compound=tk.CENTER, bg="#3366CC", fg="white", font=("Helvetica", 12), padx=10, pady=5, borderwidth=0, highlightthickness=0, activebackground="#6699FF")
            self.Beb_Knopp = tk.Button(self, text="Kontakt bearbeiten", command=self.kBe, relief=tk.RAISED,border=10, bd=3, compound=tk.CENTER, bg="#3366CC", fg="white", font=("Helvetica", 12), padx=10, pady=5, borderwidth=0, highlightthickness=0, activebackground="#6699FF")
            self.Kontakt_löschen = tk.Button(self, text="löschen", command= self.Kontakt_löschen_bst_c, relief=tk.RAISED,border=10, bd=3, compound=tk.CENTER, bg="#3366CC", fg="white", font=("Helvetica", 12), padx=10, pady=5, borderwidth=0, highlightthickness=0, activebackground="#6699FF")
            
        else:
            self.Anmelde_entry = tk.Entry(self, show="*")
            self.Anmelde_Knopp = tk.Button(self, text="Anmelden", highlightbackground=self.Hintergrund_farbe, bg=self.Hintergrund_farbe, command="")
            self.PW_F_Knopp = tk.Button(self, text="Passwort einstellen", command=self.PW_Check)
            self.KonvKnopp = tk.Button(self, text="Umwandeln", command=self.beides)
            
            self.Kontakte_AnzeigenMainMenu = tk.Button(self, text="Kontaktliste anzeigen", command= self.Krams)
            self.TauschenLBundEN = tk.Button(self, text="eigenes Passwort verwenden", command=self.TLBUEN)
            
            self.Thunderbird_anEmail_anfügen = tk.Button(self, text="an neue Email anfügen", highlightbackground="lightsteelblue", command=Thunderbird)
            self.Kontakte_Einfügen_Knopp_zeigen = tk.Button(self, text="+", highlightbackground="lightsteelblue", command=self.NeuenKontaktHinzufügen)
            self.Kontakt_löschen = tk.Button(self, text="Löschen", command= self.Kontakt_löschen_bst_c)
            self.kwpä_knopp = tk.Button(self.KndPW_ändern_fenster, text="Dieses Passwort einstellen", command=self.KPW_ändern_c)
            self.KTLS = tk.Button(self, text="x", highlightbackground="lightsteelblue", command= self.KTLS_C)
            self.Beb_Knopp = tk.Button(self, text="Kontakt bearbeiten", command=self.kBe)
            self.Kontakt_löschen = tk.Button(self, text="löschen", command= self.Kontakt_löschen_bst_c)
            

        #####except:
        #####    print("das mit dem if und dem Design dings hat so ganricht geklapt...")
        #####    messagebox.showerror(title= "Fehler: 10", message="Das Programm konnte nicht gestartet werden. Fehlercode 10")
            

        root.bind('<Return>', self.Widget_spawn)
        self.Anmelde_Knopp.bind('<Button-1>', self.Widget_spawn)
        
        
        self.Anmelde_Text = tk.Label(self, text="Bitte Melden Sie sich an um fortzufahren.", bg=self.Hintergrund_farbe, fg="Black")
        self.Anmelde_Text.pack(pady=10,padx=10)
        self.Anmelde_entry.pack(pady=10,padx=10)
        self.Anmelde_Knopp.pack(pady=5,padx=10)
        
    
        self.pwtext = tk.Label(self,  text="Passwort eingeben:", bg=self.Hintergrund_farbe)
        self.pwtextB = tk.Label(self,  text="Passwort wiederholen:", bg=self.Hintergrund_farbe)
        self.password_entryB = tk.Entry(self)
        self.password_entry = tk.Entry(self)
        self.Zu_Blöd_zum_schreiben = tk.Label(self, text="Die Passwörter stimmen nicht über ein!", fg="red", width=15)
        self.bestätigung = tk.Label (self, text="Passwort eingestellt", bg="white", fg="black", borderwidth="10", width=10)
        self.Kontaktelistbox = tk.Listbox(self, bg="Yellow", fg="White" , width=42)
        
        
        try:
            self.DND_Bild = Image.open("assets/Bild11.png")
            print("[-INFO-] Bild geladen")
        except:
            try:
                self.DND_Bild = Image.open("assets/Bild11.png")
                print("[-INFO-] Bild geladen.")
            except:
                print("[-FATAL-] Bild konnte nicht gefunden werden.")
        try:
            self.Bild_dings = self.DND_Bild.resize((210, 200))
            self.DND_asset = ImageTk.PhotoImage(self.Bild_dings)
            self.Bild_Label = tk.Label(self, image=self.DND_asset, bg=self.Hintergrund_farbe, pady=105)
        
        ################self.Bild_Label.place(x=285, y=0)
            self.DND_Text_Label = tk.Label(self, text="Hier Fallenlassen", fg="Black", bg=self.Hintergrund_farbe)
        except:
            print("[-INFO-] DND wurde deaktiviert")
        
        ###############self.DND_Text_Label.place(x=340,y=50)
        def read_registry_value(key_path, value_name):
            try:
                key = winreg.OpenKey(winreg.HKEY_CURRENT_USER, key_path, 0, winreg.KEY_READ)
                value, value_type = winreg.QueryValueEx(key, value_name)
                winreg.CloseKey(key)
                return value
            except:
                return None

        # Beispiel: Auslesen des Standard-Mailers
        key_path = r"Software\Microsoft\Windows\Shell\Associations\UrlAssociations\mailto\UserChoice"
        value_name = "ProgId"

        self.default_mailer = read_registry_value(key_path, value_name)
        if self.default_mailer:
            print("[-INFO-] Standard-Mailer:", self.default_mailer)
        else:
            print("[-INFO-]  Kein Standard-Mailer festgelegt bzw. nicht gefunden.")
            messagebox.showwarning(title="Fehler 23", message="Es konnte kein Standart Mailprogramm gefunden werden, bitte wennden Sie sich an den Support oder starten Sie Ihren Rechner Neu. \n Fehlercode: 23")
        
        print("[-INFO-] Die Hauptladeteile sind nun Durcheglaufen, beginne nun mit GUI und co.")
        print("--------------------------------------------")

        self.Dings_Fertsch_und_so = tk.Label(self, text="Dateien fertig verarbeitet.", bg="White", fg="Black")
        self.PW_F_Knopp.place_forget()

        def Super_Drop(event): # Diese Funktion hier ist das kleine Dropfenster mit Bild und code welcher es zum Laufen bringt
            print(event.data)
            print(len(event.data))
            dings_event_data = event.data.split("} {")
            print(dings_event_data)
            dings_event_data = event.data.split("} ")
            print(dings_event_data)
            dings_event_data = event.data.split(" {")
            print(dings_event_data)
            if len(dings_event_data) == 1:
                print("len ist 1")
                self.DND_Pfad = event.data
                print("Datei gezogen:", self.DND_Pfad)
                self.DND_Pfad.replace("{", "")
                self.DND_Pfad.replace("}", "")
                print(self.DND_Pfad)
                self.entrydnd = tk.Entry(self, width=100)
                try:
                    self.Entrylabel.pack_forget()
                except:
                    pass
                self.pwtext.configure(bg=self.dieser_komische_grünton)
                self.pwtextB.configure(bg=self.dieser_komische_grünton)
                dings_event_dataf = str(dings_event_data)
                dings_event_data1 = dings_event_dataf.replace("{", "")
                dings_event_data1 = dings_event_data1.replace("}", "")
                self.Entrylabel = tk.Label(self, width=80, background=self.dieser_komische_grünton, text="Ausgewählte Datei: " + dings_event_data1)
                self.Entrylabel.pack()
                self.entrydnd.place(x=69420,y=69420)
                self.entrydnd.insert(END, self.DND_Pfad)
                self.configure(bg=self.dieser_komische_grünton)
                self.entry21_r1 = self.entrydnd.get()
                print(self.entry21_r1)
                self.KonvKnopp.pack(side="right", anchor="s")
                self.Datei_gezogen = 1
                self.etwas_bereits_eingefügt = 1
                if self.tree_iz_da == 1:
                    print("[-DEV-]  tree iz da")
                else:
                    print("[-DEV-] tree iz ni da")
                    self.Krams()
            elif len(dings_event_data) > 1:
                print("len ist > 2")
                self.Datei_gezogen = 0
                messagebox.showerror(title="Fehlercode: 21", message="Bitte ziehen sie nur eine Datei hinein oder legen Sie die Dateien vorher in einen Ordner.")
        try:
            self.Bild_Label.drop_target_register(DND_FILES)
            self.Bild_Label.dnd_bind('<<Drop>>', Super_Drop, ('DND_Single'))
            self.DND_Text_Label.drop_target_register(DND_FILES)
            self.DND_Text_Label.dnd_bind('<<Drop>>', Super_Drop, ('DND_Single'))
            print("[-INFO-] DnD ist ist höchst wahrscheinlich aktiv")
        except:
            print("[-INFO-] DnD komplett deaktiviert.")
    def Gui_spawn(self):
        print("[-DEV-] Gui_spawn(def)")
        
################################            EIN PAAR EINSTELLUNSG /DEV SACHEN           ######################

    def outputordner_öffnen_c(self):
        print("[-DEV-] Outputordner_öffenen_c")
        subprocess.Popen('explorer "output"')

    def outputordner_öffnen_c_l(self):
        print("[-DEV-] Outputordner_öffenen_c_L")
        subprocess.Popen('explorer "/logs"')

    def design_einst_w_c(self):
        print("[-DEV-] design_einst_w_c")
        try:
            Einstellungen_w_Dvar = {"Design_mode" : "Windoof"} 
            with open ("einstellungen/design.json", "w+") as w_c:
                json.dump(Einstellungen_w_Dvar, w_c)
                print("Design Einstellungen wurden erfolgreich geändert.")
        except:
            print("Einstellung: Design 'Windoof' konnten nicht Übernommen werden")
            try:
                print("Versuche erneut die Einstellung Design 'Windoof' zu Übernehmen")
                Einstellungen_w_Dvar = {"Design_mode" : "Windoof"} 
                with open ("einstellungen/design.json", "w+") as w_c:
                    json.dump(Einstellungen_w_Dvar, w_c)
                    print("Design Einstellungen wurden erfolgreich geändert.")
            except:
                print("Das Übernehmen des Designs 'Windoof' hat Komplett nicht geklappt.")
                messagebox.showerror(title="Fehler: 9 ", message="Es ist ein Fehler aufgetreten, bitte verssuchen Sie es erneut oder wenden Sie sich an den Support. Fehlercode: 9")
    
    def design_einst_m_c(self):
        print("design_einst_m_c")
        try:
            Einstellungen_m_Dvar = {"Design_mode" : "Modern"}
            with open ("einstellungen/design.json", "w+") as m_c:
                json.dump(Einstellungen_m_Dvar, m_c)
                print("Design Einstellungen wurden erfolgreich geändert.")
        except:
            print("Einstellung: Design 'Modern' konnten nicht Übernommen werden")
            try:
                print("Versuche erneut die Einstellung Design 'Modern' zu Übernehmen")
                Einstellungen_m_Dvar = {"Design_mode" : "Modern"} 
                with open ("einstellungen/design.json", "w+") as m_c:
                    json.dump(Einstellungen_m_Dvar, m_c)
                    print("Design Einstellungen wurden erfolgreich geändert.")
            except:
                print("Das Übernehmen des Designs hat Komplett nicht geklappt.")
                messagebox.showerror(title="Fehler: 9 ", message="Es ist ein Fehler aufgetreten, bitte verssuchen Sie es erneut oder wenden Sie sich an den Support. Fehlercode: 9")

    

    def KTK_speicherort_c(self):
        print("[-DEV-] KTK_speicherort_c(def)")
        self.Neu_gewählterordner_für_ktk = filedialog.askdirectory()
        print(self.Neu_gewählterordner_für_ktk)
        self.Neu_gewählterordner_für_ktk1 = self.Neu_gewählterordner_für_ktk + "/"
        print(self.Neu_gewählterordner_für_ktk1)
        self.einstellungenN_ktk = {"Kontaktliste_Speicherort": self.Neu_gewählterordner_für_ktk1}
        print("die var wurde als json objekt gelegt.")
        print(self.einstellungenN_ktk)
        print("[-DEV-] Die Einstellung war wohl leer und wird nun überschrieben. (KTK) ")
        try:
            with open("einstellungen/Kontaktliste_Speicherort.json", "w+" ) as fn:
                json.dump(self.einstellungenN_ktk, fn)
                messagebox.showinfo(title="Erfolg", message="Der Pfad der Kontaktliste wurde erfolgreich gändert und wird beim nächsten Programmstart aktiv.")
        except:
            print("Das ändern des KTK_Speicherortes ist Fehlgeschlagen.")
            messagebox.showinfo(title="Fehler", message="Das Anlegen des Neuen Speicherpfades für die Kontakliste ist Fehlgeschlagen bitte Starten Sie das Programm neu und versuchen Sie es Erneut")
    
###############################################################                                         #####################################################################

    def Widget_spawn_e(event, self):
        self.Widget_spawn(event)

    def Widget_spawn(self, event):
        if self.Anmelde_entry.get() == self.Dings: #Kunde
            print("[-DEV-] Kunde")
            root.unbind('<Return>')
            root.geometry("820x600")
            root.attributes('-toolwindow', False)
            try:
                self.Bild_Label.place(x=285, y=50)
                self.DND_Text_Label.place(x=340,y=100)
            except:
                pass
            self.Kontakte_AnzeigenMainMenu.pack(side="bottom", anchor="w")
            self.menu.add_cascade(label="Zipa" + self.Version, menu=self.filemenu2)
            self.filemenu2.add_command(label="Info", command=self.info)
            #self.filemenu2.add_command(label="Einstellungen", command=self.einstellungen)
            #self.filemenu2.add_command(label="Zip Datei an Email hängen", command=self.Attch_an_mail_packn)
            self.menu.add_cascade(label="Einfügen", menu=self.filemenu)
            self.filemenu.add_command(label="Ordner Einfügen", command=self.OrdnKonv)
            self.filemenu.add_command(label="Datei Einfügen", command=self.DataKonv)
            filemenu1 = Menu(self.menu, tearoff=0)
            self.menu.add_cascade(label="Kontakte", menu=filemenu1, )
            filemenu1.add_command(label="Kontakte anzeigen", command=self.Krams)
            filemenu1.add_command(label="Kontakt hinzufügen", command=self.NeuenKontaktHinzufügen)
            filemenu3 = Menu(self.menu, tearoff=0)
            #self.menu.add_cascade(label="Info", menu=filemenu3)
            #filemenu3.add_command(label="#Anleitung", command=self.einstellungen)
            #filemenu3.add_command(label="#Probleme")
            filemenu4 = Menu(self.menu, tearoff=0)
            #self.menu.add_cascade(label="Design", menu=filemenu4, )
            #filemenu4.add_command(label="Design: Modern", command=self.design_einst_m_c)
            #filemenu4.add_command(label="Design: Windoof", command=self.design_einst_w_c)
            self.menu.add_command(label="An Email Hängen", command=self.Attch_an_mail_packn)
            #self.menu.add_command(label="Eigenes Passwort verwenden", command=self.TLBUEN)
            
            self.Anmelde_entry.pack_forget()
            self.Anmelde_Knopp.pack_forget()
            self.Anmelde_Text.pack_forget()
            self.Gui_spawn()

        elif self.Anmelde_entry.get() == self.Bums: #Admin
            print("[-DEV-] Admin")
            root.unbind('<Return>')
            root.geometry("820x600")
            root.attributes('-toolwindow', False)
            try:
                self.Bild_Label.place(x=285, y=50)
                self.DND_Text_Label.place(x=340,y=100)
            except:
                pass
            self.Kontakte_AnzeigenMainMenu.pack(side="bottom", anchor="w")
            self.menu.add_cascade(label="Zippa" + self.Version, menu=self.filemenu2)
            self.filemenu2.add_command(label="Einstellungen", command=self.einstellungen)
            self.filemenu2.add_command(label="Info", command=self.info)
            #self.filemenu2.add_command(label="Test Knopf", command=self.guckn)
            self.filemenu2.add_command(label="Zip an Email hängen", command=self.Attch_an_mail_packn)
            self.menu.add_cascade(label="Einfügen", menu=self.filemenu)
            self.filemenu.add_command(label="Ordner Einfügen", command=self.OrdnKonv)
            self.filemenu.add_command(label="Datei Einfügen", command=self.DataKonv)
            #self.filemenu.add_command(label="absolut arschkrass", command=self.absolut_arschkrass)
            filemenu1 = Menu(self.menu, tearoff=0)
            self.menu.add_cascade(label="Kontakte", menu=filemenu1, )
            filemenu1.add_command(label="Kontakt Liste anzeigen", command=self.Krams)
            filemenu1.add_command(label="Kontakt Hinzufügen", command=self.NeuenKontaktHinzufügen)
            filemenu3 = Menu(self.menu, tearoff=0)
            #self.menu.add_cascade(label="Info", menu=filemenu3)
            filemenu4 = Menu(self.menu, tearoff=0)
            self.menu.add_cascade(label="Support", menu=filemenu4)
            filemenu4.add_command(label="Passwort des Kunden einstellen oder ändern", command=self.KPW_ändern)
            filemenu4.add_command(label="Speicherort der Kontaktliste Ändern", command=self.KTK_speicherort_c)
            filemenu4.add_command(label="Log Speicherort Ändern", command=self.outputordner_suchen)
            filemenu4.add_command(label="Log Speicherort öffnen", command=self.outputordner_öffnen_c_l)
            filemenu4.add_command(label="Kontaktliste Auslesen", command=self.Kontaktliste_auslesen)
            self.menu.add_command(label="An Email Hängen", command=self.Attch_an_mail_packn)
            #self.menu.add_command(label="Eigenes Passwort verwenden", command=self.TLBUEN)
            #filemenu3.add_command(label="#Anleitung", command=self.einstellungen)
            #filemenu3.add_command(label="#Probleme")
            self.Anmelde_entry.pack_forget()
            self.Anmelde_Knopp.pack_forget()
            self.Anmelde_Text.pack_forget()
            self.Gui_spawn()
            

        elif self.Anmelde_entry.get() == self.Ja: #Dev
        #elif self.Anmelde_entry.get() == "":
            print("[-DEV-] Gott der Welt, des Univesums und der Galaxie. bringer des Lebens und des Todes. International anerkannter Hasser des standard Mailers.")
            root.unbind('<Return>')
            root.geometry("820x600")
            root.attributes('-toolwindow', False)
            try:
                self.Bild_Label.place(x=285, y=50)
                self.DND_Text_Label.place(x=345,y=100)
            except:
                pass
            self.Kontakte_AnzeigenMainMenu.pack(side="bottom", anchor="w")
            self.menu.add_cascade(label="Zippa" + self.Version, menu=self.filemenu2)
            self.filemenu2.add_command(label="Info", command=self.info)
            self.filemenu2.add_command(label="Einstellungen", command=self.einstellungen)
            self.filemenu2.add_command(label="Test Knopf", command=self.guckn)
            #self.filemenu2.add_command(label="Test Knopf", command= MyConfig.guckn1(self))
            self.filemenu2.add_command(label="Zip an Email hängen", command=self.Attch_an_mail_packn)
            self.menu.add_cascade(label="Einfügen", menu=self.filemenu)
            self.filemenu.add_command(label="Ordner Einfügen", command=self.OrdnKonv)
            self.filemenu.add_command(label="Datei Einfügen", command=self.DataKonv)
            
            filemenu1 = Menu(self.menu, tearoff=0)
            self.menu.add_cascade(label="Kontakte", menu=filemenu1, )
            filemenu1.add_command(label="Kontakt Liste anzeigen", command=self.Krams)
            filemenu1.add_command(label="Kontakt Hinzufügen", command=self.NeuenKontaktHinzufügen)
            filemenu3 = Menu(self.menu, tearoff=0)
            filemenu4 = Menu(self.menu, tearoff=0)
            filemenu5 = Menu(self.menu, tearoff=0)
            
            self.menu.add_cascade(label="Dev", menu=filemenu4)
            filemenu4.add_command(label="Kontaktliste Auslesen", command=self.Kontaktliste_auslesen)
            self.menu.add_cascade(label="Test", menu=filemenu3)
            filemenu3.add_command(label="kBe", command=self.kBe)
            filemenu3.add_command(label="#Probleme")
            filemenu3.add_command(label="Zip Speicherort Ändern", command=self.outputordner_suchen_z)

            filemenu4.add_command(label="Passwort des Dev einstellen oder ändern", command=self.dev_ändern)
            filemenu4.add_command(label="Passwort des Admins einstellen oder ändern", command=self.adm_ändern)
            filemenu4.add_command(label="Passwort des Kunden einstellen oder ändern", command=self.KPW_ändern)
            #filemenu4.add_command(label="absolut arschkrass", command=self.absolut_arschkrass)
            filemenu4.add_command(label="Log Speicherort Ändern", command=self.outputordner_suchen)
            filemenu4.add_command(label="Log Speicherort öffnen", command=self.outputordner_öffnen_c_l)
            filemenu4.add_command(label="Design: Modern", command=self.design_einst_m_c)
            filemenu4.add_command(label="Design: Windoof", command=self.design_einst_w_c)
            filemenu4.add_command(label="Speicherort der Kontaktliste Ändern", command=self.KTK_speicherort_c)

            filemenu4.add_command(label="Debug Instanz mit Adminrechten starten", command=self.Admin_Rechte)
            
            self.menu.add_command(label="An Email Hängen", command=self.Attch_an_mail_packn)
            self.menu.add_command(label="Eigenes Passwort verwenden", command=self.TLBUEN)
            

            self.Anmelde_entry.pack_forget()
            self.Anmelde_Knopp.pack_forget()
            self.Anmelde_Text.pack_forget()
            self.Gui_spawn()
        else:
            messagebox.showinfo(title='Information', message="Fehler 60: Falsches Passwort, wenn Sie sich sicher sind, dass Sie das richtige Passwort eingegeben haben. Kontaktieren Sie bitte den Support.")
            self.Anmelde_entry.delete(0, tk.END)

    def Admin_Rechte(self):
        response = ctypes.windll.user32.MessageBoxW(None, "Möchten Sie Administratorrechte anfordern? Dies wird das Programm mit Adminrechten neustarten.", "Administratorrechte erforderlich", 4)
        if response == 6:  # Wert 6 entspricht dem Klick auf "Ja"
            try:
                # Hier führen wir die Funktion mit Administratorrechten aus
                print("Instanz mit Admin Rechten gestartet")
                ctypes.windll.shell32.ShellExecuteW(None, "runas", sys.executable, " ".join(sys.argv), None, 1)
                sys.exit()
            except Exception as e:
                print("Fehler beim Ausführen der 'Admin_Rechte'-Funktion:", e)
        else:
            print("Administratorrechte wurden nicht angefordert.")
    


    def KPW_ändern(self):
        try:
            with open("usr.txt", "rb") as KPW:
                KndPW = KPW.read()
                print("[-DEV-] das momentane Passwort lautet: ", KndPW)
        except:
                print("[-ERR-] kpwändern, kann kein pw finden in der txt.")
                pass
        print("[-DEV-] verschl KndPW:")
        print(KndPW)
        try:
            KndPW = self.fernet.decrypt(KndPW)
        except:
            print("[-ERR-] beim decrypten gabs nen fehler")
            pass
        print("[-DEV-] jetzt kommt das entschlüsselte kdnpw aus der txt datei")
        KndPW_utf8 = KndPW.decode('utf-8')
        print(KndPW_utf8)
        self.KndPW_ändern_fenster = tk.Toplevel()
        self.KndPW_ändern_fenster.title("das Kundenpasswort ändern")
        self.KndPW_ändern_fenster.geometry("520x260+950+350")
        self.KndPW_ändern_fenster.resizable(False,False)
        self.KndPW_ändern_fenster.configure(bg=self.Hintergrund_farbe)
        self.kwpä_entry = tk.Entry(self.KndPW_ändern_fenster)
        self.kwpä_entry.pack()
        self.kwpä_knopp = tk.Button(self.KndPW_ändern_fenster, text="Dieses Passwort einstellen", command=self.KPW_ändern_c, relief=tk.RAISED,border=10, bd=3, compound=tk.CENTER, bg="#3366CC", fg="white", font=("Helvetica", 12), padx=10, pady=5, borderwidth=0, highlightthickness=0, activebackground="#6699FF")
        #self.kwpä_knopp = tk.Button(KndPW_ändern_fenster, text="Dieses Passwort einstellen", command=self.KPW_ändern_c)
        self.kwpä_knopp.pack()

    def KPW_ändern_c(self): #ändern des Kunden Passwortes
        print(self.kwpä_entry.get())
        self.NKPW_E = self.kwpä_entry.get()
        self.NKPW_E = self.NKPW_E.encode()
        self.NKPW_E = self.fernet.encrypt(self.NKPW_E)
        print(self.NKPW_E)
        try:
            with open("usr.txt", "wb+") as NKPW:
                NKPW.write(self.NKPW_E)
                messagebox.showinfo(title="Info", message="Das Passwort des Kunden wurde erfolgreich geändert.")
        except:
            messagebox.showerror(title="Das hat nicht funktioniert. Bitte in den Code schauen.")

    def info(self):
        print("[-DEV-] Info def")
        messagebox.showinfo(title="CMS Zipa", message="CMS Zipa Version:" + self.Version + " \n \n Programmiert von: Maximilian Becker \n CMS Weißenfels: www.beese-computer.de")

    def adm_ändern(self):
        try:
            with open("admn.txt", "rb") as adm2:
                admPW = adm2.read()
                print("[-DEV-] das momentane Passwort lautet: ", admPW)
        except:
                print("[-ERR-] admändern, kann kein pw finden in der txt.")
                pass
        print("[-DEV-] verschl admPW:")
        try:
            admPW = self.fernetadm.decrypt(admPW)
            print("[-DEV-] jetzt kommt das entschlüsselte kdnpw aus der txt datei")
            adm_utf8 = admPW.decode('utf-8')
            print(adm_utf8)
        except:
            print("[-ERR-] beim decrypten gabs nen fehler")
            pass
        
        self.admPW_ändern_fenster = tk.Toplevel()
        self.admPW_ändern_fenster.title("das Kundenpasswort ändern")
        self.admPW_ändern_fenster.geometry("520x260+950+350")
        self.admPW_ändern_fenster.resizable(False,False)
        self.admPW_ändern_fenster.configure(bg=self.Hintergrund_farbe)
        self.admä_entry = tk.Entry(self.admPW_ändern_fenster)
        self.admä_entry.pack()
        self.admä_knopp = tk.Button(self.admPW_ändern_fenster, text="Dieses Passwort einstellen", command=self.adm_ändern_c)
        #self.kwpä_knopp = tk.Button(KndPW_ändern_fenster, text="Dieses Passwort einstellen", command=self.KPW_ändern_c)
        self.admä_knopp.pack()

    def adm_ändern_c(self): #ändern des Kunden Passwortes
        print(self.admä_entry.get())
        self.Nadm_E = self.admä_entry.get()
        self.Nadm_E = self.Nadm_E.encode()
        self.Nadm_E = self.fernetadm.encrypt(self.Nadm_E)
        print(self.Nadm_E)
        try:
            with open("admn.txt", "wb+") as Nadm:
                Nadm.write(self.Nadm_E)
                messagebox.showinfo(title="Info", message="Das Passwort des Admins wurde geändert.")
        except:
            messagebox.showerror(title="Das hat nicht funktioniert. Bitte in den Code schauen.")

    def dev_ändern(self):
        print("[-INFO-] dev_ändern")
        try:
            with open("dev.txt", "rb") as dev:
                devPW = dev.read()
                print("[-DEV-] das momentane Passwort lautet: ", devPW)
        except:
                print("[-ERR-] devändern, kann kein pw finden in der txt.")
                pass
        print("[-DEV-] verschl devPW:")
        try:
            devPW = self.fernetdev.decrypt(devPW)
            print("[-DEV-] jetzt kommt das entschlüsselte devpw aus der txt datei")
            dev_utf8 = devPW.decode('utf-8')
            print(dev_utf8)
        except:
            print("[-ERR-] beim decrypten gabs nen fehler")
            pass
        
        self.devPW_ändern_fenster = tk.Toplevel()
        self.devPW_ändern_fenster.title("das dev passwort ändern")
        self.devPW_ändern_fenster.geometry("520x260+950+350")
        self.devPW_ändern_fenster.resizable(False,False)
        self.devPW_ändern_fenster.configure(bg=self.Hintergrund_farbe)
        self.dev_entry = tk.Entry(self.devPW_ändern_fenster)
        self.dev_entry.pack()
        self.dev_knopp = tk.Button(self.devPW_ändern_fenster, text="Dieses Passwort einstellen", command=self.dev_ändern_c)
        #self.kwpä_knopp = tk.Button(KndPW_ändern_fenster, text="Dieses Passwort einstellen", command=self.KPW_ändern_c)
        self.dev_knopp.pack()

    def dev_ändern_c(self): #ändern des Kunden Passwortes
        print("[-INFO-] dev_ändern_c")
        print(self.dev_entry.get())
        self.Ndev_E = self.dev_entry.get()
        self.Ndev_E = self.Ndev_E.encode()
        self.Ndev_E = self.fernetdev.encrypt(self.Ndev_E)
        print(self.Ndev_E)
        try:
            with open("dev.txt", "wb+") as Ndev:
                Ndev.write(self.Ndev_E)
                messagebox.showinfo(title="Info", message="Das Passwort des Devs wurde geändert.")
                self.devPW_ändern_fenster.destroy()
        except:
            messagebox.showerror(title="Das hat nicht funktioniert. Bitte in den Code schauen.")

    def Kontakt_löschen_bst_c(self):
        self.tag_und_zeit_string = time.strftime("%m/%d/%Y, %H:%M:%S")
        print("[-DEV-] lösch bestätigung_c (def)")
        abfrage_wegen_löschen = messagebox.askquestion(title='Information', message="möchten Sie den Kontakt wirklich löschen?")
        if abfrage_wegen_löschen == "yes":
            #try:
                print("löschen vom Nutzer bestätigt")
                print(self.tree.selection())
                print(self.tag_und_zeit_string)
                self.Kontakt_löschen_c()
            #except:
            #    AttributeError
            #    print("na vielleichts wählste mal noch aus WAS du löschen willst?")
            #    einz = tk.Label(self, width=100 , height=1, bg="white", fg="black", text="Sie müssen zuerst auswählen welchen Kontakt Sie löschen möchten.")
            #    einz.place(x=0,y=0)
            #    self.after( 5000, einz.place_forget)
            #    messagebox.showerror(title="Fehler 61", message="Fehler 61: Sie müssen zuerst auswählen welchen Kontakt Sie bearbeiten möchten. Wenn dieses Problem bestehen bleibt wenden Sie sich bitte an den Support")

                #ValueError
                #print("scheiße")
                #messagebox.showerror(title="ein schwerwiegender Fehler ist aufgetreten.", message=self.Absturz_meldung)

        elif abfrage_wegen_löschen == "no":
            print("[-INFO-]  löschen vom Nutzer abgerbrochen.")
        else:
            print("[-DEV-] else des msg box dings")
            print("[-FATAL-] Falsche auswahl bei dem Bestätigungsfenster")
            messagebox.showerror(title="ein schwerwiegender Fehler ist aufgetreten.", message=self.Absturz_meldung)

    def Kontakt_löschen_c(self):
        print("[-DEV-] Kontakt:löschen_c gestartet...")
        self.kontaktE = {"Vorname": self.Vorname1 , "Nachname": self.Nachname1, "Passwort": self.Passwort1, "Firma": self.Firma1}
        try:
            with open(self.KTK_Speicherort + "Kontaktliste.txt", "rb") as f:
                verschlüsselter_byte_aus_txt = f.read()
        except PermissionError:
            print("[-FATAL-] Die berechtigung zum Lesen fehlt.")
            messagebox.showerror(title="Fehlercode 22", message="Es Fehlt für diesen Ordner die nötige Berechtigung, Die Kontakliste konnte nicht aufgerufen werden.")
            return
        print("[-DEV-] jetzt kommt die txt")
        print(verschlüsselter_byte_aus_txt)
        entschlüsselter_byte_aus_txt = self.fernet.decrypt(verschlüsselter_byte_aus_txt)
        #print("[-DEV-]  jetzt kommt das entschlüsselte aus der txt datei")
        #print(entschlüsselter_byte_aus_txt)
        entschlüsselter_byte_aus_txt_als_utf8 = entschlüsselter_byte_aus_txt.decode('utf-8')
        entschlüsselter_byte_aus_txt_für_json = json.loads(entschlüsselter_byte_aus_txt_als_utf8)
        print(entschlüsselter_byte_aus_txt_für_json)
        print(self.kontaktE)
        formatierter_string = {key: f'{value}' if isinstance(value, int) else value for key, value in self.kontaktE.items()}
        print("[-DEV-]  !")
        print(formatierter_string) #Ich weiß das diese Variable sehr unprofessionell benannt wurde aber Ihr könnt den Frust nicht verstehen welcher mit dieser Funktion einhergeht.
        entschlüsselter_byte_aus_txt_für_json.remove(formatierter_string)
        print("jetzt das fertige dingssss")
        print(entschlüsselter_byte_aus_txt_für_json)
        Liste_mit_neuem_kontakt = entschlüsselter_byte_aus_txt_für_json
        neues_verschlüsseltes_dings = self.fernet.encrypt(json.dumps(Liste_mit_neuem_kontakt).encode('utf-8'))
        try:
            with open(self.KTK_Speicherort + "Kontaktliste.txt", "wb") as f:
                f.write(neues_verschlüsseltes_dings)
                selected_item = self.tree.selection()
                if selected_item:
                    self.tree.delete(selected_item)
        except PermissionError:
            print("[-FATAL-] Die berechtigung zum schreiben fehlt.")
            messagebox.showerror(title="Fehlercode 20", message="Es fehlt für diesen Ordner die nötige Berechtigung, Die Kontakliste konnte nicht aufgerufen werden.")

        
        
        
        


    def Krams(self):
        self.tree = None

        if self.tree_iz_da == 1:
            print("tree iz da")
        else:
            print("tree iz ni da")

            
            self.KTLS.pack(side="right", anchor="s")
            self.Kontakte_AnzeigenMainMenu.pack_forget()
            print("4")
            self.Kopfzeile = ['Vorname', 'Nachname', 'Passwort', 'Firma']
            self.msg = ttk.Label(wraplength="4i", justify="left", anchor="n",  text="Wählen Sie durch Klicken einen Kontakt aus der Liste aus")
            self.msg.pack(fill='x')
            self.container = ttk.Frame()
            self.container.pack(side="bottom", fill='x')
            aussehen_des_ttks = ttk.Style(root)
            try:
                aussehen_des_ttks.theme_use("winnative")
            except:
                print("scheint wohl nicht auf Windows zu sein, konnte die treeview nicht in 'Winnative' darstellen.")

                # wenn das ding voll7text zu lang, dann werden scrollbars erstellt
            self.tree = ttk.Treeview(columns=self.Kopfzeile, show="headings")
            vsb = ttk.Scrollbar(orient="vertical", command=self.tree.yview)
            hsb = ttk.Scrollbar(orient="horizontal", command=self.tree.xview)
            self.tree.configure(yscrollcommand=vsb.set, xscrollcommand=hsb.set)
            self.tree.grid(column=0, row=0, sticky='nsew', in_=self.container)
            self.tree_iz_da = 1
            aussehen_des_ttks.configure("Treeview", background=self.Hintergrund_farbe, foreground="Black", highlightedbackground="#4774cf")


            def item_selected(event):
                print("def item_selected(event):")
                for selected_item in self.tree.selection():
                    item = self.tree.item(selected_item)
                    values = item["values"]

                    self.Vorname1, self.Nachname1, self.Passwort1, self.Firma1 = values
                    print(values)
                if self.etwas_bereits_eingefügt == 1:
                    print("[-DEV-] Die Var self.etwas_bereits_eingefügt = ", self.etwas_bereits_eingefügt)
                    if self.Kontakt_löschen_knopp_iz_da == 1:
                        print("kontakt löschen knopf iz da")
                    elif self.Kontakt_löschen_knopp_iz_da == 0:
                        print("kontakt löschen knopf iz ni da")
                        try:
                            self.KTLS.pack_forget()
                            self.Kontakte_Einfügen_Knopp_zeigen.pack_forget()
                            self.Beb_Knopp.pack_forget()
                            self.Kontakt_löschen.pack:forget()
                            self.TauschenLBundEN.pack_forget()
                            self.Kontakte_Einfügen_Knopp_zeigen.pack_forget()
                            self.KonvKnopp.pack_forget()
                        except:
                            print("[-DEV-] im item_select konnten nicht alle Sachen despawnen, Das ist nicht schlimm, außer es ist schlimm. 1")
                        self.KTLS.pack(side="right", anchor="s")
                        self.Kontakt_löschen_knopp_iz_da = 1
                        self.Beb_Knopp.pack(side="right", anchor="s")
                        self.Kontakt_löschen.pack(side="right", anchor="s")
                        self.TauschenLBundEN.pack(side="right", anchor="s")
                        self.KonvKnopp.pack(side="right", anchor="s")
                        self.Kontakte_Einfügen_Knopp_zeigen.pack(side="bottom", anchor="w")
                        
                elif self.etwas_bereits_eingefügt == 0:
                    print("[-DEV-] Die Var self.etwas_bereits_eingefügt = ", self.etwas_bereits_eingefügt)
                    if self.Kontakt_löschen_knopp_iz_da == 1:
                        print("kontakt löschen knopf iz da")
                    elif self.Kontakt_löschen_knopp_iz_da == 0:
                        print("kontakt löschen knopf iz ni da")
                        try:
                            self.KTLS.pack_forget()
                            self.Kontakte_Einfügen_Knopp_zeigen.pack_forget()
                            self.Beb_Knopp.pack_forget()
                            self.Kontakt_löschen.pack:forget()
                            self.TauschenLBundEN.pack_forget()
                            self.Kontakte_Einfügen_Knopp_zeigen.pack_forget()
                            self.KonvKnopp.pack_forget()
                        except:
                            print("[-DEV-] im item_select konnten nicht alle Sachen despawnen, Das ist nicht schlimm, außer es ist schlimm. 2")
                        #self.KTLS.pack_forget()
                        #self.Kontakte_Einfügen_Knopp_zeigen.pack_forget()
                        self.KTLS.pack(side="right", anchor="s")
                        self.Kontakt_löschen_knopp_iz_da = 1
                        self.Beb_Knopp.pack(side="right", anchor="s")
                        self.Kontakt_löschen.pack(side="right", anchor="s")
                        self.TauschenLBundEN.pack(side="right", anchor="s")
                        self.Kontakte_Einfügen_Knopp_zeigen.pack(side="bottom", anchor="w")
                        

            self.tree.bind('<<TreeviewSelect>>', item_selected)

            vsb.grid(column=1, row=0, sticky='ns', in_=self.container)
            hsb.grid(column=0, row=1, sticky='ew', in_=self.container)

            self.container.grid_columnconfigure(0, weight=1)
            self.container.grid_rowconfigure(0, weight=1)


            self.Thunderbird_anEmail_anfügen.place_forget()
            self.show_button = tk.Button(self, text="Details", highlightbackground="lightsteelblue", command=self.KTL_D,  relief=tk.RAISED, bd=3, compound=tk.CENTER, bg="#3366CC", fg="white", font=("Helvetica", 12), padx=10, pady=5, borderwidth=0, highlightthickness=0, activebackground="#6699FF")

            print("5")
            self.kontakte = []
            try:
                with open(self.KTK_Speicherort + "Kontaktliste.txt", "rb") as f:
                    verschlüsselter_byte_aus_txt = f.read()
                    print("[-INFO-] Kontaktliste gelesen.")
            except FileNotFoundError:
                print("Kontaktliste nicht gefunden.")
                messagebox.showinfo(title="Kontaktlistenfehler", message="Die Kontaktliste wurde nicht gefunden. Fehlercode: 18")
                verschlüsselter_byte_aus_txt = "b''"
            except PermissionError:
                print("[-FATAL-] Die berechtigung zum Lesen fehlt.")
                messagebox.showerror(title="Fehlercode 22", message="Es Fehlt für diesen Ordner die nötige Berechtigung, Die Kontakliste konnte nicht aufgerufen werden.")
            if verschlüsselter_byte_aus_txt == "b''":
                        print("Kontaktliste ist Leer")
                        self.kontakte = ""
            elif verschlüsselter_byte_aus_txt != "b''":
                #try:
                #print("jetzt kommt die txt")
                #print(verschlüsselter_byte_aus_txt)
                entschlüsselter_byte_aus_txt = self.fernet.decrypt(verschlüsselter_byte_aus_txt)
                #print("jetzt kommt das entschlüsselte aus der txt datei")
                #print(entschlüsselter_byte_aus_txt)
                entschlüsselter_byte_aus_txt_als_utf8 = entschlüsselter_byte_aus_txt.decode('utf-8')
                entschlüsselter_byte_aus_txt_für_json = json.loads(entschlüsselter_byte_aus_txt_als_utf8)
                #print(entschlüsselter_byte_aus_txt_für_json)
                self.kontakte = entschlüsselter_byte_aus_txt_für_json
                #except:
                #    print("[-FATAL-] Konnte die Kontaktliste nicht entschlüsseln, Ein unbekannter Fehler ist aufgetreten, wahrscheinlich ist die Kontaktliste beschädigt.")
            self.Kopfzeile = ['Vorname', 'Nachname', 'Passwort', 'Firma']


            for col in self.Kopfzeile:
                self.tree.heading(col, text=col.title(),
                    command=lambda c=col: sortby(self.tree, c, 0))
                # Spaltenbreite an schriftart anpassen
                self.tree.column(col,
                    width=tkFont.Font().measure(col.title()))
                
            for item in self.kontakte:
                self.tree.insert('', 'end', values=[item['Vorname'], item['Nachname'], item['Passwort'], item['Firma']])

            try:    # Spaltenbreite anpassen wenn nötig
                for ix, val in enumerate(item):
                    col_w = tkFont.Font().measure(val)
                    if self.tree.column(self.Kopfzeile[ix],width=None)<col_w:
                        self.tree.column(self.Kopfzeile[ix], width=col_w)
            except:
                print("Fehler beim Berechnen der Spaltenbreiten.")

            def sortby(tree, col, descending):
                print("6")

                # wert zum sortieren wählen
                data = [(tree.set(child, col), child) \
                    for child in tree.get_children('')]
                # wenn die Daten zum sortieren zahlen sind, dann die untere Gleitkomma funktion nutzen
                #data =  change_numeric(data)
                # sortieren
                data.sort(reverse=descending)
                for ix, item in enumerate(data):
                    tree.move(item[1], '', ix)
                # das selbe in rückwärts
                tree.heading(col, command=lambda col=col: sortby(tree, col, \
                    int(not descending)))

            self.Kontakte_Einfügen_Knopp_zeigen.pack(side="bottom", anchor="w")
            
        
            
##################################################################################################################### 

    def kBe(self):
        print("kbe hat angefangen")
        self.Kontakt_bearbeiten = tk.Toplevel()
        self.Kontakt_bearbeiten.title("Einen Kontakt bearbeiten")
        self.Kontakt_bearbeiten.geometry("520x260+950+350")
        self.Kontakt_bearbeiten.resizable(False,False)
        self.Kontakt_bearbeiten.attributes('-toolwindow', True)
        self.Kontakt_bearbeiten.configure(bg=self.Hintergrund_farbe)
        self.Kontakt_bearbeiten.grab_set()  # Deaktiviert das Hauptfenster
        self.Kontakt_bearbeiten.lift() # packt das fenster immer in den Vordergrund.
        
        def altes_löschen():
            print("[-DEV-] Kontakt:löschen_c gestartet...")
            self.kontaktE = {"Vorname": self.Vorname1 , "Nachname": self.Nachname1, "Passwort": self.Passwort1, "Firma": self.Firma1}
            print("[-DEV-] jetzt nochmal das was ich speichern wollte: ", self.kontaktE)
            with open(self.KTK_Speicherort + "Kontaktliste.txt", "rb") as f:
                verschlüsselter_byte_aus_txt = f.read()
            print("[-DEV-] jetzt kommt die txt")
            print(verschlüsselter_byte_aus_txt)
            entschlüsselter_byte_aus_txt = self.fernet.decrypt(verschlüsselter_byte_aus_txt)
            print("[-DEV-]  jetzt kommt das entschlüsselte aus der txt datei")
            print(entschlüsselter_byte_aus_txt)
            entschlüsselter_byte_aus_txt_als_utf8 = entschlüsselter_byte_aus_txt.decode('utf-8')
            entschlüsselter_byte_aus_txt_für_json = json.loads(entschlüsselter_byte_aus_txt_als_utf8)
            print(entschlüsselter_byte_aus_txt_für_json)
            print("hier kommt nochmal das self.kontaktE",self.kontaktE)
            formatierter_string = {key: f'{value}' if isinstance(value, int) else value for key, value in self.kontaktE.items()}
            print(formatierter_string)
            entschlüsselter_byte_aus_txt_für_json.remove(formatierter_string)
            selected_item = self.tree.selection()
            if selected_item:
                self.tree.delete(selected_item)
            print("jetzt das fertige dingssss")
            print(entschlüsselter_byte_aus_txt_für_json)
            Liste_mit_neuem_kontakt = entschlüsselter_byte_aus_txt_für_json
            neues_verschlüsseltes_dings = self.fernet.encrypt(json.dumps(Liste_mit_neuem_kontakt).encode('utf-8'))
            try:
                with open(self.KTK_Speicherort  + "Kontaktliste.txt", "wb+") as f:
                    f.write(neues_verschlüsseltes_dings)
            except PermissionError:
                print("[-FATAL-] Die berechtigung zum Schreiben fehlt.")
                messagebox.showerror(title="Fehlercode 20", message="Es Fehlt für diesen Ordner die nötige Berechtigung, Die Kontakliste konnte nicht aufgerufen werden.")
        self.bearbeiten_fertsch = tk.Button(self.Kontakt_bearbeiten, text="Speichern", command="")
        #self.bearbeiten_fertsch.bind('<Button-1>', KTest)
        #self.Kontakt_bearbeiten.bind('<Return>', KTest)
        self.bearbeiten_fertsch.pack()
        def Kontakt_bearbeiten_f_schließen():
            print("[-INFO-] Kontakte bearbeiten fenster wurde wieder geschlossen und das hauptfenster sollte wieder freigegenben sein.")
            self.Kontakt_bearbeiten.grab_release()
            self.Kontakt_bearbeiten.destroy()
            #self.Kontakt_bearbeiten.unbind('<Return>')
        self.Kontakt_bearbeiten.protocol("WM_DELETE_WINDOW", Kontakt_bearbeiten_f_schließen)
        self.BebVN_E = tk.Entry(self.Kontakt_bearbeiten)
        self.BebVN_E.place(x=200, y=50)
        self.BebNN_E = tk.Entry(self.Kontakt_bearbeiten)
        self.BebNN_E.place(x=200, y=80)
        self.BebVN_L = tk.Label(self.Kontakt_bearbeiten, bg="lightsteelblue", fg="Black", text="Vorname")
        self.BebNN_L = tk.Label(self.Kontakt_bearbeiten, bg="lightsteelblue", fg="Black", text="Nachname")
        self.BebFN_L =tk.Label(self.Kontakt_bearbeiten, bg="lightsteelblue", fg="Black", text="Firma")   
        self.BebFN_E = tk.Entry(self.Kontakt_bearbeiten)
        self.BebFN_E.place(x=200,y=110)
        self.BebP_E = tk.Entry(self.Kontakt_bearbeiten)
        self.BebP_E.place(x=200, y=150)
        self.BebP_E1 = tk.Entry(self.Kontakt_bearbeiten) 
        self.BebP_E1.place(x=200, y=180)
        self.BebP_L = tk.Label(self.Kontakt_bearbeiten, bg="lightsteelblue", fg="Black", text="Passwort")
        self.BebP_L1 = tk.Label(self.Kontakt_bearbeiten, bg="lightsteelblue", fg="Black", text="Passwort Bestätigen")
        self.BebVN_L.place(x=120 ,y=50)
        self.BebNN_L.place(x=120 ,y=80)
        self.BebFN_L.place(x=120 ,y=110)
        self.BebP_L.place (x=120 ,y=150)
        self.BebP_L1.place(x=70,y=180)
        try:
            self.BebVN_E.insert(END,self.Vorname1)
            self.BebNN_E.insert(END,self.Nachname1)
            self.BebP_E.insert(END,self.Passwort1)
            self.BebP_E1.insert(END,self.Passwort1)
            self.BebFN_E.insert(END,self.Firma1)
        except:
            AttributeError
            Kontakt_bearbeiten_f_schließen()
            print("na vielleichts wählste mal noch aus WAS du bearbeiten willst?")
            DingsLabel = tk.Label(self, text="Sie müssen zuerst auswählen welchen Kontakt Sie bearbeiten möchten.", fg="Black")
            self.Kontakt_bearbeiten.unbind('<Return>')
            print("fehler fertch")
            

            messagebox.showinfo(title="Fehler 60", message="Fehler 60: Sie müssen zuerst auswählen welchen Kontakt Sie bearbeiten möchten. Wenn dieses Problem bestehen bleibt wenden Sie sich bitte an den Support")
        self.Beb_Knopp.pack_forget

        def KTest(event):#kbe
            print("KTest kbe hat angefangen...")
            #self.H_Name = ""
            #self.H_NName = ""
            #self.H_Passwort = ""
            #self.Passwort1 = ""
            #self.H_FirmName = ""
            self.kontakte = []
            #try:
            self.H_Name = self.BebVN_E.get()
            self.H_NName = self.BebNN_E.get()
            self.H_Passwort = self.BebP_E.get()
            self.H_Passwort1 = self.BebP_E1.get()
            self.H_FirmName = self.BebFN_E.get()
            print("[-DEV-] self.H_Name: ",self.H_Name)
            print("[-DEV-] self.H_NName: ",self.H_NName)
            print("[-DEV-] self.H_Passwort: ",self.H_Passwort)
            print("[-DEV-] self.H_Passwort: ",self.H_Passwort1)
            print("[-DEV-] self.H_FirmName: ",self.H_FirmName)
            #except:
                #print("is doch alles schaise ey")
                #pass
            #if self.H_Name != "" or self.H_NName != "" or self.H_Passwort != "" or self.Passwort1 != "" or self.H_FirmName != "":
            print("[-INFO-] die var entrys hats genommen (KTest von kbe) ")
            if self.H_Passwort == self.H_Passwort1:
                print("[-DEV-] die ersten gehen")
                if self.H_Name != "":
                    print("[-DEV-] Dings Name ist ein wert")
                    if self.H_NName !="":
                        print("[-DEV-] Dings nname ist ein wert")
                        if self.H_Passwort !="":
                            print("[-DEV-] Dings passwort ist ein wert")
                            if self.H_Passwort1 != "":
                                PW_falsch = tk.Label(self.Kontakt_bearbeiten, text="Die Passwörter stimmen nicht überein", bg="white", fg="red")
                                PW_falsch.place_forget()
                                print("[-DEV-] Dings Passwort1 ist ein Wert")
                                if self.H_FirmName !="":
                                    print("[-DEV-] Dings Firmaname ist ein Wert")
                                    self.kontaktE = {"Vorname": self.H_Name, "Nachname": self.H_NName, "Passwort": self.H_Passwort, "Firma": self.H_FirmName }
                                    with open(self.KTK_Speicherort + "Kontaktliste.txt", "rb") as f:
                                        verschlüsselter_byte_aus_txt = f.read()
                                    print("[-DEV-] jetzt kommt die txt")
                                    print(verschlüsselter_byte_aus_txt)
                                    entschlüsselter_byte_aus_txt = self.fernet.decrypt(verschlüsselter_byte_aus_txt)
                                    print("[-DEV-] jetzt kommt das entschlüsselte aus der txt datei")
                                    print(entschlüsselter_byte_aus_txt)
                                    entschlüsselter_byte_aus_txt_als_utf8 = entschlüsselter_byte_aus_txt.decode('utf-8')
                                    entschlüsselter_byte_aus_txt_für_json = json.loads(entschlüsselter_byte_aus_txt_als_utf8)
                                    print(entschlüsselter_byte_aus_txt_für_json)
                                    entschlüsselter_byte_aus_txt_für_json.append(self.kontaktE)
                                    print("[-DEV-] jetzt das fertige dingssss")
                                    print(entschlüsselter_byte_aus_txt_für_json)
                                    Liste_mit_neuem_kontakt = entschlüsselter_byte_aus_txt_für_json
                                    if isinstance(self.kontaktE, dict) and 'Vorname' in self.kontaktE and 'Nachname' in self.kontaktE and 'Firma' in self.kontaktE:
                                        #self.Kontaktelistbox.insert(tk., kontaktE['Vorname'] + " " + kontaktE['Nachname'] + " (" + kontaktE['Firma'] + ")")
                                        self.tree.insert('', 'end', values=[self.kontaktE['Vorname'], self.kontaktE['Nachname'], self.kontaktE['Passwort'], self.kontaktE['Firma']])
                                    else:
                                        messagebox.showwarning(title="Fehler 941", message="Fehler 941 bitte starten Sie das Programm neu.")
                                    #neues_verschlüsseltes_dings = self.fernet.encrypt(bytes(Liste_mit_neuem_kontakt, 'utf-8'))
                                    neues_verschlüsseltes_dings = self.fernet.encrypt(json.dumps(Liste_mit_neuem_kontakt).encode('utf-8'))
                                    try:
                                        with open(self.KTK_Speicherort + "Kontaktliste.txt", "wb") as f:
                                            f.write(neues_verschlüsseltes_dings)
                                    except PermissionError:
                                        print("[-FATAL-] Die berechtigung zum Beschreiben fehlt.")
                                        messagebox.showerror(title="Fehlercode 20", message="Es Fehlt für diesen Ordner die nötige Berechtigung, Die Kontakliste konnte nicht aufgerufen werden.")

                                    self.Kontakt_bearbeiten.destroy()
                                    altes_löschen()
                                else:
                                    print("[-DEV-] Firmenname is leer")
                                    self.H_FirmName = " "
                                    print("[-DEV-] Dings Firmenname ist ein Wert")
                                    self.kontaktE = {"Vorname": self.H_Name, "Nachname": self.H_NName, "Passwort": self.H_Passwort, "Firma": self.H_FirmName }
                                    with open(self.KTK_Speicherort + "Kontaktliste.txt", "rb") as f:
                                        verschlüsselter_byte_aus_txt = f.read()
                                    print("[-DEV-] jetzt kommt die txt")
                                    print(verschlüsselter_byte_aus_txt)
                                    entschlüsselter_byte_aus_txt = self.fernet.decrypt(verschlüsselter_byte_aus_txt)
                                    print("[-DEV-] jetzt kommt das entschlüsselte aus der txt datei")
                                    print(entschlüsselter_byte_aus_txt)
                                    entschlüsselter_byte_aus_txt_als_utf8 = entschlüsselter_byte_aus_txt.decode('utf-8')
                                    entschlüsselter_byte_aus_txt_für_json = json.loads(entschlüsselter_byte_aus_txt_als_utf8)
                                    print(entschlüsselter_byte_aus_txt_für_json)
                                    entschlüsselter_byte_aus_txt_für_json.append(self.kontaktE)
                                    print("jetzt das fertige dingssss")
                                    print(entschlüsselter_byte_aus_txt_für_json)
                                    Liste_mit_neuem_kontakt = entschlüsselter_byte_aus_txt_für_json
                                    if self.tree_iz_da == 1:
                                        if isinstance(self.kontaktE, dict) and 'Vorname' in self.kontaktE and 'Nachname' in self.kontaktE and 'Firma' in self.kontaktE:
                                            #self.Kontaktelistbox.insert(tk.END, kontaktE['Vorname'] + " " + kontaktE['Nachname'] + " (" + kontaktE['Firma'] + ")")
                                            self.tree.insert('', 'end', values=[self.kontaktE['Vorname'], self.kontaktE['Nachname'], self.kontaktE['Passwort'], self.kontaktE['Firma']])
                                        else:
                                            messagebox.showwarning(title="Fehler 941", message="Fehler 941 bitte starten Sie das Programm neu.")
                                    elif self.tree_iz_da == 0:
                                        self.Krams()
                                        if isinstance(self.kontaktE, dict) and 'Vorname' in self.kontaktE and 'Nachname' in self.kontaktE and 'Firma' in self.kontaktE:
                                            #self.Kontaktelistbox.insert(tk.END, kontaktE['Vorname'] + " " + kontaktE['Nachname'] + " (" + kontaktE['Firma'] + ")")
                                            self.tree.insert('', 'end', values=[self.kontaktE['Vorname'], self.kontaktE['Nachname'], self.kontaktE['Passwort'], self.kontaktE['Firma']])
                                        else:
                                            messagebox.showwarning(title="Fehler 941", message="Fehler 941 bitte starten Sie das Programm neu.")
                                    #neues_verschlüsseltes_dings = self.fernet.encrypt(bytes(Liste_mit_neuem_kontakt, 'utf-8'))
                                    neues_verschlüsseltes_dings = self.fernet.encrypt(json.dumps(Liste_mit_neuem_kontakt).encode('utf-8'))
                                    with open(self.KTK_Speicherort + "Kontaktliste.txt", "wb") as f:
                                        f.write(neues_verschlüsseltes_dings)
                                    altes_löschen()
                                    self.Kontakt_bearbeiten.destroy()
                            else:
                                print("Passwört1 ist kein Wert")
                                print("[-ERR-] Passwörter stimmen nicht überein")
                                messagebox.showerror(title="Fehler", message="Die Passwörter stimmen nicht überein, bitte überprüfen Sie Ihre angaben.")
                        else:
                            print("passwort ist kein wert")
                            print("[-ERR-] Passwörter stimmen nicht überein")
                            messagebox.showerror(title="Fehler", message="Die Passwörter stimmen nicht überein, bitte überprüfen Sie Ihre angaben.")
                    else:
                        print("NName hat keinen wert")
                        print("[-ERR-] Passwörter stimmen nicht überein")
                        messagebox.showerror(title="Fehler", message="Der Nachname darf nicht frei sein, bitte überprüfen Sie Ihre angaben.")
                else:
                    print("name ist kein wert da")
                    print("[-ERR-] Passwörter stimmen nicht überein")
                    messagebox.showerror(title="Fehler", message="Der Vorname darf nicht frei sein, bitte überprüfen Sie Ihre angaben.")
            else:
                print("[-ERR-] Passwörter stimmen nicht überein")
                messagebox.showerror(title="Fehler", message="Die Passwörter stimmen nicht überein, bitte überprüfen Sie Ihre angaben.")
                #self.pw_ne = tk.Label(self.Kontakt_bearbeiten,text="Die Passwörter stimmen nicht überein", bg="White", fg="RED")
                #self.pw_ne.place(x=110,y=0)
                #Thread(target = self.Kontakt_bearbeiten.after(2000, self.pw_ne_h())).start()
                

        
        #else:
         #   print("[-ERR-] Nicht alle Entrys waren gefüllt.")
        
        
        self.bearbeiten_fertsch.bind('<Button-1>', KTest)
        self.Kontakt_bearbeiten.bind('<Return>', KTest)
        

        
    def pw_ne_h(self):
        print("[-INFO-] pw_ne_h()")
        self.pw_ne.place_forget()

    def rrschl(self):
        def read_registry_value(key_path, value_name):
            try:
                key = winreg.OpenKey(winreg.HKEY_CURRENT_USER, key_path, 0, winreg.KEY_READ)
                value, value_type = winreg.QueryValueEx(key, value_name)
                winreg.CloseKey(key)
                return value
            except WindowsError:
                print("'Windows Error' bei der def 'rrschl' wer weiß was es bedeutet...")


        # Beispiel: Auslesen des Standard-Mailers
        key_path = r"Software\Microsoft\Windows\Shell\Associations\UrlAssociations\mailto\UserChoice"
        value_name = "ProgId"

        self.default_mailer = read_registry_value(key_path, value_name)
        if self.default_mailer:
            print("Standard-Mailer:", self.default_mailer)
        else:
            print("Kein Standard-Mailer festgelegt bzw. nicht gefunden.")
            
    


    def KTLS_C(self):
        
        self.KTLS.pack_forget()
        self.tree.grid_forget()
        self.container.pack_forget()
        self.msg.pack_forget()
        self.TauschenLBundEN.pack_forget()
        #self.show_button.pack_forget()
        self.Kontakte_AnzeigenMainMenu.pack(side="bottom", anchor="w")
        self.Kontakte_Einfügen_Knopp_zeigen.pack_forget()
        self.Beb_Knopp.pack_forget()
        self.Kontakt_löschen.pack_forget()
        self.KonvKnopp.pack_forget()
        self.tree_iz_da = 0
        self.kbe_k_iz_da = 0
        self.Kontakt_löschen_knopp_iz_da = 0

    def KTL_D(self):
        messagebox.showinfo(title='Information', message="Vorname: {} Nachname: {} Firma: {} Passwort: {}".format(self.Vorname1, self.Nachname1, self.Firma1, self.Passwort1))
    

    def guckn(self):
        print("gucken (def)")
        
        with open (self.KTK_Speicherort + "Kontaktliste.txt", "rb") as f:
            verschlüsselter_byte_aus_txt = f.read()
        print("jetzt kommt die txt")
        print(verschlüsselter_byte_aus_txt)
        entschlüsselter_byte_aus_txt = self.fernet.decrypt(verschlüsselter_byte_aus_txt)
        print("jetzt kommt das entschlüsselte aus der txt datei")
        print(entschlüsselter_byte_aus_txt)
        entschlüsselter_byte_aus_txt_als_utf8 = entschlüsselter_byte_aus_txt.decode('utf-8')
        entschlüsselter_byte_aus_txt_für_json = json.loads(entschlüsselter_byte_aus_txt_als_utf8)
        print(entschlüsselter_byte_aus_txt_für_json)

    def Kontaktliste_auslesen(self):
        print("[-DEV-] Kontaktliste_auslesen (def)")
        try:
            with open(self.KTK_Speicherort + "Kontaktliste.txt", "rb") as f:
                verschlüsselter_byte_aus_txt = f.read()
        except FileNotFoundError:
            if self.vnv == 1:
                messagebox.showerror(title="Fehler", message="Die Kontaktliste konnte nicht ausgelesen werden, da es die Datei dazu nicht gibt.")
                print("[-ERR-] Fehler beim Auslesen der KTK (1)")
                self.vnv = 2
                return
            elif self.vnv == 2:
                messagebox.showerror(title="Fehler", message="Nein es gibt sie immernoch nicht sorry.")
                print("[-ERR-] Fehler beim Auslesen der KTK (2)")
                self.vnv = 3
                return
            elif self.vnv == 3:
                messagebox.showerror(title="NEIN", message="Auch beim dritten mal muss ich dir leider sagen dass es die KTK (Kontaktliste.txt) immer noch nicht gibt, tut mir leid, wenn du aber bereits in die Tischkannte beißt, dann sprich mal den ach so witzigen Programmierer an der diese Nachrichten hier geschrieben hat :D.")
                print("[-ERR-] Fehler beim Auslesen der KTK (3)")
                self.vnv = 1
                return
            else:
                messagebox.showerror(title="Fehler", message="Die Kontaktliste konnte nicht ausgelesen werden, da es die Datei dazu nicht gibt.")
                print("[-ERR-] Fehler beim Auslesen der KTK (1)")
                self.vnv = 2
                return
        print("jetzt kommt die txt")
        print(verschlüsselter_byte_aus_txt)
        entschlüsselter_byte_aus_txt = self.fernet.decrypt(verschlüsselter_byte_aus_txt)
        print("jetzt kommt das entschlüsselte aus der txt datei")
        print(entschlüsselter_byte_aus_txt)
        entschlüsselter_byte_aus_txt_als_utf8 = entschlüsselter_byte_aus_txt.decode('utf-8')
        print("jetzt als utf8")
        print(entschlüsselter_byte_aus_txt_als_utf8)
        entschlüsselter_byte_aus_txt_für_json = json.loads(entschlüsselter_byte_aus_txt_als_utf8)
        print(entschlüsselter_byte_aus_txt_für_json)
        messagebox.showinfo(title="Info", message="Die Kontaktliste wurde ausgelesen und steht im zugehörigen Terminal oder in der Logdatei.")
        
        
    




    def Attch_an_mail_packn(self):#### hat nur 15h und viel kaffee gedauert(was man halt so macht Mittwoch Nacht/Dienstag Morgen)
        if self.default_mailer == "Thunderbird.Url.mailto":#thunderbird
            print("g1")
            Thunderbird()
        elif self.default_mailer == "Outlook.URL.mailto.15":#outlook
            try:
                print("g2")
                file_path = "verschluesselt.zip"
                outlook = win32com.client.Dispatch("Outlook.Application")
                mail = outlook.CreateItem(0)  # 0 steht für eine neue E-Mail
                # Empfänger, Betreff und Text der E-Mail
                mail.Subject = ""
                mail.Body = "Anbei die Datei."
                # Anhang hinzufügen
                attachment_path = os.path.abspath(file_path)
                attachment = attachment_path
                mail.Attachments.Add(attachment)
                # E-Mail anzeigen
                mail.Display()
            except:
                #try:
                    print("datei nicht im standat ort zum anhängen gefunden, versuche den selbst einegstellten ort.")
                    file_path = "output/verschluesselt.zip"
                    print(file_path)
                    outlook = win32com.client.Dispatch("Outlook.Application")
                    mail = outlook.CreateItem(0)  # 0 steht für eine neue E-Mail
                    # Empfänger, Betreff und Text der E-Mail
                    mail.Subject = ""
                    mail.Body = "Anbei die Datei."
                    # Anhang hinzufügen
                    attachment_path = os.path.abspath(file_path)
                    attachment = attachment_path
                    mail.Attachments.Add(attachment)
                    # E-Mail anzeigen
                    mail.Display()
                #except:
                #    print("Konnte die Datei nicht anhängen da sie nicht gefunden wurde, versuchen sie die Datei erneut zu konvertieren und versuchen Sie es dann erneut.")
                #    messagebox.showerror(title="Fehler beim anhängen der Datei", message="Konnte die Datei nicht anhängen da sie nicht gefunden wurde, versuchen sie die Datei erneut zu konvertieren und versuchen Sie es dann erneut.")
        elif self.default_mailer == "AppXydk58wgm44se4b399557yyyj1w7mbmvd":#dieses standard windows mail dings
            print("g3")
            messagebox.showerror(title="Fehler", message="Die standart Windows Mail App wird ncht unterstützt.")
        else:
            messagebox.showinfo(title='Information: Fehler 17', message="Fehler 17: Bitte stellen Sie sicher dass sie Thunderbird oder Microsoft Outlook auf dieser Maschine Installiert bzw als Email Programm eingestellt haben, wenn Sie hilfe Benötigen wenden Sie sich bitte an Ihren Administrator oder an den Support")


    


    
    
    def dings1(self):
        pyautogui.hotkey('tab')
        pyautogui.hotkey('tab')
        pyautogui.hotkey('alt')
        pyautogui.hotkey('i')
        pyautogui.hotkey('5')
        pyautogui.hotkey('s')
        pyautogui.write(self.DND_Pfad)
        pyautogui.hotkey('Enter')

    def einstellungentestdings(self):
        einstellungenjson = {"test_einstellung": "Dings"}
        
        with open("einstellungenjson.json", "w" ) as f:
            json.dump(einstellungenjson, f)

    #def Log_pfad_json(self):
    #    print("Log_pfad_json(def)")
    #    self.einstellungenN = {"Log_pfad": self.Neu_gewählterordner_für_logs}
    #    print("die var wurde als json objekt gelegt.")
    #    print(self.einstellungenN)
    #    try:
    #        with open("einstellungen.json" "r") as f:
    #            self.einstellungen = json.load(f)
    #    except:
    #        print("in Log_pfad_json konnten wir die einstellungen nicht laden.")
    #    
    #    
    #    try:
    #        with open("einstellungen.json", "w" ) as fn:
    #            self.einstellungen.append(self.einstellungenN, fn)
    #    except:
    #        print("einstellungen waren wohl leer und werden nun überschrieben...")
    #        try:
    #            with open("einstellungen.json", "w" ) as fn:
    #                json.dump(self.einstellungenN, fn)
    #        except:
    #            print("okay... hier stimmt etwas gewaltig nicht.")

    def einstellungentestwat(self):
        with open("einstellungenjson.json", "r") as f:
            einstellungenjson = json.load(f)

        if einstellungenjson["test_einstellung"] == "Dings":
            print("Die einstellung heißt Dings ")

        if einstellungenjson["test_einstellung"] == "Bums":
           print("Die einstellung heißt Bums ")

    def einstellungen_laden(self):
        with open("einstellungen/log_einst.json", "r") as E:
            Einstellungen_Inhalt = json.load(E)

        if Einstellungen_Inhalt["Speicherort"] == "":
            print("keine Einstellung zum speicherort vorhanden")
        else:
            print("Einstellungen zum Speicherort vorhanden")

        #self.Speicherort.set(Einstellungen_Inhalt["Speicherort"])
        #if Einstellungen_Inhalt["Speicherort"] == "12":
        #    print("speicherort ist 12")
        ##setting2.set(Einstellungen_Inhalt["einstellung2"])
        #print("Einstellungen geladen!")

    #def Einstellung_Speicherort_ändern(self):
    #    self.einstellungenSO = {"Speicherort": self.Speicherort_entry.get(),"einstellung2": "setting2.get()"}
    #    with open("einstellungen.json", "w") as Eb:
    #        json.dump(self.einstellungenSO, Eb)
    #        print("Einstellungen gespeichert!")
#
    #def dngs
    #    try:
    #        with open("einstellungen.json", "r") as f:
    #            settings = json.load(f)
    #            self.Speicherort.set(Einstellungen_Inhalt["Speicherort"])
    #            if settings["einstellung1"] == "12":
    #                print("JAHUHUHUUUIIIIII")
    #            setting2.set(settings["einstellung2"])
    #            print("Einstellungen geladen!")
    #    except FileNotFoundError:
    #        print("Keine gespeicherten Einstellungen gefunden.")


        


    def OrdnKonv(self):
        
        self.folder_path = filedialog.askdirectory()
        if self.folder_path:
            self.etwas_bereits_eingefügt = 1
            dings_event_data1 = self.folder_path
            self.Entrylabel = tk.Label(self, width=80, background=self.dieser_komische_grünton, text="Ausgewählte Datei: " + dings_event_data1)
            self.configure(bg=self.dieser_komische_grünton)
            self.Entrylabel.pack()
            self.entrydnd.insert(END, self.folder_path)
            self.entry21_r1 = self.folder_path
            #self.folder_path = self.Entry.get()
            #self.DataKnopp.place_forget()
            ##self.KonvKnopp.pack_forget()
            self.KonvKnopp.pack(side="right", anchor="s")
            #self.TauschenLBundEN.place(x=200,y=0)
            if self.tree_iz_da == 1:
                print("tree iz da")
            else:
                print("tree iz ni da")
                self.Krams()
        # bei sowohl data als auch ordn konv kann der fehler "objc[1458]: Invalid or prematurely-freed autorelease pool 0x7fce290acf08.zsh: abort      /usr/local/bin/python3 " 
        # auftreten was bedeutet das eine def funktion in einer def funktion aufgerufen wurde bevor die erste fertig war.#### wie sich herausstellte ist dies nicht immer der fall... aber es klingt logisch.
        
    

    def DataKonv(self):
        self.file_path = filedialog.askopenfilename()
        if self.file_path:
            self.etwas_bereits_eingefügt = 1
            dings_event_data1 = self.file_path
            self.Entrylabel = tk.Label(self, width=80, background=self.dieser_komische_grünton, text="Ausgewählte Datei: " + dings_event_data1)
            self.Entrylabel.pack()
            self.configure(bg=self.dieser_komische_grünton)
            #self.file_path = self.file_path
            self.entrydnd.insert(END, self.file_path)
            self.entry21_r1 = self.file_path
            #self.file_path = 
            #self.OrdnKnopp.place_forget()
            #self.KonvKnopp.pack_forget()
            self.KonvKnopp.pack(side="right", anchor="s")
            #self.TauschenLBundEN.place(x=200,y=0)
            #self.KonvKnopp.place(x=330,y=210)
            if self.tree_iz_da == 1:
                print("tree is offen")
            else:
                print("tree is nicht offen")
                self.Krams()
                
                
        # bei sowohl data als auch ordn konv kann der fehler "objc[1458]: Invalid or prematurely-freed autorelease pool 0x7fce290acf08.zsh: abort      /usr/local/bin/python3 " 
        # auftreten was bedeutet das eine def funktion in einer def funktion aufgerufen wurde bevor die erste fertig war.#### wie sich herausstellte ist dies nicht immer der fall... aber es klingt logisch.
            

    def verschieben(self):
        self.speicherort = self.zip_ordner_speicherort
        print("verschieben (def)")
        print("speicherort: " + self.speicherort)
        try:
            print("packe das verschl. zip in den output")
            shutil.copy("verschluesselt.zip", "output/")
            print("hat geklappt!")
        except:
            try:
                print("Das hat nicht geklappt, ich versuche es nochmal...")
                shutil.copy("verschluesselt.zip", "output/")
                print("jetzt hats funktioniert! :)")
            except:
                print("das hat nicht geklappt!")
        try:
            print("versuche die Verschlüsslte Datei zu verschieben...")
            shutil.move("verschluesselt.zip", self.speicherort)
            print("hat geklappt!")
        except:
            try:
                print("Das hat nicht geklappt, ich versuche es nochmal...")
                shutil.move("verschluesselt.zip", self.speicherort)
                print("jetzt hats funktioniert! :)")
            except:
                print("das hat nicht geklappt!")
        print("Datei in den Ordner gelegt.")

        try:
            print("versuche die NICHT verschluesselte Datei zu verschieben...")
            shutil.move("gepackt.zip", "temp/")
            print("hat geklappt!")
        except:
            try:
                print("[-DEV-] Das hat nicht geklappt, ich versuche es nochmal...")
                shutil.move("gepackt.zip", "temp/")
                print("[-DEV-] jetzt hats funktioniert! :)")
            except:
                print("[-ERR-] das hat nicht geklappt!")
        print("[-DEV-] Datei in den temp Ordner gelegt.")
        
        

        

    def OrdnFertsch(self):
        print("[-DEV-] OrdnFertsch(def)")
        self.configure(bg="Yellow")
        self.Entrylabel.configure(bg="Yellow")
        self.KonvKnopp.pack_forget()
        
        try:
            print("[-DEV-] versuche die alte Datei zu löschen..")
            os.remove(self.zip_ordner_speicherort + "verschluesselt.zip")
            print("[-DEV-] hat geklappt!")
        except:
            try:
                os.remove(self.zip_ordner_speicherort + "/verschluesselt.zip")
                print("[-DEV-] alte datei mit slash wurde gelöscht")
            except:
                print("[-ERR-] das hat nicht geklappt!")
        try:
            print("[-DEV-] Versuche die alte unverschlüsselte Datei zu löschen..")
            os.remove("temp/gepackt.zip")
            print("[-DEV-] hat geklappt!")
        except:
            print("[-ERR-] Das verschieben mit gepackt.zip hat nicht geklappt!")
        print("[-DEV-] Das Passwort aus den Entrys lautet")
        print("[-DEV-] " ,self.password_entry.get())
        if self.password_entry.get() and self.password_entryB.get() != "":
            print("[-DEV-] Die Entrys self.password_entry und self.password_entry sind NICHT leer")
            if self.password_entry.get() != self.password_entryB.get():
                print("[-DEV-] Die Entrys self.password_entry und self.password_entry stimmen NICHT über ein.")
                self.Zu_Blöd_zum_schreiben.place(x=50,y=160)
                self.after(5000, self.Zu_Blöd_zum_schreiben.place_forget())
                self.Ladebalken.pack_forget()
                self.Ladebalkenfenster.destroy()
                self.Entrylabel.pack_forget()
            else:
                    self.Ladebalken['value'] += 5
                    self.Zu_Blöd_zum_schreiben.place_forget()
                    if hasattr(self, "folder_path"):
                        self.Ladebalken['value'] += 5
                        with zipfile.ZipFile("gepackt.zip", "w", zipfile.ZIP_DEFLATED) as zip_file:
                            self.Ladebalken['value'] += 20
                            for foldername, subfolders, filenames in os.walk(self.folder_path):
                                self.Ladebalken['value'] += 10
                                for filename in filenames:
                                    self.Ladebalken['value'] += 10
                                    file_path = os.path.join(foldername, filename)
                                    zip_file.write(file_path, os.path.relpath(file_path, self.folder_path))
                                    self.Ladebalken['value'] += 10
                        with pyzipper.AESZipFile("verschluesselt.zip", "w", compression=pyzipper.ZIP_DEFLATED, encryption=pyzipper.WZ_AES) as encrypted_zip:
                            self.Ladebalken['value'] += 10
                            encrypted_zip.setpassword(self.password_entry.get().encode())
                            print(self.password_entry.get())
                            for foldername, subfolders, filenames in os.walk(self.folder_path):
                                for filename in filenames:
                                    file_path = os.path.join(foldername, filename)
                                    self.Ladebalken['value'] += 20
                                    encrypted_zip.write(file_path, os.path.relpath(file_path, self.folder_path))
                                    print("[-DEV-] Fertig")
                            self.KonvKnopp.pack_forget()
                            self.Ladebalken.pack_forget()
                            self.Ladebalkenfenster.destroy()
                            self.Entrylabel.pack_forget()
                            self.Datei_gezogen = 0
                            self.etwas_bereits_eingefügt = 0
                            self.configure(bg=self.Hintergrund_farbe)
                            try:
                                self.KonvKnopp.pack_forget()
                            except:
                                print("[-INFO-] Konnte den dndknv knopf nicht despawnen lassen es gab ihn wohl nicht.")
                            zip_file.close()
                            encrypted_zip.close()
                            messagebox.showinfo(title="Info", message="Datei wurde erfolgreich verarbeitet und kann nun an Eine Email gehängt werden.")
                            self.Entrylabel.pack_forget()
                            self.verschieben()
                            print("[-DEV-] Dateien geschlossen")
                    else:
                        messagebox.showinfo(title='Fehler 5', message="Fehler 5: Verpacken der Datei fehlgeschlagen, wenn dieses Problem bestehen bleibt wenden Sie sich bitte an den Support.")
                        self.Ladebalken.pack_forget()
                        self.Ladebalkenfenster.destroy()
                        print("[-ERR-] err def OrdnFertsch (ohne kontakt) Fehler 5")
                        self.Datei_gezogen = 0
                        self.etwas_bereits_eingefügt = 0
                        self.Entrylabel.pack_forget()
                        self.configure(bg=self.Hintergrund_farbe)
                        try:
                            self.KonvKnopp.pack_forget()
                        except:
                            print("[-INFO-] Konnte den dndknv knopf nicht despawnen lassen es gab ihn wohl nicht.") 
        else:
            #try:
                if self.Passwort1 != "":
                    #self.kontaktM = self.Passwort1    
                    self.entry_pw_u = tk.Entry(self)
                    self.entry_pw_u.place(x=69420,y=69420)
                    self.entry_pw_u.insert(END, self.Passwort1)
                    print(self.entry_pw_u.get())
                    self.folder_path = self.path
                    print("[-DEV-] else funktion wurde erwischt")
                    self.Ladebalken['value'] += 5
                    #self.Kontakt_Passwort = self.kontaktM
                    #print(self.kontaktM)
                    #print(self.Kontakt_Passwort)
                    if hasattr(self, "folder_path"):
                        print("[-DEV-] geht noch")
                        self.Ladebalken['value'] += 5
                        with zipfile.ZipFile("gepackt.zip", "w", zipfile.ZIP_DEFLATED) as zip_file:
                            self.Ladebalken['value'] += 20
                            # 68 49 110 103 53 #
                            print("[-DEV-] geht noch1")
                            for foldername, subfolders, filenames in os.walk(self.folder_path):
                                print("[-DEV-] geht noch2")
                                for filename in filenames:
                                    print("[-DEV-] geht noch3")
                                    self.file_path = os.path.join(foldername, filename)
                                    self.Ladebalken['value'] += 20
                                    print("[-DEV-] hier das andere path dings")
                                    print("[-DEV-] "  ,self.file_path)
                                    zip_file.write(self.file_path, os.path.relpath(self.file_path, self.folder_path))
                                    print("[-DEV-] ordner zu zip verarbeitet")
                                    print("[-DEV-] ",self.entry_pw_u.get())
                        with pyzipper.AESZipFile("verschluesselt.zip", "w", compression=pyzipper.ZIP_DEFLATED, encryption=pyzipper.WZ_AES) as encrypted_zip:
                            self.Ladebalken['value'] += 30
                            print("[-DEV-] encr 1")
                            encrypted_zip.setpassword(self.entry_pw_u.get().encode())
                            print("[-DEV-] encr 2")
                            for foldername, subfolders, filenames in os.walk(self.folder_path):
                                print("[-DEV-] encr 3")
                                for filename in filenames:
                                    print("[-DEV-] encr 4")
                                    self.file_path = os.path.join(foldername, filename)
                                    print("[-DEV-] encr 5")
                                    encrypted_zip.write(self.file_path, os.path.relpath(self.file_path, self.folder_path))
                                    print("[-DEV-] encr 6")
                                print("[-DEV-] verschlüsselte zip erstellt.")
                                self.Ladebalken['value'] += 20
                            self.KonvKnopp.pack_forget()
                            zip_file.close()
                            encrypted_zip.close()
                            print("[-DEV-] dateien geschlossen")
                            self.entry_pw_u.delete(0, tk.END)
                            self.entry_pw_u.place_forget()
                            self.Ladebalken.pack_forget()
                            self.Ladebalkenfenster.destroy()
                            self.Datei_gezogen = 0
                            self.etwas_bereits_eingefügt = 0
                            self.Entrylabel.pack_forget()
                            self.configure(bg=self.Hintergrund_farbe)
                            try:
                                self.KonvKnopp.pack_forget()
                            except:
                                print("[-INFO-] Konnte den dndknv knopf nicht despawnen lassen es gab ihn wohl nicht.")
                            messagebox.showinfo(title="Info", message="Datei wurde erfolgreich verarbeitet und kann nun an Eine Email gehängt werden.")
                            self.file_path = ""
                            self.verschieben()
                else:
                    messagebox.showinfo(title='Fehler 5', message="Fehler 5: Verpacken der Datei fehlgeschlagen, wenn dieses Problem bestehen bleibt wenden Sie sich bitte an den Support.")
                    self.Entrylabel.pack_forget()
                    self.configure(bg=self.Hintergrund_farbe)
                    self.Ladebalkenfenster.destroy()
                    self.Entrylabel.pack_forget()
                    self.Datei_gezogen = 0
                    self.etwas_bereits_eingefügt = 0
                    try:
                        self.KonvKnopp.pack_forget()
                    except:
                        print("[-INFO-] Konnte den dndknv knopf nicht despawnen lassen es gab ihn wohl nicht.")

    def TLBUEN(self):
        self.password_entry.place(x=130,y=60)
        self.password_entryB.place(x=130,y=90)
        self.pwtextB.place(x=0, y=90)
        self.pwtext.place(x=0, y=60)
        if self.Datei_gezogen == 1:
            self.pwtext.configure(background=self.dieser_komische_grünton)
            self.pwtextB.configure(background=self.dieser_komische_grünton)
        elif self.Datei_gezogen == 0:
            self.pwtext.configure(background=self.Hintergrund_farbe)
            self.pwtextB.configure(background=self.Hintergrund_farbe)
        self.TauschenLBundEN.config(text="Schließen", command=self.TauschenLBundEN_Wech)
        #self.menu.configure(test="Schließen")
        
    
    def TauschenLBundEN_Wech(self):
        if self.tree_iz_da == 1:
            print("[-INFO-] Tree iz da")
        elif self.tree_iz_da == 0:
            self.Kontakte_AnzeigenMainMenu.pack(side="bottom", anchor="w")
            self.tree_iz_da = 1
        else:
            print("[-ERR-] Es ist ein Fehler beim entscheiden von tree_iz_da aufgetreten")
        self.password_entry.place_forget()
        self.password_entryB.place_forget()
        self.pwtext.place_forget()
        self.pwtextB.place_forget()
        self.TauschenLBundEN.config(text="eigenes Passwort verwenden", command=self.TLBUEN)
        #self.menu.configure(label="Schließen", command=self.TLBUEN)

                

    def DataFertsch(self):
        print("[-DEV-] DataFertsch(def)")
        self.configure(bg="Yellow")
        self.Entrylabel.configure(bg="Yellow")
        try:
            self.KonvKnopp.pack_forget()
        except:
            print("[-INFO-] Konnte den dndknv knopf nicht despawnen lassen es gab ihn wohl nicht.")
        try:
            print("[-INFO-] versuche die alte Datei zu löschen..")
            os.remove(self.zip_ordner_speicherort + "verschluesselt.zip")
            print("[-INFO-] hat geklappt!")
        except:
            print("[-ERR-] das hat nicht geklappt!")
        try:
            print("[-INFO-] versuche die alte unverschlüsselte Datei zu löschen..")
            os.remove("temp/gepackt.zip")
            print("[-ERR-] hat geklappt!")
        except:
            print("[-ERR-] das mit gepackt.zip hat nicht geklappt!")
        self.file_path = self.path
        print(self.password_entry.get())
        if self.password_entry.get() and self.password_entryB.get() != "":
            self.Ladebalken['value'] += 1
            print("[-INFO-] es hat mal was funktioniert")
            if self.password_entry.get() != self.password_entryB.get():
                self.Ladebalken['value'] += 4
                self.Zu_Blöd_zum_schreiben.place(x=50,y=160)
                self.after(5000, self.Zu_Blöd_zum_schreiben.place_forget())
                self.Ladebalken.pack_forget()
                self.Entrylabel.pack_forget()
            else:
                    print("[-INFO-] passwörter der entry stimmten überein")
                    self.Ladebalken['value'] += 5
                    self.Zu_Blöd_zum_schreiben.place_forget()
                    if hasattr(self, "file_path"):
                        with zipfile.ZipFile("gepackt.zip", "w", zipfile.ZIP_DEFLATED) as zip_file:
                            self.Ladebalken['value'] += 10
                            zip_file.write(self.file_path)
                            self.Ladebalken['value'] += 10
                        with pyzipper.AESZipFile("verschluesselt.zip", "w", compression=pyzipper.ZIP_DEFLATED, encryption=pyzipper.WZ_AES) as encrypted_zip:
                            self.Ladebalken['value'] += 20
                            encrypted_zip.setpassword(self.password_entry.get().encode())
                            self.Ladebalken['value'] += 10
                            encrypted_zip.write(self.file_path, os.path.basename(self.file_path))
                            self.Ladebalken['value'] += 30
                        self.KonvKnopp.pack_forget()
                        self.Ladebalken['value'] += 10
                        self.Ladebalken.pack_forget()
                        self.Ladebalkenfenster.destroy()
                        self.Datei_gezogen = 0
                        self.etwas_bereits_eingefügt = 0
                        self.Entrylabel.pack_forget()
                        self.configure(bg=self.Hintergrund_farbe)
                        try:
                            self.KonvKnopp.pack_forget()
                        except:
                            print("[-INFO-] Konnte den dndknv knopf nicht despawnen lassen es gab ihn wohl nicht.")
                        messagebox.showinfo(title="Info", message="Datei wurde erfolgreich verarbeitet und kann nun an Eine Email gehängt werden.")
                        self.verschieben()
                    else:
                        messagebox.showinfo(title='Fehler 5', message="Fehler 5: Verpacken der Datei fehlgeschlagen, wenn dieses Problem bestehen bleibt wenden Sie sich bitte an den Support.")
                        print("[-ERR-] err def DataFertsch")
                        self.Ladebalken.pack_forget()
                        self.Ladebalkenfenster.destroy()
                        self.Datei_gezogen = 0
                        self.etwas_bereits_eingefügt = 0
                        self.Entrylabel.pack_forget()
                        self.configure(bg=self.Hintergrund_farbe)
                        
        else:
                    print("[-INFO-] 0%")
                    if self.Passwort1 != "": 
                        self.kontaktM = self.Passwort1    
                        self.entry_pw_u = tk.Entry(self)
                        self.entry_pw_u.place(x=69420,y=69420)
                        self.entry_pw_u.insert(END, self.Passwort1)
                        print(self.entry_pw_u.get())
                        print("[-INFO-] else funktion wurde erwischt")
                        print(self.kontaktM)
                        if hasattr(self, "file_path"):
                            print("[-INFO-] 10%")
                            self.Ladebalken['value'] += 10
                            with zipfile.ZipFile("gepackt.zip", "w", zipfile.ZIP_DEFLATED) as zip_file:
                                print("[-INFO-] 15%")
                                self.Ladebalken['value'] += 5
                                zip_file.write(self.file_path)
                                print("[-INFO-] 30%")
                                self.Ladebalken['value'] += 15
                            with pyzipper.AESZipFile("verschluesselt.zip", "w", compression=pyzipper.ZIP_DEFLATED, encryption=pyzipper.WZ_AES) as encrypted_zip:
                                print("[-INFO-] 34%")
                                self.Ladebalken['value'] += 4
                                encrypted_zip.setpassword(self.entry_pw_u.get().encode())
                                print("[-INFO-] 69%")
                                self.Ladebalken['value'] += 35
                                encrypted_zip.write(self.file_path, os.path.basename(self.file_path))
                                print("[-INFO-] 99%")
                                self.Ladebalken['value'] += 30
                            self.KonvKnopp.pack_forget()
                            self.entry_pw_u.delete(0, tk.END) 
                            self.entry_pw_u.place_forget() 
                            self.Ladebalken['value'] += 1
                            self.Ladebalken.pack_forget()
                            self.Ladebalkenfenster.destroy()
                            self.Datei_gezogen = 0
                            self.etwas_bereits_eingefügt = 0
                            self.Entrylabel.pack_forget()
                            self.configure(bg=self.Hintergrund_farbe)
                            try:
                                self.KonvKnopp.pack_forget()
                            except:
                                print("[-INFO-] Konnte den dndknv knopf nicht despawnen lassen es gab ihn wohl nicht.")
                            messagebox.showinfo(title="Info", message="Datei wurde erfolgreich verarbeitet und kann nun an eine Email gehängt werden.")
                            self.Entrylabel.pack_forget()
                            
                            self.file_path = ""
                            self.path = ""
                            print("[-INFO-] 100%")
                            print("[-INFO-] Konvertierung der Datei zum verschlüsselten Zip abgeschlossen")
                            self.verschieben()
                        else:
                            messagebox.showinfo(title='Fehler 5', message="Fehler 5: Verpacken der Datei fehlgeschlagen, wenn dieses Problem bestehen bleibt wenden Sie sich bitte an den Support.")
                            print("err def DataFertsch")
                            self.Ladebalken.pack_forget()
                            self.Ladebalkenfenster.destroy()
                            self.Datei_gezogen = 0
                            self.etwas_bereits_eingefügt = 0
                            self.Entrylabel.pack_forget()
                            self.configure(bg=self.Hintergrund_farbe)
                            try:
                                self.KonvKnopp.pack_forget()
                            except:
                                print("[-INFO-] Konnte den dndknv knopf nicht despawnen lassen es gab ihn wohl nicht.")
    def machste_dich(self):
        self.Dings_Fertsch_und_so.place_forget()
                
    def PW_Check(self):
        if self.password_entry.get() != self.password_entryB.get():
            self.Zu_Blöd_zum_schreiben.place(x=50,y=160)
        else:
            self.Zu_Blöd_zum_schreiben.place_forget()
            self.bestätigung.place(x=200, y=130)
            self.after(5000, self.best_Hide)

    def beides(self):
        Thread(target = self.absolut_arschkrass).start()
        self.Ladebalken_aktivieren()

    def Nix(self):
        print("Nix...")
        print("einfach Nix...")
        print("es passiert einfach Nix.")
        print("Fertsch. Feierabend. Schluss im Bus. Endegelände.")
        print("Diese funktion macht nix... keine Ahnung warum sie aufgerufen wurde... ach so ja du wolltest das Fenster schlieen tja das geht nicht.")


    def Ladebalken_aktivieren(self):
        self.Ladebalkenfenster = tk.Toplevel()
        self.Ladebalkenfenster.resizable(False,False)
        self.Ladebalkenfenster.protocol("WM_DELETE_WINDOW", self.Nix)
        self.Ladebalken = ttk.Progressbar(self.Ladebalkenfenster, orient="horizontal", mode="determinate", length=420)
        
        self.Ladebalkenfenster.title("Lädt")
        self.Ladebalkenfenster.configure(bg="lightsteelblue")
        
        self.Ladebalken.pack()
        
        
        #print("after für 5")
        #self.after(5000, self.abs())

    #def abs(self):
    #    print("ende des 5er after")
    #    if tk.Toplevel.winfo_exists(self.Ladebalken_Data_Fertsch):
    #        print("eigentlich sollte das fenster da sein.")
    #        self.absolut_arschkrass()
    #    else:
    #        print("def absolut_arsckrass_aktivieren ist fehlgeschlagen.")
        

    def absolut_arschkrass(self):
        print("[-DEV-] absakr")
        print("[-DEV-] entry: ", self.entrydnd.get())
        ##self.Entrylabel = tk.Label(self, width=80, background=self.dieser_komische_grünton)
        ##self.pwtext.configure(bg=self.dieser_komische_grünton)
        ##self.pwtextB.configure(bg=self.dieser_komische_grünton)
        ##self.Entrylabel.pack()
        ##dings_event_data1 = self.entrydnd.get().replace("{", "")
        ##dings_event_data1 = dings_event_data1.replace("}", "")
        ##self.Entrylabel.configure(text=("Ausgewählte Datei: " , dings_event_data1))
        dings10 = self.entry21_r1
        dings12 = dings10.replace("{", "")
        print("[-DEV-]",dings10," bums ",dings12)
        self.path = dings12.replace("}", "")
        print("[-DEV-] ",self.path)
        if os.path.isdir(self.path):  
            print("is ne dir")
            if self.entry21_r1 != "":
                self.folder_path = self.path
                ##self.KonvKnopp.pack_forget()
                self.KonvKnopp.pack_forget()
                #self.TauschenLBundEN.place(x=200,y=0)
                if self.password_entry.get() and self.password_entryB.get() == "":
                    if self.Passwort1 == "":
                        print("FEHLER 4: kein pw in absakr, wohl die treeview ignoriert.")
                        messagebox.showinfo(title='Fehler', message="Fehler 4: Bitte wählen sie ein passwort aus der Kontaktliste aus, oder wählen Sie ein eigenes \n Fehlercode: 4")
                    else:
                        self.OrdnFertsch()
                else:
                    self.OrdnFertsch()
        elif os.path.isfile(self.path):  
            print("is ne datei")
            if self.entry21_r1 != "":
                self.file_path = self.entry21_r1
                #self.KonvKnopp.pack_forget()
                self.KonvKnopp.pack_forget()
                #self.TauschenLBundEN.place(x=200,y=0)
                self.DataFertsch()
                
        else:  
            print("es wurde mehr als eine Datei hineingezogen welche nicht in einem ordner war, oder es konnte nicht erkannt werden ob es sich um eine Datei oder Ordner handelt. (womöglich ist was mit dem Datei/ordner pfad schiefgegangen)" )
            self.Ladebalken.pack_forget()
            self.Ladebalkenfenster.destroy()
            messagebox.showerror(title="Fehler", message="Es ist ein Fehler aufgetreten, Wenn Sie mehr als eine Datei Verschlüsseln möchten, legen Sie diese Bitte zuerst in einen Ordner und ziehen Sie diesen Hier Hinein.\nWenn Dieser Fehler bestehen bleibt, Wenden Sie sich bitte an den Support.\nFehlercode: 23")
            

    def best_Hide(self):
        self.bestätigung.place_forget()  

        
    #def create_widgets(self):
        #beide pfade abgleichen mit if wenn eins leer ist
        


    def löschen(self):
        if os.path.exists("gepackt.zip"):
            os.remove("gepackt.zip")
        else:
            print("Diese Datei Existiert noch nicht")
    
    def open_file_dialog(self, event):
        self.file_path = filedialog.askopenfilename()
        if self.file_path:
            self.file_path = self.file_path
            

    

    def ordner_öffnen_dialog(self):
        self.folder_path = filedialog.askdirectory()
        if self.folder_path:
            self.folder_path = self.folder_path
            

      


    #def packenundverschlüsseln(self):
    #    if hasattr(self, "file_path"):
    #        with zipfile.ZipFile("gepackt.zip", "w", zipfile.ZIP_DEFLATED) as zip_file:
    #            zip_file.write(self.file_path)
    #        with pyzipper.AESZipFile("verschlüsselt.zip", "w", compression=pyzipper.ZIP_DEFLATED, encryption=pyzipper.WZ_AES) as encrypted_zip:
    #            encrypted_zip.setpassword(self.password_entry.get().encode())
    #            encrypted_zip.write(self.file_path, os.path.basename(self.file_path))
    #        self.drop_label.config(text="Datei gepackt und verschlüsselt.")
    #    else:
    #        self.drop_label.config(text="Keine Datei ausgewählt.")

    
    

    def Aufreumen(self):
        if os.path.exists("gepackt.zip"):
            os.remove("gepackt.zip")

        else:
            print("Keine Dateien zum löschen gefunden")

###################################         EINSTELLUNGEN       ###########################

    def einstellungen(self):
        einstellungen = tk.Toplevel()
        einstellungen.title("Einstellungen")
        einstellungen.geometry("420x420+950+350")
        einstellungen.configure(bg="lightsteelblue")
#########if self.geladene_design_einst["Design_mode"] == "Windoof":
#########                    print("Windoof Design wird genutzt.")


        if self.geladene_design_einst["Design_mode"] == "Modern":
            einstellungen.Leeren_Knopp = tk.Button(einstellungen, text="Alte Zip Dateien leeren", cursor="pirate", command=self.Leeren,  relief=tk.RAISED, bd=3, compound=tk.CENTER, bg="#3366CC", fg="white", font=("Helvetica", 12), padx=10, pady=5, borderwidth=0, highlightthickness=0, activebackground="#6699FF")
            einstellungen.jsonLeeren_Knopp = tk.Button(einstellungen, text="Kontaktliste Löschen", command= self.ktk_l_bst_c,  relief=tk.RAISED, bd=3, compound=tk.CENTER, bg="#3366CC", fg="white", font=("Helvetica", 12), padx=10, pady=5, borderwidth=0, highlightthickness=0, activebackground="#6699FF") #sind jetzt txt dateien mit verschlüsselung
            self.outputordner_öffnen = tk.Button(einstellungen, text="Zielordner öffnen", command= self.outputordner_öffnen_c, relief=tk.RAISED, bd=3, compound=tk.CENTER, bg="#3366CC", fg="white", font=("Helvetica", 12), padx=10, pady=5, borderwidth=0, highlightthickness=0, activebackground="#6699FF" )
            self.log_ordner_suchen = tk.Button(einstellungen, text="Log-Datei Speicherort auswählen", command=self.outputordner_suchen)
        elif self.geladene_design_einst["Design_mode"] == "Windoof":
            einstellungen.Leeren_Knopp = tk.Button(einstellungen, text="Alte Zip Dateien leeren", cursor="pirate", command=self.Leeren)
            einstellungen.jsonLeeren_Knopp = tk.Button(einstellungen, text="Kontaktliste Löschen", command= self.ktk_l_bst_c) #sind jetzt txt dateien mit verschlüsselung
            self.outputordner_öffnen = tk.Button(einstellungen, text="Zielordner öffnen", command= self.outputordner_öffnen_c)
            self.log_ordner_suchen = tk.Button(einstellungen, text="Log-Datei Speicherort auswählen", command=self.outputordner_suchen)
        else:
            print("Fehler beim überprüfen der eintellungen. Standart Design bzw. Windoof wird nun verwendet.")
            einstellungen.Leeren_Knopp = tk.Button(einstellungen, text="Alte Zip Dateien leeren", cursor="pirate", command=self.Leeren)
            einstellungen.jsonLeeren_Knopp = tk.Button(einstellungen, text="Kontaktliste Löschen", command= self.ktk_l_bst_c) #sind jetzt txt dateien mit verschlüsselung
            self.outputordner_öffnen = tk.Button(einstellungen, text="Zielordner öffnen", command= self.outputordner_öffnen_c)
            self.log_ordner_suchen = tk.Button(einstellungen, text="Log-Datei Speicherort auswählen", command=self.outputordner_suchen)
        
        einstellungen.Leeren_Knopp.place(x=0, y=0)
        einstellungen.jsonLeeren_Knopp.place(x=0,y=30)
        self.ausgabe_Leeren_KnoppG = tk.Label(einstellungen, text="Zip Dateien Gelöscht.")
        self.ausgabe_Leeren_KnoppErr = tk.Label(einstellungen, text="Keine Dateien zum löschen gefunden.")
        self.ausgabe_Leeren_KnoppGV = tk.Label(einstellungen, text="Verschlüsselte Zip Dateien Gelöscht.")
        self.ausgabe_Leeren_KnoppGV.pack()
        self.ausgabe_Leeren_KnoppGV.pack_forget()
        self.ausgabe_Leeren_KnoppG.pack()
        self.ausgabe_Leeren_KnoppG.pack_forget()
        self.ausgabe_Leeren_KnoppErr.pack()
        self.ausgabe_Leeren_KnoppErr.pack_forget()

        
        self.outputordner_öffnen.pack()

        
        #self.log_ordner_suchen.pack()

        Email_C_AUSW_L = tk.Label(einstellungen, text="Explitites Email Programm auswählen")
        Thunderbird_t_L = tk.Label(einstellungen, text="Nur Thunderbird nutzen")

        Email_C_AUSW_L.place(x=10,y=100)
        Thunderbird_t_L.place(x=10,y=130)
        try:
            with open("einstellungen/log_einst.json", "r") as f:
                einstellungen = json.load(f)
            print(einstellungen)
        except:
            print("Das Laden der einstellungen in dem einstellungsfenster ist fehlgeschlagen.")

    def outputordner_suchen(self):
        print("outputordner_suchen(def)")
        self.Neu_gewählterordner_für_logs = filedialog.askdirectory()
        print(self.Neu_gewählterordner_für_logs)
        self.Neu_gewählterordner_für_logs1 = self.Neu_gewählterordner_für_logs + "/"
        print(self.Neu_gewählterordner_für_logs1)
        #self.Log_pfad_json()
        print("Log_pfad_json(def)")
        self.einstellungenN = {"Log_pfad": self.Neu_gewählterordner_für_logs1}
        print("die var wurde als json objekt gelegt.")
        print(self.einstellungenN)
        #try:
        #    with open("einstellungen.json" "r") as f:
        #        self.einstellungen = json.load(f)
        #except:
        #    print("in Log_pfad_json konnten wir die einstellungen nicht laden.")
        
        
        try:
            with open("einstellungen/log_einst.json", "w" ) as fn:
                self.einstellungen.append(self.einstellungenN, fn)
        except:
            print("einstellungen waren wohl leer und werden nun überschrieben.")
            try:
                with open("einstellungen/log_einst.json", "w" ) as fn:
                    json.dump(self.einstellungenN, fn)
            except:
                print("okay... hier stimmt etwas gewaltig nicht.")
    
    def outputordner_suchen_z(self):
        print("outputordner_suchen(def)")
        self.Neu_gewählterordner_für_zips = filedialog.askdirectory()
        print(self.Neu_gewählterordner_für_zips)
        self.Neu_gewählterordner_für_zips1 = self.Neu_gewählterordner_für_zips + "/"
        print(self.Neu_gewählterordner_für_zips1)
        print("Log_pfad_json(def)")
        self.einstellungenN_zips = {"Zip_pfad": self.Neu_gewählterordner_für_zips1}
        print("die var wurde als json objekt gelegt.")
        print(self.einstellungenN_zips)
        try:
            with open("einstellungen/outp_einst.json", "w" ) as fnzips:
                json.dump(self.einstellungenN_zips, fnzips)
        except:
            print("okay... hier stimmt etwas gewaltig nicht. zips")
        
#####################

    def ktk_l_bst_c(self):
        print("ktk_l_bst_c(def)")
        self.tag_und_zeit_string = time.strftime("%m/%d/%Y, %H:%M:%S")
        abfrage_wegen_löschen_db = messagebox.askquestion(title='Information', message="möchten Sie wirklich die gesamte Kontaktliste unwiderruflich löschen?")
        if abfrage_wegen_löschen_db == "yes":
            
                print("löschen der db vom Nutzer bestätigt")
                print(self.tag_und_zeit_string)
                self.db_Leeren()
        elif abfrage_wegen_löschen_db == "no":
            print("löschen der db vom Nutzer abgerbrochen.")
        else:
            print("db löschen fehler (def kk_l_bst_c(self))")
            messagebox.showerror(title="ein schwerwiegender Fehler ist aufgetreten.", message=self.Absturz_meldung)

    def Leeren(self):
        if os.path.exists("output/verschluesselt.zip"):
            os.remove("output/verschluesselt.zip")
            self.ausgabe_Leeren_KnoppGV.place(x=0 , y=340)
            self.after(5000, self.G_Hide)
            
        else:
          self.ausgabe_Leeren_KnoppErr.place(x=0,y=320)
          self.after(5000, self.Err_Hide)

        if os.path.exists("temp/gepackt.zip"): #du hast an der verschwindenen dings gearbeitet ; nein habe ich nicht, der linke kommentar ist monate her, huch...
            os.remove("temp/gepackt.zip")
            self.ausgabe_Leeren_KnoppG.place(x=20,y=320)
            self.after(5000, self.G_Hide)
            
        else:
           print("Keine Dateien zum löschen gefunden")
           self.ausgabe_Leeren_KnoppErr.place(x=0,y=320)
           self.after(5000, self.Err_Hide)

    def db_Leeren(self):
        try:
            if os.path.exists(self.KTK_Speicherort + "Kontaktliste.txt"):
                os.remove(self.KTK_Speicherort + "Kontaktliste.txt")
                print("Kontaktliste erfolgreich gelöscht.")
                self.after(5000, self.G_Hide)  

            else:
              self.ausgabe_Leeren_KnoppErr.place(x=0,y=320)
              self.after(5000, self.Err_Hide)
        except PermissionError:
            messagebox.showerror(title="Fehler, Zugriff verweigert", message="Sie haben nicht die nötige Berechtigung um die Kontaktliste zu löschen da diese sich in einem Speziell geschüzten Bereich bedindet, vesuchen Sie es mit den nötigen Berechtigungen erneut.")
            print("[-ERR-] Fehler, jemand hat versucht die KTK zu löschen hatte aber die nötige Berechtigung nicht.")
    def G_Hide(self):
        self.ausgabe_Leeren_KnoppG.pack_forget()

    def GV_Hide(self):
        self.ausgabe_Leeren_KnoppGV.pack_forget()

    def Err_Hide(self):
        self.ausgabe_Leeren_KnoppErr.pack_forget()

    def NeuenKontaktHinzufügen(self):
        print("NeuenKontaktHinzufügen (def)")
        NeuenKontaktHinzufügen_F = tk.Toplevel()
        NeuenKontaktHinzufügen_F.title("Einen neuen Kontakt erstellen.")
        NeuenKontaktHinzufügen_F.geometry("520x260+950+350")
        NeuenKontaktHinzufügen_F.resizable(False,False)
        NeuenKontaktHinzufügen_F.attributes('-toolwindow', True)
        NeuenKontaktHinzufügen_F.configure(bg="lightsteelblue")
        NeuenKontaktHinzufügen_F.grab_set()  # Deaktiviert das Hauptfenster
        NeuenKontaktHinzufügen_F.lift() # --__--
        def NeuenKontaktHinzufügen_F_schließen():
            print("Kontakte Hinzufügen fenster wurde wieder geschlossen und das hauptfenster sollte wieder freigegenben sein.")
            NeuenKontaktHinzufügen_F.grab_release()
            NeuenKontaktHinzufügen_F.destroy()
        NeuenKontaktHinzufügen_F.protocol("WM_DELETE_WINDOW", NeuenKontaktHinzufügen_F_schließen)

        Name1 = tk.Entry(NeuenKontaktHinzufügen_F)
        Name1.place(x=200, y=50)
        Name2 = tk.Entry(NeuenKontaktHinzufügen_F)
        Name2.place(x=200, y=80)
        TextBox_Name_KHvN = tk.Label(NeuenKontaktHinzufügen_F, bg="lightsteelblue", fg="Black", text="Vorname")
        TextBox_Name_KHnN = tk.Label(NeuenKontaktHinzufügen_F, bg="lightsteelblue", fg="Black", text="Nachname")
        
        TextBox_Name_KHFN =tk.Label(NeuenKontaktHinzufügen_F, bg="lightsteelblue", fg="Black", text="Firma")   
        FirmenName = tk.Entry(NeuenKontaktHinzufügen_F)
        FirmenName.place(x=200,y=110)

        PW_eingabe1 = tk.Entry(NeuenKontaktHinzufügen_F)
        PW_eingabe1.place(x=200, y=150)
        PW_eingabe2 = tk.Entry(NeuenKontaktHinzufügen_F)
        PW_eingabe2.place(x=200, y=180)
        TextBox_Name_KHP = tk.Label(NeuenKontaktHinzufügen_F, bg="lightsteelblue", fg="Black", text="Passwort")
        TextBox_Name_KHPB = tk.Label(NeuenKontaktHinzufügen_F, bg="lightsteelblue", fg="Black", text="Passwort Bestätigen")
        TextBox_Name_KHvN.place(x=120 ,y=50 )
        TextBox_Name_KHnN.place(x=120 ,y=80 )
        TextBox_Name_KHFN.place(x=120 ,y=110 )
        TextBox_Name_KHP.place (x=120 ,y=150 )
        TextBox_Name_KHPB.place(x=70,y=180 )
        
        #scrollbar = tk.Scrollbar(NeuenKontaktHinzufügen)
        #listbox = tk.Listbox(NeuenKontaktHinzufügen, height=20, width=30,fg="Black", bg="White", yscrollcommand= scrollbar.set)
        #self.listbox.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
        #MulmVerbot
        
        #scrollbar.place(x=275 ,y=40)
        #scrollbar.config( command = listbox.yview )

        #listbox.place(x=10,y=10)

        self.kontakte = []
        for kontakt in self.kontakte:
            self.tree.insert('', 'end', values=[kontakt['Vorname'], kontakt['Nachname'], kontakt['Passwort'], kontakt['Firma']])
        def KTest(event):
            print("[-INFO-] das originale KTest hat angefangen")
        

            self.kontakte = []

            self.kontakte = {}
            self.kontaktE = {}

            H_Name = Name1.get()
            H_NName = Name2.get()
            H_Passwort = PW_eingabe1.get()
            H_Passwort1 = PW_eingabe2.get()
            H_FirmName = FirmenName.get()

            if all([H_Name, H_NName, H_Passwort]):
                if FirmenName.get():
                    print("[-DEV-] Firmname ist ein Wert")
                else:
                    print("[-DEV-] Firmname ist Leer")
                    H_FirmName = " "

                if Name1.get():
                    print("[-DEV-] VName ist ein Wert")
                else:
                    print("[-DEV-] VName ist Leer")
                    TextBox_Name_KHvN.configure(fg="RED")
                    messagebox.showerror(title="Fehler", message="Bitte füllen Sie alle Felder aus.")
                    return
                if Name2.get():
                    print("[-DEV-] NName ist ein Wert")
                else:
                    print("[-DEV-] NName ist Leer")
                    TextBox_Name_KHnN.configure(fg="RED")
                    messagebox.showerror(title="Fehler", message="Bitte füllen Sie alle Felder aus.")
                    return
                if PW_eingabe1.get() != PW_eingabe2.get():
                    print("[-DEV-] PW_eingabe1 und 2 stimmen nicht überein")
                    messagebox.showerror(title="Fehler", message="Die Passwörter stimmen nicht Überein..")
                    return
                # Verschlüsselte Daten vorbereiten
                kontakt = {"Vorname": H_Name, "Nachname": H_NName, "Passwort": H_Passwort, "Firma": H_FirmName}
                verschl_kontakt = self.fernet.encrypt(bytes(json.dumps(kontakt), 'utf-8'))
                #D1ng5
                # Bestehende Kontakte lesen und zur Liste hinzufügen, wenn vorhanden
                try:
                    with open(self.KTK_Speicherort + "Kontaktliste.txt", "rb") as datei:
                        verschl_contacts = datei.read()
                        entschluesselter_byte_aus_txt = self.fernet.decrypt(verschl_contacts)
                        bestehende_kontakte = json.loads(entschluesselter_byte_aus_txt.decode('utf-8'))
                        NeuenKontaktHinzufügen_F.destroy()
                except FileNotFoundError:
                    bestehende_kontakte = []

                bestehende_kontakte.append(kontakt)

                # Die aktualisierte Kontaktliste in der Textdatei speichern
                try:
                    with open(self.KTK_Speicherort + "Kontaktliste.txt", "wb+") as datei:
                        verschl_contacts = self.fernet.encrypt(bytes(json.dumps(bestehende_kontakte), 'utf-8'))
                        datei.write(verschl_contacts)
                        NeuenKontaktHinzufügen_F.destroy()
                except PermissionError:
                        print("[-FATAL-] Die berechtigung zum Beschreiben fehlt.")
                        messagebox.showerror(title="Fehlercode 20", message="Es Fehlt für diesen Ordner die nötige Berechtigung, Die Kontakliste konnte nicht aufgerufen werden.")
                except:
                    print("[-FATAL-] Der für die KTK gewählte Ordner Existiert nicht.")
                    messagebox.showerror(title="Fehlercode 19", message="Der Pfad konnte zwar gelesen werden, allerdings scheint der Ausgewählte Ordner nicht zu existieren.")
                    
                if self.tree_iz_da == 1:
                    #if isinstance(self.kontaktE, dict) and 'Vorname' in self.kontaktE and 'Nachname' in self.kontaktE and 'Firma' in self.kontaktE:
                    #    self.tree.insert('', 'end', values=[self.kontaktE['Vorname'], self.kontaktE['Nachname'], self.kontaktE['Passwort'], self.kontaktE['Firma']])
                    #else:
                    #    self.tree.insert('', 'end', values=[self.kontaktE['Vorname'], self.kontaktE['Nachname'], self.kontaktE['Passwort'], self.kontaktE['Firma']])
                    #    messagebox.showwarning(title="Fehler 941", message="Fehler 941: Der Kontakt wurde Hinzugefügt aber es ist ein anderer Fehler aufgetreten, bitte Öffnen Sie die Kontaktliste erneut. (1)")
                    self.KTLS_C()
                    self.Krams()
                elif self.tree_iz_da == 0:
                    self.Krams()
                    #if isinstance(self.kontaktE, dict) and 'Vorname' in self.kontaktE and 'Nachname' in self.kontaktE and 'Firma' in self.kontaktE:
                    #    #self.Kontaktelistbox.insert(tk.END, kontaktE['Vorname'] + " " + kontaktE['Nachname'] + " (" + kontaktE['Firma'] + ")")
                    #    self.tree.insert('', 'end', values=[self.kontaktE['Vorname'], self.kontaktE['Nachname'], self.kontaktE['Passwort'], self.kontaktE['Firma']])
                    #else:
                    #    messagebox.showwarning(title="Fehler 941", message="Fehler 941: Der Kontakt wurde Hinzugefügt aber es ist ein anderer Fehler aufgetreten, bitte Öffnen Sie die Kontaktliste erneut. (0)")
            else:
                print("Nicht alle erforderlichen Felder sind ausgefüllt.")
                TextBox_Name_KHP .configure(fg="RED")
                TextBox_Name_KHPB.configure(fg="RED")
                TextBox_Name_KHvN.configure(fg="RED")
                TextBox_Name_KHnN.configure(fg="RED")
                messagebox.showerror(title="Fehler", message="Bitte füllen Sie alle benötigten Felder aus.")



        self.KTEST = tk.Button(NeuenKontaktHinzufügen_F, text="Fertig", highlightbackground="lightsteelblue", command="", relief=tk.RAISED, bd=3, compound=tk.CENTER, bg="#3366CC", fg="white", font=("Helvetica", 12), padx=10, pady=5, borderwidth=0, highlightthickness=0, activebackground="#6699FF")
        self.KTEST.place(x=0,y=220)
        NeuenKontaktHinzufügen_F.bind('<Return>', KTest)
        self.KTEST.bind('<Button-1>', KTest)

    
    

    
def Thunderbird():
    # Neues E-Mail-Verfassen-Fenster öffnen
    thunderbird_title = 'Thunderbird'

        #dieses dings mit dem try versucht das fenster zu finden sodass ich auf error reagieren kann
    try:
        Fenster_Thunderbird = pyautogui.getWindowsWithTitle(thunderbird_title)[0]

    except AttributeError:
        messagebox.showerror(title="Fehler", message="Diese funktion funtkioniert derzeit nur unter Windows, wenn Sie sich unter Windows befinden, wenden Sie sich bitte an den Support.")
        #err3 = tk.Toplevel()
     #   err3.title("Fehler 3")
     #   err3.geometry("520x240+950+350")

    #  Err3_text = tk.Label(err3, text="Fehler: Attribut Error, diese funktion funtkioniert derzeit nur unter Windows.")
      #  Err3_text.pack() 

    except IndexError: #wenn das fenster nicht gefunden wird also ein "index error", kommt der text unten
        messagebox.showinfo(title="Fehler 8", message="Bitte öffnen Sie zuerst Thunderbird, wemn dieses Problem bestehen bleibt wenden Sie sich an den Support oder nutzen Sie ein anderes Emailprogramm.")
        print("Fehler: IndexError: Thunderbird wird wohl nicht geöffnet sein, denn ich konnte das Fenster nicht finden :c ")
    else:

    # Setzen Sie den Fokus auf das Thunderbird-Fenster
        if Fenster_Thunderbird.isActive == False:
            Fenster_Thunderbird.activate()
        pyautogui.hotkey('ctrl', 'n')
        pyautogui.press('tab')
        pyautogui.press('tab')
        pyautogui.hotkey('ctrl', 'm')
        pyautogui.hotkey("ctrl", "shift", "a")
        pyautogui.write(r'verschlusselt.zip')
        pyautogui.press('enter')

    #def Details_Listbox(self):
def bye():
    print("[-INFO-] Programm wurde geschlossen.")
    print(time.strftime("%m/%d/%Y, %H:%M:%S"))
    print("[-INFO-] Lösche nun alte Dateien aus den Standard Verzeichnissen")
    if os.path.exists("output/verschluesselt.zip"):
        os.remove("output/verschluesselt.zip")
        print("[-INFO-] verschlüsseltes ZIP gelöscht")
    if os.path.exists("temp/gepackt.zip"): #du hast an der verschwindenen dings gearbeitet ; nein habe ich nicht, der linke kommentar ist monate her, huch...
        os.remove("temp/gepackt.zip")
        print("[-INFO-] unverschlüsseltes ZIP gelöscht")
    else:
       print("[-INFO-] Keine Dateien zum löschen gefunden")
    print("===========================================")
    
    sys.exit()
root.resizable(False,False)
root.geometry("420x200")
app = App(master=root)
root.protocol("WM_DELETE_WINDOW", bye)
app.mainloop()