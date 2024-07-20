try:
    import sys
    import customtkinter as tk
    ###import tkinter as tk
    from tkinter import ttk
    import tkinter as Atk
    from tkinter import messagebox
    from tkinter import filedialog
    from tkinter import Menu
    import time
    import os
    import csv
    import ctypes
    import json
    from threading import Thread
    from http.server import BaseHTTPRequestHandler, HTTPServer
    import urllib.parse
    import threading
    import subprocess
    import platform
    import smtplib
    from email.mime.multipart import MIMEMultipart
    from email.mime.text import MIMEText
    from tkinterdnd2 import DND_FILES
    from PIL import Image
    from collections import defaultdict
    from nltk.corpus import wordnet
    import re
except Exception as E:
    print(f"(FATAL) Fehler beim laden der Bibliotheken, Fehlermeldung: {E}")
    try:
        messagebox.showerror("Kritischer Fehler",f"(FATAL) Fehler beim laden der Bibliotheken, Fehlermeldung: {E}")
    except:
        sys.exit()
    sys.exit()

class Listendings:
    Programm_läuft = True
    class ChangelogLeer(Exception): # Die Exception die kommt, wenn der Changelog leer ist.
        "- Der Changelog ist leer -"

    class RequestHandler(BaseHTTPRequestHandler):
        def do_GET(self):
            saite = "<!DOCTYPE html><html lang='de'><head><meta charset='UTF-8'><meta name='viewport' content='width=device-width, initial-scale=1.0'><title>Ganzflächiger Hintergrund</title><style>body {margin: 0;padding: 0;background-color: #40444c;}.content {padding: 20px;color: white;font-family: Arial, sans-serif;}</style></head><body><div class='content'><h1>Meine Seite mit ganzflächigem Hintergrund</h1><p>Hier ist etwas Text auf der Seite.</p></div></body></html>"
            self.send_response(200)
            self.send_header('Content-type', 'text/html')
            self.end_headers()
            parsed_path = urllib.parse.urlparse(self.path)
            print("Angeforderter Pfad:", parsed_path.path)
            besserer_pfad = parsed_path.path.replace("/", "")
            print("Nummer die angerufen hat/wurde: ", besserer_pfad)
            if besserer_pfad == "b":
                ende_des_anrufs = time.strftime("%H:%M:%S")
                try:
                    with open("tmp1.txt", "w+") as tmp:
                            tmp.write(ende_des_anrufs)
                except Exception as e:
                    print(f"Fehler beim Schreiben in tmp1.txt: {e}")
                print("Der Anruf war wohl fertig. var: ", besserer_pfad)
            elif besserer_pfad == "a":
                print("Der bessere Pfad ist ein a.")
            else:
                try:
                    with open("tmp.txt", "w+") as tmp:
                        tmp.write(besserer_pfad)
                except Exception as e:
                    print(f"Fehler beim Schreiben in tmp.txt: {e}")
            self.wfile.write(b"<html><head><title>Starface Modul</title></head>")
            self.wfile.write(b"<meta name='viewport' content='width=device-width, initial-scale=1.0'><style>body {margin: 0;padding: 0;background-color: #293136;}.content {padding: 20px;color: white;font-family: Arial, sans-serif;}</style></head><body><div class='content'></div></body></html>")

    class WebServerThread(threading.Thread):
        def run(self):
            port = 8080
            server_address = ('', port)
            httpd = HTTPServer(server_address, Listendings.RequestHandler)
            try:
                while Listendings.Programm_läuft == True:
                    print(f'Ich horche mal auf Port {port}...') 
                    httpd.handle_request()
                    if Listendings.Programm_läuft == False: # wenn diese funktion hier jemals funktionieren würde, könnten hier auch Fehler erscheinen.
                        httpd.shutdown()
                        httpd.server_close()
                        print(f'Server auf Port {port} gestoppt.')
                        sys.exit()
            except KeyboardInterrupt:
                httpd.server_close()
                httpd.shutdown()
                print(f'Server auf Port {port} gestoppt.')

    class Logger(object):
        def __init__(self): #eine init welche nur das "unwichtige" vorgeplänkel macht (Logs und so)
            self.tag_und_zeit_string = time.strftime("%m/%d/%Y, %H:%M:%S")
            self.tag_string = str(time.strftime("%d %m %Y"))
            self.Benutzerordner = os.path.expanduser('~')
            self.Logs_Speicherort_ordner = os.path.join(self.Benutzerordner, 'CiM', 'Logs')
            Logname = self.tag_string + ".log"
            self.Logs_Speicherort_Datei = os.path.join(self.Logs_Speicherort_ordner, Logname)
            print("[-INFO-] ", self.tag_und_zeit_string)
            if not os.path.exists(self.Logs_Speicherort_ordner):
                try:
                    os.mkdir(self.Logs_Speicherort_ordner)
                    print(f"Konnte den Ordner {self.Logs_Speicherort_ordner} erstellen.")
                except:
                    print(f"Konnte den Ordner {self.Logs_Speicherort_ordner} nicht erstellen.")
            
            try:
                log_pfad = (self.Logs_Speicherort_Datei)
                self.terminal = sys.stdout
                self.log = open(log_pfad, "w")
            except:
                try:
                    log_pfad = (self.Logs_Speicherort_Datei)
                    self.terminal = sys.stdout
                    self.log = open(log_pfad, "w+")
                except:
                    print("heute keine Logs")
        def write(self, message):
            self.terminal.write(message)
            try:
                self.log.write(message)
            except:
                pass
        def flush(self):
            #für Python 3 wichtig wegen kompatibilität, hab aber keine wirkliche ahnung was das macht
            pass    
    sys.stdout = Logger()
