try:
    import customtkinter as tk
    ###import tkinter as tk
    from tkinter import ttk
    import tkinter as Atk
    from tkinter import messagebox
    from tkinter import filedialog
    from tkinter import Menu
    import time
    import os
    import sys
    import csv
    import ctypes
    import json
    from threading import Thread
    from http.server import BaseHTTPRequestHandler, HTTPServer
    import urllib.parse
    import threading
    from customtkinter import ThemeManager
    import datetime
except:
    print("(FATAL) Konnte die wichtigen Bilbioteken nicht Laden!")
    messagebox.showerror(title="Kritischer Fehler", message="(FATAL) Konnte die wichtigen Bilbioteken nicht Laden! Das Programm wird nun Beendet.")
    sys.exit()

root = tk.CTk()




class Listendings:
    Programm_läuft = True
    class RequestHandler(BaseHTTPRequestHandler):
        def do_GET(self):
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
            else:
                try:
                    with open("tmp.txt", "w+") as tmp:
                        tmp.write(besserer_pfad)
                except Exception as e:
                    print(f"Fehler beim Schreiben in tmp.txt: {e}")
            self.wfile.write(b"<html><head><title>CiM Modul</title></head>")
            self.wfile.write(b"<body><h1>Dings</h1></body></html>")

    class WebServerThread(threading.Thread):
        def run(self):
            port = 8080
            server_address = ('', port)
            httpd = HTTPServer(server_address, Listendings.RequestHandler)
            try:
                while Listendings.Programm_läuft == True:
                    print(f'Ich horche mal auf Port {port}...') 
                    httpd.handle_request()
                    if Listendings.Programm_läuft == False:
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

    

        

    def __init__(self, master):
        self.master = master
        self.DB = "liste.txt"
        self.Programm_Name = "ListenDings"
        self.Version = "Alpha 1.2.4.4 (4)"
        self.Zeit = "Lädt.."
        master.title(self.Programm_Name + " " + self.Version + "                                                                          " + self.Zeit)
        root.configure(resizeable=False)
        root.geometry("1420x520")
        self.Programm_läuft = True
        self.Uhr_läuft = True
        root.protocol("WM_DELETE_WINDOW", self.bye)
        self.Listen_Speicherort_Netzwerk_geladen = None
        self.Zeit_text = None
        self.Uhrzeit_anruf_start = None
        self.Pause = True
        self.Menü_da = False
        self.Starface_Modul = "0"
        self.Auto_speichern_Einstellung = "0"
        self.Autospeichern_tkvar = "0"
        self.Uhrzeit_anruf_ende = None
        self.tag_string = str(time.strftime("%d %m %Y"))
        self.Benutzerordner = os.path.expanduser('~')
        self.Listen_Speicherort_standard = os.path.join(self.Benutzerordner, 'CiM', 'Listen')
        self.Einstellungen_ordner = os.path.join(self.Benutzerordner, 'CiM', "Einstellungen")
        self.Starface_Einstellungsdatei = os.path.join(self.Einstellungen_ordner , "Starface_Modul.txt")
        self.Listen_Speicherort_Einstellungsdatei = os.path.join(self.Einstellungen_ordner, "Listendingsspeicherort.json")
        self.Listen_Speicherort_Netzwerk_Einstellungsdatei = os.path.join(self.Einstellungen_ordner, "Listendingsspeicherort_Netzwerk.json")
        self.Auto_speichern_Einstellungsdatei = os.path.join(self.Einstellungen_ordner, "Auto_speichern.txt") 
        self.icon_pfad = os.path.join(self.Benutzerordner, 'CiM', 'Assets', 'CiM_icon.jpg')
        
        
        self.Monat = time.strftime("%m")
        self.Thread_Kunderuftan = threading.Timer(2, self.Kunde_ruft_an)
        self.thread_uhr = threading.Timer(1, self.Uhr)
        self.thread_webserver = Listendings.WebServerThread()
        self.thread_webserver.setDaemon(True)
        self.thread_uhr.setDaemon(True)
        self.Thread_Kunderuftan.setDaemon(True)
        self.thread_uhr.start()
        self.Thread_Kunderuftan.start()
        
        self.Hintergrund_farbe = "SlateGrey"
        root.configure(fg_color=self.Hintergrund_farbe)
        root.resizable(False, False)
        self.Weiterleitung_an = ""
        self.wollte_sprechen = ""
        self.Starface_Farbe = "#4d4d4d"

        self.zachen = 0
        self.fertsch_var = None
        self.fertsch_vars = None

        
        
        
        
        self.zeit_string = time.strftime("%H:%M:%S")
        self.tag_string = str(time.strftime("%d %m %Y"))
        self.Tag_und_Liste = self.tag_string + " Dateien.txt"
        self.Liste_mit_datum = os.path.join(self.Listen_Speicherort_standard, self.Monat, self.Tag_und_Liste)
        self.Monat_ordner_pfad = os.path.join(self.Listen_Speicherort_standard, self.Monat)

        
        try:
            p1 = Atk.PhotoImage(file = "CiM_icon.png")
            root.iconphoto(False, p1)
        except:
            try:
                root.iconphoto(False, Atk.PhotoImage(file = self.icon_pfad))
            except Exception as err:
                messagebox.showinfo(message=err)
                print("icon gibt heute nicht.")
            

        print(self.tag_string)
        if not os.path.exists(self.Monat_ordner_pfad):
            try:
                os.makedirs(self.Monat_ordner_pfad)
                print("Ordner ", {self.Monat_ordner_pfad}, "Erfolgreich erstellt.")
            except:
                print("Fehler beim erstellen der Ordner")

        try:
            with open(self.Auto_speichern_Einstellungsdatei, "r") as einst_gel_autsp:
                self.Auto_speichern_Einstellungsdatei_var = einst_gel_autsp.read()
                print("Einstellunsgdatei zum Autospeichern geladen. Wert = ", self.Auto_speichern_Einstellungsdatei)
                if self.Auto_speichern_Einstellungsdatei_var == "1":
                    print("Die Autospeichern Var welche aus den Einstellungen zum Programmstart geladen wurde ist: ", self.Auto_speichern_Einstellungsdatei_var)
                else:
                    print("Die Autospeichern Var welche aus den Einstellungen zum Programmstart geladen wurde ist: ", self.Auto_speichern_Einstellungsdatei_var)
                    self.Auto_speichern_Einstellungsdatei_var = "0"
        except Exception as autpsp_err:
            messagebox.showerror(title="CiM Fehler", message="Konnte die Datei zum Autospeichern nicht finden, vielleicht gibt es sie auch einfach nicht.")
            print("Fehler beim Laden des Autospeicherns. Funktion wurde deaktiviert. self.Auto_speichern_Einstellungsdatei = 0. Fehlercode: ", autpsp_err)
            self.Auto_speichern_Einstellungsdatei_var = "0"
                
        
        
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
        except Exception as ex_stern:
            print("Die Starface Moduleinstelllungen konten nicht überprüft werden.")

        try:
            with open(self.Listen_Speicherort_Einstellungsdatei , "r") as Liste_Speicherort_data:
                self.Listen_Speicherort = json.load(Liste_Speicherort_data)
                self.Listen_Speicherort_geladen = (self.Listen_Speicherort["ListenDings_Speicherort"])
        except PermissionError:
                messagebox.showerror(title="Listendings Speicherort", message="Es Fehlt für diesen Ordner die nötige Berechtigung, Die Speicherorte konnten nicht geladen werden")
        except:
            messagebox.showerror(title="Listendings Speicherort", message="Die Einstellung scheint nicht zu existieren")

        try:
            with open(self.Listen_Speicherort_Netzwerk_Einstellungsdatei , "r") as Liste_Speicherort_Netzwerk_data:
                self.Listen_Speicherort_Netzwerk = json.load(Liste_Speicherort_Netzwerk_data)
                self.Listen_Speicherort_Netzwerk_geladen = (self.Listen_Speicherort_Netzwerk["ListenDings_Speicherort_Netzwerk"])
        except PermissionError:
                messagebox.showerror(title="Listendings Speicherort", message="Es Fehlt für diesen Ordner die nötige Berechtigung, Der Gespeicherte Netzwerkpfad konnte nicht aufgerufen werden.")
        except Exception as e:
            ex = "Irgendwas ist passiert: ", e
            print(ex)
        



        

        # Labels für Textfelder
        self.kunde_label = tk.CTkLabel(master, text="Kunde:")
        self.problem_label = tk.CTkLabel(master, text="Problem:")
        self.info_label = tk.CTkLabel(master, text="Info:")        

        # Textfelder

        self.kunde_entry = tk.CTkEntry(master,width=600, placeholder_text="Kunde")
        self.t_nummer = tk.CTkEntry(master, width=600, placeholder_text="Telefonnummer")
        self.t_nummer.configure(state="disabled")
        self.problem_entry = tk.CTkEntry(master,width=1200, placeholder_text="Problem")
        self.info_entry = tk.CTkEntry(master,width=1200, placeholder_text="Info")

        
        

        # "Senden" Knopf
        self.senden_button = tk.CTkButton(master, text="Senden", command="")
        self.senden_button.bind('<Button-1>', self.senden)
        root.bind('<Return>', self.senden)

        # Alles löschen knopf
        self.alles_löschen_knopp = tk.CTkButton(master, text="Alle Eintrage löschen", command=self.alles_löschen)
        #self.alles_löschen_knopp.place(x=1250,y=400)

        #self.beb_knopp = tk.CTkButton(master, text="Bearbeiten", command=self.beb)
        ##self.beb_knopp.grid(row=3, column=2)

        # Ausgabe-Textfeld
        self.ausgabe_text = tk.CTkTextbox(master, width=1250, height=400, wrap="word")
        ###self.ausgabe_text.configure(highlightthickness=0)
        self.ausgabe_text.configure(state='disabled')
        #self.ausgabe_text.configure(font=("Helvetica", "14"))

        # Positionierung von Labels und Textfeldern
        #self.kunde_label.grid(row=0, column=0)
        #self.problem_label.grid(row=1, column=0)
        #self.info_label.grid(row=2, column=0)

        #self.kunde_entry.grid(row=0, column=1)
        self.kunde_entry.place(x=5,y=5)
        self.problem_entry.place(x=5,y=35)
        self.info_entry.place(x=5,y=65)
        self.t_nummer.place(x=605,y=5)
        #self.senden_button.grid(row=3, column=1)
        self.ausgabe_text.place(x=5,y=110)


        # erschaffen des Column Menü Dings
        self.menu = Menu(root)
        root.configure(menu=self.menu)
        self.menudings = Menu(self.menu, tearoff=0)
        self.Einstellungen = Menu(self.menu, tearoff=0)
        self.Speichern_Menu = Menu(self.menu, tearoff=0)
        self.Bearbeiten_Menu = Menu(self.menu, tearoff=0)
        self.Suchen_Menu = Menu(self.menu, tearoff=0)
        self.Menü = Menu(self.menu, tearoff=0)
        self.menu.add_cascade(label=self.Programm_Name + self.Version, menu=self.menudings)
        self.menu.add_cascade(label="Einstellungen", menu=self.Einstellungen)
        self.menu.add_cascade(label="Bearbeiten", menu=self.Bearbeiten_Menu)
        self.menu.add_cascade(label="Speichern", menu=self.Speichern_Menu)
        self.menu.add_cascade(label="Suchen", menu=self.Suchen_Menu)
        self.menudings.add_command(label="Info", command=self.info)
        self.menudings.add_command(label="Admin rechte aktivieren", command=self.Admin_rechte)
        self.Einstellungen.add_command(label="Speicherort des ListenDings ändern...", command=self.ListenDings_speicherort_ändern)
        self.Speichern_Menu.add_command(label="als CSV Speichern", command=self.als_csv_speichern_eigener_ort)
        self.Speichern_Menu.add_command(label="als CSV Speichern unter...", command=self.als_csv_speichern)
        self.Speichern_Menu.add_command(label="als CSV Speichern auf Netzlaufwerk", command=self.Netzlaufwerk_speichern)
        self.Einstellungen.add_command(label="Netzlaufwerk einstellen...", command=self.ListenDings_speicherort_Netzwerk_ändern)
        self.Bearbeiten_Menu.add_command(label="Bearbeiten Umschalten", command=self.beb_c)
        self.Bearbeiten_Menu.add_command(label="Alle Einträge löschen", command=self.alles_löschen)
        self.Suchen_Menu.add_command(label="Nach alten Eintrag suchen", command=self.Suche)
        
        # Initialisierung wichtiger Variablen

        self.beb = "0"
        
        try:
            # Ausgabe-Textfeld aktualisieren
            print("(INFO) versuche die alten Aufzeichenungen zu Laden")
            self.ausgabe_text.configure(state='normal')
            with open(self.Liste_mit_datum, "r") as f:
                feedback_text = f.read()
                self.ausgabe_text.delete("1.0", tk.END)
                self.ausgabe_text.insert(tk.END, feedback_text)
                self.ausgabe_text.configure(state='disabled')
                print("-----------------------------------------")
                print("(DEV) Hier ist nun das geladene aus der bisherigen Liste:")
                print(feedback_text)
                print("(DEV) Das War das geladene aus der bisherigen Liste.")
                print("-----------------------------------------")
        except FileNotFoundError:
            print("(INFO) Die Datei Liste.txt gibts net")
            self.ausgabe_text.configure(state='disabled')
        except:
            messagebox.showinfo(title="Fehler", message="Ein Unbekannter Fehler ist aufgetreten beim Versuch während des Programmstarts die bisherigen aufzeichnungen zu laden, es könnte sein dass das Programm trotzdem fehlerfrei funktioniert.")
            self.ausgabe_text.configure(state='disabled')


    ###### Hier kommt das animations dings der seitenleiste #####
        self.menu_frame = tk.CTkFrame(master, width=200, height=400)  # Adjust size as needed
        #self.menu_frame.place(x=1100, y=50)  # Position it outside the visible area to the right

        # Add buttons to the menu frame
        #self.beb_knopp = tk.CTkButton(self.menu_frame, text="Bearbeiten", command=self.beb_c)
        self.beb_knopp = tk.CTkButton(master, text="Bearbeiten", command=self.beb_c, fg_color="White", border_color="Black", border_width=1, text_color="Black", hover_color="pink")
        self.beb_knopp.place(x=1260, y=100)  # Add more buttons as needed
        self.alles_löschen_knopp = tk.CTkButton(master, text="Alle Eintrage löschen", command=self.alles_löschen, fg_color="White", border_color="Black", border_width=1, text_color="Black", hover_color="pink")
        self.alles_löschen_knopp.place(x=1260, y=130)
        self.Menü_Knopp = tk.CTkButton(master, text="Menü Anzeigen", command=self.Menu_anzeige_wechseln, fg_color="White", border_color="Black", border_width=1, text_color="Black", hover_color="pink")
        self.Menü_Knopp.place(x=1260, y=160)

        
        self.Pause_menu = tk.CTkFrame(master, width=420, height=300, fg_color="Grey32", border_color="Black", border_width=5)
        self.Suche_knopp = tk.CTkButton(self.Pause_menu, text="Nach alten Eintrag Suchen...", command=self.Suche)
        self.Starface_Modul_Einstellung_Knopp = tk.CTkButton(self.Pause_menu, text="Starface Modul umschalten", command=self.Starface_Modul_umschalten)
        self.Auto_speichern_ändern_knopp = tk.CTkButton(self.Pause_menu, text="Auto Speichern umschalten", command=self.autospeichern_ä_c)
        self.Zhe_Clock = tk.CTkLabel(self.Pause_menu, text=self.Zeit)
        self.Zhe_Clock.place(x=10,y=10)

        def auswahl_gedingst(choice):
            if choice == "An Chefe gegeben":
                self.Weiterleitung_an = "An Holger Beese weitergeleitet."
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
                self.wollte_sprechen = "Mit Chefe sprechen"
            elif choice == "Mit Christian sprechen":
                self.wollte_sprechen = "Mit Christian sprechen"
            elif choice == "Mit Mike sprechen":
                self.wollte_sprechen = "Mit Mike sprechen"
            elif choice == "Mit Frau Tarnath sprechen":
                self.wollte_sprechen = "Mit Frau Tarnath sprechen"
            elif choice == "Keine Weiterleitung":
                self.wollte_sprechen = "-"

        self.optionmenu = tk.CTkOptionMenu(root, values=["An Chefe gegeben", "An Christian gegeben", "An Mike gegeben", "An Frau Tarnath gegeben","Keine Weiterleitung"], command=auswahl_gedingst, fg_color="White", text_color="Black", dropdown_hover_color="pink")
        self.optionmenu.set("Keine Weiterleitung")
        self.optionmenu.place(x=1260,y=220)
        self.optionmenu1 = tk.CTkOptionMenu(root, values=["Mit Chefe sprechen", "Mit Christian sprechen", "Mit Mike sprechen", "Mit Frau Tarnath sprechen","Keine Anfrage"], command=auswahl_gedingst_sprechen, fg_color="White", text_color="Black", dropdown_hover_color="pink")
        self.optionmenu1.set("Mit Wem sprechen?")
        self.optionmenu1.place(x=1260,y=190)

        self.kalender_menü = tk.CTkFrame(master, width=1250, height=520, fg_color="White", border_color="Black", border_width=2)
        self.kalender_menü_Knopp = tk.CTkButton(master, text="Kalender öffnen", command=self.Kalender_anzeigen, fg_color="White", border_color="Black", border_width=1, text_color="Black", hover_color="pink")
        self.kalender_menü_Knopp.place(x=1260,y=480)

        self.Liste_mit_zeugs =  tk.CTkScrollableFrame(self.kalender_menü, width=500, height=420, bg_color="Green")

        
        

        


        



    







    ####### ======================== init ende ======================== #######
    ####### ======================== init ende ======================== #######
    ####### ======================== init ende ======================== #######
    ####### ======================== init ende ======================== #######
    ####### ======================== init ende ======================== #######
        
    def Kalender_anzeigen(self):
        print("kalender_anzeigen(def)")
        self.kalender_menü.place(x=0,y=0)
        self.Liste_mit_zeugs.place(x=100,y=50)
        self.kalender_menü_Knopp.configure(text="Kalender schließen", command=self.Kalender_anzeigen_weg, fg_color="White", border_color="Black", border_width=1, text_color="Black", hover_color="pink")
        self.Aufgabe_hinzufügen_Knopp = tk.CTkButton(self.kalender_menü, text="Eintrag Hinzufügen", command=self.Aufgabe_hinzufügen)
        self.Aufgabe_hinzufügen_Knopp.place(x=620,y=50)

    def Aufgabe_hinzufügen(self):
        text_des_dings = None
        Aufgabe = None
        text_des_dings = tk.CTkInputDialog(text="Gib was ein:")
        Aufgabe = self.Zeit + "  --  " + text_des_dings.get_input()
        if Aufgabe:
            print("Das is: ", text_des_dings, "und Aufgabe ist: ", Aufgabe)
            self.zachen += 1
          
            self.fertsch_var = tk.StringVar()
            self.fertsch_var.set("") 
            try:
                self.fertsch_vars.append(self.fertsch_var)
            except:
                pass
            self.chkbx = tk.CTkCheckBox(self.Liste_mit_zeugs, text=Aufgabe, bg_color="White", text_color="Black", variable=self.fertsch_var, command=lambda: self.callback_fertsch_var(self.fertsch_var))
            self.chkbx.grid(row=self.zachen, column=0, padx=10)
        else:
            pass

    def callback_fertsch_var(self, fertsch_var):
        index = self.fertsch_vars.index(fertsch_var)
        print("Hier ist was fertsch geworden für Eintrag {}: {}".format(index, fertsch_var.get()))


    def Kalender_anzeigen_weg(self):
        print("Kalender_anzeigen_weg")
        self.kalender_menü.place_forget()
        self.Liste_mit_zeugs.place_forget()
        self.Aufgabe_hinzufügen_Knopp.place_forget()
        self.kalender_menü_Knopp.configure(text="Kalender öffnen", command=self.Kalender_anzeigen, fg_color="White", border_color="Black", border_width=1, text_color="Black", hover_color="pink")

        
        

        

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
        
        
        

        if self.Starface_Modul == "1":
            self.Starface_Modul_Einstellung_Knopp.configure(text="Staface Modul ist aktiviert", fg_color="aquamarine", text_color="Black")
        else:
            self.Starface_Modul_Einstellung_Knopp.configure(text="Staface Modul ist deaktiviert", fg_color="chocolate1", text_color="White")

        if self.Auto_speichern_Einstellungsdatei_var == "1":
            self.Auto_speichern_ändern_knopp.configure(text="Autospeichern aktiviert",fg_color="aquamarine", text_color="Black")
        else:
            self.Auto_speichern_ändern_knopp.configure(text="Autospeichern deaktiviert", fg_color="chocolate1", text_color="White")

       
        if self.Menü_da == True:
            print("menü == true")
            self.Suche_knopp.place_forget()
            self.Starface_Modul_Einstellung_Knopp.place_forget()
            self.Auto_speichern_ändern_knopp.place_forget()
            self.Pause_menu.place_forget()
            self.Menü_da = False
            self.Menü_Knopp.configure(text="Menü Anzeigen")
        elif self.Menü_da == False:
            print("menü == false")
            self.Pause_menu.place(x=300,y=10)
            self.Menü_da = True
            self.Menü_Knopp.configure(text="Menü schließen")
            self.Suche_knopp.place(x=10,y=110)
            self.Starface_Modul_Einstellung_Knopp.place(x=10,y=50)
            self.Auto_speichern_ändern_knopp.place(x=10,y=80)

    
        
        

    def Suche(self):
        print("Suchen(def)")
        Suche_suche = ""
        such_dialog = tk.CTkInputDialog(text="Wonach suchst Du? Es werden die bisher noch gespeichertern Liste aus dem Programmverzeichnis durchsucht. (Groß-und Kleinschreibung beachten)", title="CiM Suche")
        Suche_suche = such_dialog.get_input()
        if Suche_suche:
            def read_text_file(file_path):
                try:
                    with open(file_path, 'r', encoding='utf-8') as file:
                        return file.read()
                except Exception as e:
                    print(f"Fehler: {e}")
                    return ""
            folder_path = self.Listen_Speicherort_standard
            content_to_search = Suche_suche
            results = []
            try:
                for root, dirs, files in os.walk(folder_path):
                    for file_name in files:
                        try:
                            if file_name.endswith('.txt'):
                                file_path = os.path.join(root, file_name)
                                file_content = read_text_file(file_path)
                                if content_to_search in file_content:
                                    results.append(file_path)
                        except Exception as e:
                            print(f"irgendwas ging nicht: {file_name}: {e}")
            except Exception as e:
                print(f"konnte den pfad nicht öffnen: {e}")

            if results:
                print("Das hab ich gefunden:")
                for file_path in results:
                    print(file_path)
                    ganzes_ergebnis = f"In Disen Dateien habe ich etwas gefundenf: {results}" 
                messagebox.showinfo(title="CiM Suche", message=ganzes_ergebnis)
                self.Suche_thread.cancel()
            else:
                print("gab nüscht")
                dmsg = "Dazu konnte ich leider nichts finden."
                messagebox.showinfo(title="CiM Suche", message=dmsg)
                self.Suche_thread.cancel()


    def Kunde_ruft_an(self):
        chefe_nummer = "00491772446952"
        christian_nummer = "004915233836862"
        mike_nummer = "004915229048779"
        ich_nummer = "004915758382618"
        print("Thread gestartet: Kunde_ruft_an (def)")
        while self.Programm_läuft == True:
            try:
                with open("tmp.txt", "r") as tmp_ld:
                    gel_tmp = tmp_ld.read()
                    self.Anruf_Telefonnummer = gel_tmp
                    print("abgefangene Telefonummer: ", self.Anruf_Telefonnummer)
                    self.Uhrzeit_anruf_start = self.Zeit
                    tmp_ld.close()
                    os.remove("tmp.txt")
                    self.t_nummer.configure(state="normal")
                    #self.t_nummer.delete(0,tk.END)
                    
                    if self.Anruf_Telefonnummer == chefe_nummer: #chefe
                        self.t_nummer.insert(1,self.Anruf_Telefonnummer)
                        chefe = "Holger Beese aka el Chefe"
                        self.kunde_entry.insert(tk.END,chefe)
                        self.Anruf_Telefonnummer = None

                    elif self.Anruf_Telefonnummer == christian_nummer: #Christian
                        self.t_nummer.insert(1,self.Anruf_Telefonnummer)
                        Christian = "Christian Melges"
                        self.kunde_entry.insert(tk.END,Christian)
                        self.Anruf_Telefonnummer = None

                    elif self.Anruf_Telefonnummer == mike_nummer: #Mike
                        self.t_nummer.insert(tk.END,self.Anruf_Telefonnummer)
                        Mike = "Mike Bosse"
                        self.kunde_entry.insert(1,Mike)
                        self.Anruf_Telefonnummer = None

                    elif self.Anruf_Telefonnummer == ich_nummer: #Ich
                        self.t_nummer.insert(tk.END,self.Anruf_Telefonnummer)
                        ich = "Ich"
                        self.kunde_entry.insert(1,ich)
                        self.Anruf_Telefonnummer = None
                        
                    elif self.Anruf_Telefonnummer.startswith("b") == False:
                        if self.t_nummer.get() != "":
                            self.ganz = " : " + self.Anruf_Telefonnummer
                            self.t_nummer.insert(tk.END,self.ganz)
                            self.Anruf_Telefonnummer = None
                            self.ganz = None
                        else:
                            self.t_nummer.insert(1,self.Anruf_Telefonnummer)
                            self.Anruf_Telefonnummer = None
                    self.t_nummer.configure(state="disabled")
            except Exception as eld:
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
            
    
    #### emde der werbung #######
    def info(self):
        print("(INFO) Info(def)")
        messagebox.showinfo(title="Info", message=self.Programm_Name + " " + self.Version + "\n Programmiert von Maximilian Becker, \n https://dings.software für mehr Informationen")

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

            


        
        


    def Neuladen_der_Liste(self):
        try:
            # Ausgabe-Textfeld aktualisieren
            print("(INFO) versuche die alten Aufzeichenungen zu Laden")
            self.ausgabe_text.configure(state='normal')
            with open(self.Liste_mit_datum, "r") as f:
                feedback_text = f.read()
                self.ausgabe_text.delete("1.0", tk.END)
                self.ausgabe_text.insert(tk.END, feedback_text)
                self.ausgabe_text.configure(state='disabled')
                print("-----------------------------------------")
                print("(DEV) Hier ist nun das geladene aus der bisherigen Liste:")
                print(feedback_text)
                print("(DEV) Das War das geladene aus der bisherigen Liste.")
                print("-----------------------------------------")
        except FileNotFoundError:
            print("(INFO) Die Datei Liste.txt gibts net")
            self.ausgabe_text.configure(state='disabled')
        except:
            messagebox.showinfo(title="Fehler", message="Ein Unbekannter Fehler ist aufgetreten beim Versuch während des Programmstarts die bisherigen aufzeichnungen zu laden, es könnte sein dass das Programm trotzdem fehlerfrei funktioniert.")
            self.ausgabe_text.configure(state='disabled')

    def Admin_rechte(self):
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

    def senden(self, event):
        print("(DEV) senden(def)")
        # Textfeld-Inhalte lesen
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
                    f.write(f"Uhrzeit: {self.Uhrzeit_text}\nKunde: {kunde}\nProblem: {problem}\nInfo: {info}\nTelefonnummer: {T_Nummer}\nJemand bestimmtes sprechen: {self.wollte_sprechen}\nWeiterleitung: {self.Weiterleitung_an}\n\n")
                with open(self.Liste_mit_datum, "r") as f:
                    feedback_text = f.read()
                    self.ausgabe_text.delete("1.0", tk.END)
                    self.ausgabe_text.insert(tk.END, feedback_text)
                self.ausgabe_text.configure(state='disabled')
                self.ausgabe_text.see(tk.END)
                self.Weiterleitung_an = ""
                self.optionmenu.set("Keine Weiterleitung")
                self.optionmenu1.set("Mit Wem sprechen?")
            else:
                print("(INFO) Liste zum beschreiben existiert bereits.")
                with open(self.Liste_mit_datum, "w+") as f:
                    f.write(f"Uhrzeit: {self.Uhrzeit_text}\nKunde: {kunde}\nProblem: {problem}\nInfo: {info}\nTelefonnummer: {T_Nummer}\nJemand bestimmtes sprechen: {self.wollte_sprechen}\nWeiterleitung: {self.Weiterleitung_an}\n\n")
                with open(self.Liste_mit_datum, "r") as f:
                    feedback_text = f.read()
                    self.ausgabe_text.delete("1.0", tk.END)
                    self.ausgabe_text.insert(tk.END, feedback_text)
                    self.ausgabe_text.configure(state='disabled')
                    self.Weiterleitung_an = ""
                    self.wollte_sprechen = ""
                    self.optionmenu.set("Keine Weiterleitung")
                    self.optionmenu1.set("Mit Wem sprechen?")
            

            
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
        self.text_tk_text = self.ausgabe_text.get("1.0", "end-1c")
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
            self.beb_knopp.configure(text="Bearbeiten", fg_color="white", hover_color="pink")
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
            #self.alles_löschen_knopp.pack_forget()
            #self.beb_knopp.grid_forget()
            self.kunde_label.grid_forget()
            self.problem_label.grid_forget()
            self.info_label.grid_forget()
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
                elif zeile.startswith("Kunde:"):
                    kunde = zeile.replace("Kunde:", "").strip()
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
                    schreiber.writerow(["Uhrzeit", "Kunde", "Problem", "Info", "Telefonnummer", "Wollte Sprechen", "Weiterleitung"])
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
                elif zeile.startswith("Kunde:"):
                    kunde = zeile.replace("Kunde:", "").strip()
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
                    schreiber.writerow(["Uhrzeit", "Kunde", "Problem", "Info", "Telefonnummer", "Wollte Sprechen", "Weiterleitung"])
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

    def neue_GUI(self):
        print("neue_GUI (def)")
        self.senden_button.unbind('<Button-1>')
        root.unbind('<Return>')
        #self.alles_löschen_knopp.place_forget()
        #self.beb_knopp.grid_forget()
        self.kunde_label.grid_forget()
        self.problem_label.grid_forget()
        self.info_label.grid_forget()
        self.kunde_entry.grid_forget()
        self.problem_entry.grid_forget()
        self.info_entry.grid_forget()
        self.senden_button.grid_forget()
        self.ausgabe_text.grid_forget()

        self.kunde_label.place(x=5,y=10)
        self.problem_label.place(x=5,y=40)
        self.info_label.place(x=5,y=70)
        self.kunde_entry.place(x=60,y=10)
        self.problem_entry.place(x=60,y=40)
        self.info_entry.place(x=60,y=70)
    
    def Netzlaufwerk_speichern(self):
        print("Netzlaufwerk_speichern(def)")
        print("Als CSV speichern, im Standard Ort")
        self.csv_datei_pfad_Netzwerk = self.Listen_Speicherort_Netzwerk_geladen

        if self.csv_datei_pfad:
            with open(self.Liste_mit_datum, 'r') as text_datei:
                daten = text_datei.read()
            zeilen = daten.strip().split('\n')
            datensaetze = []
            uhrzeit, kunde, problem, info, Telefonnummer, wollte_sprechen, Weiterleitung = "", "", "", "", "", "", ""
            for zeile in zeilen:
                if zeile.startswith("Uhrzeit:"):
                    uhrzeit = zeile.replace("Uhrzeit:", "").strip()
                elif zeile.startswith("Kunde:"):
                    kunde = zeile.replace("Kunde:", "").strip()
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
                    schreiber.writerow(["Uhrzeit", "Kunde", "Problem", "Info", "Telefonnummer", "Wollte Sprechen", "Weiterleitung"])
                    schreiber.writerows(datensaetze)
                    self.zeit_string = time.strftime("%H:%M:%S")
                    self.tag_string = str(time.strftime("%d %m %Y"))
                print("Daten wurden in die CSV-Datei gespeichert.")
                messagebox.showinfo(title="Gespeichert", message="Daten wurden erfolgreich gespeichert.")
            else:
                print("Fehler: Keine vollständigen Informationen wurden in der Textdatei gefunden.")
                messagebox.showerror(title="Fehler", message="Das ist etwas beim Speichern schiefgelaufen.")


    def bye(self):
        print("(ENDE) Das Programm wurde Beendet, auf wiedersehen! \^_^/ ")
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
        try:
            try:
                auto_speichern = "Ja"
                with open(self.Auto_speichern_Einstellungsdatei, "r") as aSp:
                    dings_aSp = aSp.read()
                    auto_speichern = dings_aSp
            except:
                auto_speichern = "Nein"

            if auto_speichern == "Ja":
                csv_datei_pfad_Netzwerk = Listen_Speicherort_Netzwerk_geladen
                if self.csv_datei_pfad:
                    with open(self.Liste_mit_datum, 'r') as text_datei:
                        daten = text_datei.read()
                    zeilen = daten.strip().split('\n')
                    datensaetze = []
                    uhrzeit, kunde, problem, info, Telefonnummer, wollte_sprechen, Weiterleitung = "", "", "", "", "", "", ""
                    for zeile in zeilen:
                        if zeile.startswith("Uhrzeit:"):
                            uhrzeit = zeile.replace("Uhrzeit:", "").strip()
                        elif zeile.startswith("Kunde:"):
                            kunde = zeile.replace("Kunde:", "").strip()
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
                            schreiber.writerow(["Uhrzeit", "Kunde", "Problem", "Info", "Telefonnummer", "Wollte Sprechen", "Weiterleitung"])
                            schreiber.writerows(datensaetze)
                            self.zeit_string = time.strftime("%H:%M:%S")
                            self.tag_string = str(time.strftime("%d %m %Y"))
                        print("Daten wurden in die CSV-Datei gespeichert.")
                        messagebox.showinfo(title="Gespeichert", message="Daten wurden erfolgreich gespeichert.")
                    else:
                        print("Fehler: Keine vollständigen Informationen wurden in der Textdatei gefunden.")
                        messagebox.showerror(title="Fehler", message="Das ist etwas beim Speichern schiefgelaufen.")
            else:
                print("die var zum auto_speichern lag bei was anderem als 1")
        except Exception as e:
            ei = "Es ein Fehler beim Speichern aufgetreten, keine Ahnung was passiert ist wahrscheinlich fehlt nur das Laufwerk. Hier ist noch ein Code mit dem Du nicht anfangen kannst: ", e
            messagebox.showerror(title="CiM Fehler", message=ei)
        
        print("======================================")
        sys.exit()

# Hauptprogramm
#root.resizable(False,False)
Listendings = Listendings(root)
#root.protocol("WM_DELETE_WINDOW", bye)
root.mainloop()
