try:
    import sys
    from tkinter import ttk
    import tkinter as Atk
    from tkinter import messagebox
    from tkinter import filedialog
    from tkinter import simpledialog
    from tkinter import Menu
    import webbrowser
    import time
    import os
    import customtkinter as tk
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
    from email.mime.base import MIMEBase
    from email import encoders
    from tkinterdnd2 import DND_FILES
    from PIL import Image
    #from collections import defaultdict
    #from nltk.corpus import wordnet
    #import re
    #import matplotlib.pyplot as plt
    import pyperclip
    import numpy as np
    from reportlab.lib.pagesizes import letter
    from reportlab.pdfgen import canvas
    #import shutil
    #import fitz  # Das ist dieses PyMuPDF für die Checklisten, bitte frag mich nicht wie man auf so einen Namen kommt (ich weiß, meine Namen sind auch nicht besser *Hust* M.U.L.M *Hust* )
except Exception as E:
    print(f"(FATAL) Fehler beim laden der Bibliotheken, Fehlermeldung: {E}")
    try:
        messagebox.showerror("Kritischer Fehler",f"(FATAL) Fehler beim laden der Bibliotheken, Fehlermeldung: {E}")
        antw = messagebox.askyesno(title="CiM Paket Manager", message="Soll ich mal schauen ob ich die fehlenden Pakete installieren kann?")
        if antw:
            if antw == True:
                print("ich versuche nun die fehlenden Pakete zu installieren...")
                try:
                    command= "pip install -r requirements.txt"
                    if sys.platform == "win32":
                        # Windows
                        subprocess.run(['cmd.exe', '/c', command], check=True)
                    elif sys.platform == "darwin":
                        # macOS
                        subprocess.run(['open', '-a', 'Terminal', '-n', '--args', command], check=True)
                    else:
                        print("Unbekanntes Betriebssystem. Dieses Programm unterstützt nur Windows und macOS.")
                        sys.exit()
                    
                    print("Befehl erfolgreich ausgeführt.")
                
                except subprocess.CalledProcessError as e:
                    print(f"Fehler bei der Ausführung des Befehls: {e}")
                print("und weils so toll war das ganze nochmal in Python3.12 um ganz sicher zu gehen!")
                try:
                    command= "pip3.12 install -r requirements.txt"
                    if sys.platform == "win32":
                        # Windows
                        subprocess.run(['cmd.exe', '/c', command], check=True)
                    elif sys.platform == "darwin":
                        # macOS
                        subprocess.run(['open', '-a', 'Terminal', '-n', '--args', command], check=True)
                    else:
                        print("Unbekanntes Betriebssystem. Dieses Programm unterstützt nur Windows und macOS.")
                        sys.exit()
                    
                    print("Befehl erfolgreich ausgeführt.")
                
                except subprocess.CalledProcessError as e:
                    print(f"Fehler bei der Ausführung des Befehls: {e}")
            elif antw == False:
                print("na denn mach doch dei shais Aleene!")
                sys.exit()
    except:
        sys.exit()
    sys.exit()

class Listendings:
    Programm_läuft = True
    class ChangelogLeer(Exception): # Die Exception die kommt, wenn der Changelog leer ist.
        "[-INFO-] Der Changelog ist leer -"

    class RequestHandler(BaseHTTPRequestHandler):
        def do_GET(self):
            # saite = "<!DOCTYPE html><html lang='de'><head><meta charset='UTF-8'><meta name='viewport' content='width=device-width, initial-scale=1.0'><title>Ganzflächiger Hintergrund</title><style>body {margin: 0;padding: 0;background-color: #40444c;}.content {padding: 20px;color: white;font-family: Arial, sans-serif;}</style></head><body><div class='content'><h1>Meine Seite mit ganzflächigem Hintergrund</h1><p>Hier ist etwas Text auf der Seite.</p></div></body></html>"
            #neue_saite = "<!DOCTYPE html><html lang="de"><head><meta charset="UTF-8"><title>Fenster schließen Beispiel</title><script type="text/javascript">window.onload = function() {window.close();};</script></head><body><p>Das Fenster wird nach dem Laden automatisch geschlossen.</p></body></html>"
            self.send_response(200)
            self.send_header('Content-type', 'text/html')
            self.end_headers()
            parsed_path = urllib.parse.urlparse(self.path)
            print("[- Starface-Modul - HTTP - INFO -] Angeforderter Pfad:", parsed_path.path)
            besserer_pfad = parsed_path.path.replace("/", "")
            print("[- Starface-Modul - HTTP - INFO -] Nummer die angerufen hat/wurde: ", besserer_pfad)
            if besserer_pfad == "b":
                ende_des_anrufs = time.strftime("%H:%M:%S")
                
                try:
                    with open("tmp1.txt", "w+") as tmp:
                            tmp.write(ende_des_anrufs)
                except Exception as e:
                    print(f"Fehler beim Schreiben in tmp1.txt: {e}")
                print("[- Starface-Modul - HTTP - INFO -] Der Anruf war wohl fertig. var: ", besserer_pfad)
            elif besserer_pfad == "a":
                print("[- Starface-Modul - HTTP - INFO -] Der bessere Pfad ist ein a.")
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
            try:
                httpd = HTTPServer(server_address, Listendings.RequestHandler)
            except Exception as exhttp:
                print(f"[- Starface-Modul - HTTP - ERR -] {exhttp}")
                return
            try:
                while Listendings.Programm_läuft == True:
                    print(f'[- Starface-Modul - HTTP - INFO -] Ich horche mal auf Port {port}...') 
                    httpd.handle_request()
                    if Listendings.Programm_läuft == False: # wenn diese funktion hier jemals funktionieren würde, könnten hier auch Fehler erscheinen.
                        httpd.shutdown()
                        httpd.server_close()
                        print(f'[- Starface-Modul - HTTP - INFO -] Server auf Port {port} gestoppt.')
                        sys.exit()
            except KeyboardInterrupt:
                httpd.server_close()
                httpd.shutdown()
                print(f'[- Starface-Modul - HTTP - INFO -] Server auf Port {port} gestoppt.')

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
                    pass
        def write(self, message):
            try:
                self.terminal.write(message)
            except:
                pass
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
        self.Programm_Name = "M.U.L.M" # -> sowas nennt man übrigens ein Apronym, ist einem Akronym sehr ähnlich aber nicht gleich
        self.Programm_Name_lang = "Multifunktionaler Unternehmens-Logbuch-Manager"
        self.Version = "Beta 1.0.6 (1)"
        print(f"[-VERSION-] {self.Version}")
        self.Zeit = "Die Zeit ist eine Illusion."
        master.title(self.Programm_Name + " " + self.Version + "                                                                          " + self.Zeit)
        root.configure(resizeable=False)
        self.Programm_läuft = True
        self.Uhr_läuft = True
        root.protocol("WM_DELETE_WINDOW", self.bye)
        self.Listen_Speicherort_Netzwerk_geladen = None
        self.Zeit_text = None
        self.Uhrzeit_anruf_start = None
        self.letzter_eintrag_text = None
        self.Pause = True
        self.Menü_da = False
        self.beb = "0"
        self.Starface_Modul = "0"
        self.Auto_speichern_Einstellung = "0"
        self.Autospeichern_tkvar = "0"
        self.Uhrzeit_anruf_ende = None
        self.zeile_zahl = 0
        self.Anzahl_der_Ergebnisse = 0
        self.tag_string = str(time.strftime("%d %m %Y"))
        self.Benutzerordner = os.path.expanduser('~')
        self.Asset_ordner = os.path.join(self.Benutzerordner, 'CiM', 'Assets')
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
        self.Weiterleitungs_ordner_datei = os.path.join(self.Einstellungen_ordner, "Weiterleitung.txt")
        self.TASKS_FILE = 'tasks.json'
        self.Asset_ordner_beb_pfad = os.path.join(self.Asset_ordner, 'Bilder', 'Bearbeiten.png')
        self.Asset_ordner_dur_pfad = os.path.join(self.Asset_ordner, 'Bilder', 'Durchsuchen.png') 
        self.Asset_ordner_spr_pfad = os.path.join(self.Asset_ordner, 'Bilder', 'Speichern.png')
        self.Asset_ordner_menu_pfad = os.path.join(self.Asset_ordner, 'Bilder', 'Menü.png')
        self.Asset_ordner_tickt_pfad = os.path.join(self.Asset_ordner, 'Bilder', 'Ticket.png')
        self.Asset_ordner_Kal_pfad = os.path.join(self.Asset_ordner, 'Bilder', 'Kalender.png')
        self.Asset_ordner_kunds_pfad = os.path.join(self.Asset_ordner, 'Bilder', 'Kunde_suchen.png')
        self.Asset_ordner_dlist_pfad = os.path.join(self.Asset_ordner, 'Bilder', 'Dings_Liste.png')
        self.Asset_ordner_dings_pfad = os.path.join(self.Asset_ordner, 'Bilder', 'Dings.png')
        self.Asset_ordner_kop_pfad = os.path.join(self.Asset_ordner, 'Bilder', 'Kopieren.png')
        self.Asset_ordner_schnelln_pfad = os.path.join(self.Asset_ordner, 'Bilder', 'Schnellnotiz.png')
        self.Asset_ordner_durch_zu_pfad = os.path.join(self.Asset_ordner, 'Bilder', 'Durchsuchen_zu.png')
        self.Asset_totdo_pfad = os.path.join(self.Asset_ordner, 'Bilder', 'totdo.png')
        self.Checklisten_Ordner = os.path.join(self.Db_Ordner_pfad, 'Checklisten')
        self.Checklisten_Speicherort_Datei = os.path.join(self.Checklisten_Ordner, 'Checkliste.pdf')
        self.Checklisten_Option_1 = "Test Checkliste 1"
        self.Checklisten_Option_2 = "Test Checkliste 2"
        self.Checklisten_Option_3 = "Test Checkliste 3"