# Freude ist bloß ein Mangel an Informationen
    def __init__(self, master):
        self.master = master
        self.Programm_Name = "M.U.L.M"
        self.Programm_Name_lang = "Multifunktionaler Unternehmens-Logbuch-Manager"
        self.Version = "Beta 1.0"
        self.Zeit = "Die Zeit ist eine Illusion."
        master.title(self.Programm_Name + " " + self.Version + "                                                                          " + self.Zeit)
        root.configure(resizeable=False)
        self.Programm_läuft = True
        self.Uhr_läuft = True
        root.protocol("WM_DELETE_WINDOW", self.bye)
        self.Listen_Speicherort_Netzwerk_geladen = None
        self.Zeit_text = None
        self.Uhrzeit_anruf_start = None
        self.Pause = True
        self.Menü_da = False
        self.beb = "0"
        self.Starface_Modul = "0"
        self.Auto_speichern_Einstellung = "0"
        self.Autospeichern_tkvar = "0"
        self.Uhrzeit_anruf_ende = None
        self.zeile_zahl = 0
        self.Anzal_der_Ergebnisse = 0
        self.tag_string = str(time.strftime("%d %m %Y"))
        self.Benutzerordner = os.path.expanduser('~')
        self.Listen_Speicherort_standard = os.path.join(self.Benutzerordner, 'CiM', 'Listen')
        self.Einstellungen_ordner = os.path.join(self.Benutzerordner, 'CiM', "Einstellungen")
        self.Starface_Einstellungsdatei = os.path.join(self.Einstellungen_ordner , "Starface_Modul.txt")
        self.Listen_Speicherort_Einstellungsdatei = os.path.join(self.Einstellungen_ordner, "Listendingsspeicherort.json")
        self.Listen_Speicherort_Netzwerk_Einstellungsdatei = os.path.join(self.Einstellungen_ordner, "Listendingsspeicherort_Netzwerk.json")
        self.Auto_speichern_Einstellungsdatei = os.path.join(self.Einstellungen_ordner, "Auto_speichern.txt") 
        self.icon_pfad = os.path.join(self.Benutzerordner, 'CiM', 'Assets', 'CiM_icon.png')
        self.index_liste_pfad_Einstellungsdatei = os.path.join(self.Benutzerordner, 'CiM', 'Einstellungen', 'CiM_Index.txt')
        self.Einstellung_Email_Sender_Adresse = os.path.join(self.Einstellungen_ordner , "Email_sender.txt")
        self.Einstellung_Email_Empfänge_Adresse = os.path.join(self.Einstellungen_ordner, "Email_Empfänger.txt")
        self.Einstellung_smtp_server = os.path.join(self.Einstellungen_ordner, "SMTP_Server.txt")
        self.Einstellung_smtp_Passwort = os.path.join(self.Einstellungen_ordner, "SMTP_Passwort.txt")
        self.Db_Ordner_pfad = os.path.join(self.Benutzerordner, 'CiM', 'Db')
        self.Json_pfad = os.path.join(self.Db_Ordner_pfad, 'Db.json')
        self.Einstellung_Theme = os.path.join(self.Einstellungen_ordner, "Theme.txt")
        self.Blacklist_pfad = os.path.join(self.Db_Ordner_pfad, "Db_Blacklist.json")
        self.Listen_Speicherort_Netzwerk_geladen_anders = "Netzwerkspeicherort: "
        self.Listen_Speicherort_geladen_anders = "Lokaler Speicherpfad: "
        
        try: ## das hier sind die Bilder
            self.Bearbeiten_Bild = tk.CTkImage(Image.open("Bilder/Bearbeiten.png"))
            self.Durchsuchen_Bild = tk.CTkImage(Image.open("Bilder/Durchsuchen.png"))
            self.Speichern_Bild = tk.CTkImage(Image.open("Bilder/Speichern.png"))
            self.Menü_Bild = tk.CTkImage(Image.open("Bilder/Menü.png"))
            self.Ticket_Bild = tk.CTkImage(Image.open("Bilder/Ticket.png"))
            self.Kalender_Bild = tk.CTkImage(Image.open("Bilder/Kalender.png"))
            self.Kunde_suchen_Bild = tk.CTkImage(Image.open("Bilder/Kunde_suchen.png"))
            self.Dings_Liste_Bild = tk.CTkImage(Image.open("Bilder/Dings_Liste.png"))
            self.Dings_Bild = tk.CTkImage(Image.open("Bilder/Dings.png"))
            self.Kopieren_Bild = tk.CTkImage(Image.open("Bilder/Kopieren.png"))
            self.Schnellnotiz_Bild = tk.CTkImage(Image.open("Bilder/Schnellnotiz.png"))
            self.Durchsuchen_Bild_zu = tk.CTkImage(Image.open("Bilder/Durchsuchen_zu.png"))
        except Exception as alk:
            messagebox.showinfo("", f"beim laden der Bild Assets ist ein Fehler aufgetreten: {alk}")
        
        self.Monat = time.strftime("%m")
        self.Thread_Kunderuftan = threading.Timer(2, self.Kunde_ruft_an)
        self.thread_uhr = threading.Timer(1, self.Uhr)
        self.thread_webserver = Listendings.WebServerThread()
        self.thread_webserver.daemon = True
        self.thread_uhr.daemon = True
        self.Thread_Kunderuftan.daemon = True
        self.thread_uhr.start()
        self.Thread_Kunderuftan.start()
        #self.thread_suche = threading.Thread(target=self.Suche_algo)
        #self.thread_suche.setDaemon(True)
        self.smtp_server_anmeldung_thread = threading.Timer(1, self.SMTP_Anmeldung)
        self.smtp_server_anmeldung_thread.daemon = True
        self.smtp_server_anmeldung_thread.start()
        
    #### Farben ####
        #self.Hintergrund_farbe = "SlateGrey"
        self.Hintergrund_farbe = "AntiqueWhite2"
        self.Hintergrund_farbe_Text_Widget = "AntiqueWhite2" #"AntiqueWhite" #"AntiqueWhite2"
        self.Textfarbe = "Black"
        self.Border_Farbe = "AntiqueWhite4"
        self.Entry_Farbe = "AntiqueWhite3"
        self.Ereignislog_farbe = self.Hintergrund_farbe_Text_Widget
        self.aktiviert_farbe = "aquamarine2"
        self.deaktiviert_farbe = "White"
        self.dunkle_ui_farbe = "burlywood2"
        self.helle_ui_farbe = "burlywood1"
        self.ja_ui_fabe = "burlywood"
    #### Farben Ende ####

        root.configure(fg_color=self.Hintergrund_farbe)
        root.resizable(False, False)
        self.Weiterleitung_an = ""
        self.wollte_sprechen = ""
        self.Starface_Farbe = "#4d4d4d"
        self.Starface_Farbe_Neu = "#293136"#-> Das hier ist die Dunklere Version und das hier
        self.Ort_wo_gesucht_wird = ""
        self.sender_email = ""
        self.empfänger_email = ""
        self.smtp_server = ""
        self.pw_email = ""
        self.smtp_login_erfolgreich = False
        self.das_hübsche_grau = "LightSlateGray"

        self.zachen = 0
        self.fertsch_var = None
        self.fertsch_vars = []
        self.etwas_suchen = False
        self.etwas_suchen1 = False
        self.Index_stand = None
        self.Kalender_offen = False
        self.Kontakt_soll_gleich_mitgespeichert_werden = True
        self.Design_Einstellung = None
        self.Suche_suche_3 = None
        
        self.zeit_string = time.strftime("%H:%M:%S")
        self.tag_string = str(time.strftime("%d %m %Y"))
        self.Tag_und_Liste = self.tag_string + " Dateien.txt"
        self.Jahr = str(time.strftime("%Y"))
        self.Liste_mit_datum = os.path.join(self.Listen_Speicherort_standard, self.Jahr, self.Monat, self.Tag_und_Liste) # Das ist der Ort wo dann immer alles gespeichert wird
        self.Monat_ordner_pfad = os.path.join(self.Listen_Speicherort_standard, self.Jahr, self.Monat) # Das ist der Ort welcher zum Programmstart erstellt wird falls er nicht bereits existieren sollte

    ################ Jetzt werden hier so Dinge geladen wie Einstellungen, oder es wird hier geguckt, ob alle benötigten Ordner Existieren ############
        
        try:
            p1 = Atk.PhotoImage(file = "CiM_icon.png")
            root.iconphoto(False, p1)
        except Exception as exci1:
            print(f"Fehlschlag beim setzen des Icons, versuche es nun erneut. Fehlercode: {exci1}")
            try:
                root.iconphoto(False, Atk.PhotoImage(file = self.icon_pfad))
            except Exception as err:
                err1 = "Es ist ein Fehler beim setzen des Icons aufgetreten. Fehlerlode: ", err
                messagebox.showinfo(message=err1)
                print("icon gibt heute nicht.")
        try:
            print(f"Ich lade nun die Theme Einstellungen...")
            with open(self.Einstellung_Theme, "r") as E_theme_gel:
                self.Einstellungen_Theme_Inhalt = E_theme_gel.read()
                if self.Einstellungen_Theme_Inhalt == "dunkel":
                    tk.set_default_color_theme("Designs/dunkel.json")
                elif self.Einstellungen_Theme_Inhalt == "hell":
                    tk.set_default_color_theme("Designs/hell.json")
                elif self.Design_Einstellung == "System":
                    print("Es wird versucht die System Design Einstellung zu laden.")
                    tk.set_appearance_mode("System")
                else:
                    print("Es gab einen Fehler bei der geladenen Designeinstellung, es wird nun der Systemstandard geladen...")
                    tk.set_appearance_mode("System")
                    print("Die System Design Einstellung wurde geladen.")
        except Exception as exko:
            print(f"Es ist ein Fehler beim Laden der Theme Einstellungen aufgetreten. Fehlercode: {exko}")
        try:
            if not os.path.exists(self.Db_Ordner_pfad):
                print("[-INFO-] Der Db Ordner scheint nicht zu existieren. Erstelle ihn nun.")
                os.mkdir(self.Db_Ordner_pfad)
                print("[-INFO-] Der Db Ordner wurde erfolgreich erstellt.")
        except Exception as ex_einst:
            print("[-ERR-] Fehler beim Erstellen des Db Ordners. Fehlercode:", ex_einst)

        print(self.tag_string)
        if not os.path.exists(self.Monat_ordner_pfad):
            try:
                os.makedirs(self.Monat_ordner_pfad)
                print("[-INFO-] Ordner ", {self.Monat_ordner_pfad}, "Erfolgreich erstellt.")
            except Exception as EX1_Monat_ordn:
                print(f"[-ERR-] Fehler beim erstellen der Ordner. Fehlercode: {EX1_Monat_ordn}")

        try:
            with open(self.Auto_speichern_Einstellungsdatei, "r") as einst_gel_autsp:
                self.Auto_speichern_Einstellungsdatei_var = einst_gel_autsp.read()
                print("[-EINSTELLUNGEN-] Einstellunsgdatei zum Autospeichern geladen. Dateipfad: ", self.Auto_speichern_Einstellungsdatei)
                if self.Auto_speichern_Einstellungsdatei_var == "1":
                    print("[-EINSTELLUNGEN-] Die Autospeichern Var welche aus den Einstellungen zum Programmstart geladen wurde ist: ", self.Auto_speichern_Einstellungsdatei_var)
                else:
                    print("[-EINSTELLUNGEN-] Die Autospeichern Var welche aus den Einstellungen zum Programmstart geladen wurde ist: ", self.Auto_speichern_Einstellungsdatei_var)
                    self.Auto_speichern_Einstellungsdatei_var = "0"
        except Exception as autpsp_err:
            messagebox.showerror(title="CiM Fehler", message="Konnte die Datei zum Autospeichern nicht finden, vielleicht gibt es sie auch einfach nicht.")
            print("[-EINSTELLUNGEN-] Fehler beim Laden des Autospeicherns. Funktion wurde deaktiviert. self.Auto_speichern_Einstellungsdatei = 0. Fehlercode: ", autpsp_err)
            self.Auto_speichern_Einstellungsdatei_var = "0"
                
                
        try:  # vehrindern das n bug geschieht
            os.remove("tmp.txt")
            os.remove("tmp1.txt")
            print("[-INFO-] fehlerhafte Dateien wurden bereinigt.")
        except FileNotFoundError:
            pass
        except Exception as Ex_tmp_bug:
            print(f"Es gibt einen Hinweis auf fehlende Schreibrechte im Programmverzeichnis. Fehlermeldung: {Ex_tmp_bug}")
            messagebox.showerror(title="CiM Fehler", message=f"Es scheint so als hätten Sie keine Schreibrechte im Programmverzeichnis, das sollre nur mit dem Starface Modul ein Problem werden. Fehlercode: {Ex_tmp_bug}") 
        
        
        try: 
            if not os.path.exists(self.Einstellungen_ordner):
                try:
                    print("Der Einstellungsordner scheint nicht zu existieren. Erstelle ihn nun.")
                    os.mkdir(self.Einstellungen_ordner)
                    print("Der Einstellungsornder wurde erfolgreich erstellt.")
                except Exception as ex_einst:
                    print("Fehler beim Erstellen des Einstellungsordners. Fehlercode:", ex_einst)
                    messagebox.showerror(title="CiM Fehler", message=ex_einst)
                    try:
                        with open(self.Starface_Einstellungsdatei, "r") as SternGesicht_data:
                            self.Starface_Modul = SternGesicht_data.read()
                            if self.Starface_Modul == "1":
                                print("Starface Modul wird aktiviert.")
                                self.thread_webserver.start()
                            else:
                                print("Das Starface Modul ist nicht aktiviert: self.Starface_Modul == ", self.Starface_Modul)
                    except Exception as Exp:
                        print("Konnte die Einstellungsdatei nicht öffnen. Fehlercode: ", Exp)
                        messagebox.showerror(title="CiM Fehler", message="Konnte die Einstellungsdatei nicht öffnen. Bitte in die Logs schauen.")
            else:
                try:
                    with open(self.Starface_Einstellungsdatei, "r") as SternGesicht_data:
                        self.Starface_Modul = SternGesicht_data.read()
                        if self.Starface_Modul == "1":
                            print("Starface Modul wird aktiviert.")
                            self.thread_webserver.start()
                        else:
                            print("Das Starface Modul ist nicht aktiviert: self.Starface_Modul == ", self.Starface_Modul)
                except Exception as Exp:
                    print("Konnte die Einstellungsdatei nicht öffnen. Fehlercode: ", Exp)
                    messagebox.showerror(title="CiM Fehler", message="Konnte die Einstellungsdatei nicht öffnen. Bitte in die Logs schauen.")

            
        except Exception as ex_stern2:
            print(f"Die Starface Moduleinstelllungen konten nicht überprüft werden. Fehlercode: {ex_stern2}")

        try:
            with open(self.Listen_Speicherort_Einstellungsdatei , "r") as Liste_Speicherort_data:
                self.Listen_Speicherort = json.load(Liste_Speicherort_data)
                self.Listen_Speicherort_geladen = (self.Listen_Speicherort["ListenDings_Speicherort"])
                #self.csv_datei_pfad = self.Listen_Speicherort_geladen
        except PermissionError:
                messagebox.showerror(title="Listendings Speicherort", message="Es Fehlt für diesen Ordner die nötige Berechtigung, Die Speicherorte konnten nicht geladen werden")
        except:
            messagebox.showerror(title="Listendings Speicherort", message="Die Einstellung scheint nicht zu existieren")

        try:
            with open(self.Listen_Speicherort_Netzwerk_Einstellungsdatei , "r") as Liste_Speicherort_Netzwerk_data:
                self.Listen_Speicherort_Netzwerk = json.load(Liste_Speicherort_Netzwerk_data)
                self.Listen_Speicherort_Netzwerk_geladen = (self.Listen_Speicherort_Netzwerk["ListenDings_Speicherort_Netzwerk"])
               # self.Listen_Speicherort_Netzwerk_geladen = os.path.join(self.Listen_Speicherort_Netzwerk_geladen, self.Jahr,self.Monat, self.tag_string + ".csv")
                self.Listen_Speicherort_Netzwerk_geladen_ordner = os.path.join(self.Listen_Speicherort_Netzwerk_geladen, self.Jahr, self.Monat)
        except PermissionError:
                messagebox.showerror(title="Listendings Speicherort", message="Es Fehlt für diesen Ordner die nötige Berechtigung, Der Gespeicherte Netzwerkpfad konnte nicht aufgerufen werden.")
        except Exception as e:
            print(f"Irgendwas ist passiert: {e}")

    ######### JETZT KOMMT HIER DIE SHAISE FÜR DAS EMAIL TICKET ZEUGS ###########
        try:
            with open(self.Einstellung_Email_Sender_Adresse, "r") as Email_S_Datei:
                self.sender_email = Email_S_Datei.read()
                print("[-EINSTLLUNGEN LADEN-] Sender Email geladen.")
            with open(self.Einstellung_Email_Empfänge_Adresse, "r") as Email_E_Datei:
                self.empfänger_email = Email_E_Datei.read()
                print("[-EINSTLLUNGEN LADEN-] Empfänger Adresse geladen.")
            with open(self.Einstellung_smtp_server, "r") as SMTP_Server_Datei:
                self.smtp_server = SMTP_Server_Datei.read()
                print("[-EINSTLLUNGEN LADEN-] SMTP Server Adresse geladen.")
            with open(self.Einstellung_smtp_Passwort, "r") as SMTP_Server_Passwort_Datei:
                self.pw_email= SMTP_Server_Passwort_Datei.read()
                print("[-EINSTLLUNGEN LADEN-] Absender Kennwort geladen.s")
        except Exception as EmailEx3_l:
            print(EmailEx3_l)
            self.sender_email = ""
            self.empfänger_email = ""
            self.smtp_server = ""
            self.pw_email = ""
            print(f"Beim Laden der Email Einstellungen unter {self.Einstellung_Email_Sender_Adresse} ; {self.Einstellung_Email_Empfänge_Adresse} und {self.Einstellung_smtp_server} ist ein Fehler aufgetreten. Fehlercode: {EmailEx3_l}")
    ########### SHAISE ENDE ###########
    ###################################

    #### Die Stars der Stunde ####
        self.kunde_entry = tk.CTkEntry(master,width=600, placeholder_text="Name des Anrufers", fg_color=self.Entry_Farbe, text_color="Black", placeholder_text_color="FloralWhite")
        self.t_nummer = tk.CTkEntry(master, width=600, placeholder_text="Telefonnummer", state="disabled", fg_color=self.Entry_Farbe, text_color="Black", placeholder_text_color="FloralWhite")
        self.problem_entry = tk.CTkEntry(master,width=1200, placeholder_text="Problem", fg_color=self.Entry_Farbe, text_color="Black", placeholder_text_color="FloralWhite")
        self.info_entry = tk.CTkEntry(master,width=1200, placeholder_text="Info", fg_color=self.Entry_Farbe, text_color="Black", placeholder_text_color="FloralWhite")
    #### ####
        

        self.senden_button = tk.CTkButton(master, text="Senden", command="")
        self.senden_button.bind('<Button-1>', self.senden)
        root.bind('<Return>', self.senden)
        self.alles_löschen_knopp = tk.CTkButton(master, text="Alle Eintrage löschen", command=self.alles_löschen)
        self.ausgabe_text = tk.CTkTextbox(master, width=1255, height=420, wrap="word", fg_color=self.Hintergrund_farbe_Text_Widget, text_color=self.Textfarbe, border_color=self.Border_Farbe, border_width=2)
        self.ausgabe_text.configure(state='disabled')
        self.kunde_entry.place(x=5,y=5)
        self.problem_entry.place(x=5,y=35)
        self.info_entry.place(x=5,y=65)
        self.t_nummer.place(x=605,y=5)
        self.ausgabe_text.place(x=0,y=100)

        
        self.menu = Menu(root)
        root.configure(menu=self.menu)
        self.menudings = Menu(self.menu, tearoff=0)
        self.Einstellungen = Menu(self.menu, tearoff=0)
        self.Speichern_Menu = Menu(self.menu, tearoff=0)
        self.Bearbeiten_Menu = Menu(self.menu, tearoff=0)
        self.Suchen_Menu = Menu(self.menu, tearoff=0)
        self.Menü = Menu(self.menu, tearoff=0)
        self.menu.add_cascade(label=self.Programm_Name  + " " + self.Version, menu=self.menudings)
        self.menu.add_cascade(label="Einstellungen", menu=self.Einstellungen)
        self.menu.add_cascade(label="Bearbeiten", menu=self.Bearbeiten_Menu)
        self.menu.add_cascade(label="Speichern", menu=self.Speichern_Menu)
        self.menu.add_cascade(label="Suchen", menu=self.Suchen_Menu)
        self.menudings.add_command(label="Info", command=self.info)
        self.menudings.add_command(label="Changelog", command=self.changelog_aufmachen)
        self.menudings.add_command(label="Admin rechte aktivieren", command=self.Admin_rechte)
        self.Einstellungen.add_command(label="Speicherort des ListenDings ändern...", command=self.ListenDings_speicherort_ändern)
        self.Speichern_Menu.add_command(label="als CSV Speichern", command=self.als_csv_speichern_eigener_ort)
        self.Speichern_Menu.add_command(label="als CSV Speichern unter...", command=self.als_csv_speichern)
        self.Speichern_Menu.add_command(label="als CSV Speichern auf Netzlaufwerk", command=self.Netzlaufwerk_speichern)
        self.Einstellungen.add_command(label="Netzlaufwerk einstellen...", command=self.ListenDings_speicherort_Netzwerk_ändern)
        self.Einstellungen.add_command(label="Beim SMTP Server anmelden...", command=self.SMTP_Anmeldung_Manuell)
        self.Einstellungen.add_command(label="Einen neuen Kontakt hinzufügen...", command=self.zeugs1)
        self.Bearbeiten_Menu.add_command(label="Blacklist erweitern...", command=self.zeugs1_blacklist)
        self.Bearbeiten_Menu.add_command(label="Bearbeiten Umschalten", command=self.beb_c)
        self.Bearbeiten_Menu.add_command(label="Alle Einträge löschen", command=self.alles_löschen)
        self.Bearbeiten_Menu.add_command(label="JSON Explorer öffnen", command=self.JSON_Explorer_öffnen)
        self.Suchen_Menu.add_command(label="Nach alten Einträgen suchen", command=self.Suche_alte_Einträge)
        self.Suchen_Menu.add_command(label="In der Kundenablage suchen...", command=self.Suche_KDabl)
        self.Suchen_Menu.add_command(label="Ergebnisse von gerade eben öffnen...", command=self.aufmachen_results)
        self.Suchen_Menu.add_command(label="Such Menü öffnen", command=self.such_menü_hauptmenu)
        self.Suchen_Menu.add_command(label="Sehr genaue Suche nutzen (Suche 3.0)(verbugt)", command=self.genaue_suche_start)
        
        try:
            print("(INFO) versuche die alten Aufzeichenungen zu Laden")
            self.ausgabe_text.configure(state='normal')
            with open(self.Liste_mit_datum, "r") as f:
                feedback_text = f.read()
                self.ausgabe_text.delete("1.0", tk.END)
                self.ausgabe_text.insert(tk.END, feedback_text)
                self.ausgabe_text.configure(state='disabled')
        except FileNotFoundError:
            print("(INFO) Die Datei Liste.txt gibts net")
            self.ausgabe_text.configure(state='disabled')
        except:
            messagebox.showinfo(title="Fehler", message="Ein Unbekannter Fehler ist aufgetreten beim Versuch während des Programmstarts die bisherigen aufzeichnungen zu laden, es könnte sein dass das Programm trotzdem fehlerfrei funktioniert.")
            self.ausgabe_text.configure(state='disabled')


    ############################ GUI INNIT ######################
    ############################ GUI INNIT ######################
    ############################ GUI INNIT ######################
        self.menu_frame = tk.CTkFrame(master, width=200, height=400)
        self.beb_knopp = tk.CTkButton(master, text="Bearbeiten", command=self.beb_c, fg_color="White", border_color="Black", border_width=1, text_color="Black", hover_color="DarkSlateGray1", image=self.Bearbeiten_Bild)
        self.beb_knopp.place(x=1260, y=100)
        self.Such_menu_haupt_frame = tk.CTkFrame(root, width=180, height=110, fg_color=self.Hintergrund_farbe, border_color=self.Border_Farbe, border_width=3, corner_radius=5)
        self.irgendwo_suchen = tk.CTkButton(master, text="durchsuchen...", command=self.such_menü_hauptmenu, fg_color="White", border_color="Black", border_width=1, text_color="Black", hover_color="pink", image=self.Durchsuchen_Bild_zu)
        self.irgendwo_suchen.place(x=1260, y=130)
        self.Menü_Knopp = tk.CTkButton(master, text="Menü", command=self.Menu_anzeige_wechseln, fg_color="White", border_color="Black", border_width=1, text_color="Black", hover_color="pink", image=self.Menü_Bild)
        self.Menü_Knopp.place(x=1260, y=160)


        
        self.Pause_menu = tk.CTkFrame(master, width=769, height=420, fg_color="LightSlateGray", border_color="White", border_width=1, corner_radius=1)
        

        self.Ereignislog = tk.CTkTextbox(root, width=220, height=80, wrap="word", text_color="Black", fg_color=self.Ereignislog_farbe, border_color=self.Border_Farbe, border_width=2)
        self.Ereignislog.place(x=1210,y=10)
        self.Ereignislog.insert(tk.END, "[-Ereignislog-]\n")

        


        # jetzt kommen die ganzen stat Sachen des Pause Menüs.
        # jetzt kommen die ganzen stat Sachen des Pause Menüs.
        # jetzt kommen die ganzen stat Sachen des Pause Menüs.
        # jetzt kommen die ganzen stat Sachen des Pause Menüs.
        # jetzt kommen die ganzen stat Sachen des Pause Menüs.
        # jetzt kommen die ganzen stat Sachen des Pause Menüs.

        
        

        self.gel_Email_Empfänger_L = tk.CTkLabel(self.Pause_menu, text="Ziel Email Adresse", text_color="White", bg_color=self.das_hübsche_grau, corner_radius=3)
        self.gel_Email_Sender_L = tk.CTkLabel(self.Pause_menu, text="Absende Email Adresse", text_color="White", bg_color=self.das_hübsche_grau, corner_radius=3)
        self.gel_Email_Absender_Passwort_L = tk.CTkLabel(self.Pause_menu, text="Absende Mail Kennwort", text_color="White", bg_color=self.das_hübsche_grau, corner_radius=3)
        self.gel_SMTP_Server_L = tk.CTkLabel(self.Pause_menu, text="SMTP Server", text_color="White", bg_color=self.das_hübsche_grau, corner_radius=3)

        self.gel_Email_Empfänger_E = tk.CTkEntry(self.Pause_menu, placeholder_text="Empfänger Adresse", width=300)
        self.gel_Email_Sender_E = tk.CTkEntry(self.Pause_menu, placeholder_text="Sender Email Adresse", width=300)
        self.gel_Email_Absender_Passwort_E = tk.CTkEntry(self.Pause_menu, placeholder_text="Passwort der Email Adresse", width=300, show="#")
        self.gel_SMTP_Server_E = tk.CTkEntry(self.Pause_menu, placeholder_text="IPv4 oder Namen des SMTP Eintragen", width=300)

        self.Mail_Einstellungen_speichern = tk.CTkButton(self.Pause_menu, text="Email Einstellungen speichern", command=self.Email_Einstellungen_speichern, fg_color="White", border_color="Black", border_width=1, text_color="Black", hover_color="DarkSlateGray1")
        self.smtp_login_erfolgreich_l = tk.CTkLabel(self.Pause_menu, text="Anmeldestatus")

        self.SMTP_Server_erneut_anmelden = tk.CTkButton(self.Pause_menu, text="erneut mit SMTP Server verbinden", command=self.SMTP_Anmeldung_Manuell, fg_color="White", border_color="Black", border_width=1, text_color="Black", hover_color="pink")

        self.Suche_knopp = tk.CTkButton(self.Pause_menu, text="Nach alten Eintrag Suchen...", command=self.Suche_alte_Einträge, fg_color="White", border_color="Black", border_width=1, text_color="Black", hover_color="pink")
        
        
        self.Zhe_Clock = tk.CTkLabel(self.Pause_menu, text=self.Zeit)
        self.Zhe_Clock.place(x=10,y=10)

        def auswahl_gedingst(choice):
            if choice == "An Chefe gegeben":
                self.Weiterleitung_an = "An el Chefe weitergeleitet."
            elif choice == "An Christian gegeben":
                self.Weiterleitung_an = "An Christian Melges weitergeleitet."
            elif choice == "An Mike gegeben":
                self.Weiterleitung_an = "An Mike Bosse weitergeleitet."
            elif choice == "An Frau Tarnath gegeben":
                self.Weiterleitung_an = "An Frau Tarnath weitergeleitet"
            elif choice == "Keine Weiterleitung":
                self.Weiterleitung_an = ""

        def auswahl_gedingst_sprechen(choice):
            if choice == "Mit Chefe sprechen":
                self.wollte_sprechen = "Mit el Chefe sprechen"
            elif choice == "Mit Christian sprechen":
                self.wollte_sprechen = "Mit Christian sprechen"
            elif choice == "Mit Mike sprechen":
                self.wollte_sprechen = "Mit Mike sprechen"
            elif choice == "Mit Frau Tarnath sprechen":
                self.wollte_sprechen = "Mit Frau Tarnath sprechen"
            elif choice == "Mit Irgendwen sprechen":
                self.wollte_sprechen = "Mit Irgendwen sprechen"
            elif choice == "Keine Weiterleitung":
                self.wollte_sprechen = "-"

        def auswahl_design_gedingst(choice):
            if choice == "hell":
                self.Design_Einstellung = "hell"
            elif choice == "dunkel":
                self.Design_Einstellung = "dunkel"
            elif choice == "System":
                self.Design_Einstellung = "System"
            else:
                print("[-ERR-] Fehler bei der Auswahl der Designeinstellung, nutze nun den Systemstandard.")
                self.Design_Einstellung = "System"
        

        self.optionmenu1 = tk.CTkOptionMenu(root, values=["Mit Chefe sprechen", "Mit Christian sprechen", "Mit Mike sprechen", "Mit Frau Tarnath sprechen", "Irgendwen sprechen", "Keine Anfrage"], command=auswahl_gedingst_sprechen, fg_color="White", text_color="Black", dropdown_hover_color="pink")
        self.optionmenu1.set("Mit Wem sprechen?")
        self.optionmenu1.place(x=1260,y=190)
        self.optionmenu = tk.CTkOptionMenu(root, values=["An Chefe gegeben", "An Christian gegeben", "An Mike gegeben", "An Frau Tarnath gegeben","Keine Weiterleitung"], command=auswahl_gedingst, fg_color="White", text_color="Black", dropdown_hover_color="pink")
        self.optionmenu.set("Keine Weiterleitung")
        self.optionmenu.place(x=1260,y=220)

        self.Einstellung_Design_auswahl = tk.CTkOptionMenu(self.Pause_menu, values=["hell", "dunkel", "System"], command=auswahl_design_gedingst)
        self.Einstellung_Design_L = tk.CTkLabel(self.Pause_menu, text="Design Einstellung:")
        


        self.kalender_menü = tk.CTkFrame(master, width=1250, height=520, fg_color="White", border_color="Black", border_width=2)
        self.Liste_mit_zeugs =  tk.CTkScrollableFrame(self.kalender_menü, width=500, height=420, bg_color="Green")
        self.Aufgabe_hinzufügen_Knopp = tk.CTkButton(self.kalender_menü, text="Eintrag Hinzufügen", command=self.Aufgabe_hinzufügen)


        ################################ MENU FRAMES ENDE ################################
        ################################ MENU FRAMES ENDE ################################
        ################################ MENU FRAMES ENDE ################################
        ################################ MENU FRAMES ENDE ################################

        self.kalender_menü_Knopp = tk.CTkButton(master, text="Kalender öffnen", command=self.Kalender_anzeigen, fg_color="White", border_color="Black", border_width=1, text_color="Black", hover_color="pink", image=self.Kalender_Bild)
        self.kalender_menü_Knopp.place(x=1260,y=480)
        self.Einstellungsseite_Knopp = tk.CTkButton(root, text="Einstellungen", command=self.Einstellungen_öffnen, fg_color="white", border_color="Black", border_width=1, text_color="Black", hover_color="DarkSlateGray1", image=self.Dings_Bild)
        self.Einstellungsseite_Knopp.place(x=1260,y=420)
        self.Ticket_erstellen_Knopp = tk.CTkButton(root, text="Ticket erstellen", command=self.Ticket_erstellen, fg_color="White", border_color="Black", border_width=1, text_color="Black", hover_color="pink", image=self.Ticket_Bild)
        self.Ticket_erstellen_Knopp.place(x=1260,y=450)
        self.Eintrag_raus_kopieren_knopp = tk.CTkButton(root, text="Letztes kopieren", command=self.Eintrag_raus_kopieren, fg_color="White", border_color="Black", border_width=1, text_color="Black", hover_color="pink", image=self.Kopieren_Bild)
        self.Eintrag_raus_kopieren_knopp.place(x=1260,y=390)
        self.Notizen_knopp = tk.CTkButton(root, text="Schnellnotiz", command=self.schnellnotizen_öffnen, fg_color="White", border_color="Black", border_width=1, text_color="Black", hover_color="DarkSlateGray1", image=self.Schnellnotiz_Bild)
        self.Notizen_knopp.place(x=1260,y=360)

        

        
    ####### ======================== init ende ======================== #######
    ####### ======================== init ende ======================== #######
    ####### ======================== init ende ======================== #######
    ####### ======================== init ende ======================== #######
    ####### ======================== init ende ======================== #######

    def changelog_aufmachen(self):
        print("changelog_aufmachen(def)")
        self.changelog_Fenster = tk.CTkToplevel(root)
        self.changelog_Fenster.title("Changelogs")
        self.changelog_Fenster.configure(fg_color="White")
        self.Textfeld_changelog = tk.CTkTextbox(self.changelog_Fenster, width=820, height=420, text_color="Black", fg_color="azure", wrap="word", border_width=0)
        height = 420
        width = 820
        try:
            x = root.winfo_x() + root.winfo_width()//2 - self.changelog_Fenster.winfo_width()//2
            y = root.winfo_y() + root.winfo_height()//2 - self.changelog_Fenster.winfo_height()//2
            self.changelog_Fenster.geometry(f"{width}x{height}+{x}+{y}")
        except:
            print("Konnte das changelogfenster nicht zentrieren.")
            self.changelog_Fenster.geometry(f"{width}x{height}+{x}+{y}")
        self.changelog_Fenster.resizable(False,False)
        self.Textfeld_changelog.pack()
        try:
            with open("changelog.txt", "r") as chlg:
                changelog_text = chlg.read()
                if changelog_text == "":
                    raise Listendings.ChangelogLeer("Dings is leer.")
                self.Textfeld_changelog.insert(tk.END, changelog_text)
                self.Textfeld_changelog.configure(state="disabled")
                changelog_text = None
                chlg = None
        except FileNotFoundError:
            self.Textfeld_changelog.insert(tk.END,"- Changelog ist existiert nicht oder konnte nicht gefunden werden -")
            self.Textfeld_changelog.configure(state="disabled")
            changelog_text = None
            chlg = None
        except Listendings.ChangelogLeer as chlg_leer:
            self.Textfeld_changelog.insert(tk.END,f"- {chlg_leer} -")
            self.Textfeld_changelog.configure(state="disabled")
            changelog_text = None
            chlg = None
        except Exception as chlg_ex:
            self.Textfeld_changelog.insert(tk.END,f"- Beim öffnen des Changelogs ist ein Fehler aufgetreten: {chlg_ex} -")
            self.Textfeld_changelog.configure(state="disabled")
            changelog_text = None
            chlg = None

    def schnellnotizen_öffnen(self):
        print("schnellnotizen_öffnen(def)")
        self.schnellnotizen_Fenster = tk.CTkToplevel(root)
        self.schnellnotizen_Fenster.title("Schnellnotiz (wird NICHT gespeichert)")
        self.schnellnotizen_Fenster.configure(fg_color="White")
        self.Textfeld_Schnellnotizen = tk.CTkTextbox(self.schnellnotizen_Fenster, width=420, height=420, text_color="Black", fg_color="azure", wrap="word", border_color="Black", border_width=2)
        height = 420
        width = 420
        try:
            x = root.winfo_x() + root.winfo_width()//2 - self.schnellnotizen_Fenster.winfo_width()//2
            y = root.winfo_y() + root.winfo_height()//2 - self.schnellnotizen_Fenster.winfo_height()//2
            self.schnellnotizen_Fenster.geometry(f"{width}x{height}+{x}+{y}")
        except:
            print("Konnte das Schnellnotizfenster nicht zentrieren.")
            self.schnellnotizen_Fenster.geometry(f"{width}x{height}+{x}+{y}")
        self.schnellnotizen_Fenster.resizable(False,False)
        self.Textfeld_Schnellnotizen.pack()
    
    def JSON_Explorer_öffnen(self):
        print("[-INFO-] öffne nun den JSON Explorer...")
        try:
            exec(open('json_explorer.py').read())
        except Exception as JSON_E:
            messagebox.showerror(title="CiM Fehler", message=f"Konnte die Datei json_explorer.py nicht finden, stelle sicher, dass sie sich im Programmverzeichnis befindet! Fehlercode: {JSON_E}")

    def Einstellungen_öffnen(self):
        print("Einstellungen_öffnen (def)")
        self.Einstellungsseite_Knopp.configure(command=self.Einstellungen_schließen, text="Einstellungen schließen", fg_color=self.aktiviert_farbe, hover_color="Pink")
        self.Einstellungen_Frame = tk.CTkFrame(root, width=600, height=380, border_color="Pink", border_width=3, fg_color="transparent")
        self.tabview = tk.CTkTabview(self.Einstellungen_Frame, width=600, height=380, fg_color=self.Entry_Farbe, segmented_button_fg_color=self.Hintergrund_farbe_Text_Widget, segmented_button_selected_hover_color=self.dunkle_ui_farbe, segmented_button_unselected_hover_color=self.dunkle_ui_farbe, segmented_button_selected_color=self.helle_ui_farbe, text_color="Black", segmented_button_unselected_color=self.ja_ui_fabe)
        self.tabview.add("Starface Modul")
        self.tabview.add("Adressbuch")
        self.tabview.add("Speichern")
        self.tabview.add("SMTP")
        self.tabview.add("Speicherorte")
        self.Einstellungen_Frame.place(x=400,y=120)
        self.Auto_speichern_ändern_knopp = tk.CTkButton(self.tabview.tab("Speichern"), text="Auto Speichern umschalten", command=self.autospeichern_ä_c, hover_color="pink")
        self.tabview.place(x=0, y=0)
        self.Starface_Modul_Einstellung_Knopp = tk.CTkButton(self.tabview.tab("Starface Modul"), text="Starface Modul umschalten", command=self.Starface_Modul_umschalten, hover_color="pink")
        self.Starface_Modul_Einstellung_Knopp.pack()
        if self.Starface_Modul == "1":
            self.Starface_Modul_Einstellung_Knopp.configure(text="Staface Modul ist aktiviert.", fg_color="aquamarine", text_color="Black")
        else:
            self.Starface_Modul_Einstellung_Knopp.configure(text="Staface Modul ist deaktiviert.", fg_color="chocolate1", text_color="White")
        if self.Auto_speichern_Einstellungsdatei_var == "1":
            self.Auto_speichern_ändern_knopp.configure(text="Autospeichern aktiviert.",fg_color="aquamarine", text_color="Black")
        else:
            self.Auto_speichern_ändern_knopp.configure(text="Autospeichern deaktiviert.", fg_color="chocolate1", text_color="White")  # den shais hier kann man so safe beser machen aber egal, vllt irgendwann mal
        self.Listen_Speicherort_geladen_anders_Entry = tk.CTkEntry(self.tabview.tab("Speicherorte"), width=300)
        self.Listen_Speicherort_Netzwerk_geladen_anders_Entry = tk.CTkEntry(self.tabview.tab("Speicherorte"), width=300)
        self.Netzlaufwerk_pfad_geladen_Label = tk.CTkLabel(self.tabview.tab("Speicherorte"), text=self.Listen_Speicherort_Netzwerk_geladen_anders, text_color="Black", bg_color=self.Entry_Farbe, corner_radius=3)
        self.Pfad_geladen_Label = tk.CTkLabel(self.tabview.tab("Speicherorte"), text=self.Listen_Speicherort_geladen_anders, text_color="Black", bg_color=self.Entry_Farbe, corner_radius=3)
        self.Netzlaufwerk_pfad_geladen_Label.place(x=10,y=80)
        self.Pfad_geladen_Label.place(x=10,y=110)
        self.Listen_Speicherort_geladen_anders_Entry.place(x=160, y=110)
        self.Listen_Speicherort_Netzwerk_geladen_anders_Entry.place(x=160,y=80)
        try:
            self.Listen_Speicherort_geladen_anders_Entry.delete(0, tk.END)
            self.Listen_Speicherort_Netzwerk_geladen_anders_Entry.delete(0, tk.END)
        except:
            print("Konnte den Inhalt der Entrys für die Pfade nicht löschen")
        try:
            self.Listen_Speicherort_geladen_anders_Entry.insert(0, self.Listen_Speicherort_geladen)
            self.Listen_Speicherort_Netzwerk_geladen_anders_Entry.insert(0, self.Listen_Speicherort_Netzwerk_geladen)
        except:
            print("Konnte die geladenen Speicherorte nicht in die Entrys übernehmen.")
        def rückruf_speichern():
            print("self.mitspeichern.get() = :", self.mitspeichern.get())
            self.Kontakt_soll_gleich_mitgespeichert_werden = True

        self.mitspeichern = tk.StringVar(value="on")
        try:
            self.abhgehakt_hinzufügen_box.place_forget()
        except:
            pass
        self.abhgehakt_hinzufügen_box = tk.CTkCheckBox(self.tabview.tab("Speichern"), text_color="Black",text="Namen und Telefonnummer in KtDb speichern?", command=rückruf_speichern, variable=self.mitspeichern, onvalue="on", offvalue="off")
        self.abhgehakt_hinzufügen_box.place(x=20,y=20)
        self.Auto_speichern_ändern_knopp.place(x=20,y=60)

    def Einstellungen_schließen(self):
        print("Einstellungen_schließen(def)")
        self.Einstellungsseite_Knopp.configure(command=self.Einstellungen_öffnen, text="Einstellungen", fg_color=self.deaktiviert_farbe, hover_color="Pink")
        self.Einstellungen_Frame.place_forget()
        self.tabview.place_forget()

    def Eintrag_raus_kopieren(self):
        print("Eintrag_raus_kopieren(def)")
        self.geladener_Text = self.ausgabe_text.get("0.0", "end")
        self.einzelner_Eintrag = self.geladener_Text.split("\n\n")
        print(f"Aufgteilter Text: {self.einzelner_Eintrag}")

    def Ticket_erstellen_mail(self): # naja das halt dann mit dem Mail.to Befehl.
        print("Ticket_erstellen (Email)")
        self.alternative_empfänger_adresse = ""
        self.Betreff_Mail = self.Betreff_Ticket_e.get()
        self.alternative_empfänger_adresse = self.alternative_empfänger_adresse_e.get()
        self.Nachricht_Mail_Inhalt = self.Nachricht_Ticket_e.get("0.0", "end")

        msg = MIMEMultipart()
        msg["From"] = self.sender_email
        if self.alternative_empfänger_adresse == "":
            msg["To"] = self.empfänger_email
            print(self.empfänger_email)
            print(self.alternative_empfänger_adresse)
            print("[-TICKET ERSTELLEN-] Ticket wird an die hinterlegte Emailadresse versendet...")
            self.Ereignislog.insert(tk.END, "-[-TICKET ERSTELLEN-] Ticket wird an die hinterlegte Emailadresse versendet...-\n")
        elif self.alternative_empfänger_adresse != "":
            msg["To"] = self.alternative_empfänger_adresse
            print(self.alternative_empfänger_adresse)
            print(self.empfänger_email)
            print("[-TICKET ERSTELLEN-] Ticket wird an alternative Emailadresse versendet...")
        msg["Subject"] = self.Betreff_Mail
        msg.attach(MIMEText(self.Nachricht_Mail_Inhalt, "plain"))

        with smtplib.SMTP_SSL(self.smtp_server, 465) as server:
            try:
                server.login(self.sender_email, self.pw_email)
                self.smtp_login_erfolgreich = True
            except Exception as EmailEx1:
                print("Fehler beim anmelde beim Mailserver. Fehlercode: ", EmailEx1)
                self.smtp_login_erfolgreich = False
                try:
                    self.smtp_login_erfolgreich_l.configure(text="Anmeldung am SMTP fehlgeschlagen.", text_color="Red")
                    self.Ereignislog.insert(tk.END, "-Anmeldung am SMTP fehlgeschlagen.-\n")
                except:
                    pass
                messagebox.showerror(title="CiM Fehler", message=f"Es gab einen Fehler beim Anmelden am Mailserver. Fehlercode: {self.smtp_server}")
            if self.alternative_empfänger_adresse == "":
                try:
                    server.sendmail(self.sender_email, self.empfänger_email, msg.as_string())
                    self.Ereignislog.insert(tk.END, "-Email an SMTP Server versendet.-\n")
                except Exception as EmailEx2:
                    print("Fehler beim anmelden beim senden an den Mailserver. Fehlercode: ", EmailEx2)
                    self.Ereignislog.insert(tk.END, "-Anmeldung am SMTP fehlgeschlagen.-\n")
                    messagebox.showerror(title="CiM Fehler", message=f"Es gab einen Fehler beim senden der Nachricht an den Mailserver. Fehlercode: {EmailEx2}")
                self.Ticket_Fenster.destroy()
                messagebox.showinfo(title="CiM", message="Das Ticket wurde erfolgreich erstellt.")
                print("E-Mail erfolgreich gesendet!")
            


    def Ticket_erstellen_api(self): # Ich denke nicht, dass ich das hier so schnell hinbekommen werde, da das Ding immer wieder nen fehler schmeißt den ich nicht mal verstehe haha.
        print("Ticket_erstellen_api")
        messagebox.showerror(title="Fehler", message="Dieses Feature existiert noch nicht, wie hast Du überhaupt geschafft diese Funktion aufzurufen!?!???")

    def genaue_suche_start(self):
        self.thread_suche_3 = threading.Thread(target=self.genaue_suche)
        self.thread_suche_3.start()

    

    def Ticket_erstellen(self): # Die erste frage, ob es per Mail oder API erstellt werden soll.
        print("Ticket_erstellen(def)")
        self.Ticket_Fenster = tk.CTkToplevel()
        self.Ticket_Fenster.title(self.Programm_Name + " " + "                          Ein Ticket erstellen                          ")
        self.Ticket_Fenster.configure(resizeable=False)
        try:
            height = 520
            width = 680
            fenster_breite = root.winfo_screenwidth()
            fenster_höhe = root.winfo_screenheight()
            x = (fenster_breite - width) // 2
            y = (fenster_höhe - height) // 2
            self.Ticket_Fenster.geometry(f"{width}x{height}+{x}+{y}")
        except:
            pass
        #self.Ticket_Fenster.geometry("680x520")
        self.Betreff_Ticket_e = tk.CTkEntry(self.Ticket_Fenster, width=300, placeholder_text="Betreffzeile")
        self.Nachricht_Ticket_e = tk.CTkTextbox(self.Ticket_Fenster, width=300, height=420, wrap="word")
        self.Ticket_abschicken_mail = tk.CTkButton(self.Ticket_Fenster, text="Ticket erstellen und versenden", command=self.Ticket_erstellen_mail)
        self.alternative_empfänger_adresse_e = tk.CTkEntry(self.Ticket_Fenster, placeholder_text="Alternative Empfänger", width=300)
        self.alternative_empfänger_adresse_e.place(x=330,y=120)
        self.Ticket_abschicken_mail.place(x=330,y=50)
        self.Betreff_Ticket_e.place(x=10,y=50)
        self.Nachricht_Ticket_e.place(x=10,y=80)

    def Email_Einstellungen_speichern(self):
        print("Email_Einstellungen_speichern (def)")
        try:
            if self.gel_Email_Sender_E.get() and self.gel_SMTP_Server_E.get() and self.gel_Email_Empfänger_E.get() and self.gel_Email_Absender_Passwort_E.get():
                with open(self.Einstellung_Email_Sender_Adresse, "w+") as Email_S_Datei_s:
                    Email_S_Datei_s.write(self.gel_Email_Sender_E.get())
                with open(self.Einstellung_Email_Empfänge_Adresse, "w+") as Email_E_Datei_s:
                    Email_E_Datei_s.write(self.gel_Email_Empfänger_E.get())
                with open(self.Einstellung_smtp_server, "w+") as SMTP_Server_Datei_s:
                    SMTP_Server_Datei_s.write(self.gel_SMTP_Server_E.get())
                with open(self.Einstellung_smtp_Passwort, "w+") as SMTP_Server_Passwort_Datei_s:
                    SMTP_Server_Passwort_Datei_s.write(self.gel_Email_Absender_Passwort_E.get())
                messagebox.showinfo(title="CiM", message="Die Einstellungen wurden erfolgreich gespeichert und werden beim nächsten Start oder durch erneutes verbinden aktiv.")
            else:
                messagebox.showinfo(title="CiM", message="Bitte geben Sie BEVOR Sie speichern, zuerst in ALLEN Feldern etwas ein.")

        except Exception as EmailEx3_l:
            print("Beim versuch die Email Daten zu speichern ist ein Fehler aufgetreten. Fehlercode: ", EmailEx3_l)
            messagebox.showerror(title="CiM Fehler", message=f"Beim speichern der Email Einstellungen unter {self.Einstellung_Email_Sender_Adresse} ; {self.Einstellung_Email_Empfänge_Adresse} und {self.Einstellung_smtp_server} ist ein Fehler aufgetreten. Fehlercode: {EmailEx3_l}")
        
    def Kalender_anzeigen(self):
        if self.Kalender_offen == True:
            print("Kalender ist bereits geöffnet, ich ignoriere diese Anfrage einfach.")
        elif self.Kalender_offen == False:
            print("kalender_anzeigen(def)")
            self.kalender_menü.place(x=0,y=0)
            self.Liste_mit_zeugs.place(x=100,y=50)
            self.kalender_menü_Knopp.configure(text="Kalender schließen", command=self.Kalender_anzeigen_weg, fg_color="White", border_color="Black", border_width=1, text_color="Black", hover_color="pink")
            self.Aufgabe_hinzufügen_Knopp = tk.CTkButton(self.kalender_menü, text="Eintrag Hinzufügen", command=self.Aufgabe_hinzufügen)
            self.Aufgabe_hinzufügen_Knopp.place(x=620,y=50)

            try:
                print("Lade nun die alten Aufgaben...")
                with open("tasks.json", "r") as f:
                    self.tasks = json.load(f)
                    print("Daten der alten Aufgaben erfolgreich geladen..")
                    self.D1 = tk.CTkToplevel(root)
                    self.D1.protocol("WM_DELETE_WINDOW", self.D1_schließen)
                    self.D1.configure(title="Aufgabenliste")
                    self.Kalender_offen = True
                    
                    for task in self.tasks:
                        self.check_var = tk.StringVar(value="aus")
                        ##self.checkbox = tk.CTkCheckBox(self.D1, text=task, command=self.checkbox_event,variable=self.check_var, onvalue="an", offvalue="aus")
                        self.checkbox = tk.CTkCheckBox(self.D1, text=task, command=self.checkbox_event,variable=self.check_var, onvalue="an", offvalue="aus")
                        self.checkbox.place(x=10,y=self.zeile_zahl)
                        print("Aufgabe platziert...")
                        self.zeile_zahl +=30
                print("Alle Aufgaben wurden platziert.")
            except FileNotFoundError:
                print("File not found beim laden der Aufgaben aufgetrenen. Versuche fortzufahren...")
                pass
        
    def save_tasks(self):
        with open("Aufgaben.json", "w") as f:
            json.dump(self.tasks, f)
    
    def D1_schließen(self):
        print("D1_schließen(def)")
        self.D1.destroy()
        self.zeile_zahl = 0
        self.Kalender_offen = False
        self.checkbox = None
    
    def SMTP_Anmeldung_Manuell(self):
        print("[-SMTP Anmeldung-] Führe nun eine Manuelle Anmeldung beim SMTP Server durch...")
        print("[-SMTP Anmeldung-] Ich lade nun zu allerst die Einstellungen neu...")
        try:
            with open(self.Einstellung_Email_Sender_Adresse, "r") as Email_S_Datei:
                self.sender_email = Email_S_Datei.read()
                print("[-EINSTLLUNGEN LADEN-] Sender Email geladen.")
            with open(self.Einstellung_Email_Empfänge_Adresse, "r") as Email_E_Datei:
                self.empfänger_email = Email_E_Datei.read()
                print("[-EINSTLLUNGEN LADEN-] Empfänger Adresse geladen.")
            with open(self.Einstellung_smtp_server, "r") as SMTP_Server_Datei:
                self.smtp_server = SMTP_Server_Datei.read()
                print("[-EINSTLLUNGEN LADEN-] SMTP Server Adresse geladen.")
            with open(self.Einstellung_smtp_Passwort, "r") as SMTP_Server_Passwort_Datei:
                self.pw_email= SMTP_Server_Passwort_Datei.read()
                print("[-EINSTLLUNGEN LADEN-] Absender Kennwort geladen.s")
        except Exception as EmailEx3_l:
            print(EmailEx3_l)
            self.sender_email = ""
            self.empfänger_email = ""
            self.smtp_server = ""
            self.pw_email = ""
            messagebox.showerror(title="CiM Fehler", message=f"Beim Laden der Email Einstellungen unter {self.Einstellung_Email_Sender_Adresse} ; {self.Einstellung_Email_Empfänge_Adresse} und {self.Einstellung_smtp_server} ist ein Fehler aufgetreten. Fehlercode: {EmailEx3_l}")
        messagebox.showinfo(title="CiM SMTP Anmeldung", message="Es wird nun eine Manuelle SMTP Server Verbindung durchgeführt, das sollte nicht länger als ein paar Sekunden dauern.")
        self.smtp_login_erfolgreich_l.configure(text="Anmeldung erfolgt...", text_color="Grey42")
        self.SMTP_Anmeldung()

    def SMTP_Anmeldung(self):
        print("[-SMTP ANMELDUNG-] Melde mich nun am SMTP Server an...")
        with smtplib.SMTP_SSL(self.smtp_server, 465) as server:
            try:
                server.login(self.sender_email, self.pw_email)
                print("[-SMTP ANMELDUNG-] Anmeldung beim SMTP Server erfolgreich.")
                self.smtp_login_erfolgreich = True
                try:
                    self.smtp_login_erfolgreich_l.configure(text="Anmeldung am SMTP Server war erfolgreich.", text_color="SeaGreen1")
                except:
                    pass
            except Exception as EmailEx1:
                print("[-SMTP ANMELDUNG-] Fehler beim anmelden beim Mailserver. Fehlercode: ", EmailEx1)
                self.smtp_login_erfolgreich = False
                try:
                    self.smtp_login_erfolgreich_l.configure(text="Anmeldung am SMTP fehlgeschlagen.", text_color="Red")
                except:
                    pass
                messagebox.showerror(title="CiM Fehler", message=f"Es gab einen Fehler beim Anmelden am Mailserver. Fehlercode: {EmailEx1}")

    def Aufgabe_hinzufügen(self):
        text_des_dings = tk.CTkInputDialog(text="Gib eine neue Aufgabe ein:")
        Aufgabe = self.Zeit + "  --  " + text_des_dings.get_input() 
        if Aufgabe:
            try:
                task = Aufgabe
                if task:
                    self.tasks.append(task)
                    #self.task_menu.add_checkbutton(label=task, onvalue=True, offvalue=False)
                    #self.save_tasks()
                    self.check_var = tk.StringVar(value="Numero Uno")
                    self.checkbox = tk.CTkCheckBox(self.Liste_mit_zeugs, text=task, command=self.checkbox_event,variable=self.check_var, onvalue="an", offvalue="aus")
                    self.checkbox.place(x=10,y=self.zeile_zahl)
                    self.zeile_zahl +=30
                    with open("tasks.json", "w") as f: # Speichern der gerade eben hinzugefügten Aufgabe
                        json.dump(self.tasks, f)
            except Exception as Excio:
                print("Fehler beim hinzufügen der Aufgabe Fehlercode: ",Excio)
            try:
                with open(self.index_liste_pfad_Einstellungsdatei, "w+") as Datei_offn:
                    Datei_offn.write(self.zeile_zahl)
                    print("Index Datei geschrieben. geschriebener Wert: ", self.zeile_zahl)
            except Exception as edx:
                print("Fehler aber Programm läuft weiter: ",edx)
        else:
            print("pass")
            pass
            
    def checkbox_event(self):  # löschen der Aufgabe
        print("die self.checkbox hat gerade den folgenden Wert #W3#: ", self.check_var.get())
        #if self.check_var.get() == "an":
        self.checkbox.place_forget()

    def callback_fertsch_var(self, fertsch_var):
        try:
            index = self.fertsch_vars.index(fertsch_var)
            print("Index beim löschen lautet: ", index)
            del self.fertsch_vars[index]
            chkbx = self.Liste_mit_zeugs.grid_slaves(row=index+1, column=0)[0]
            self.zachen -= 1
            chkbx.destroy()  # Zerstöre die Checkbox
        except Exception as exc1:
            print("Fehler: ", exc1)

    def Kalender_anzeigen_weg(self):
        print("Kalender_anzeigen_weg")
        self.D1.destroy()
        self.kalender_menü.place_forget()
        self.Liste_mit_zeugs.place_forget()
        self.Aufgabe_hinzufügen_Knopp.place_forget()
        self.kalender_menü_Knopp.configure(text="Kalender öffnen", command=self.Kalender_anzeigen, fg_color="White", border_color="Black", border_width=1, text_color="Black", hover_color="pink", image=self.Kalender_Bild)
        
    def Starface_Modul_umschalten(self):
        print("Starface_Modul_umschalten(def)")
        try:
            if not os.path.exists(self.Einstellungen_ordner):
                try:
                    print("Der Einstellungsordner scheint nicht zu existieren. Erstelle ihn nun.")
                    os.mkdir(self.Einstellungen_ordner)
                    print("Der Einstellungsornder wurde erfolgreich erstellt.")
                except Exception as ex_einst:
                    print("Fehler beim Erstellen des Einstellungsordners. Fehlercode:", ex_einst)
                    messagebox.showerror(title="CiM Fehler", message=ex_einst)
            elif os.path.exists(self.Starface_Einstellungsdatei):
                try:
                    with open(self.Starface_Einstellungsdatei, "r") as SternGesicht_data:
                        self.Starface_Modul = SternGesicht_data.read()
                        if self.Starface_Modul == "1":
                            print("Starface Modul wird deaktiviert.")
                            try:
                                with open(self.Starface_Einstellungsdatei, "w+") as SternGesicht_data_neu:
                                    SternGesicht_data_neu.write("0")
                                self.Starface_Modul_Einstellung_Knopp.configure(text="Staface Modul ist deaktiviert", fg_color="chocolate1", text_color="White")
                                messagebox.showinfo(title="CiM Einstellungen", message="Das Starface Modul wird nun nach dem Neustart des Programms deaktiviert.")
                            except Exception as Ex_schr_stern:
                                print(Ex_schr_stern)
                                messagebox.showerror(title="CiM Fehler", message="Die Einstellungsdatei konnte nicht beschrieben werden.")
                        elif self.Starface_Modul == "0":
                            print("Starface Modul wird aktiviert.")
                            try:
                                with open(self.Starface_Einstellungsdatei, "w+") as SternGesicht_data_neu:
                                    SternGesicht_data_neu.write("1")
                                self.Starface_Modul_Einstellung_Knopp.configure(text="Staface Modul ist aktiviert", fg_color="aquamarine", text_color="Black")
                                messagebox.showinfo(title="CiM Einstellungen", message="Das Starface Modul wird nun nach dem Neustart des Programms aktiviert, bitte schauen Sie, für die korrekte Einrichtung in die Dokumentation.")
                            except Exception as Ex_schr_stern:
                                print(Ex_schr_stern)
                                messagebox.showerror(title="CiM Fehler", message="Die Einstellungsdatei konnte nicht beschrieben werden.")
                        else:
                            print("Das Starface Modul ist nicht aktiviert: self.Starface_Modul == ", self.Starface_Modul)
                except Exception as Exp:
                    print("Konnte die Einstellungsdatei nicht öffnen. Fehlercode: ", Exp)
                    messagebox.showerror(title="CiM Fehler", message="Konnte die Einstellungsdatei nicht öffnen. Bitte in die Logs schauen.")
            else:
                try:
                    with open(self.Starface_Einstellungsdatei, "w+") as SternGesicht_data_neu:
                        SternGesicht_data_neu.write("1")
                        self.Starface_Modul_Einstellung_Knopp.configure(text="Staface Modul ist aktiviert", fg_color="aquamarine", text_color="Black")
                    messagebox.showinfo(title="CiM Einstellungen", message="Das Starface Modul wird nun nach dem Neustart des Programms aktiviert.")
                except Exception as Ex_schr_stern:
                    print(Ex_schr_stern)
                    messagebox.showerror(title="CiM Fehler", message="Die Einstellungsdatei konnte nicht beschrieben werden.")
        except Exception as ex_stern:
            print("Die Starface Moduleinstelllungen konten nicht überprüft werden. Fehlercode: ", ex_stern)

    def autospeichern_ä_c(self):
        print("autospeichern_ä_c")
        if self.Auto_speichern_Einstellungsdatei_var == "1":
            try:
                with open(self.Auto_speichern_Einstellungsdatei, "w+") as schr_asp:
                    schr_asp.write("0")
                    self.Auto_speichern_ändern_knopp.configure(text="Autospeichern deaktiviert",fg_color="chocolate1", text_color="White")
                    self.Auto_speichern_Einstellungsdatei_var = "0"
            except Exception as o:
                print("Es ist ein fehler aufgetreten: ",o)
        else:
            print("autospeicher = aus oder was anderes")
            try:
                with open(self.Auto_speichern_Einstellungsdatei, "w+") as schr_asp:
                    schr_asp.write("1")
                    self.Auto_speichern_ändern_knopp.configure(text="Autospeichern aktiviert", fg_color="aquamarine", text_color="Black")
                    self.Auto_speichern_Einstellungsdatei_var = "1"
            except Exception as o1:
                print("Es ist ein fehler aufgetreten: ",o1)
                    
    def Menu_anzeige_wechseln(self): ############# Hier kommt der ganze Text für das Menü rein.
        print("Menu_anzeige_wechseln(def)")

       
        if self.Menü_da == True:
            print("menü == true(Menü war offen)")
            # Menu wird jetzt nicht mehr da sein.
            self.Pause_menu.place_forget()
            self.Menü_da = False
            self.Menü_Knopp.configure(text="Menü", fg_color="White", border_color="Black", border_width=1, text_color="Black", hover_color="pink")
            self.smtp_login_erfolgreich_l.place_forget()
            self.Einstellung_Design_auswahl.place_forget()
        elif self.Menü_da == False:
            # Menu wird jetzt angezeigt (Ja, wirklich.)
            print("menü == false (Menü war nicht offen)")
            self.Pause_menu.place(x=300,y=10)
            self.Menü_da = True
            self.Menü_Knopp.configure(text="Menü schließen", fg_color="aquamarine", hover_color="aquamarine3")

            

            self.gel_Email_Empfänger_L.place(x=220,y=150)
            self.gel_Email_Sender_L.place(x=220,y=180)
            self.gel_Email_Absender_Passwort_L.place(x=220,y=210)
            self.gel_SMTP_Server_L.place(x=220,y=240)

            self.gel_Email_Empfänger_E.place(x=370,y=150)
            self.gel_Email_Sender_E.place(x=370,y=180)
            self.gel_Email_Absender_Passwort_E.place(x=370,y=210)
            self.gel_SMTP_Server_E.place(x=370,y=240)
            self.Mail_Einstellungen_speichern.place(x=420,y=280)
            self.SMTP_Server_erneut_anmelden.place(x=420,y=360)

            self.Einstellung_Design_auswahl.place(x=10,y=200)
            self.Einstellung_Design_L.place(x=10,y=170)
            try:
                try:
                    self.gel_Email_Empfänger_E.delete(0, tk.END)
                    self.gel_Email_Sender_E.delete(0, tk.END)
                    self.gel_Email_Absender_Passwort_E.delete(0, tk.END)
                    self.gel_SMTP_Server_E.delete(0, tk.END)
                    self.gel_Email_Empfänger_E.delete(0, tk.END)
                except:
                    print("konnte die entrys nicht leeren")

                self.gel_Email_Empfänger_E.insert(0, self.empfänger_email)
                self.gel_Email_Sender_E.insert(0, self.sender_email)
                self.gel_Email_Absender_Passwort_E.insert(0, self.pw_email)
                self.gel_SMTP_Server_E.insert(0, self.smtp_server)
                print("Alles was mit den Email Einstellungen zu tun hat wurde erfolgreich gelade")
                
            except Exception as ExGelEm1:
                print("Fehler beim einfügen der Email Daten in die Entrys. Fehlercode: ", ExGelEm1)
            
            try:
                if self.smtp_login_erfolgreich == True:
                    self.smtp_login_erfolgreich_l.configure(text="Anmeldung am SMTP Server war erfolgreich.", text_color="SeaGreen1")
                    self.smtp_login_erfolgreich_l.place(x=220,y=320)
                elif self.smtp_login_erfolgreich == False:
                    self.smtp_login_erfolgreich_l.configure(text="Anmeldung am SMTP fehlgeschlagen.", text_color="Red")
                    self.smtp_login_erfolgreich_l.place(x=220,y=320)
            except Exception as Exc21:
                print(f"Fehler bei der entscheidung ob die Anmeldung bei Server erfolgreich war, wie auch immer das jetzt nun wieder schiefgehen konnte... Fehlercode: {Exc21}")



    def zeugs1_blacklist(self): # zuegs1 zum zeugs anstarrten
        print("zuegs1 zum zeugs anstarrten")
        self.Blacklist_bearbeiten = tk.CTkToplevel()
        best_bl_add = tk.CTkButton(self.Blacklist_bearbeiten, text="Kontakt speichern",command=self.zeugs_blacklist)
        self.t_nummer_bl = tk.CTkEntry(self.Blacklist_bearbeiten, placeholder_text="Telefonnummer")
        self.kunde_entry_bl = tk.CTkEntry(self.Blacklist_bearbeiten, placeholder_text="Name der Person")

        best_bl_add.pack()
        self.t_nummer_bl.pack()
        self.kunde_entry_bl.pack()
        
    def such_menü_hauptmenu_schließen(self):
        print("such_menü_hauptmenu_schließen(def)")
        self.Such_menu_haupt_frame.place_forget()
        self.KDabl_durchsuchen_Knopp.place_forget()
        self.durchsuchen_egal.place_forget()
        self.In_alten_Einträgen_suchen.place_forget()
        self.irgendwo_suchen.configure(text="durchsuchen...", command=self.such_menü_hauptmenu, hover_color="pink", fg_color="White", image=self.Durchsuchen_Bild_zu)

    def such_menü_hauptmenu(self):
        print("def such_menü_hauptmenu(self)")
        self.irgendwo_suchen.configure(text="schließen", command=self.such_menü_hauptmenu_schließen, hover_color="CadetBlue1", fg_color=self.aktiviert_farbe, image=self.Durchsuchen_Bild)
        self.Such_menu_haupt_frame.place(x=1060,y=100)
        self.KDabl_durchsuchen_Knopp = tk.CTkButton(self.Such_menu_haupt_frame, text="In Kndn-DB suchen", command=self.Suche_KDabl, fg_color="White", border_color="Black", border_width=1, text_color="Black", hover_color="pink", image=self.Kunde_suchen_Bild)
        self.KDabl_durchsuchen_Knopp.place(x=10,y=40)
        self.durchsuchen_egal = tk.CTkButton(self.Such_menu_haupt_frame, text="irgendwo suchen...", command=self.Suche1, fg_color="White", border_color="Black", border_width=1, text_color="Black", hover_color="pink", image=self.Durchsuchen_Bild)
        self.durchsuchen_egal.place(x=10, y=10)
        self.In_alten_Einträgen_suchen = tk.CTkButton(self.Such_menu_haupt_frame, text="In DB suchen", command=self.Suche_alte_Einträge, fg_color="White", border_color="Black", border_width=1, text_color="Black", hover_color="pink", image=self.Dings_Liste_Bild)
        self.In_alten_Einträgen_suchen.place(x=10,y=70)

    def zeugs_blacklist(self):
        DATEI_PFAD = self.Blacklist_pfad
        def lade_kontakte():
            try:
                with open(DATEI_PFAD, 'r', encoding='utf-8') as datei:
                    return json.load(datei)
            except FileNotFoundError:
                return {"Kontakte": []}
            except json.JSONDecodeError:
                messagebox.showerror("Fehler", "Fehler beim Lesen der JSON-Datei.")
                return {"Kontakte": []}

        def speichere_kontakte(kontakte):
            try:
                with open(DATEI_PFAD, 'w', encoding='utf-8') as datei:
                    json.dump(kontakte, datei, ensure_ascii=False, indent=4)
            except Exception as e:
                messagebox.showerror("Fehler", f"Fehler beim Speichern der JSON-Datei: {e}")

        def hinzufuegen_kontakt():
            telefonnummer = self.t_nummer_bl.get()
            name = self.kunde_entry_bl.get()

            if not telefonnummer or not name:
                messagebox.showwarning("Warnung", "Bitte beide Felder ausfüllen.")
                return

            kontakte = lade_kontakte()
            gefunden = False
            for kontakt in kontakte['Kontakte']:
                if kontakt['Telefonnummer_jsn_gesperrt'] == telefonnummer:
                    #messagebox.showinfo(title="CiM", message=f"Dieser Kontakt existiert bereits unter dem Namen {kontakt['Name']} mit der Telefonnummer {kontakt['Telefonnummer_jsn']}.")
                    self.Ereignislog.insert(tk.END, "-Der Name besteht bereits.-\n")
                    kontakt['Name'] = name
                    gefunden = True
                    #messagebox.showinfo("Info", "Name der bestehenden Telefonnummer aktualisiert.")
                    self.Ereignislog.insert(tk.END, "-bestehende Nummer wurde aktualisiert.-\n")
                    break

            if not gefunden:
                kontakte['Kontakte'].append({"Telefonnummer_jsn_gesperrt": telefonnummer, "Name": name})
                self.Ereignislog.insert(tk.END, "-Kontakt wurde hinzugefügt.-\n")
                #messagebox.showinfo("Erfolg", "Kontakt hinzugefügt.")

            speichere_kontakte(kontakte)
            self.Kontakt_soll_gleich_mitgespeichert_werden = True
        hinzufuegen_kontakt()
    
        
    
    def zeugs1(self): # zuegs1 zum zeugs anstarrten
        print("zuegs1 zum zeugs anstarrten")
        self.Kontakt_soll_gleich_mitgespeichert_werden = False
        self.zeugs()

    def zeugs(self):  # Diese beiden Funtkionen sind dafür da die Telefonummern in ner Json zu speichern, das hab ich nicht selbst geschrieben sondern nur kopiert und eingefügt weil es schnell gehen musste, wenn ich mal Zeit hab mach ichs selbst.
        DATEI_PFAD = self.Json_pfad 
        if self.Kontakt_soll_gleich_mitgespeichert_werden == True: # Es soll mitgespeichert werden
            def lade_kontakte():
                try:
                    with open(DATEI_PFAD, 'r', encoding='utf-8') as datei:
                        return json.load(datei)
                except FileNotFoundError:
                    return {"Kontakte": []}
                except json.JSONDecodeError:
                    messagebox.showerror("Fehler", "Fehler beim Lesen der JSON-Datei.")
                    return {"Kontakte": []}

            def speichere_kontakte(kontakte):
                try:
                    with open(DATEI_PFAD, 'w', encoding='utf-8') as datei:
                        json.dump(kontakte, datei, ensure_ascii=False, indent=4)
                except Exception as e:
                    messagebox.showerror("Fehler", f"Fehler beim Speichern der JSON-Datei: {e}")

            def hinzufuegen_kontakt():
                telefonnummer = self.t_nummer.get()
                name = self.kunde_entry.get()

                if not telefonnummer or not name:
                    #messagebox.showwarning("Warnung", "Bitte beide Felder ausfüllen.")
                    return

                kontakte = lade_kontakte()
                gefunden = False
                for kontakt in kontakte['Kontakte']:
                    if kontakt['Telefonnummer_jsn'] == telefonnummer:
                        #messagebox.showinfo(title="CiM", message=f"Dieser Kontakt existiert bereits unter dem Namen {kontakt['Name']} mit der Telefonnummer {kontakt['Telefonnummer_jsn']}.")
                        self.Ereignislog.insert(tk.END, "-Der Name besteht bereits.-\n")
                        kontakt['Name'] = name
                        gefunden = True
                        #messagebox.showinfo("Info", "Name der bestehenden Telefonnummer aktualisiert.")
                        self.Ereignislog.insert(tk.END, "-bestehende Nummer wurde aktualisiert.-\n")
                        break

                if not gefunden:
                    kontakte['Kontakte'].append({"Telefonnummer_jsn": telefonnummer, "Name": name})
                    self.Ereignislog.insert(tk.END, "-Kontakt wurde hinzugefügt.-\n")
                    #messagebox.showinfo("Erfolg", "Kontakt hinzugefügt.")

                speichere_kontakte(kontakte)
                self.Kontakt_soll_gleich_mitgespeichert_werden = True

            def loeschen_kontakt():
                telefonnummer = entry_telefonnummer.get()
                kontakte = lade_kontakte()
                neue_kontakte = [kontakt for kontakt in kontakte['Kontakte'] if kontakt["Telefonnummer_jsn"] != telefonnummer]
                if len(neue_kontakte) == len(kontakte['Kontakte']):
                    messagebox.showinfo("Info", "Telefonnummer nicht gefunden.")
                else:
                    kontakte['Kontakte'] = neue_kontakte
                    speichere_kontakte(kontakte)
                    self.Ereignislog.insert(tk.END, "-Kontakt wurde gelöscht.-\n")
                    #messagebox.showinfo("Erfolg", "Kontakt gelöscht.")
            hinzufuegen_kontakt()
        else: # Es soll nicht mitgespeichert werden.

            def lade_kontakte():
                try:
                    with open(DATEI_PFAD, 'r', encoding='utf-8') as datei:
                        return json.load(datei)
                except FileNotFoundError:
                    return {"Kontakte": []}
                except json.JSONDecodeError:
                    messagebox.showerror("Fehler", "Fehler beim Lesen der JSON-Datei.")
                    return {"Kontakte": []}

            def speichere_kontakte(kontakte):
                try:
                    with open(DATEI_PFAD, 'w', encoding='utf-8') as datei:
                        json.dump(kontakte, datei, ensure_ascii=False, indent=4)
                except Exception as e:
                    messagebox.showerror("Fehler", f"Fehler beim Speichern der JSON-Datei: {e}")

            def hinzufuegen_kontakt():
                telefonnummer = entry_telefonnummer.get()
                name = entry_name.get()
                if not telefonnummer or not name:
                    #messagebox.showwarning("Warnung", "Bitte beide Felder ausfüllen.")
                    return

                kontakte = lade_kontakte()
                gefunden = False
                for kontakt in kontakte['Kontakte']:
                    if kontakt['Telefonnummer_jsn'] == telefonnummer:
                        kontakt['Name'] = name
                        gefunden = True
                        messagebox.showinfo("Info", "Name der bestehenden Telefonnummer aktualisiert.")
                        break

                if not gefunden:
                    kontakte['Kontakte'].append({"Telefonnummer_jsn": telefonnummer, "Name": name})
                    messagebox.showinfo("Erfolg", "Kontakt hinzugefügt.")

                speichere_kontakte(kontakte)
                entry_telefonnummer.delete(0, tk.END)
                entry_name.delete(0, tk.END)

            def loeschen_kontakt():
                telefonnummer = entry_telefonnummer.get()
                kontakte = lade_kontakte()
                neue_kontakte = [kontakt for kontakt in kontakte['Kontakte'] if kontakt["Telefonnummer_jsn"] != telefonnummer]
                if len(neue_kontakte) == len(kontakte['Kontakte']):
                    messagebox.showinfo("Info", "Telefonnummer nicht gefunden.")
                else:
                    kontakte['Kontakte'] = neue_kontakte
                    speichere_kontakte(kontakte)
                    messagebox.showinfo("Erfolg", "Kontakt gelöscht.")
                entry_telefonnummer.delete(0, tk.END)
                entry_name.delete(0, tk.END)

            root1 = Atk.Toplevel()
            root1.title("Kontaktmanager")
            width = 420
            height = 320

            def mittig_fenster(root1, width, height):
                fenster_breite = root1.winfo_screenwidth()
                fenster_höhe = root1.winfo_screenheight()
                x = (fenster_breite - width) // 2
                y = (fenster_höhe - height) // 2
                root1.geometry(f"{width}x{height}+{x}+{y}")

            mittig_fenster(root1, width, height)

            frame = Atk.Frame(root1)
            frame.pack(pady=10)
            
            label_telefonnummer = Atk.Label(frame, text="Telefonnummer:")
            label_telefonnummer.grid(row=0, column=0, padx=5, pady=5)
            entry_telefonnummer = Atk.Entry(frame)
            entry_telefonnummer.grid(row=0, column=1, padx=5, pady=5)
            
            label_name = Atk.Label(frame, text="Name:")
            label_name.grid(row=1, column=0, padx=5, pady=5)
            entry_name = Atk.Entry(frame)
            entry_name.grid(row=1, column=1, padx=5, pady=5)
            
            button_hinzufuegen = Atk.Button(frame, text="Hinzufügen", command=hinzufuegen_kontakt)
            button_hinzufuegen.grid(row=2, column=0, padx=5, pady=5)
            
            button_loeschen = Atk.Button(frame, text="Löschen", command=loeschen_kontakt)
            button_loeschen.grid(row=2, column=1, padx=5, pady=5)


    def Suche1(self):
        print("Suchen(def)")
        self.Suche_suche = ""
        self.gesucht_zahl = 0
        self.gesucht_zahl_mit_fehlern = 0
        self.Ergebnise_zahl = 0
        try:
            
            self.Ergebnisse_des_scans_feld = tk.CTkTextbox(self.suchfenster_ergebnisse, width=500, height=500)
        except:
            pass
        self.durchsucht_text = f"bis jetzt wurden {self.gesucht_zahl} Dateien durchsucht."
        self.durchsucht_text_mit_fehlern = f"Fehler: {self.gesucht_zahl_mit_fehlern}"
        try:
            self.suchfenster_ergebnisse = tk.CTkToplevel(root)
            self.suchfenster_ergebnisse.resizable(False,False)
            try:
                height = 350
                width = 920
                x = root.winfo_x() + root.winfo_width()//2 - self.suchfenster_ergebnisse.winfo_width()//2
                y = root.winfo_y() + root.winfo_height()//2 - self.suchfenster_ergebnisse.winfo_height()//2
                self.suchfenster_ergebnisse.geometry(f"{width}x{height}+{x}+{y}")
            except:
                pass
            self.suchfenster_ergebnisse.title("Suchergebnisse")
        except:
            pass
        
        print("fenster fürs suchen geladen...")
        self.Zahl_anzeige = tk.CTkLabel(self.suchfenster_ergebnisse, text=self.durchsucht_text)
        self.Zahl_anzeige.pack()
        self.Zahl_anzeige_der_fehler = tk.CTkLabel(self.suchfenster_ergebnisse, text=self.durchsucht_text_mit_fehlern)
        self.Zahl_anzeige_der_fehler.pack()
        self.Ergebnisse_Listbox = Atk.Listbox(self.suchfenster_ergebnisse)
        self.Ergebnisse_Listbox.pack(fill="both", expand=True)
        self.suchfenster_ergebnisse.protocol("WM_DELETE_WINDOW", self.bye_suchfenster)
        scrollbar = Atk.Scrollbar(self.Ergebnisse_Listbox, orient=Atk.VERTICAL)
        scrollbar.pack(side=Atk.RIGHT, fill=Atk.Y)
        self.Ergebnisse_Listbox.config(yscrollcommand=scrollbar.set)
        scrollbar.config(command=self.Ergebnisse_Listbox.yview)
        
        if self.Ort_wo_gesucht_wird == "":
            self.Ort_wo_gesucht_wird = filedialog.askdirectory()
        print("pfad wurde ausgewählt")
        such_dialog = tk.CTkInputDialog(title="CiM Suche", text="Wonach suchst Du? Es werden die bisher noch gespeichertern Liste aus dem Programmverzeichnis durchsucht. (Groß-und Kleinschreibung wird ignoriert)")
        try:
            x = root.winfo_x() + root.winfo_width()//2 - such_dialog.winfo_width()//2
            y = root.winfo_y() + root.winfo_height()//2 - such_dialog.winfo_height()//2
            such_dialog.geometry(f"x+{x}+{y}")
        except:
            print("Fehler beim zentrieren des Such-Dialogs. selbst wenn ich hier die Fehlermeldung hinschreiben würde, würdest Du sie nicht verstehen denn ich habe auch keine Ahnung.")

        self.Suche_suche = such_dialog.get_input()
        such_dialog.destroy()
        if self.Suche_suche != "":
            try:
                #if self.etwas_suchen1 == False:
                 #   self.etwas_suchen1 = True
                self.thread_suche = threading.Thread(target=self.Suche_algo)
                self.thread_suche.start()
                    #self.Suche_algo()
                print("Thread für die Suche gestartet.")
            except:
                #self.etwas_suchen1 = True
                print("Thread für die Suche konnte nicht gestartet werden.")
                try:
                    self.etwas_suchen1 = True
                    self.Suche_algo()
                except Exception as esisx:
                    print("fehler161: ",esisx)
        else:
            messagebox.showinfo(message="Suche Abgebrochen.")
            self.suchfenster_ergebnisse.destroy()

    def Eintrag_aufmachen(self, event):
        auswahl_der_Listbox = self.Ergebnisse_Listbox.curselection()
        index = auswahl_der_Listbox[0]
        zu_aufmachen_Eintrag = self.Ergebnisse_Listbox.get(index)
        if platform.system() == "Windows":
            os.startfile(zu_aufmachen_Eintrag) # Für Windows
        elif platform.system() == "Darwin":
            subprocess.call(["open", zu_aufmachen_Eintrag]) # Für MacOS

    def bye_suchfenster(self):
        print("Suchfenster wurde geschlossen.")
        self.Ergebnisse_Listbox.unbind("<Double-1>")
        self.suchfenster_ergebnisse.destroy()

    def Suche_KDabl(self):
        self.Ort_wo_gesucht_wird = "/Volumes/Kundenablage/"
        self.Suche1()

    def Suche_alte_Einträge(self):
        self.Ort_wo_gesucht_wird = self.Listen_Speicherort_standard
        self.Suche1()

    def Suche_algo(self):
        self.Ergebnise_zahl = 0

        if self.Suche_suche:
            def read_text_file(file_path):
                try:
                    with open(file_path, 'r', encoding='utf-8') as file:
                        return file.read()
                except Exception as e:
                    self.gesucht_zahl_mit_fehlern += 1
                    self.durchsucht_text_mit_fehlern = f"Fehler: {self.gesucht_zahl_mit_fehlern}"
                    self.Zahl_anzeige_der_fehler.configure(text=self.durchsucht_text_mit_fehlern)
                    #print(f"Fehler: {e}")
                    return ""

            folder_path = self.Ort_wo_gesucht_wird
            content_to_search = self.Suche_suche.lower()  # Konvertiere den Suchinhalt in Kleinbuchstaben
            results = []
            try:
                for root, dirs, files in os.walk(folder_path):
                    for file_name in files:
                        try:
                            if file_name.endswith('.txt'):
                                file_path = os.path.join(root, file_name)
                                file_content = read_text_file(file_path).lower()# Konvertiere den Dateiinhalt in Kleinbuchstaben
                                self.gesucht_zahl += 1
                                self.durchsucht_text = f"bis jetzt durchsucht: {self.gesucht_zahl}"
                                self.Zahl_anzeige.configure(text=self.durchsucht_text)  
                                if content_to_search in file_content:
                                    self.Ergebnise_zahl += 1
                                    results.append(file_path)
                                    self.Ergebnisse_Listbox.insert(tk.END, file_path)
                                    self.Ergebnisse_Listbox.yview(tk.END)
                        except Exception as e:
                            self.gesucht_zahl_mit_fehlern += 1
                            self.durchsucht_text_mit_fehlern = f"Fehler: {self.gesucht_zahl_mit_fehlern}"
                            self.Zahl_anzeige_der_fehler.configure(text=self.durchsucht_text_mit_fehlern)
            except Exception as e:
                self.etwas_suchen1 = False
                self.Suche_suche = ""
                self.Ort_wo_gesucht_wird = ""
                try:
                    self.thread_suche.join()
                    print("Thread wurde erfolgreich beendet. (exception vor der Suche)")
                except Exception as E_t:
                    print(f"Konnte den Thread self.thread_suche nicht beenden, (vor der Suche) Fehlermeldung: {E_t}")

            if results:
                ganzes_ergebnis = "Ich habe in folgenden Dateien " + str(self.Ergebnise_zahl) + " Ergebnisse gefunden:"
                erg_l = tk.CTkLabel(self.suchfenster_ergebnisse, text=ganzes_ergebnis)
                erg_l.pack()
                self.rearesults = results
                self.durchsucht_text = f"Es wurden insgesammt: {self.gesucht_zahl} Daten durchsucht. {ganzes_ergebnis}"
                self.knopp_offnen = tk.CTkButton(self.suchfenster_ergebnisse, text="Alle einfach aufmachen", command=self.aufmachen_results_vor)
                self.knopp_offnen.pack()
                self.Ergebnisse_Listbox.bind("<Double-1>", self.Eintrag_aufmachen)
                self.Anzal_der_Ergebnisse = self.Ergebnise_zahl
                self.etwas_suchen1 = False
                self.etwas_suchen = False
                self.Suche_suche = ""
                self.Ort_wo_gesucht_wird = ""
                try:
                    self.thread_suche.join()
                    print("Thread wurde erfolgreich beendet. (nach dem die Results festehen)")
                except Exception as E_t:
                    print(f"Konnte den Thread self.thread_suche nicht beenden, (im results) Fehlermeldung: {E_t}")
            else:
                self.Ergebnisse_Listbox.unbind("<Double-1>")
                dmsg = "Dazu konnte ich leider nichts finden."
                self.etwas_suchen1 = False
                self.Suche_suche = ""
                self.Ort_wo_gesucht_wird = ""
                try:
                    self.thread_suche.join()
                    print("Thread wurde erfolgreich beendet. (im else der results)")
                except Exception as E_t:
                    print(f"Konnte den Thread self.thread_suche nicht beenden, (im else der results) Fehlermeldung: {E_t}")
                messagebox.showinfo(title="CiM Suche", message=dmsg)
                self.suchfenster_ergebnisse.destroy()
                
        else:
            print("gab nüscht")
            self.Ergebnisse_Listbox.unbind("<Double-1>")
            dmsg = "Dazu konnte ich leider nichts finden..."
            self.Suche_suche = ""
            self.etwas_suchen1 = False
            try:
                self.thread_suche.join()
                print("Thread wurde erfolgreich beendet. (else des gab nüscht)")
            except Exception as E_t:
                print(f"Konnte den Thread self.thread_suche nicht beenden, Fehlermeldung: {E_t}")
            messagebox.showinfo(title="CiM Suche", message=dmsg)
            self.suchfenster_ergebnisse.destroy()

    def aufmachen_results(self):
        try:
            for result in self.rearesults:
                if platform.system() == "Windows":
                    os.startfile(result) # Für Windows
                elif platform.system() == "Darwin":
                    subprocess.call(["open", result]) # Für MacOS
        except Exception as exci_leer:
            messagebox.showerror(title="Fehler CiM", message=exci_leer)

    def aufmachen_results_vor(self):
        print("suche_alles aufamachen davor warnmeldung dings")
        if self.Anzal_der_Ergebnisse >= 20:
            print(f"Es sind >= 20 Suchergebnisse... {self.Anzal_der_Ergebnisse}")
            antw = messagebox.askyesno(title="CiM Suche", message=f"Sind Sie sicher dass sie wirklich alle {self.Anzal_der_Ergebnisse} Ergbnisse öffnen möchten? (Unter Windows könnte Ihr System einfrieren)")
            if antw:
                if antw == True:
                    self.aufmachen_results()
                elif antw == False:
                    print("[-INFO-] Nutzer wollte doch nicht alles aufmachen")
        elif self.Anzal_der_Ergebnisse <= 20:
            print(f"Es sind weniger als 20 Suchergbnisse.{self.Anzal_der_Ergebnisse}")
            self.aufmachen_results()
            
####
    def genaue_suche(self):
        self.suchedrei_Fenster = tk.CTkToplevel(root)
        self.suchedrei_Fenster.title("Changelogs")
        self.suchedrei_Fenster.configure(fg_color="White")
        self.Textfeld_suchedrei = tk.CTkTextbox(self.suchedrei_Fenster, width=820, height=420, text_color="Black", fg_color="azure", wrap="word", border_width=0)
        height = 420
        width = 820
        try:
            x = root.winfo_x() + root.winfo_width()//2 - self.suchedrei_Fenster.winfo_width()//2
            y = root.winfo_y() + root.winfo_height()//2 - self.suchedrei_Fenster.winfo_height()//2
            self.suchedrei_Fenster.geometry(f"{width}x{height}+{x}+{y}")
        except:
            print("Konnte das changelogfenster nicht zentrieren.")
            self.suchedrei_Fenster.geometry(f"{width}x{height}+{x}+{y}")
        self.suchedrei_Fenster.resizable(False,False)
        self.Textfeld_suchedrei.pack()
        
        def list_synonyms(word):
            synonyms = set()
            for synset in wordnet.synsets(word):
                for lemma in synset.lemmas():
                    synonyms.add(lemma.name())
            return list(synonyms)

        def is_text_file(file_name):
            text_extensions = {'.txt', '.rtf', '.md', '.html', '.xml', '.csv'}
            _, ext = os.path.splitext(file_name)
            return ext.lower() in text_extensions

        def search_files_for_words(path, words):
            results = defaultdict(list)
            word_synonyms = defaultdict(list)
            
            
            for word in words:
                synonyms = list_synonyms(word)
                word_synonyms[word] = synonyms + [word]  # Include the word itself as a synonym
            
            
            for root, _, files in os.walk(path):
                for file in files:
                    if is_text_file(file):
                        file_path = os.path.join(root, file)
                        with open(file_path, 'r', encoding='utf-8', errors='ignore') as f:
                            for line_num, line in enumerate(f, 1):
                                for word, synonyms in word_synonyms.items():
                                    pattern = r'\b({})\b'.format('|'.join(map(re.escape, synonyms)))
                                    matches = re.findall(pattern, line, flags=re.IGNORECASE)
                                    if matches:
                                        results[word].append((file_path, line_num, line.strip()))
                                    
            return results, word_synonyms
        

        path = filedialog.askdirectory()
        such_dialog_3 = tk.CTkInputDialog(title="CiM Suche", text="Wonach suchst Du? Es werden die bisher noch gespeichertern Liste aus dem Programmverzeichnis durchsucht. (Groß-und Kleinschreibung wird ignoriert)")
        try:
            x = root.winfo_x() + root.winfo_width()//2 - such_dialog_3.winfo_width()//2
            y = root.winfo_y() + root.winfo_height()//2 - such_dialog_3.winfo_height()//2
            such_dialog_3.geometry(f"x+{x}+{y}")
        except:
            print("Fehler beim zentrieren des Such-Dialogs. selbst wenn ich hier die Fehlermeldung hinschreiben würde, würdest Du sie nicht verstehen denn ich habe auch keine Ahnung.")

        self.Suche_suche_3 = such_dialog_3.get_input()
        if self.Suche_suche_3:
            words = self.Suche_suche_3
            print("dann mal los")
            
            if not os.path.isdir(path):
                print("Der angegebene Pfad existiert nicht oder ist kein Verzeichnis.")
            else:
                results, word_synonyms = search_files_for_words(path, words)
                
                if not results:
                    print("Keine Ergebnisse gefunden.")
                    messagebox.showinfo(title="Info", message="Darunter wurde nichts gefunden.")
                else:
                    for word, occurrences in results.items():
                        self.Textfeld_suchedrei.insert(tk.END, f"\nWort: {word}")
                        self.Textfeld_suchedrei.insert(tk.END, f"   Synonyme: {', '.join(word_synonyms[word])}")
                        for occurrence in occurrences:
                            self.Textfeld_suchedrei.insert(tk.END, f"   Datei: {occurrence[0]}")
                            self.Textfeld_suchedrei.insert(tk.END, f"   Zeile {occurrence[1]}: {occurrence[2]}")

                    
                    
                    
        else:
            messagebox.showinfo(title="Info", message="Suche abgebrochen.")
            self.Suche_suche_3 = ""