#            _ .-') _             .-') _                   
#           ( (  OO) )           ( OO ) )                  
#           \     .'_  .---.,--./ ,--,'   ,--.   .-----.  
#           ,`'--..._)/_   ||   \ |  |\  /  .'  / ,-.   \ 
#           |  |  \  ' |   ||    \|  | ).  / -. '-'  |  | 
#           |  |   ' | |   ||  .     |/ | .-.  '   .'  /  
#           |  |   / : |   ||  |\    |  ' \  |  |.'  /__  
#           |  '--'  / |   ||  | \   |  \  `'  /|       | 
#           `-------'  `---'`--'  `--'   `----' `-------'  <-2023 - 2024->
        
        try: ## das hier sind die Bilder
            self.Bearbeiten_Bild = tk.CTkImage(Image.open(self.Asset_ordner_beb_pfad))
            self.Durchsuchen_Bild = tk.CTkImage(Image.open(self.Asset_ordner_dur_pfad))
            self.Speichern_Bild = tk.CTkImage(Image.open(self.Asset_ordner_spr_pfad))
            self.Menü_Bild = tk.CTkImage(Image.open(self.Asset_ordner_menu_pfad))
            self.Ticket_Bild = tk.CTkImage(Image.open(self.Asset_ordner_tickt_pfad))
            self.Kalender_Bild = tk.CTkImage(Image.open(self.Asset_ordner_Kal_pfad ))
            self.Kunde_suchen_Bild = tk.CTkImage(Image.open(self.Asset_ordner_kunds_pfad))
            self.Dings_Liste_Bild = tk.CTkImage(Image.open(self.Asset_ordner_dlist_pfad))
            self.Dings_Bild = tk.CTkImage(Image.open(self.Asset_ordner_dings_pfad))
            self.Kopieren_Bild = tk.CTkImage(Image.open(self.Asset_ordner_kop_pfad))
            self.Schnellnotiz_Bild = tk.CTkImage(Image.open(self.Asset_ordner_schnelln_pfad))
            self.Durchsuchen_Bild_zu = tk.CTkImage(Image.open(self.Asset_ordner_durch_zu_pfad))
            self.totdo_Bild = tk.CTkImage(Image.open(self.Asset_totdo_pfad))
        except Exception as alk:
            messagebox.showinfo(self.Programm_Name, f"Beim laden der Bild Assets ist ein Fehler aufgetreten: {alk}")
        
        self.Monat = time.strftime("%m")
        self.Thread_Kunderuftan = threading.Timer(2, self.Kunde_ruft_an)
        self.thread_uhr = threading.Timer(1, self.Uhr)
        self.thread_webserver = Listendings.WebServerThread()
        self.thread_webserver.daemon = True
        self.thread_uhr.daemon = True
        self.Thread_Kunderuftan.daemon = True
        self.thread_uhr.start()
        self.Thread_Kunderuftan.start()
        self.smtp_server_anmeldung_thread = threading.Timer(5, self.SMTP_Anmeldung)
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
        self.Ja_UI_Farbe = "burlywood"
        self.das_hübsche_grau = "LightSlateGray"
        self.helle_farbe_für_knopfe = "LightSkyBlue"
    #### Farben Ende ####

        root.configure(fg_color=self.Hintergrund_farbe)
        root.resizable(False, False)
        self.Weiterleitung_an = ""
        self.wollte_sprechen = ""
        self.Starface_Farbe = "#4d4d4d"
        self.Starface_Farbe_Neu = "#293136"#-> Das hier ist die Dunklere Version und das hier
        self.Ort_wo_gesucht_wird = ""
        self.sender_email = None
        self.empfänger_email = ""
        self.smtp_server = ""
        self.pw_email = None
        self.einz = "1. Kontakt"
        self.zwee = "2. Kontakt"
        self.dree = "3. Kontakt"
        self.vir = "4. Kontakt"
        self.Listen_Speicherort_Netzwerk_geladen_anders = "Netzwerkspeicherort: "
        self.Listen_Speicherort_geladen_anders = "Lokaler Speicherpfad: "

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
        self.smtp_login_erfolgreich = False
        nachricht_f_e = None
        self.Mail_Anhang = None
        self.task = None
        self.Todo_offen = False
        self.Weiterleitungen = None
        self.Kontakte_aus_json_gel = None
        self.pfad_der_suche = None
        self.Suchwort = None
        self.kopie_der_mail_erhalten = True
        self.Windows = False # denkt dran dafür noch eine richtige erkenung zu schreiben!!!
        self.Einf_aktiv = True
        
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
                err1 = "[-ERR-] Es ist ein Fehler beim setzen des Icons aufgetreten. Fehlerlode: ", err
                messagebox.showinfo(message=err1)
                print("icon gibt heute nicht.")
        
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
            with open(self.Weiterleitungs_ordner_datei, "r") as einst_gel_autsp:
                self.Auto_speichern_Einstellungsdatei_var = einst_gel_autsp.read()
                print("[-EINSTELLUNGEN-] Einstellunsgdatei zum Autospeichern geladen. Dateipfad: ", self.Auto_speichern_Einstellungsdatei)
                if self.Auto_speichern_Einstellungsdatei_var == "1":
                    print("[-EINSTELLUNGEN-] Die Autospeichern Var welche aus den Einstellungen zum Programmstart geladen wurde ist: ", self.Auto_speichern_Einstellungsdatei_var)
                else:
                    print("[-EINSTELLUNGEN-] Die Autospeichern Var welche aus den Einstellungen zum Programmstart geladen wurde ist: ", self.Auto_speichern_Einstellungsdatei_var)
                    self.Auto_speichern_Einstellungsdatei_var = "0"
        except Exception as autpsp_err:
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
                    print("[-init-] Der Einstellungsordner scheint nicht zu existieren. Erstelle ihn nun.")
                    os.mkdir(self.Einstellungen_ordner)
                    print("[-INFO-] Der Einstellungsornder wurde erfolgreich erstellt.")
                except Exception as ex_einst:
                    print("[-ERR-] Fehler beim Erstellen des Einstellungsordners. Fehlercode:", ex_einst)
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
                        
            else:
                try:
                    with open(self.Starface_Einstellungsdatei, "r") as SternGesicht_data:
                        self.Starface_Modul = SternGesicht_data.read()
                        if self.Starface_Modul == "1":
                            print("[ INIT - Starface - INFO ] Starface Modul wird aktiviert.")
                            self.thread_webserver.start()
                        else:
                            print("[ INIT - Starface - INFO ] Das Starface Modul ist nicht aktiviert: self.Starface_Modul == ", self.Starface_Modul)
                except Exception as Exp:
                    print("Konnte die Einstellungsdatei nicht öffnen. Fehlercode: ", Exp)
            
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
            print("[ INIT - EINSTELLUNGEN - ERR ]Die Einstellung scheint nicht zu existieren")
        

    #### Die Stars der Stunde ####
        self.kunde_entry = tk.CTkEntry(master,width=600, placeholder_text="Name des Anrufers", fg_color=self.Entry_Farbe, text_color="Black", placeholder_text_color="FloralWhite")
        self.t_nummer = tk.CTkEntry(master, width=250, placeholder_text="Telefonnummer", state="disabled", fg_color=self.Entry_Farbe, text_color="Black", placeholder_text_color="FloralWhite")
        self.problem_entry = tk.CTkEntry(master,width=1200, placeholder_text="Problem", fg_color=self.Entry_Farbe, text_color="Black", placeholder_text_color="FloralWhite")
        self.info_entry = tk.CTkEntry(master,width=1200, placeholder_text="Info", fg_color=self.Entry_Farbe, text_color="Black", placeholder_text_color="FloralWhite")
        self.Anruf_Zeit = tk.CTkLabel(master, text_color="Black", text=f"Kein akiver Anruf             ", bg_color=self.Entry_Farbe)

    #    self.kunde_entry.bind('<FocusIn>', self.einf_f_schnellnotizen_switch)
    #    self.t_nummer.bind('<FocusIn>', self.einf_f_schnellnotizen_switch)
    #    self.problem_entry.bind('<FocusIn>', self.einf_f_schnellnotizen_switch)
    #    self.info_entry.bind('<FocusIn>', self.einf_f_schnellnotizen_switch)
    #    self.Anruf_Zeit.bind('<FocusIn>', self.einf_f_schnellnotizen_switch)
    #### ####
        
        self.senden_button = tk.CTkButton(master, text="Senden", command="")
        self.senden_button.bind('<Button-1>', self.senden)
        root.bind('<Return>', self.senden)
        self.ausgabe_text = tk.CTkTextbox(master, width=1255, height=420, wrap="word", fg_color=self.Hintergrund_farbe_Text_Widget, text_color=self.Textfarbe, border_color=self.Border_Farbe, border_width=2)
        self.ausgabe_text.configure(state='disabled')
        self.kunde_entry.place(x=5,y=5)
        self.problem_entry.place(x=5,y=35)
        self.info_entry.place(x=5,y=65)
        self.t_nummer.place(x=605,y=5)
        self.ausgabe_text.place(x=0,y=100)
        self.Anruf_Zeit.place(x=860,y=5)
        
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
        self.Speichern_Menu.add_command(label="als CSV Speichern", command=self.als_csv_speichern_eigener_ort)
        self.Speichern_Menu.add_command(label="als CSV Speichern unter...", command=self.als_csv_speichern)
        self.Speichern_Menu.add_command(label="als CSV Speichern auf Netzlaufwerk", command=self.Netzlaufwerk_speichern)
        self.Einstellungen.add_command(label="Einen neuen Kontakt hinzufügen...", command=self.zeugs1)
        self.Bearbeiten_Menu.add_command(label="Blacklist erweitern...", command=self.zeugs1_blacklist)
        self.Bearbeiten_Menu.add_command(label="Alle Einträge löschen", command=self.alles_löschen)
        self.Bearbeiten_Menu.add_command(label="JSON Explorer öffnen", command=self.JSON_Explorer_öffnen)
        self.Suchen_Menu.add_command(label="Ergebnisse von gerade eben öffnen...", command=self.aufmachen_results_vor)
        self.menudings.add_command(label="Checklisten (Demo)...", command=self.Checkboxen_dingsen)
        self.menudings.add_command(label="Email Baukasten (Demo)...", command=self.email_baukasten)
        #self.Suchen_Menu.add_command(label="Sehr genaue Suche nutzen (Suche 3.0)(Beta)", command=self.frage_nach_string_suche3)
        
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

    ############################ GUI init ######################
    ############################ GUI init ######################
    ############################ GUI init ######################
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
        self.Ereignislog_insert(nachricht_f_e="[-Ereignislog-]")

        # jetzt kommen die ganzen stat Sachen des Pause Menüs.
        # jetzt kommen die ganzen stat Sachen des Pause Menüs.
        # jetzt kommen die ganzen stat Sachen des Pause Menüs.
        # jetzt kommen die ganzen stat Sachen des Pause Menüs.
        # jetzt kommen die ganzen stat Sachen des Pause Menüs.
        # jetzt kommen die ganzen stat Sachen des Pause Menüs.

        #self.Suche_knopp = tk.CTkButton(self.Pause_menu, text="Nach alten Eintrag Suchen...", command=self.Suche_alte_Einträge, fg_color="White", border_color="Black", border_width=1, text_color="Black", hover_color="pink")
        
        self.Zhe_Clock = tk.CTkLabel(self.Pause_menu, text=self.Zeit)
        self.Zhe_Clock.place(x=10,y=10)

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

        self.Einstellung_Design_auswahl = tk.CTkOptionMenu(self.Pause_menu, values=["hell", "dunkel", "System"], command=auswahl_design_gedingst)
        self.Einstellung_Design_L = tk.CTkLabel(self.Pause_menu, text="Design Einstellung:")
        
        self.kalender_menü = tk.CTkFrame(master, width=1250, height=520, fg_color="White", border_color="Black", border_width=2)
        self.Liste_mit_zeugs = tk.CTkScrollableFrame(self.kalender_menü, width=500, height=420, bg_color="Green")
        
        ################################ MENU FRAMES ENDE ################################
        ################################ MENU FRAMES ENDE ################################
        ################################ MENU FRAMES ENDE ################################
        ################################ MENU FRAMES ENDE ################################
        
        self.Einstellungsseite_Knopp = tk.CTkButton(root, text="Einstellungen", command=self.Einstellungen_öffnen, fg_color="white", border_color="Black", border_width=1, text_color="Black", hover_color="DarkSlateGray1", image=self.Dings_Bild)
        self.Einstellungsseite_Knopp.place(x=1260,y=420)
        self.Ticket_erstellen_Knopp = tk.CTkButton(root, text="Ticket erstellen", command=self.Ticket_erstellen, fg_color="White", border_color="Black", border_width=1, text_color="Black", hover_color="pink", image=self.Ticket_Bild)
        self.Ticket_erstellen_Knopp.place(x=1260,y=450)
        self.Eintrag_raus_kopieren_knopp = tk.CTkButton(root, text="Letztes kopieren", command=self.Eintrag_raus_kopieren, fg_color="White", border_color="Black", border_width=1, text_color="Black", hover_color="pink", image=self.Kopieren_Bild)
        self.Eintrag_raus_kopieren_knopp.place(x=1260,y=390)
        self.Notizen_knopp = tk.CTkButton(root, text="Schnellnotiz", fg_color="White", border_color="Black", border_width=1, text_color="Black", hover_color="DarkSlateGray1", image=self.Schnellnotiz_Bild)
        self.Notizen_knopp.place(x=1260,y=360)
        self.Notizen_knopp.bind('<Button-1>', self.schnellnotizen_öffnen)

        self.Berichtsheft_knopp = tk.CTkButton(self.Pause_menu, text="Berichtsheft öffnen", command=self.Berichtsheft_aufmachen, fg_color="White", border_color="Black", border_width=1, text_color="Black", hover_color="pink")
        self.Einstellungen_Frame = tk.CTkFrame(root, width=600, height=380, border_color="Pink", border_width=3, fg_color="transparent")
        self.tabview = tk.CTkTabview(self.Einstellungen_Frame, width=600, height=380, fg_color=self.Entry_Farbe, segmented_button_fg_color=self.Hintergrund_farbe_Text_Widget, segmented_button_selected_hover_color=self.dunkle_ui_farbe, segmented_button_unselected_hover_color=self.dunkle_ui_farbe, segmented_button_selected_color=self.helle_ui_farbe, text_color="Black", segmented_button_unselected_color=self.Ja_UI_Farbe)
        self.tabview.add("Starface Modul")
        self.tabview.add("Adressbuch")
        self.tabview.add("Speichern")
        self.tabview.add("SMTP")
        self.tabview.add("Speicherorte")
        self.tabview.add("Weiterleitungen")
        self.gel_Email_Empfänger_L = tk.CTkLabel(self.tabview.tab("SMTP"), text="Ziel Email Adresse", text_color="Black", bg_color=self.Entry_Farbe, corner_radius=3)
        self.gel_Email_Sender_L = tk.CTkLabel(self.tabview.tab("SMTP"), text="Absende Email Adresse", text_color="Black", bg_color=self.Entry_Farbe, corner_radius=3)
        self.gel_Email_Absender_Passwort_L = tk.CTkLabel(self.tabview.tab("SMTP"), text="Absende Mail Kennwort", text_color="Black", bg_color=self.Entry_Farbe, corner_radius=3)
        self.gel_SMTP_Server_L = tk.CTkLabel(self.tabview.tab("SMTP"), text="SMTP Server", text_color="Black", bg_color=self.Entry_Farbe, corner_radius=3)
        self.gel_Email_Empfänger_E = tk.CTkEntry(self.tabview.tab("SMTP"), placeholder_text="Empfänger Adresse", width=300)
        self.gel_Email_Sender_E = tk.CTkEntry(self.tabview.tab("SMTP"), placeholder_text="Sender Email Adresse", width=300)
        self.gel_Email_Absender_Passwort_E = tk.CTkEntry(self.tabview.tab("SMTP"), placeholder_text="Passwort der Email Adresse", width=300, show="#")
        self.gel_SMTP_Server_E = tk.CTkEntry(self.tabview.tab("SMTP"), placeholder_text="IPv4 oder Hostnamen für SMTP Eintragen", width=300)
        self.Mail_Einstellungen_speichern = tk.CTkButton(self.tabview.tab("SMTP"), text="Email Einstellungen speichern", command=self.Email_Einstellungen_speichern, fg_color="White", border_color="Black", border_width=1, text_color="Black", hover_color="DarkSlateGray1")
        self.smtp_login_erfolgreich_l = tk.CTkLabel(self.tabview.tab("SMTP"), text="Anmeldestatus")
        self.SMTP_Server_erneut_anmelden = tk.CTkButton(self.tabview.tab("SMTP"), text="erneut mit SMTP Server verbinden", command=self.SMTP_Anmeldung_Manuell, fg_color="White", border_color="Black", border_width=1, text_color="Black", hover_color="pink")
        
        self.weiterleitungen_l = tk.CTkLabel(self.tabview.tab("Weiterleitungen"), text="Namen für die Weiterleitungen einstellen")
        self.weiterleitungen_einz_e = tk.CTkEntry(self.tabview.tab("Weiterleitungen"), placeholder_text="erstes", width=300)
        self.weiterleitungen_zwei_e = tk.CTkEntry(self.tabview.tab("Weiterleitungen"), placeholder_text="zweites", width=300)
        self.weiterleitungen_drei_e = tk.CTkEntry(self.tabview.tab("Weiterleitungen"), placeholder_text="drittes", width=300)
        self.weiterleitungen_vier_e = tk.CTkEntry(self.tabview.tab("Weiterleitungen"), placeholder_text="erstexs", width=300)
        self.Weiterleitungen_speichern_knopp = tk.CTkButton(self.tabview.tab("Weiterleitungen"), text="Speichern", command=self.weiterleitungen_speichern)
        #self.Speicherort_lokal_ändern_knopp = tk.CTkButton(self.tabview.tab("Speichern"), text="ändern", command=self.ListenDings_speicherort_ändern, fg=self.helle_farbe_für_knopfe, border=self.Border_Farbe)
        #self.Speicherort_lokal_ändern_l = tk.CTkLabel(self.tabview("Speichern"), text="den lokalen Speicherort ändern")
    #### todo gui ####
        self.Todo_aufmachen_main_knopp = tk.CTkButton(root, text="Totdo öffnen", command=self.todo_aufmachen, fg_color="white", border_color="Black", border_width=1, text_color="Black", hover_color="DarkSlateGray1", image=self.totdo_Bild)
        self.Todo_aufmachen_main_knopp.place(x=1260,y=480)
        self.ans_totdo_senden_knopp = tk.CTkButton(root, text="An TotDo senden", command=self.Eintrag_ans_totdo, fg_color="White", border_color="Black", border_width=1, text_color="Black", hover_color="pink", image=self.Menü_Bild)
        self.ans_totdo_senden_knopp.place(x=1260,y=330)
        
        #self.todo_hinzufügen_knopp = tk.CTkButton(self.todo_frame, text="Aufgabe hinzufügen", command=self.todo_hinzufügen)
        self.Adressbuch_anzeigen_frame = tk.CTkFrame(self.tabview.tab("Adressbuch"), width=575, height=300, fg_color=self.Hintergrund_farbe, border_color=self.Ja_UI_Farbe, border_width=1, corner_radius=0)
        self.init_auf_wish()
    #### ende todo gui ####
    ####### ======================== init ende ======================== #######
    ####### ======================== init ende ======================== #######
    ####### ======================== init ende ======================== #######
    ####### ======================== init ende ======================== #######
    ####### ======================== init ende ======================== #######

    def Netzlaufwerk_Einstellung_laden(self):
        try:
            print("[-INFO-] Lade nun das eingestellte Netzlaufwerk")
            with open(self.Listen_Speicherort_Netzwerk_Einstellungsdatei , "r") as Liste_Speicherort_Netzwerk_data:
                self.Listen_Speicherort_Netzwerk = json.load(Liste_Speicherort_Netzwerk_data)
                self.Listen_Speicherort_Netzwerk_geladen = (self.Listen_Speicherort_Netzwerk["ListenDings_Speicherort_Netzwerk"])
                self.Listen_Speicherort_Netzwerk_geladen_ordner = os.path.join(self.Listen_Speicherort_Netzwerk_geladen, self.Jahr, self.Monat)
        except PermissionError:
                messagebox.showerror(title="Listendings Speicherort", message="Es Fehlt für diesen Ordner die nötige Berechtigung, Der Gespeicherte Netzwerkpfad konnte nicht aufgerufen werden.")
        except Exception as e:
            print(f"[-FATAL-] Irgendwas ist bei den Netzwerkeinstellungen passiert: {e}")

    def Theme_Einstellungen_laden(self):
        try:
            print(f"[-INFO-] Ich lade nun die Theme Einstellungen...")
            with open(self.Einstellung_Theme, "r") as E_theme_gel:
                self.Einstellungen_Theme_Inhalt = E_theme_gel.read()
                if self.Einstellungen_Theme_Inhalt == "dunkel":
                    tk.set_default_color_theme("Designs/dunkel.json")
                elif self.Einstellungen_Theme_Inhalt == "hell":
                    tk.set_default_color_theme("Designs/hell.json")
                elif self.Design_Einstellung == "System":
                    print("[-ERR-] Es wird versucht die System Design Einstellung zu laden.")
                    tk.set_appearance_mode("System")
                else:
                    print("[-ERR-] Es gab einen Fehler bei der geladenen Designeinstellung, es wird nun der Systemstandard geladen...")
                    tk.set_appearance_mode("System")
                    print("[-INFO-] Die System Design Einstellung wurde geladen.")
        except Exception as exko:
            print(f"[-ERR-] Es ist ein Fehler beim Laden der Theme Einstellungen aufgetreten. Fehlercode: {exko}")

    def Einstellungen_laden(self): # hier sollen zukünftig alle Einstellungen geladen werden
        print("[-Einstellungen_laden - INFO -] Lade nun alle Einstellungen")
        self.Netzlaufwerk_Einstellung_laden()
        self.Theme_Einstellungen_laden()
        print(f"[-EINSTLLUNGEN LADEN-] ich lade nun die Mail Einstellungen")
        try:
            print(f"[-EINSTLLUNGEN LADEN-] ich lade nun die EMail Sender Einstellungen")
            with open(self.Einstellung_Email_Sender_Adresse, "r") as Email_S_Datei:
                self.sender_email = Email_S_Datei.read()
                print(f"[-EINSTLLUNGEN LADEN-] Sender Email geladen: {self.sender_email}")
        except Exception as EmailEx3_l:
            print(f"Fehler beim laden der Maileinstellungen: {EmailEx3_l}")
            self.sender_email = "Fehler"
        try:
            print(f"[-EINSTLLUNGEN LADEN-] ich lade nun die EMail Empfänger Einstellungen")
            with open(self.Einstellung_Email_Empfänge_Adresse, "r") as Email_E_Datei:
                self.empfänger_email = Email_E_Datei.read()
                print(f"[-EINSTLLUNGEN LADEN-] Empfänger Adresse geladen: {self.empfänger_email}")
        except Exception as EmailEx3_l:
            print(f"Fehler beim laden der Maileinstellungen: {EmailEx3_l}")
            self.empfänger_email = "Fehler"
        try:
            print(f"[-EINSTLLUNGEN LADEN-] ich lade nun die EMail SMTP Einstellungen")
            with open(self.Einstellung_smtp_server, "r") as SMTP_Server_Datei:
                self.smtp_server = SMTP_Server_Datei.read()
                print("[-EINSTLLUNGEN LADEN-] SMTP Server Adresse geladen.")
        except Exception as EmailEx3_l:
            print(f"Fehler beim laden der Maileinstellungen: {EmailEx3_l}")
            self.smtp_server = "Fehler"
        try:
            print(f"[-EINSTLLUNGEN LADEN-] ich lade nun die EMail Passwörters")
            with open(self.Einstellung_smtp_Passwort, "r") as SMTP_Server_Passwort_Datei:
                self.pw_email = SMTP_Server_Passwort_Datei.read()
                print(f"[-EINSTLLUNGEN LADEN-] Absender Kennwort geladen. {self.pw_email}")
        except Exception as EmailEx3_l:
            print(f"Fehler beim laden der Passwort Maileinstellungen: {EmailEx3_l}")
            self.pw_email = ""
        

    def init_auf_wish(self):
        print("[-init-] init auf wish bestellt...")
        self.Kontakte_aus_json_laden()
        self.weiterleitung_laden()
        self.Einstellungen_laden()
        print("[-init-] Die Wish init is vorbei.")

    def email_baukasten(self):
        print("email_baukasten(def)")

        self.Email_Text_Widget = tk.CTkTextbox(width=200,height=100)

    def einf_f_schnellnotizen_switch(self, event): # Das Dings hier ist relativ obsolete, weil die event binder in der init deaktiviert sind. (ca Zeile: 526, Commit vom 4.9.24)
        print("einf_f_schnellnotizen_switch(def)")
        if self.Einf_aktiv == False:
            if self.Windows == True:  #  Das gegenteil von dem was da oben steht
                self.master.bind('<Control-v>', self.schnellnotizen_öffnen(event))  # Windows/Linux
                self.Einf_aktiv = True
                print("Das bind steht nun wieder")
            else:
                self.master.bind('<Command-v>', self.schnellnotizen_öffnen(event)) # Normal
                self.Einf_aktiv = True
                print("Das bind steht nun wieder")
        else:   ## Das .bind wieder deaktivieren (es wird kein schnellnotizen Fenster mehr geöffnet)
            if self.Windows == True:
                print("Das Bind wurde deaktiviert")
                self.master.unbind('<Control-v>')
                self.Einf_aktiv = False
            else:
                print("Das Bind wurde deaktiviert")
                self.master.unbind('<Command-v>')
                self.Einf_aktiv = False

    def weiterleitungen_speichern(self):
        print("[-INFO-] weiterleitungen_speichern(def)")
        alles = self.weiterleitungen_einz_e.get() + ","+ self.weiterleitungen_zwei_e.get() + ","+ self.weiterleitungen_drei_e.get() + ","+ self.weiterleitungen_vier_e.get() 
        try:
            with open(self.Weiterleitungs_ordner_datei, "w+") as schreiben_weiterl:
                schreiben_weiterl.write(alles)
                schreiben_weiterl.close()
                print("[-INFO-] Die neuen Weiterleitungen wurden gespeichert.")
                self.weiterleitungen_einz_e.delete(0, tk.END)
                self.weiterleitungen_zwei_e.delete(0, tk.END)
                self.weiterleitungen_drei_e.delete(0, tk.END)
                self.weiterleitungen_vier_e.delete(0, tk.END)
            alles = None
        except Exception as Ex1w:
            print(f"[-ERR-] Es gab einen Fehler beim speichern der Weiterleitungen: {Ex1w}")
            alles = None

    def Kontakte_aus_json_laden(self):
        print("[-INFO-] self.Kontakte_aus_JSON_laden(def)")
        self.Benutzerordner = os.path.expanduser('~')
        self.Db_Ordner_pfad = os.path.join(self.Benutzerordner, 'CiM', 'Db')
        self.Json_pfad = os.path.join(self.Db_Ordner_pfad, 'Db.json')
        file_path = self.Json_pfad
        with open(file_path, 'r+') as f:
            self.Kontakte_aus_json_gel = json.load(f)
    
    def weiterleitung_laden(self):
        print("[-INFO-] Weiterleitungenladen(def)")
        try:
            with open(self.Weiterleitungs_ordner_datei, "r" ) as gel_weiterleitung:
                self.Weiterleitungen = gel_weiterleitung.read()
                print(f"[-INFO-] Hier sind die Weiterleitungen vor der Konvertierung: {self.Weiterleitungen}")
                self.Weiterleitungen = self.Weiterleitungen.split(",")
                self.einz, self.zwee, self.dree, self.vir = self.Weiterleitungen
                print(f"[-INFO-] Hier sind sie nun formatiert: {self.einz, self.zwee, self.dree, self.vir}")
                print("[-INFO-] Weiterleitungen wurden erfolgreich geladen.")
        except Exception as Exwtl:
            print(f"[-ERR-] Beim laden der Weiterleitungen ist ein Fehler aufgetreten. Fehlermeldung: {Exwtl}")
            return
        def auswahl_gedingst(choice):
            print("WAI !")
            if choice == f"An {self.einz} weitergeleitet":
                self.Weiterleitung_an = f"An {self.einz} weitergeleitet"
            elif choice == f"An {self.zwee} weitergeleitet":
                self.Weiterleitung_an = f"An {self.zwee} weitergeleitet"
            elif choice == f"An {self.dree} weitergeleitet":
                self.Weiterleitung_an = f"An {self.dree} weitergeleitet"
            elif choice == f"An {self.vir} weitergeleitet":
                self.Weiterleitung_an = f"An {self.vir} weitergeleitet"
            elif choice == "Keine Weiterleitung":
                self.Weiterleitung_an = "-"
                
        def auswahl_gedingst_sprechen(choice):
            if choice == f"Mit {self.einz} sprechen":
                self.wollte_sprechen = f"Mit {self.einz} sprechen"
            elif choice == f"Mit {self.zwee} sprechen":
                self.wollte_sprechen = f"Mit {self.zwee} sprechen"
            elif choice == f"Mit {self.dree} sprechen":
                self.wollte_sprechen = f"Mit {self.dree} sprechen"
            elif choice == f"Mit {self.vir} sprechen":
                self.wollte_sprechen = f"Mit {self.vir} sprechen"
            elif choice == f"Mit Irgendwen sprechen":
                self.wollte_sprechen = "Mit Irgendwen sprechen"
            elif choice == "Keine Weiterleitung":
                self.wollte_sprechen = "-"
       
        try:
            self.optionmenu1.place_forget()
            self.optionmenu.place_forget()
        except:
            pass
        try:
            self.optionmenu1 = tk.CTkOptionMenu(root, values=[f"Mit {self.einz} sprechen", f"Mit {self.zwee} sprechen", f"Mit {self.dree} sprechen", f"Mit {self.vir} sprechen", "Irgendwen sprechen"], command=auswahl_gedingst_sprechen, fg_color="White", text_color="Black", dropdown_hover_color="pink")
            self.optionmenu1.set("Mit Wem sprechen?")
            self.optionmenu1.place(x=1260,y=190)
            self.optionmenu = tk.CTkOptionMenu(root, values=[f"An {self.einz} weitergeleitet", f"An {self.zwee} weitergeleitet", f"An {self.dree} weitergeleitet", f"An {self.vir} weitergeleitet", "Keine Weiterleitung"], command=auswahl_gedingst, fg_color="White", text_color="Black", dropdown_hover_color="pink")
            self.optionmenu.set("Keine Weiterleitung")
            self.optionmenu.place(x=1260,y=220)
            print(f"[-WEITERLEITUNG LADEN-] Die Weiterleitungen wurden geladen und wieder platziert.")
        except Exception as ellkk:
            print(f"[-ERR-] Konnte die Weiterleitungen nicht platzieren: {ellkk}")

    def changelog_aufmachen(self):
        print("[-INFO-] changelog_aufmachen(def)")
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
            print("[ CHANGELOG - ERR ] Konnte das changelogfenster nicht zentrieren.")
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
            self.Textfeld_changelog.insert(tk.END,"- Changelog existiert nicht oder konnte nicht gefunden werden -")
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

    def Ereignislog_insert(self, nachricht_f_e): # wenn ichs richtig gemacht hab, wird mir das mega viel Zeit ersparen.
        if nachricht_f_e != None:
            nachricht_f_e_fertsch = nachricht_f_e + "\n"
            self.Ereignislog.insert(tk.END, nachricht_f_e_fertsch)
            self.Ereignislog.see(tk.END)
            return
        return

    #def schnellnotizen_öffnen(self, event):  wie oben geschildert, musste die event var mit raus weil ich den mist deaktiviert hab
    def schnellnotizen_öffnen(self, event):
        print("[-INFO-] schnellnotizen_öffnen(def)")
        self.schnellnotizen_Fenster = tk.CTkToplevel(root)
        self.schnellnotizen_Fenster.title("Schnellnotiz")
        self.schnellnotizen_Fenster.configure(fg_color="White")
        self.Textfeld_Schnellnotizen = tk.CTkTextbox(self.schnellnotizen_Fenster, width=420, height=420, text_color="Black", fg_color="azure", wrap="word")
        height = 420
        width = 420

        try:
            x = root.winfo_x() + root.winfo_width()//2 - self.schnellnotizen_Fenster.winfo_width()//2
            y = root.winfo_y() + root.winfo_height()//2 - self.schnellnotizen_Fenster.winfo_height()//2
            self.schnellnotizen_Fenster.geometry(f"{width}x{height}+{x}+{y}")
        except:
            print("[-ERR-] Konnte das Schnellnotizfenster nicht zentrieren.")
            self.schnellnotizen_Fenster.geometry(f"{width}x{height}+{x}+{y}")
        self.schnellnotizen_Fenster.resizable(True,True)
        self.Textfeld_Schnellnotizen.pack(expand=True, fill="both")
        
    
    def JSON_Explorer_öffnen(self):
        print("[-INFO-] JSON_Explorer_öffnen(def)")
        try:
            exec(open('json_explorer.py').read())
        except Exception as JSON_E:
            messagebox.showerror(title="CiM Fehler", message=f"Konnte die Datei json_explorer.py nicht finden, stelle sicher, dass sie sich im Programmverzeichnis befindet! Fehlercode: {JSON_E}")

    def Einstellungen_öffnen(self):
        print("[-INFO-] Einstellungen_öffnen (def)")
        self.Einstellungsseite_Knopp.configure(command=self.Einstellungen_schließen, text="Einstellungen schließen", fg_color=self.aktiviert_farbe, hover_color="Pink")
        self.Einstellungen_Frame.place(x=400,y=120)
        self.tabview.place(x=0, y=0)
        self.Auto_speichern_ändern_knopp = tk.CTkButton(self.tabview.tab("Speichern"), text="Auto Speichern umschalten", command=self.autospeichern_ä_c, hover_color="pink")
        
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

        self.Normaler_Speicherort_change = tk.CTkButton(self.tabview.tab("Speicherorte"), text="ändern", command=self.ListenDings_speicherort_ändern, width=100)
        self.Netzwerk_Speicherort_change = tk.CTkButton(self.tabview.tab("Speicherorte"), text="ändern", command=self.ListenDings_speicherort_Netzwerk_ändern, width=100)

        # Adressbuch
        self.Adressbuch_anzeige_Einstellungen_t = tk.CTkTextbox(self.Adressbuch_anzeigen_frame, width=300, height=200, fg_color=self.Ja_UI_Farbe)
        self.Adressbuch_anzeige_Einstellungen_t.place(x=10,y=10) 
    # Adressbuch ende

        self.Netzlaufwerk_pfad_geladen_Label.place(x=10,y=80)
        self.Pfad_geladen_Label.place(x=10,y=110)
        self.Normaler_Speicherort_change.place(x=470,y=110)
        self.Netzwerk_Speicherort_change.place(x=470,y=80)
        self.Listen_Speicherort_geladen_anders_Entry.place(x=160, y=110)
        self.Listen_Speicherort_Netzwerk_geladen_anders_Entry.place(x=160,y=80)
        try:
            self.Listen_Speicherort_geladen_anders_Entry.delete(0, tk.END)
            self.Listen_Speicherort_Netzwerk_geladen_anders_Entry.delete(0, tk.END)
        except:
            print("Konnte den Inhalt der Entrys für die Pfade nicht löschen")
            self.Ereignislog_insert(nachricht_f_e="Konnte den Inhalt der Entrys für die Pfade nicht löschen")
        try:
            self.Listen_Speicherort_geladen_anders_Entry.insert(0, self.Listen_Speicherort_geladen)
            self.Listen_Speicherort_Netzwerk_geladen_anders_Entry.insert(0, self.Listen_Speicherort_Netzwerk_geladen)
        except:
            print("Konnte die geladenen Speicherorte nicht in die Entrys übernehmen.")
            self.Ereignislog_insert(nachricht_f_e="Konnte den Inhalt der Entrys für die Pfade nicht löschen")
        def rückruf_speichern():
            print(f"self.mitspeichern.get() = : {self.mitspeichern.get()}")
            self.Kontakt_soll_gleich_mitgespeichert_werden = True

        self.mitspeichern = tk.StringVar(value="on")
        try:
            self.abhgehakt_hinzufügen_box.place_forget()
        except:
            pass
        self.abhgehakt_hinzufügen_box = tk.CTkCheckBox(self.tabview.tab("Speichern"), text_color="Black",text="Namen und Telefonnummer in KtDb speichern?", command=rückruf_speichern, variable=self.mitspeichern, onvalue="on", offvalue="off")
        self.abhgehakt_hinzufügen_box.place(x=20,y=20)
        self.Auto_speichern_ändern_knopp.place(x=20,y=60)

        self.gel_Email_Empfänger_L.place(x=10,y=150)
        self.gel_Email_Sender_L.place(x=10,y=180)
        self.gel_Email_Absender_Passwort_L.place(x=10,y=210)
        self.gel_SMTP_Server_L.place(x=10,y=240)
        self.gel_Email_Empfänger_E.place(x=160,y=150)
        self.gel_Email_Sender_E.place(x=160,y=180)
        self.gel_Email_Absender_Passwort_E.place(x=160,y=210)
        self.gel_SMTP_Server_E.place(x=160,y=240)
        self.Mail_Einstellungen_speichern.place(x=10,y=280)
        self.SMTP_Server_erneut_anmelden.place(x=250,y=280)
        self.weiterleitungen_einz_e.place(x=10,y=100)
        self.weiterleitungen_zwei_e.place(x=10,y=130)
        self.weiterleitungen_drei_e.place(x=10,y=160)
        self.weiterleitungen_vier_e.place(x=10,y=190)
        self.Weiterleitungen_speichern_knopp.place(x=10,y=240)
        self.Adressbuch_anzeigen_frame.place(x=5,y=20)

        try:
            if self.smtp_login_erfolgreich == True:
                self.smtp_login_erfolgreich_l.configure(text="Anmeldung am SMTP Server war erfolgreich.", text_color="SeaGreen1")
                self.smtp_login_erfolgreich_l.place(x=20,y=20)
            elif self.smtp_login_erfolgreich == False:
                self.smtp_login_erfolgreich_l.configure(text="Anmeldung am SMTP fehlgeschlagen.", text_color="Red")
                self.smtp_login_erfolgreich_l.place(x=20,y=20)
        except Exception as Exc21:
            print(f"Fehler bei der entscheidung ob die Anmeldung bei Server erfolgreich war, wie auch immer das jetzt nun wieder schiefgehen konnte... Fehlercode: {Exc21}")
        try:
            try:
                self.gel_Email_Empfänger_E.delete(0, tk.END)
                self.gel_Email_Sender_E.delete(0, tk.END)
                self.gel_Email_Absender_Passwort_E.delete(0, tk.END)
                self.gel_SMTP_Server_E.delete(0, tk.END)
                self.gel_Email_Empfänger_E.delete(0, tk.END)
            except:
                self.Ereignislog_insert(nachricht_f_e="konnte die Entrys nicht leeren")
                print("konnte die entrys nicht leeren")
            self.gel_Email_Empfänger_E.insert(0, self.empfänger_email)
            self.gel_Email_Sender_E.insert(0, self.sender_email)
            self.gel_Email_Absender_Passwort_E.insert(0, self.pw_email)
            self.gel_SMTP_Server_E.insert(0, self.smtp_server)
            print("Alles was mit den Email Einstellungen zu tun hat wurde erfolgreich gelade")
            self.Ereignislog_insert(nachricht_f_e="Alles was mit den Email Einstellungen zu tun hat wurde erfolgreich geladen")
        except Exception as ExGelEm1:
            print("Fehler beim einfügen der Email Daten in die Entrys. Fehlercode: ", ExGelEm1)
        
        try:
            try:
                self.weiterleitungen_einz_e.delete(0, tk.END)
                self.weiterleitungen_zwei_e.delete(0, tk.END)
                self.weiterleitungen_drei_e.delete(0, tk.END)
                self.weiterleitungen_vier_e.delete(0, tk.END)
            except:
                print("")
            self.weiterleitungen_einz_e.insert(0, self.einz)
            self.weiterleitungen_zwei_e.insert(0, self.zwee)
            self.weiterleitungen_drei_e.insert(0, self.dree)
            self.weiterleitungen_vier_e.insert(0, self.vir)
        except:
            print(f"[-EINSTELLUNGEN - ERR -]")
            pass

    def Einstellungen_schließen(self):
        print("[-INFO-] Einstellungen_schließen(def)")
        self.Einstellungsseite_Knopp.configure(command=self.Einstellungen_öffnen, text="Einstellungen", fg_color=self.deaktiviert_farbe, hover_color="Pink")
        self.Starface_Modul_Einstellung_Knopp.pack_forget()
        self.Einstellungen_Frame.place_forget()
        self.tabview.place_forget()
        

    def Eintrag_raus_kopieren(self): # kopiert den letzten in der Liste stehenden Eintrag in die Zwischenablage.
        print("[-INFO-] Eintrag_raus_kopieren(def)")
        self.geladener_Text = self.ausgabe_text.get("0.0", "end")
        self.einzelner_Eintrag = self.geladener_Text.split("\n\n")
        if self.einzelner_Eintrag:
            print(f"Aufgeteilter Text: {self.einzelner_Eintrag}")
            # Rückwärts durch die Liste gehen, um den letzten passenden Eintrag zu finden
            for eintrag in reversed(self.einzelner_Eintrag):
                if eintrag.startswith("Uhrzeit:") and "Telefonnummer:" in eintrag:
                    self.cim = eintrag
                    kopierter_text = "Hier nun der kopierte Text aus dem M.U.L.M: \n" + eintrag
                    pyperclip.copy(kopierter_text)
                    print(f"Text in der Zwischenablage: {kopierter_text}")
                    self.Ereignislog_insert(nachricht_f_e="- letzte Nachricht kopiert. -")
                    break
            else:
                print("Kein passender Eintrag gefunden")
        else:
            print("Die Liste ist leer")

    def Eintrag_ans_totdo(self):
        self.Eintrag_raus_kopieren()
        try:
            with open(self.Benutzerordner + "/CiM/cim.txt", "w") as cim_s:
                cim_s.write(self.cim)
                cim_s.close()
                self.Ereignislog_insert(nachricht_f_e="[-INFO-] Auftrag ans Totdo übermittelt.-")
        except Exception as exooo:
            print(f"Fehler beim senden ans Totdo. Fehlermeldung: {exooo}")    

    def Ticket_erstellen_mail(self): # naja das halt dann mit dem Mail.to Befehl. // nee hamwa selbst gemacht ez.
        print("[-INFO-] Ticket_erstellen (Email)")
        self.alternative_empfänger_adresse = ""
        self.Betreff_Mail = self.Betreff_Ticket_e.get()
        self.alternative_empfänger_adresse = self.alternative_empfänger_adresse_e.get()
        self.Nachricht_Mail_Inhalt = self.Nachricht_Ticket_e.get("0.0", "end")
        msg = MIMEMultipart()
        msg["From"] = self.sender_email
        if self.alternative_empfänger_adresse == "":
            empf_alle = f"{self.empfänger_email}"
            msg["To"] = empf_alle
            print("[-TICKET ERSTELLEN-] Ticket wird an die hinterlegte Emailadresse versendet...")
            self.Ereignislog_insert(nachricht_f_e="-[-TICKET ERSTELLEN-] Ticket wird an die hinterlegte Emailadresse versendet...-")
        elif self.alternative_empfänger_adresse != "":
            msg["To"] = self.alternative_empfänger_adresse
            print("[-TICKET ERSTELLEN-] Ticket wird an alternative Emailadresse versendet...")
            self.Ereignislog_insert(nachricht_f_e="[-TICKET ERSTELLEN-] Ticket wird an alternative Emailadresse versendet...")
        msg["Subject"] = self.Betreff_Mail
        msg.attach(MIMEText(self.Nachricht_Mail_Inhalt, "plain"))

        ##### Anhänge an die Mail packen ####
        if self.Mail_Anhang:
            try:
                part = MIMEBase("application", "octet-stream")
                with open(self.Mail_Anhang, "rb") as attachment:
                    part.set_payload(attachment.read())
                encoders.encode_base64(part)
                filename = self.Mail_Anhang.split('/')[-1]
                part.add_header("Content-Disposition", f"attachment; filename={filename}")
                msg.attach(part)
                self.Mail_Anhang = None
                filename = None
                print("Datei an Ticket angehängt.")
            except Exception as ez3:
                print("Fehler beim Anhängen der Datei: ", ez3)
                messagebox.showerror(title="CiM Fehler", message=f"Es gab einen Fehler beim Anhängen der Datei. Fehlercode: {ez3}")
                return

        with smtplib.SMTP_SSL(self.smtp_server, 465) as server:
            try:
                ###server.set_debuglevel(1)
                server.login(self.sender_email, self.pw_email)
                self.smtp_login_erfolgreich = True
            except Exception as EmailEx1:
                print("Fehler beim anmelde beim Mailserver. Fehlercode: ", EmailEx1)
                self.smtp_login_erfolgreich = False
                try:
                    self.smtp_login_erfolgreich_l.configure(text="Anmeldung am SMTP fehlgeschlagen.", text_color="Red")
                    self.Ereignislog_insert(nachricht_f_e="-Anmeldung am SMTP fehlgeschlagen.-")
                except:
                    pass
                messagebox.showerror(title="CiM Fehler", message=f"Es gab einen Fehler beim Anmelden am Mailserver. Fehlercode: {self.smtp_server}")
            if self.alternative_empfänger_adresse == "":
                try:
                    server.sendmail(self.sender_email, self.empfänger_email, msg.as_string())
                    if self.kopie_der_mail_erhalten == True:
                        server.sendmail(self.sender_email, self.sender_email, msg.as_string())
                        self.Ereignislog_insert(nachricht_f_e="-Email Kopie an SMTP Server versendet.-")
                    self.Ereignislog_insert(nachricht_f_e="-Email an SMTP Server versendet.-")
                except Exception as EmailEx2:
                    print("Fehler beim anmelden beim senden an den Mailserver. Fehlercode: ", EmailEx2)
                    self.Ereignislog_insert(nachricht_f_e="-Anmeldung am SMTP fehlgeschlagen.-")
                    messagebox.showerror(title="CiM Fehler", message=f"Es gab einen Fehler beim senden der Nachricht an den Mailserver. Fehlercode: {EmailEx2}")
                self.Ticket_Fenster.destroy()
                messagebox.showinfo(title="CiM", message="Das Ticket wurde erfolgreich erstellt.")
                print("E-Mail erfolgreich gesendet!")
            elif self.alternative_empfänger_adresse != "":
                try:
                    server.sendmail(self.sender_email, self.alternative_empfänger_adresse, msg.as_string())
                    self.Ereignislog_insert(nachricht_f_e="-Email an SMTP Server versendet.-")
                except Exception as EmailEx2:
                    print("Fehler beim anmelden beim senden an den Mailserver. Fehlercode: ", EmailEx2)
                    self.Ereignislog_insert(nachricht_f_e="-Anmeldung am SMTP fehlgeschlagen.-")
                    messagebox.showerror(title="CiM Fehler", message=f"Es gab einen Fehler beim senden der Nachricht an den Mailserver. Fehlercode: {EmailEx2}")
                self.Ticket_Fenster.destroy()
                messagebox.showinfo(title="CiM", message="Das Ticket wurde erfolgreich erstellt.")
                print("E-Mail erfolgreich gesendet!")

    def Ticket_erstellen_api(self): # Ich denke nicht, dass ich das hier so schnell hinbekommen werde, da das Ding immer wieder nen fehler schmeißt den ich nicht mal verstehe haha.
        print("Ticket_erstellen_api")
        messagebox.showerror(title="Fehler", message="Dieses Feature existiert noch nicht, wie hast Du überhaupt geschafft diese Funktion aufzurufen!?!???")

    def frage_nach_string_suche3(self):
        suche3_fr_fenster = tk.CTkToplevel()
        suchwort_frage_e = tk.CTkEntry(suche3_fr_fenster)
        suchwort_frage_e.pack()
        self.pfad_der_suche = filedialog.askdirectory()
        self.Suchwort = suchwort_frage_e.get()
        suche3_start_knopp = tk.CTkButton(suche3_fr_fenster, text="Starten", command=self.genaue_suche_start)
        suche3_start_knopp.pack() 

    def genaue_suche_start(self):
        if self.pfad_der_suche and self.Suchwort != None:
            self.thread_suche_3 = threading.Thread(target=self.genaue_suche)
            self.thread_suche_3.start()
            print(f"Suche nun mit {self.Suchwort} im Verzeichnis {self.pfad_der_suche}")
        else:
            print("Suche wurde abgebrochen.")

    def Berichtsheft_aufmachen(self):
        print("öffne nun Berichtsheft...")
        url = "https://bildung.ihk.de/webcomponent/dibe/AUSZUBILDENDER/berichtsheft/wochenansicht"
        try:
            webbrowser.get("chrome").open(url)
        except:
            messagebox.showerror(title=self.Programm_Name_lang, message="Konnte die Seite nicht öffnen.")

    def anhang_suchen_ticket(self):
        print("anhang_suchen_ticket(def)")
        self.Mail_Anhang = filedialog.askopenfilename()
        if self.Mail_Anhang:
            self.Mail_Anhang_status_l.configure(text=f"Anhang: {self.Mail_Anhang}")

    def letzten_text_erhalten(self):
        print("letzten_importieren(def)")
        self.geladener_Text = self.ausgabe_text.get("0.0", "end")
        self.einzelner_Eintrag = self.geladener_Text.split("\n\n")
        if self.einzelner_Eintrag:
            for eintrag in reversed(self.einzelner_Eintrag):
                if eintrag.startswith("Uhrzeit:") and "Telefonnummer:" in eintrag:
                    self.cim = eintrag      # WARUM WERDEN DIE VARS HIER WIEDER DOPPELT BELEGT?????
                    self.letzter_eintrag_text = eintrag
                    break
            else:
                print("Kein passender Eintrag gefunden")
        else:
            print("Die Liste ist leer")

    def letzten_importieren(self):
        self.letzten_text_erhalten()
        self.Nachricht_Ticket_e.insert("0.0", self.letzter_eintrag_text)
        self.letzter_eintrag_text = None

        
        

    def Ticket_erstellen(self): # Die erste frage, ob es per Mail oder API erstellt werden soll.
        print("Ticket_erstellen(def)")
        self.Ticket_Fenster = tk.CTkToplevel()
        self.Ticket_Fenster.configure(fg_color=self.Hintergrund_farbe)
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
        self.Betreff_Ticket_e = tk.CTkEntry(self.Ticket_Fenster, width=300, placeholder_text="Betreffzeile", fg_color=self.Entry_Farbe, text_color="Black", placeholder_text_color="FloralWhite")
        self.Nachricht_Ticket_e = tk.CTkTextbox(self.Ticket_Fenster, width=300, height=420, wrap="word", fg_color=self.Hintergrund_farbe_Text_Widget, text_color=self.Textfarbe, border_color=self.Border_Farbe, border_width=2)
        self.Ticket_abschicken_mail = tk.CTkButton(self.Ticket_Fenster, text="Ticket erstellen und versenden", command=self.Ticket_erstellen_mail, fg_color="aquamarine", border_color="Black", border_width=1, text_color="Black", hover_color="DarkSlateGray1")
        self.alternative_empfänger_adresse_e = tk.CTkEntry(self.Ticket_Fenster, placeholder_text="Alternative Empfänger", width=300, fg_color=self.Entry_Farbe, text_color="Black", placeholder_text_color="FloralWhite")
        self.Ticket_erstellen_anhang_suchen_knopp = tk.CTkButton(self.Ticket_Fenster, text="Anhang hinzufügen", command=self.anhang_suchen_ticket, fg_color="white", border_color="Black", border_width=1, text_color="Black", hover_color="DarkSlateGray1")
        self.Mail_Anhang_status_l = tk.CTkLabel(self.Ticket_Fenster, text=f"Anhang: ", text_color="Black", bg_color=self.Hintergrund_farbe, corner_radius=3)
        self.letztes_einfügen_knopp = tk.CTkButton(self.Ticket_Fenster, text="Letzten Anruf Importieren", command=self.letzten_importieren)
        self.letztes_einfügen_knopp.place(x=500,y=230)

        self.alternative_empfänger_adresse_e.place(x=330,y=120)
        self.Ticket_abschicken_mail.place(x=330,y=420)
        self.Betreff_Ticket_e.place(x=10,y=50)
        self.Nachricht_Ticket_e.place(x=10,y=80)
        self.Mail_Anhang_status_l.place(x=10,y=10)
        self.Ticket_erstellen_anhang_suchen_knopp.place(x=330,y=180)

    
 

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
        

    def todo_aufmachen(self):
        try:
            script_path = "totdo.py"
            subprocess.Popen([sys.executable, script_path],creationflags=subprocess.CREATE_NO_WINDOW) # Windoof
        except AttributeError as e:
            print(f"Fehler beim Starten des Skripts: {e}")
            # Unix (macOS, Linux)
            subprocess.Popen([sys.executable, script_path],stdout=subprocess.PIPE,stderr=subprocess.PIPE)
            print("Totdo wurde unter Unix geöffnet.")
        except ModuleNotFoundError:
            # Unix (macOS, Linux)
            subprocess.Popen([sys.executable, script_path],stdout=subprocess.PIPE,stderr=subprocess.PIPE)
            print("Totdo wurde unter Unix geöffnet.")
        except Exception as ejkhlsdf:
            print(f"[-FATAL-] Beim öffnen vom Totdo ist ein Fehler aufgetreten. Fehlercode: {ejkhlsdf}")

    
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
                self.pw_email = SMTP_Server_Passwort_Datei.read()
                print("[-EINSTLLUNGEN LADEN-] Absender Kennwort geladen.s")
        except Exception as EmailEx3_l:
            print(EmailEx3_l)
            #self.sender_email = ""
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
                print(f"[-SMTP ANMELDUNG - INFO ] melde mich nun mit dem Nutzer {self.sender_email} an dem Server {self.smtp_server} an..")
                server.login(self.sender_email, self.pw_email)
                print("[-SMTP ANMELDUNG-] Anmeldung beim SMTP Server erfolgreich.")
                self.smtp_login_erfolgreich = True
                try:
                    self.smtp_login_erfolgreich_l.configure(text="Anmeldung am SMTP Server war erfolgreich.", text_color="SeaGreen1")
                except:
                    pass
            except Exception as EmailEx1:
                print("[-SMTP ANMELDUNG-] Fehler beim anmelden beim Mailserver. Fehlercode: ", EmailEx1)
                self.Ereignislog_insert(nachricht_f_e="- [-SMTP ANMELDUNG-] Fehler bei der Anmeldung beim Mailserver. -")
                self.smtp_login_erfolgreich = False
                try:
                    self.smtp_login_erfolgreich_l.configure(text="Anmeldung am SMTP fehlgeschlagen.", text_color="Red")
                except:
                    pass
                 
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
            ##self.Berichtsheft_knopp.place_forget()
            self.Statistiken_anzeigen_linie_knopp.place_forget()
            self.Statistiken_anzeigen_saeule_knopp.place_forget()
        elif self.Menü_da == False:
            # Menu wird jetzt angezeigt (Ja, wirklich.)
            print("menü == false (Menü war nicht offen)")
            self.Pause_menu.place(x=300,y=10)
            self.Menü_da = True
            self.Menü_Knopp.configure(text="Menü schließen", fg_color="aquamarine", hover_color="aquamarine3")
            ##self.Berichtsheft_knopp.place(x=400,y=100)
            self.Einstellung_Design_auswahl.place(x=10,y=200)
            self.Einstellung_Design_L.place(x=10,y=170)
            self.Statistiken_anzeigen_linie_knopp = tk.CTkButton(self.Pause_menu, text="Statistiken als Liniendiagramm anzeigen", command=self.Anrufstatistiken_anzeigen_linie, fg_color="White", border_color="Black", border_width=1, text_color="Black", hover_color="pink")
            self.Statistiken_anzeigen_saeule_knopp = tk.CTkButton(self.Pause_menu, text="Statistiken als Säulendiagramm anzeigen", command=self.Anrufstatistiken_anzeigen_saeule, fg_color="White", border_color="Black", border_width=1, text_color="Black", hover_color="pink")
            self.Statistiken_anzeigen_linie_knopp.place(x=10,y=100)
            self.Statistiken_anzeigen_saeule_knopp.place(x=10,y=140)
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
                    self.Ereignislog_insert(nachricht_f_e="-Der Name besteht bereits.-")
                    kontakt['Name'] = name
                    gefunden = True
                    #messagebox.showinfo("Info", "Name der bestehenden Telefonnummer aktualisiert.")
                    self.Ereignislog_insert(nachricht_f_e="-bestehende Nummer wurde aktualisiert.-")
                    break

            if not gefunden:
                kontakte['Kontakte'].append({"Telefonnummer_jsn_gesperrt": telefonnummer, "Name": name})
                self.Ereignislog_insert(nachricht_f_e="-Kontakt wurde hinzugefügt.-")
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
                        self.Ereignislog_insert(nachricht_f_e="-Der Name besteht bereits.-")
                        kontakt['Name'] = name
                        gefunden = True
                        #messagebox.showinfo("Info", "Name der bestehenden Telefonnummer aktualisiert.")
                        self.Ereignislog_insert(nachricht_f_e="-bestehende Nummer wurde aktualisiert.-")
                        break

                if not gefunden:
                    kontakte['Kontakte'].append({"Telefonnummer_jsn": telefonnummer, "Name": name})
                    self.Ereignislog_insert(nachricht_f_e="-Kontakt wurde hinzugefügt.-")
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
                    self.Ereignislog_insert(nachricht_f_e="-Kontakt wurde gelöscht.-")
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
        print("[ SUCHE 2.0 - INFO ] Suchen(def)")
        self.Suche_suche = ""
        self.gesucht_zahl = 0
        self.gesucht_zahl_mit_fehlern = 0
        self.Ergebnise_zahl = 0
        try:
            self.Ergebnisse_des_scans_feld = tk.CTkTextbox(self.suchfenster_ergebnisse, width=500, height=500, fg_color=self.Hintergrund_farbe_Text_Widget, text_color=self.Textfarbe, border_color=self.Border_Farbe, border_width=2)
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
        
        print("[ SUCHE 2.0 - INFO ] Fenster fürs suchen geladen...")
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
        print("[ SUCHE 2.0 - INFO ] Pfad wurde ausgewählt")
        such_dialog = tk.CTkInputDialog(title="CiM Suche", text="Wonach suchst Du? Es werden die bisher noch gespeichertern Liste aus dem Programmverzeichnis durchsucht. (Groß-und Kleinschreibung wird ignoriert)")
        try:
            x = root.winfo_x() + root.winfo_width()//2 - such_dialog.winfo_width()//2
            y = root.winfo_y() + root.winfo_height()//2 - such_dialog.winfo_height()//2
            such_dialog.geometry(f"x+{x}+{y}")
        except:
            print("[ SUCHE 2.0 - ERR ] Fehler beim zentrieren des Such-Dialogs. selbst wenn ich hier die Fehlermeldung hinschreiben würde, würdest Du sie nicht verstehen denn ich habe auch keine Ahnung.")

        self.Suche_suche = such_dialog.get_input()
        such_dialog.destroy()
        if self.Suche_suche != "":
            try:
                self.thread_suche = threading.Thread(target=self.Suche_algo)
                self.thread_suche.start()
                print("[ SUCHE 2.0 - INFO ] Thread für die Suche gestartet.")
            except:
                print("[ SUCHE 2.0 - INFO ] Thread für die Suche konnte nicht gestartet werden.")
                try:
                    self.etwas_suchen1 = True
                    self.Suche_algo()
                except Exception as esisx:
                    print("[ SUCHE 2.0 - ERR ] fehler161: ",esisx)
        else:
            messagebox.showinfo(message="Suche abgebrochen.")
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
        print("[ SUCHE 2.0 - INFO ] Suchfenster wurde geschlossen.")
        self.results = None
        self.Anzahl_der_Ergebnisse = None
        self.rearesults = None ## Diese Var ist theoretisch das eigentliche self.Anzahl_der_Ergebnisse aber ich bin zu faul das jetzt zu ändern.
        self.Ergebnisse_Listbox.unbind("<Double-1>")
        self.suchfenster_ergebnisse.destroy()
        self.thread_suche.join()


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
                    return ""

            folder_path = self.Ort_wo_gesucht_wird
            content_to_search = self.Suche_suche.lower()  # Konvertiere den Suchinhalt in Kleinbuchstaben
            results = []
            try:
                for root, dirs, files in os.walk(folder_path):
                    for file_name in files:
                        try:
                            if file_name.endswith('.txt') or file_name.endswith('.md') or file_name.endswith('.html') or file_name.endswith('.xml') or file_name.endswith('.csv') or file_name.endswith('.js'):
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
                results = None
                try:
                    self.thread_suche.join()
                    print("[ SUCHE 2.0 - INFO ] Thread wurde erfolgreich beendet. (exception vor der Suche)")
                except Exception as E_t:
                    print(f"[ SUCHE 2.0 - ERR ] Konnte den Thread self.thread_suche nicht beenden, (vor der Suche) Fehlermeldung: {E_t}")

            if results:
                ganzes_ergebnis = "Ich habe in folgenden Dateien " + str(self.Ergebnise_zahl) + " Ergebnisse gefunden:"
                erg_l = tk.CTkLabel(self.suchfenster_ergebnisse, text=ganzes_ergebnis)
                erg_l.pack()
                self.rearesults = results
                self.durchsucht_text = f"Es wurden insgesammt: {self.gesucht_zahl} Daten durchsucht. {ganzes_ergebnis}"
                self.knopp_offnen = tk.CTkButton(self.suchfenster_ergebnisse, text="Alle einfach aufmachen", command=self.aufmachen_results_vor)
                self.knopp_offnen.pack()
                self.Ergebnisse_Listbox.bind("<Double-1>", self.Eintrag_aufmachen)
                self.Anzahl_der_Ergebnisse = self.Ergebnise_zahl
                self.etwas_suchen1 = False
                self.etwas_suchen = False
                self.Suche_suche = ""
                self.Ort_wo_gesucht_wird = ""
                self.Erg = results
                results = None
                try:
                    self.thread_suche.join()
                    print("[ SUCHE 2.0 - INFO ] Thread wurde erfolgreich beendet. (nach dem die Results festehen)")
                except Exception as E_t:
                    print(f"[ SUCHE 2.0 - ERR ] Konnte den Thread self.thread_suche nicht beenden, (im results) Fehlermeldung: {E_t}")
            else:
                self.Ergebnisse_Listbox.unbind("<Double-1>")
                dmsg = f"Dazu konnte ich leider nichts finden. Ich hab in {self.gesucht_zahl} Dateien gesucht."
                self.etwas_suchen1 = False
                self.Suche_suche = ""
                self.Ort_wo_gesucht_wird = ""
                results = None
                try:
                    self.thread_suche.join()
                    print("[ SUCHE 2.0 - INFO ] Thread wurde erfolgreich beendet. (im else der results)")
                except Exception as E_t:
                    print(f"[ SUCHE 2.0 - ERR ] Konnte den Thread self.thread_suche nicht beenden, (im else der results) Fehlermeldung: {E_t}")
                messagebox.showinfo(title="CiM Suche", message=dmsg)
                self.suchfenster_ergebnisse.destroy()
                
        else:
            ### wenn nichts gefunden wurde.
            print("[ SUCHE 2.0 - INFO ] gab nüscht")
            self.Ergebnisse_Listbox.unbind("<Double-1>")
            dmsg = f"Dazu konnte ich leider nichts finden. Ich hab in {self.gesucht_zahl} Dateien gesucht."
            self.Suche_suche = ""
            self.etwas_suchen1 = False
            results = None
            self.results = None
            try:
                self.thread_suche.join()
                print("[ SUCHE 2.0 - INFO ] Thread wurde erfolgreich beendet. (else des gab nüscht)")
            except Exception as E_t:
                print(f"[ SUCHE 2.0 - ERR ] Konnte den Thread self.thread_suche nicht beenden, Fehlermeldung: {E_t}")
            messagebox.showinfo(title="CiM Suche", message=dmsg)

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
        print("[ SUCHE 2.0 - INFO ] suche_alles aufamachen davor warnmeldung dings")
        if self.Anzahl_der_Ergebnisse == None:
            messagebox.showinfo(title=self.Programm_Name, message="Diese Funktion ist aus performance technischen Gründen nicht mehr verfügbar sobald das Suchfenster geschlossen wurde.")
            return
        if self.Anzahl_der_Ergebnisse >= 20:
            print(f"[ SUCHE 2.0 - INFO ] Es sind >= 20 Suchergebnisse... {self.Anzahl_der_Ergebnisse}")
            antw = messagebox.askyesno(title="CiM Suche", message=f"Sind Sie sicher dass sie wirklich alle {self.Anzahl_der_Ergebnisse} Ergbnisse öffnen möchten? (Unter Windows könnte Ihr System einfrieren)")
            if antw:
                if antw == True:
                    self.aufmachen_results()
                elif antw == False:
                    print("[ SUCHE 2.0 - INFO ] Nutzer wollte doch nicht alles aufmachen")
        elif self.Anzahl_der_Ergebnisse <= 20:
            print(f"[ SUCHE 2.0 - INFO ] Es sind weniger als 20 Suchergbnisse.{self.Anzahl_der_Ergebnisse}")
            self.aufmachen_results()

    def Kunde_ruft_an(self):
        print("Thread gestartet: Kunde_ruft_an (def)")
        while self.Programm_läuft == True:
            try:
                with open("tmp.txt", "r") as tmp_ld:
                    gel_tmp = tmp_ld.read()
                    self.Anruf_Telefonnummer = gel_tmp
                    print1 = "[i] abgefangene Telefonummer: " + self.Anruf_Telefonnummer + "-"
                    self.Ereignislog_insert(nachricht_f_e=print1)
                    self.Uhrzeit_anruf_start = self.Zeit
                    self.Anruf_Zeit.configure(text=f" 🔴 aktiver Anruf seit: {self.Uhrzeit_anruf_start} ")
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
                            self.Ereignislog_insert(nachricht_f_e="-Konnte die Blacklist nicht laden-")
                            daten_blacklist = ""
                        for Gesperrte_kontakt in daten_blacklist.get("Kontakte", []):
                            print(f"ich durchsuche die Blacklist... mit {Gesperrte_kontakt.get("Telefonnummer_jsn_gesperrt")}")
                            if str(Gesperrte_kontakt.get("Telefonnummer_jsn_gesperrt")) == str(self.Anruf_Telefonnummer):
                                print("if f")
                                self.Ereignislog_insert(nachricht_f_e="-Telefonnummer in Blacklist gefunden!\n Nummer wurde nicht eingefügt.")
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
                                    self.Ereignislog_insert(nachricht_f_e="-Anruf wurde beendet.-")
                                    # hier kommen jetzt die Ausnahmen für spezielle Kontakte hin. !!WENN SIE GEFUNDEN WUDEN!!
                                                
                                        # hier enden die speziellen Ausnahmen für spezielle Kontakte.
                    except Exception as ExcK1:
                            print(f"Fehler beim Durchsuchen der JSON DB nach dem Kontakt. Fehlercode: {ExcK1}")
            except Exception:
                pass
            try:    ##### Das hier lädt nachdem der webserver aufm localhost die Datei tmp1.txt geschrieben hat, genau diese Datei und holt sich daraus die end-Uhrzeit des Anrufs
                with open("tmp1.txt", "r") as tmp1_ld:
                    gel_tmp1 = tmp1_ld.read()
                    self.Uhrzeit_anruf_ende = gel_tmp1
                    print("End-Uhrzeit: ", self.Uhrzeit_anruf_ende)
                    tmp1_ld.close()
                    self.Anruf_Zeit.configure(text=f"Kein akiver Anruf             ")
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

    def Checkboxen_dingsen(self):  # Das zukünftige Checklisten Feature
        pdf_dateiname = self.Checklisten_Speicherort_Datei
        def checkliste_als_pdf_speichern(pdf_dateiname):
            print("checkliste_als_pdf_speichern(def)")
            Kunde = "Test" # hier dann später der Name des Kunden aus welchem man die Checkliste Importiert hat oder für welchen man diese erstellt hat // Todo: editor für checklisten bauen 
            pdf_dateiname = "Checklisten_Export.pdf"
            c = canvas.Canvas(pdf_dateiname, pagesize=letter)
            width, height = letter
            
            y_position = height - 50
            for label, checkbox in zip(labels, checkboxes):
                checkbox_status = "✔" if  checkbox.get() else "X"
                c.drawString(100, y_position, f"{label}: {checkbox_status}")
                y_position -= 20
            c.save()
            print("PDF gespeichert.")
            webbrowser.open(pdf_dateiname)
            ''' pdf_metadaten_bearbeiten(pdf_dateiname, Kunde) # Das bearbeiten der Metadaten geht noch nicht..

        def pdf_metadaten_bearbeiten(pdf_dateiname, Kunde):
            print("beabeite nun die Metadaten der PDF")
            doc = fitz.open(pdf_dateiname)
            # Metadaten ändern
            doc.metadata = {
                "title": "Checkbox Status",
                "author": "M.U.L.M",
                "subject": Kunde,
                "keywords": "PDF, Checkliste, CiM"
            }
            # Originaldatei durch temporäre Datei ersetzen
            doc.save("Checkliste_aus_dem_CiM.pdf", incremental=True)
            doc.close()'''
            
            

        print("Checklisten_aufmachen_fenster(def)")
        Checklisten_Fenster = tk.CTkToplevel()
        width = 720
        height = 540
        Checklisten_Fenster.geometry(f"{width}x{height}")

        labels = [self.Checklisten_Option_1 , self.Checklisten_Option_2, self.Checklisten_Option_3]
        checkboxes = []

        for label in labels:
            frame = tk.CTkFrame(Checklisten_Fenster)
            frame.pack(pady=5)

            label_widget = tk.CTkLabel(frame, text=label)
            checkbox = tk.CTkCheckBox(frame, text="")
            checkbox.pack(side=Atk.LEFT)
            label_widget.pack(side=Atk.LEFT)
            checkboxes.append(checkbox)

        speichern_knopp = tk.CTkButton(Checklisten_Fenster, text="Als PDF Speichern", command=lambda: checkliste_als_pdf_speichern(pdf_dateiname))
        speichern_knopp.pack()


        
        
   
    
    def Netzlaufwerk_speichern(self):
        print("Netzlaufwerk_speichern(def)")
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
        print("ende des Programms, fange nun an zu speichern...")
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
                    with open(self.csv_datei_pfad + "/AnruferlistenDings" + self.tag_string + ".csv" , 'w+', newline='') as datei:
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
        root.geometry(f"{width}x{height}+{x}+{y}")
    mittig_fenster(root, width, height)
    Listendings = Listendings(root)
    root.mainloop()