####
    def Kunde_ruft_an(self):
        print("Thread gestartet: Kunde_ruft_an (def)")
        while self.Programm_läuft == True:
            try:
                with open("tmp.txt", "r") as tmp_ld:
                    gel_tmp = tmp_ld.read()
                    self.Anruf_Telefonnummer = gel_tmp
                    print1 = "-abgefangene Telefonummer: " + self.Anruf_Telefonnummer + "-\n"
                    self.Ereignislog.insert(tk.END, print1)
                    self.Uhrzeit_anruf_start = self.Zeit
                    tmp_ld.close()
                    os.remove("tmp.txt")
                    self.Gesperrte_Nummer = False
                    try:
                        print("else f")
                        with open(self.Json_pfad, 'r', encoding='utf-8') as datei:
                            daten = json.load(datei)
                        try:
                            print("lade die Blacklist...")
                            with open(self.Blacklist_pfad, "r", encoding='utf-8') as b_datei:
                                daten_blacklist = json.load(b_datei)
                        except Exception as E:
                            self.Ereignislog.insert(tk.END, "-Konnte die Blacklist nicht laden-\n")
                            daten_blacklist = ""
                        for Gesperrte_kontakt in daten_blacklist.get("Kontakte", []):
                            print(f"ich durchsuche die Blacklist... mit {Gesperrte_kontakt.get("Telefonnummer_jsn_gesperrt")}")
                            if str(Gesperrte_kontakt.get("Telefonnummer_jsn_gesperrt")) == str(self.Anruf_Telefonnummer):
                                print("if f")
                                self.Ereignislog.insert(tk.END, "-Telefonnummer in Blacklist gefunden!\n Nummer wurde nicht eingefügt.")
                                self.Anruf_Telefonnummer = None
                                self.Gesperrte_Nummer = True
                            else:
                                print(f"offensichtlicher weise war {str(Gesperrte_kontakt.get("Telefonnummer_jsn_gesperrt"))} nicht das selbe wie {str(self.Anruf_Telefonnummer)}... oder so ähnlich.")
                            #else:
                        if self.Gesperrte_Nummer == False:
                            print("else f 1")
                            print("die Nummer stand nicht in der Blacklist")
                            self.t_nummer.configure(state="normal")
                            self.t_nummer.delete(0,tk.END)
                            self.t_nummer.insert(1,self.Anruf_Telefonnummer)
                            self.t_nummer.configure(state="disabled")
                            for kontakt in daten.get("Kontakte", []):
                                if kontakt.get("Telefonnummer_jsn") == self.Anruf_Telefonnummer: # WENN ES IN DER KTK GEFUNDEN WURDE
                                    print("if f 1")
                                    Name_gel_für_e = kontakt.get("Name")
                                    self.kunde_entry.insert(tk.END,Name_gel_für_e)
                                    self.Anruf_Telefonnummer = None
                                    self.Ereignislog.insert(tk.END, "-Anruf wurde beendet.-\n")
                                    # hier kommen jetzt die Ausnahmen für spezielle Kontakte hin. !!WENN SIE GEFUNDEN WUDEN!!
                                                
                                        # hier enden die speziellen Ausnahmen für spezielle Kontakte.
                    except Exception as ExcK1:
                            print(f"Fehler beim Durchsuchen der JSON DB nach dem Kontakt. Fehlercode: {ExcK1}")
            except Exception:
                pass
            try:
                with open("tmp1.txt", "r") as tmp1_ld:
                    gel_tmp1 = tmp1_ld.read()
                    self.Uhrzeit_anruf_ende = gel_tmp1
                    print("End-Uhrzeit: ", self.Uhrzeit_anruf_ende)
                    tmp1_ld.close()
                    try:
                        os.remove("tmp1.txt")
                    except:
                        pass  
            except:
                pass
            time.sleep(1)
        print("Thread beendet: Kunde_ruft_an (def")
            
    
#### ende der werbung ####### was für ne werbung?
    def info(self):
        print("(INFO) Info(def)")
        messagebox.showinfo(title="Info", message=self.Programm_Name_lang + " " + self.Version + "\n Programmiert von Maximilian Becker, \n https://dings.software für mehr Informationen")

    def Auto_sp_ändern(self):
        print("auto_speichern(def)")
        try:
            with open(self.Auto_speichern_Einstellungsdatei, "w+") as r_gel:
                self.aSp_var = r_gel.read()
                if self.aSp_var == "Ja":
                    r_gel.write("0")
                else:
                    r_gel.write("1")
        except Exception as esx:
            print("auto_sp ist abgekackt. Fehlercode: " , esx)

    def Admin_rechte(self):
        try:
            response = ctypes.windll.user32.MessageBoxW(None, "Möchten Sie Administratorrechte anfordern? Dies wird das Programm mit Adminrechten neustarten. Das funktioniert auch glaube nur auf Windows.", "Administratorrechte erforderlich", 4)
            if response == 6:  # Wert 6 entspricht dem Klick auf "Ja"
                try:
                    # Hier führen wir die Funktion mit Administratorrechten aus
                    print("Instanz mit Admin Rechten gestartet")
                    ctypes.windll.shell32.ShellExecuteW(None, "runas", sys.executable, " ".join(sys.argv), None, 1)
                    sys.exit()
                except Exception as e:
                    messagebox.showerror(title="ich sagte doch das geht nicht...", message=e)
                    print("Fehler beim Ausführen der 'Admin_Rechte'-Funktion:", e)
            else:
                print("Administratorrechte wurden nicht angefordert.")
        except Exception as excAdm:
            messagebox.showinfo(message=excAdm)

    def senden(self, event):
        print("(DEV) senden(def)")
        kunde = self.kunde_entry.get()
        problem = self.problem_entry.get()
        info = self.info_entry.get()
        T_Nummer = self.t_nummer.get()
        self.ausgabe_text.configure(state='normal')
        self.zeit_string = time.strftime("%H:%M:%S")
        if self.Uhrzeit_anruf_start == None:
            self.Uhrzeit_anruf_start = "-"
        if self.Uhrzeit_anruf_ende == None:
            self.Uhrzeit_anruf_ende = self.zeit_string + " (mit abweichung)"
        self.Uhrzeit_text = self.Uhrzeit_anruf_start + " bis " + self.Uhrzeit_anruf_ende
        
        if kunde or problem or info != "":
            #print("(INFO) Enter gedrückt obwohl etwas geschrieben wurde.")
            if self.kunde_entry.get() == "":
                kunde = "-"
            if self.problem_entry.get() == "":
                problem = "-"
            if self.info_entry.get() == "":
                info = "-"
            if self.t_nummer.get() == "Telefonnummer":
                T_Nummer = "-"
            elif self.t_nummer.get() == "":
                T_Nummer = "-"
            if self.Weiterleitung_an == "":
                self.Weiterleitung_an = "Keine Weiterleitung"
            if self.wollte_sprechen == "":
                self.wollte_sprechen = "Nein"

            if os.path.exists(self.Liste_mit_datum):
                with open(self.Liste_mit_datum, "a") as f:
                    f.write(f"Uhrzeit: {self.Uhrzeit_text}\nAnrufer: {kunde}\nProblem: {problem}\nInfo: {info}\nTelefonnummer: {T_Nummer}\nJemand bestimmtes sprechen: {self.wollte_sprechen}\nWeiterleitung: {self.Weiterleitung_an}\n\n")
                with open(self.Liste_mit_datum, "r") as f:
                    feedback_text = f.read()
                    self.ausgabe_text.delete("1.0", tk.END)
                    self.ausgabe_text.insert(tk.END, feedback_text)
                self.ausgabe_text.configure(state='disabled')
                self.ausgabe_text.see(tk.END)
                self.Weiterleitung_an = ""
                self.Uhrzeit_anruf_ende = None
                self.optionmenu.set("Keine Weiterleitung")
                self.optionmenu1.set("Mit Wem sprechen?")
                self.kunde_entry.focus()
                self.zeugs()
                # jetzt wurde das ding fertig in eine neue Datei versendet
            else:
                print("(INFO) Liste zum beschreiben existiert bereits.")
                with open(self.Liste_mit_datum, "w+") as f:
                    f.write(f"Uhrzeit: {self.Uhrzeit_text}\nAnrufer: {kunde}\nProblem: {problem}\nInfo: {info}\nTelefonnummer: {T_Nummer}\nJemand bestimmtes sprechen: {self.wollte_sprechen}\nWeiterleitung: {self.Weiterleitung_an}\n\n")
                with open(self.Liste_mit_datum, "r") as f:
                    feedback_text = f.read()
                    self.ausgabe_text.delete("1.0", tk.END)
                    self.ausgabe_text.insert(tk.END, feedback_text)
                    self.ausgabe_text.configure(state='disabled')
                    self.Weiterleitung_an = ""
                    self.wollte_sprechen = ""
                    self.Uhrzeit_anruf_ende = None
                    self.optionmenu.set("Keine Weiterleitung")
                    self.optionmenu1.set("Mit Wem sprechen?")
                    self.kunde_entry.focus()
                    self.zeugs()
                    # jetzt wurde das ding fertig in eine bestehende Datei versendet
        else:
            print("(ERR) Da hat wer Enter gedrückt obwohl noch nicht geschrieben war.")
            messagebox.showinfo(title="Fehler", message="Bitte geben Sie zuerst in wenigsten eine Spalte etwas ein.")
            self.ausgabe_text.configure(state='disabled')
            self.Weiterleitung_an = ""
            self.wollte_sprechen = ""
            self.optionmenu.set("Keine Weiterleitung")
            self.optionmenu1.set("Mit Wem sprechen?")
            self.Uhrzeit_anruf_start = None
            return
        self.t_nummer.configure(state="normal")
        self.t_nummer.delete(0,tk.END)
        self.kunde_entry.delete(0, tk.END)
        self.problem_entry.delete(0, tk.END)
        self.info_entry.delete(0, tk.END)
        self.t_nummer.configure(state="disabled")
        self.Weiterleitung_an = ""
        self.wollte_sprechen = ""
        self.Uhrzeit_anruf_start = None
        self.optionmenu.set("Keine Weiterleitung")
    
    def beb_c(self):
        self.text_tk_text = self.ausgabe_text.get("1.0", "end-1c") # mir fällt jetzt erst im Nachhinein (3-4 Monate später) auf das da "end-1c" steht, wtf ist das und warum ist das da?
        if self.beb == "0":
            print("beb is jetzt = 1")
            self.ausgabe_text.configure(state='normal')
            self.t_nummer.configure(state="normal")
            self.beb_knopp.configure(text="Fertig", fg_color="aquamarine", hover_color="aquamarine3")
            self.beb = "1"
            root.unbind('<Return>')
        else:
            print("beb = 0")
            self.ausgabe_text.configure(state='disabled')
            self.t_nummer.configure(state="disabled")
            root.bind('<Return>', self.senden)
            self.beb_knopp.configure(text="Bearbeiten", fg_color="white", hover_color="DarkSlateGray1")
            self.beb = "0"
            with open(self.Liste_mit_datum, "w+") as f:
                f.write(self.text_tk_text)
                print("das beb wurde geschrieben.")

    def alles_löschen(self):
        print("alles_löschen(def)")
        
        abfrage_wegen_löschen_db = messagebox.askquestion(title='Information', message="möchten Sie wirklich die gesamte Kontaktliste unwiderruflich löschen?")
        if abfrage_wegen_löschen_db == "yes":  
            print("löschen der db vom Nutzer bestätigt")
            self.tag_und_zeit_string = time.strftime("%m/%d/%Y, %H:%M:%S")
            print(self.tag_und_zeit_string)
            self.ausgabe_text.configure(state='normal')
            self.ausgabe_text.delete("1.0", tk.END)  # Hier wird der Inhalt des Textfelds gelöscht
            self.ausgabe_text.configure(state='disabled')
            try:
                print("try1")
                if os.path.exists(self.DB):
                    print("Liste existiert")
                    os.remove(self.DB)
                    print("datei gelöscht")
                    self.ausgabe_text.delete("1.0", tk.END)
                    print("textfeld gelöscht")
                else:
                    messagebox.showerror(title="Fehler", message="Es gab keine alten Einträge zum löschen.")
            except:
                messagebox.showerror(title="Fehler", message="Es ist ein unbekannter Fehler beim Löschen der alten Einträge aufgetreten, Fehlercode: 0")
        elif abfrage_wegen_löschen_db == "no":
            print("löschen der db vom Nutzer abgerbrochen.")
        else:
            print("db löschen fehler.")
            messagebox.showerror(title="Fehler", message="Kaputt")

    def pause(self):
        print("pause(def)")
        try:
            self.kunde_entry.grid_forget()
            self.problem_entry.grid_forget()
            self.info_entry.grid_forget()
            self.senden_button.grid_forget()
            self.ausgabe_text.grid_forget()
        except:
            pass
        self.p_text = tk.CTkLabel(root, text="Jetzt ist gerade Pause und mit vollem Mund spricht man nicht!")
        self.Zeit_text = tk.CTkLabel(root, text=" ")
        custom_font = ("Helvetica", 64)
        self.Zeit_text.configure(font=custom_font)
        self.pause_ende = tk.CTkButton(root, text="Pause beenden", command=self.pause_beenden_c)
        self.zeit_string = time.strftime("%H:%M:%S")
        self.start_der_pause = tk.CTkLabel(root, text=self.zeit_string, font=("Helvetica", 12))
        self.start_der_pause.place(x=100,y=350)

        self.p_text.place(x=300,y=100)
        self.pause_ende.place(x=100,y=300)
        self.Zeit_text.place(x=420,y=420)


    def Uhr(self):
        print("Thread gestartet: Uhr(def)")
        while self.Uhr_läuft == True:
            lokaler_zeit_string = time.strftime("%H:%M:%S")
            self.Zeit = time.strftime("%H:%M:%S")
            try:
                self.Zhe_Clock.configure(text=self.Zeit)
                root.title(self.Programm_Name + " " + self.Version + "                                                                          " + self.Zeit)
                if self.Zeit == "17:30:00":
                    root.title(self.Programm_Name + " " + self.Version + " FEIERABEND!!")
                    messagebox.showinfo(title="Fertsch", message="Dings, es ist Feierabend.")
                elif self.Zeit == "17:31:00":
                    root.title(self.Programm_Name + " " + self.Version + " FEIERABEND!! (eigentlich)")
                    self.Uhr_läuft = False
            except Exception as e:
                print(e)
            if self.Zeit_text:
                self.Zeit_text.configure(text=lokaler_zeit_string)
                
            time.sleep(1)
        print("Thread Beendet: Uhr(def)")
        
            

    
    def pause_beenden_c(self):
        print("pause_beenden(def)")
        self.Pause = False

    def als_csv_speichern(self): #das ist das speicher unter... dings
        print("Als CSV speichern")
        self.csv_datei_pfad = filedialog.askdirectory()

        if self.csv_datei_pfad:
            with open(self.Liste_mit_datum, 'r') as text_datei:
                daten = text_datei.read()
            zeilen = daten.strip().split('\n')
            datensaetze = []
            uhrzeit, kunde, problem, info, Telefonnummer, wollte_sprechen, Weiterleitung = "", "", "", "", "", "", ""
            for zeile in zeilen:
                if zeile.startswith("Uhrzeit:"):
                    uhrzeit = zeile.replace("Uhrzeit:", "").strip()
                elif zeile.startswith("Anrufer:"):
                    kunde = zeile.replace("Anrufer:", "").strip()
                elif zeile.startswith("Problem:"):
                    problem = zeile.replace("Problem:", "").strip()
                elif zeile.startswith("Info:"):
                    info = zeile.replace("Info:", "").strip()
                elif zeile.startswith("Telefonnummer:"):
                    Telefonnummer = zeile.replace("Telefonnummer:", "").strip()
                elif zeile.startswith("Jemand bestimmtes sprechen:"):
                    wollte_sprechen = zeile.replace("Jemand bestimmtes sprechen:", "").strip()
                elif zeile.startswith("Weiterleitung:"):
                    Weiterleitung = zeile.replace("Weiterleitung:", "").strip()
                    
                if kunde and problem and info and uhrzeit and Telefonnummer and wollte_sprechen and Weiterleitung:
                    datensaetze.append([ uhrzeit, kunde, problem, info, Telefonnummer,  wollte_sprechen, Weiterleitung])
                    uhrzeit, kunde, problem, info, Telefonnummer,  wollte_sprechen, Weiterleitung = "", "", "", "", "", "", ""

            if datensaetze:
                self.tag_string = str(time.strftime("%d %m %Y"))
                with open(self.csv_datei_pfad + "/AnruferlistenDings" + self.tag_string + ".csv" , 'w', newline='') as datei:
                    schreiber = csv.writer(datei)
                    schreiber.writerow(["Uhrzeit", "Anrufer", "Problem", "Info", "Telefonnummer", "Wollte Sprechen", "Weiterleitung"])
                    schreiber.writerows(datensaetze)
                    self.zeit_string = time.strftime("%H:%M:%S")
                    self.tag_string = str(time.strftime("%d %m %Y"))
                print("Daten wurden in die CSV-Datei gespeichert.")
                messagebox.showinfo(title="Gespeichert", message="Daten wurden erfolgreich gespeichert.")
            else:
                print("Fehler: Keine vollständigen Informationen wurden in der Textdatei gefunden.")
                messagebox.showerror(title="Fehler", message="Das ist etwas beim Speichern schiefgelaufen.")

    def als_csv_speichern_eigener_ort(self):
        print("Als CSV speichern, im Standard Ort")
        self.csv_datei_pfad = self.Listen_Speicherort_geladen

        if self.csv_datei_pfad:
            with open(self.Liste_mit_datum, 'r') as text_datei:
                daten = text_datei.read()
            zeilen = daten.strip().split('\n')
            datensaetze = []
            uhrzeit, kunde, problem, info, Telefonnummer, wollte_sprechen, Weiterleitung = "", "", "", "", "", "", ""
            for zeile in zeilen:
                if zeile.startswith("Uhrzeit:"):
                    uhrzeit = zeile.replace("Uhrzeit:", "").strip()
                elif zeile.startswith("Anrufer:"):
                    kunde = zeile.replace("Anrufer:", "").strip()
                elif zeile.startswith("Problem:"):
                    problem = zeile.replace("Problem:", "").strip()
                elif zeile.startswith("Info:"):
                    info = zeile.replace("Info:", "").strip()
                elif zeile.startswith("Telefonnummer:"):
                    Telefonnummer = zeile.replace("Telefonnummer:", "").strip()
                elif zeile.startswith("Jemand bestimmtes sprechen:"):
                    wollte_sprechen = zeile.replace("Jemand bestimmtes sprechen:", "").strip()
                elif zeile.startswith("Weiterleitung:"):
                    Weiterleitung = zeile.replace("Weiterleitung:", "").strip()
                    
                if kunde and problem and info and uhrzeit and Telefonnummer and wollte_sprechen and Weiterleitung:
                    datensaetze.append([ uhrzeit, kunde, problem, info, Telefonnummer,  wollte_sprechen, Weiterleitung])
                    uhrzeit, kunde, problem, info, Telefonnummer,  wollte_sprechen, Weiterleitung = "", "", "", "", "", "", ""

            if datensaetze:
                self.tag_string = str(time.strftime("%d %m %Y"))
                with open(self.csv_datei_pfad + "/AnruferlistenDings" + self.tag_string + ".csv" , 'w', newline='') as datei:
                    schreiber = csv.writer(datei)
                    schreiber.writerow(["Uhrzeit", "Anrufer", "Problem", "Info", "Telefonnummer", "Wollte Sprechen", "Weiterleitung"])
                    schreiber.writerows(datensaetze)
                    self.zeit_string = time.strftime("%H:%M:%S")
                    self.tag_string = str(time.strftime("%d %m %Y"))
                print("Daten wurden in die CSV-Datei gespeichert.")
                messagebox.showinfo(title="Gespeichert", message="Daten wurden erfolgreich gespeichert.")
            else:
                print("Fehler: Keine vollständigen Informationen wurden in der Textdatei gefunden.")
                messagebox.showerror(title="Fehler", message="Das ist etwas beim Speichern schiefgelaufen.")

    def ListenDings_speicherort_ändern(self):
        messagebox.showinfo(title="Anleitung", message="Bitte wähle nun den Ort aus in welchem das ListenDings automatisch gespeichert werden soll.")
        self.gewählter_ListenDings_Ort = filedialog.askdirectory()
        self.gewählter_ListenDings_Ort = self.gewählter_ListenDings_Ort + "/"
        print("Der vom Nutzer gewählte Ort für das ListenDings lautet: ", self.gewählter_ListenDings_Ort)
        self.zu_speichernder_Ort_des_ListenDings = {"ListenDings_Speicherort": self.gewählter_ListenDings_Ort}
        try:
            with open(self.Listen_Speicherort_Einstellungsdatei, "w+" ) as fn:
                json.dump(self.zu_speichernder_Ort_des_ListenDings, fn)
                messagebox.showinfo(title="Erfolg", message="Der Pfad des Listendings wurde erfolgreich geändert und wird beim nächsten Programmstart aktiv.")
        except Exception as e:
            ei = "Das ändern des ListenDings Pfades hat nicht geklappt, ich hab aber auch keine Ahnung wieso, versuch mal den Text hier zu entziffern: " , e
            messagebox.showerror(title="Fehler", message=ei)

    def ListenDings_speicherort_Netzwerk_ändern(self):
        messagebox.showinfo(title="Anleitung", message="Bitte wähle nun den Ort aus in welchem das ListenDings automatisch im Netzwerk gespeichert werden soll.")
        self.gewählter_ListenDings_Netzwerk_Ort = filedialog.askdirectory()
        self.gewählter_ListenDings_Netzwerk_Ort = self.gewählter_ListenDings_Netzwerk_Ort + "/"
        print("Der vom Nutzer gewählte Ort für das ListenDings Netzwerk lautet: ", self.gewählter_ListenDings_Netzwerk_Ort)
        self.zu_speichernder_Ort_des_ListenDings_Netzwerk = {"ListenDings_Speicherort_Netzwerk": self.gewählter_ListenDings_Netzwerk_Ort}
        try:
            with open(self.Listen_Speicherort_Netzwerk_Einstellungsdatei, "w+" ) as fn:
                json.dump(self.zu_speichernder_Ort_des_ListenDings_Netzwerk, fn)
                messagebox.showinfo(title="Erfolg", message="Der Pfad des Listendings wurde erfolgreich geändert und wird beim nächsten Programmstart aktiv.")
        except Exception as e:
            ei = "Das ändern des ListenDings Pfades hat nicht geklappt, ich hab aber auch keine Ahnung wieso, versuch mal den Text hier zu entziffern: " , e
            messagebox.showerror(title="Fehler", message=ei)

   
    
    def Netzlaufwerk_speichern(self):
        print("Netzlaufwerk_speichern(def)")
        ##try:
            ##if not os.path.exists(self.Listen_Speicherort_Netzwerk_geladen_ordner):
                ##os.mkdir(self.Listen_Speicherort_Netzwerk_geladen_ordner)
                ##print(f"Die Ordner {self.Listen_Speicherort_Netzwerk_geladen_ordner} wurden erstellt.")
        ##except Exception as Ex_sp_n_E1:
          ##  print(f"Beim erstellen der Ordner unter Pfad {self.Listen_Speicherort_Netzwerk_geladen_ordner} ist ein Fehler aufgetreten: {Ex_sp_n_E1}")
            ##messagebox.showerror(title="CiM Fehler", message=f"Beim erstellen der Ordner unter Pfad {self.Listen_Speicherort_Netzwerk_geladen_ordner} ist ein Fehler aufgetreten: {Ex_sp_n_E1}")
        if self.Listen_Speicherort_Netzwerk_geladen:
            with open(self.Liste_mit_datum, 'r') as text_datei:
                daten = text_datei.read()
            zeilen = daten.strip().split('\n')
            datensaetze = []
            uhrzeit, kunde, problem, info, Telefonnummer, wollte_sprechen, Weiterleitung = "", "", "", "", "", "", ""
            for zeile in zeilen:
                if zeile.startswith("Uhrzeit:"):
                    uhrzeit = zeile.replace("Uhrzeit:", "").strip()
                elif zeile.startswith("Anrufer:"):
                    kunde = zeile.replace("Anrufer:", "").strip()
                elif zeile.startswith("Problem:"):
                    problem = zeile.replace("Problem:", "").strip()
                elif zeile.startswith("Info:"):
                    info = zeile.replace("Info:", "").strip()
                elif zeile.startswith("Telefonnummer:"):
                    Telefonnummer = zeile.replace("Telefonnummer:", "").strip()
                elif zeile.startswith("Jemand bestimmtes sprechen:"):
                    wollte_sprechen = zeile.replace("Jemand bestimmtes sprechen:", "").strip()
                elif zeile.startswith("Weiterleitung:"):
                    Weiterleitung = zeile.replace("Weiterleitung:", "").strip()
                    
                if kunde and problem and info and uhrzeit and Telefonnummer and wollte_sprechen and Weiterleitung:
                    datensaetze.append([ uhrzeit, kunde, problem, info, Telefonnummer,  wollte_sprechen, Weiterleitung])
                    uhrzeit, kunde, problem, info, Telefonnummer,  wollte_sprechen, Weiterleitung = "", "", "", "", "", "", ""

            if datensaetze:
                self.tag_string = str(time.strftime("%d %m %Y"))
                with open(self.Listen_Speicherort_Netzwerk_geladen + self.tag_string + ".csv", 'w', newline='') as datei:
                    schreiber = csv.writer(datei)
                    schreiber.writerow(["Uhrzeit", "Anrufer", "Problem", "Info", "Telefonnummer", "Wollte Sprechen", "Weiterleitung"])
                    schreiber.writerows(datensaetze)
                    self.zeit_string = time.strftime("%H:%M:%S")
                    self.tag_string = str(time.strftime("%d %m %Y"))
                print("Daten wurden in die CSV-Datei gespeichert.")
                messagebox.showinfo(title="Gespeichert", message="Daten wurden erfolgreich im Netzlaufwerkpfad gespeichert.")
            else:
                print("Fehler: Keine vollständigen Informationen wurden in der Textdatei gefunden.")
                messagebox.showerror(title="Fehler", message="Das ist etwas beim Speichern schiefgelaufen.")


    def bye(self):
        print("(ENDE) Das Programm wurde Beendet, auf wiedersehen! :3 ")
        self.Programm_läuft = False
        Listendings.Programm_läuft = False
        self.Uhr_läuft = False
        self.thread_uhr.cancel()
        ##self.Thread_Kunderuftan.cancel()
        ##self.thread_webserver.cancel()
        zeit_string = time.strftime("%H:%M:%S")
        tag_string = str(time.strftime("%d %m %Y"))
        print(zeit_string , tag_string)
        try:
            with open(self.Listen_Speicherort_Netzwerk_Einstellungsdatei , "r") as Liste_Speicherort_Netzwerk_data:
                Listen_Speicherort_Netzwerk = json.load(Liste_Speicherort_Netzwerk_data)
                Listen_Speicherort_Netzwerk_geladen = (Listen_Speicherort_Netzwerk["ListenDings_Speicherort_Netzwerk"])
        except PermissionError:
                messagebox.showerror(title="Listendings Speicherort", message="Es Fehlt für diesen Ordner die nötige Berechtigung, Der Gespeicherte Netzwerkpfad konnte nicht aufgerufen werden.")
        except Exception as e:
            ex = "Irgendwas ist passiert: ", e
            messagebox.showerror(title="Listendings Speicherort", message=ex)
        print("ende des Programms, fange nun an zu speichern")
        #try:
        try:
            auto_speichern = "1"
            with open(self.Auto_speichern_Einstellungsdatei, "r") as aSp:
                dings_aSp = aSp.read()
                auto_speichern = dings_aSp
        except:
            auto_speichern = "0"

        if auto_speichern == "1":
            self.csv_datei_pfad = Listen_Speicherort_Netzwerk_geladen
            if self.csv_datei_pfad:
                try:
                    with open(self.Liste_mit_datum, 'r') as text_datei:
                        daten = text_datei.read()
                except FileNotFoundError:
                    print("Die Liste war leer, beende nun ohne zu speichern.")
                    print("======================================")
                    sys.exit()
                zeilen = daten.strip().split('\n')
                datensaetze = []
                uhrzeit, kunde, problem, info, Telefonnummer, wollte_sprechen, Weiterleitung = "", "", "", "", "", "", ""
                for zeile in zeilen:
                    if zeile.startswith("Uhrzeit:"):
                        uhrzeit = zeile.replace("Uhrzeit:", "").strip()
                    elif zeile.startswith("Anrufer:"):
                        kunde = zeile.replace("Anrufer:", "").strip()
                    elif zeile.startswith("Problem:"):
                        problem = zeile.replace("Problem:", "").strip()
                    elif zeile.startswith("Info:"):
                        info = zeile.replace("Info:", "").strip()
                    elif zeile.startswith("Telefonnummer:"):
                        Telefonnummer = zeile.replace("Telefonnummer:", "").strip()
                    elif zeile.startswith("Jemand bestimmtes sprechen:"):
                        wollte_sprechen = zeile.replace("Jemand bestimmtes sprechen:", "").strip()
                    elif zeile.startswith("Weiterleitung:"):
                        Weiterleitung = zeile.replace("Weiterleitung:", "").strip()
                        
                    if kunde and problem and info and uhrzeit and Telefonnummer and wollte_sprechen and Weiterleitung:
                        datensaetze.append([ uhrzeit, kunde, problem, info, Telefonnummer,  wollte_sprechen, Weiterleitung])
                        uhrzeit, kunde, problem, info, Telefonnummer,  wollte_sprechen, Weiterleitung = "", "", "", "", "", "", ""

                if datensaetze:
                    self.tag_string = str(time.strftime("%d %m %Y"))
                    with open(self.csv_datei_pfad + "/AnruferlistenDings" + self.tag_string + ".csv" , 'w', newline='') as datei:
                        schreiber = csv.writer(datei)
                        schreiber.writerow(["Uhrzeit", "Anrufer", "Problem", "Info", "Telefonnummer", "Wollte Sprechen", "Weiterleitung"])
                        schreiber.writerows(datensaetze)
                        self.zeit_string = time.strftime("%H:%M:%S")
                        self.tag_string = str(time.strftime("%d %m %Y"))
                    print("Daten wurden in die CSV-Datei gespeichert.")
                    print(f"Dateien wurden unter {self.csv_datei_pfad} gespeichert.")
                    messagebox.showinfo(title="Gespeichert", message="Daten wurden erfolgreich im Netzlaufwerkpfad gespeichert.")
                else:
                    print("Fehler: Keine vollständigen Informationen wurden in der Textdatei gefunden.")
                    messagebox.showerror(title="Fehler", message="Das ist etwas beim Speichern im Netzlaufwerkpfad schiefgelaufen. (vielleicht keine Datensätze?)")
            else:
                print("die var zum auto_speichern lag bei was anderem als 1")
        print("======================================")
        sys.exit()


if __name__ == "__main__":
    root = tk.CTk()
    width = 1444
    height = 520
    def mittig_fenster(root, width, height):
        fenster_breite = root.winfo_screenwidth()
        fenster_höhe = root.winfo_screenheight()
        x = (fenster_breite - width) // 2
        y = (fenster_höhe - height) // 2

        # Leg die Position des Fensters fest
        root.geometry(f"{width}x{height}+{x}+{y}")
    mittig_fenster(root, width, height)
    Listendings = Listendings(root)
    root.mainloop()