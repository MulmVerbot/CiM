import customtkinter as tk
from tkinter import Menu
from tkinter import messagebox
import json
import os
import sys
import time
import threading
import re
from caldav import DAVClient
from datetime import datetime, timedelta
from tkcalendar import Calendar
import tkinter as Atk


#            _ .-') _             .-') _                   
#           ( (  OO) )           ( OO ) )                  
#           \     .'_  .---.,--./ ,--,'   ,--.   .-----.  
#           ,`'--..._)/_   ||   \ |  |\  /  .'  / ,-.   \ 
#           |  |  \  ' |   ||    \|  | ).  / -. '-'  |  | 
#           |  |   ' | |   ||  .     |/ | .-.  '   .'  /  
#           |  |   / : |   ||  |\    |  ' \  |  |.'  /__  
#           |  '--'  / |   ||  | \   |  \  `'  /|       | 
#           `-------'  `---'`--'  `--'   `----' `-------'  <-2024 - 2025->

class TodoApp:
    def __init__(self, root):
        self.root = root
        self.Version = "Beta 1.2.12"
        self.Programm_Name = "TotDo Liste"
        self.Zeit = "Die Zeit ist eine Illusion."
        self.Zeit_text = None
        self.root.title(self.Programm_Name + " " + self.Version)
        self.Todo_offen = False
        self.Programm_läuft = True
        self.Mod_Suche_aktiv = True
        self.Autospeichern = True
        self.SSL_Zustand = False  #### Dafür umebdingt eine Einstellung bauen, für externe Netzwerke ist das wichtig!!!!!!!
        self.Benutzerordner = os.path.expanduser('~')
        self.tasks_pfad = os.path.join(self.Benutzerordner, 'CiM', 'Db')
        self.tasks_pfad_datei = os.path.join(self.tasks_pfad, 'tasks.json')
        self.Einstellungsordner_pfad = os.path.join(self.Benutzerordner, 'CiM', 'Einstellungen')
        self.Listenname_speicherort = os.path.join(self.Einstellungsordner_pfad, 'Listenname.txt')
        self.cim_txt_pfad = os.path.join(self.Benutzerordner , "CiM", "cim.txt")
        self.Einstellung_Email_Sender_Adresse = os.path.join(self.Einstellungsordner_pfad, "Email_sender.txt")
        self.Einstellung_smtp_server = os.path.join(self.Einstellungsordner_pfad, "SMTP_Server.txt")
        self.Einstellung_smtp_Passwort = os.path.join(self.Einstellungsordner_pfad, "SMTP_Passwort.txt")
        self.Einstellung_CalDav_Adresse_pfad = os.path.join(self.Einstellungsordner_pfad, "CalDav.txt")

        if sys.platform == "darwin":
            self.Windows = False
            print("[-Plattform-] Darwin")
        else:
            self.Windows = True
            print("[-Plattform-] Windows")

    #### Farben ####
        self.Hintergrund_farbe = "AntiqueWhite2"
        self.Hintergrund_farbe_Text_Widget = "AntiqueWhite2"
        self.Txt_farbe = "White"
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

    #wichtige
        self.f_bg = "gray11"
        self.f_l = "gray13"
        self.f_r = "#272727"   # Die Farbcode aus dem Todo sind aber schon weird oder? hab mich einfach mal an den ihrem Design orientiert
        self.f_e = "#2A2A2A"
        self.f_border = "#232323"
        self.f_r_1 = "#323232"
        self.f_hover_normal = "#424242"
        self.gruen_hell = "LawnGreen"
        self.rot = "firebrick"
        self.orange = "#ff7f24" # Orange
    #### Farben Ende ####

        self.Schriftart = ("Helvetica", 20, "bold")
        self.Schriftart_k = ("Helvetica", 20, "normal")
        self.Schriftart_n = ("Helvetica", 13, "bold")
        self.root.configure(fg_color=self.f_bg)
        self.Uhr_läuft = True
        self.thread_uhr = threading.Timer(1, self.Uhr)
        self.thread_uhr.daemon = True
        self.thread_uhr.start()
        self.thread_CiM = threading.Timer(2, self.Mod_suche)
        self.thread_CiM.daemon = True
        self.thread_CiM.start()
        #self.thread_autospeichern = threading.Timer(1, self.auto_speichern)
        #self.thread_autospeichern.daemon = True
        #self.thread_autospeichern.start()
        self.nur_tag_string = str(time.strftime("%d"))
        self.tag_string = str(time.strftime("%d %m %Y"))
        self.Monat = time.strftime("%m")
        self.zeit_string = time.strftime("%H:%M:%S")
        self.tag_string = str(time.strftime("%d %m %Y"))
        self.Jahr = str(time.strftime("%Y"))

        self.ausgw_zeitpunkt = None
        self.dauer_k = None
        self.Aufgaben_Zahl = 0
        self.Aufgaben_Zahl_erledigt = 0

        try:
            if not os.path.exists(self.tasks_pfad):
                print("[-INFO-] Der Db Ordner scheint nicht zu existieren. Erstelle ihn nun.")
                os.mkdir(self.tasks_pfad)
                print("[-INFO-] Der Db Ordner wurde erfolgreich erstellt.")
        except Exception as ex_einst:
            print("[-ERR-] Fehler beim Erstellen des Db Ordners. Fehlercode:", ex_einst)
        self.TASK_FILE = self.tasks_pfad_datei
        
        self.Zeit = time.strftime("%H:%M:%S")
        try:
            if not os.path.exists(self.Einstellungsordner_pfad):
                os.mkdir(self.Einstellungsordner_pfad)
        except Exception as ex1:
            print(f"konnte den Einstellungsordner nicht erstellen. Fehlercode: {ex1}")

        self.Einstellungen_laden_totdo()
        self.todo_aufmachen()
        self.todo_r_dispawn()

    def Einstellungen_laden_totdo(self):
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
        try:
            with open(self.Einstellung_CalDav_Adresse_pfad, "r") as cl_gel:
                self.Einstellung_CalDav_Adresse = cl_gel.read()
        except Exception as CLDvE:
            print(f"Beim laden der CalDav Einstellungen ist ein Fehler aufgetreten: {CLDvE}")

        self.ID_laden()
        self.Listennamen_laden()

    def ID_laden(self):
        try:
            with open(self.tasks_pfad + "/id.txt", "r") as ID_g:
                self.ID = int(ID_g.read().strip()) # das strp entfernt eventuelle whitespaces
                print(f"Der gespeicherte Stand der IDs liegt nun bei {self.ID}")
        except FileNotFoundError:
            print("Die Datei id.txt wurde nicht gefunden.")
            self.ID = 7572469420
        except ValueError:
            print("Der Inhalt der Datei id.txt ist keine gültige Zahl.")
            self.ID = 7572469420
        except Exception as eid1:
            print(f"Konnte den neusten ID Stand nicht speichern. Fehlercode: {eid1}")
            self.ID = 7572469420
    
    def ID_speichern(self):
        try:
            with open(self.tasks_pfad + "/id.txt", "w+") as ID_s:
                ID_s.write(str(self.ID))
                print(f"Der Stand der IDs liegt bei {self.ID}")
        except Exception as eid:
            print(f"IDs konnten nicht geladen werden. fange nun wieder bei 0 an. Fehlercode: {eid}")
            self.ID = 0

    def Listennamen_laden(self):
        try:
            self.Listenname_l.place_forget()
        except:
            pass
        try:
            with open(self.Listenname_speicherort, "r") as ln:
                self.Listenname = ln.read()
            self.Listenname_l = tk.CTkLabel(self.todo_frame_links, text=self.Listenname, font=self.Schriftart, text_color="DarkSlateGray1")
            self.Listenname_l.place(x=10,y=50)
        except:
            print("konnte den Listennamen nicht lesen.")
            self.Listenname = "Dings"
    
    def Listennamen_speichern(self):
        try:
            with open(self.Listenname_speicherort, "w+") as ln:
                ln.write(self.Ln_beb_e.get()) # nimmt sich aus der Entry für den Listennamen den Namen
                print("Listenname gespeichert.")
            self.top_ln_f.destroy()
            self.Listennamen_laden()
        except:
            print("konnte den Listennamen nicht speichern.")
            self.top_ln_f.destroy()

    def Listen_arten_laden(self):
        print("Lade nun verfügbare Listen")
        try:
            with open(self.andere_Listen_speicheort, "r") as aLs_gel:
                Listen = aLs_gel
            # for dings in Listen:
            #   knopp = button dingse und dann links spawnen
        except Exception as e:
            print(f"Beim laden der Listen gabs einen Fehler: {e}")

    def todo_aufmachen(self):
        self.Todo_offen = True
        self.menu = Menu(root)
        root.configure(menu=self.menu)
        self.menudings = Menu(self.menu, tearoff=0)
        self.Einstellungen = Menu(self.menu, tearoff=0)
        self.menu.add_cascade(label=self.Programm_Name  + " " + self.Version, menu=self.menudings)
        self.menu.add_cascade(label="Einstellungen", menu=self.Einstellungen)
        self.Einstellungen.add_command(label="Listenmamen ändern", command=self.Listenname_change)
        self.menudings.add_command(label="Info", command=self.info)

        self.todo_frame_links = tk.CTkFrame(self.root, fg_color=self.f_bg, border_color=self.f_border, border_width=1, corner_radius=5, width=240)
        self.todo_frame_rechts = tk.CTkScrollableFrame(self.root, fg_color=self.f_bg, border_color=self.f_border, border_width=1, corner_radius=5)
        self.todo_frame_einz = tk.CTkScrollableFrame(self.root, fg_color=self.f_bg, border_color=self.f_border, border_width=1, corner_radius=5)
        self.todo_frame_links.grid(row=1, column=1, padx=(0,0), pady=0, sticky="nsw")  # Links von oben nach unten
        self.todo_frame_einz.grid(row=1, column=2, padx=(0,0), pady=0, sticky="nswe")  # Mittlerer Frame ohne Abstand zu den Seiten
        self.todo_frame_rechts.grid(row=1, column=3, padx=(0,0), pady=0, sticky="nswe")  # Rechts ohne Lücke, füllt bis zum Rand

        # Entry unterm mittleren Frame
        self.Aufgaben_Titel_e = tk.CTkEntry(self.root, text_color="White", fg_color=self.f_e, border_color=self.f_border, border_width=1, corner_radius=5)
        self.Aufgaben_Titel_e.grid(row=2, column=2, padx=(0,0), pady=(10,15), sticky="ew")  # Entry unter dem mittleren Frame

        # Konfiguriere das Grid, damit es sich bei Größenänderungen anpasst
        self.root.grid_columnconfigure(1, weight=2)  # Linker Frame bleibt fest
        self.root.grid_columnconfigure(2, weight=100)  # Mittlerer Frame (self.todo_frame_einz) bekommt den meisten Platz
        self.root.grid_columnconfigure(3, weight=2)  # Rechter Frame passt sich an und füllt bis zum Fensterrand
        self.root.grid_rowconfigure(1, weight=10)    # Erste Zeile (Frames) passt sich der Fenstergröße an
        self.root.grid_rowconfigure(2, weight=0)     # Zweite Zeile (Entry) bleibt fest
        

        self.Aufgabe_hinzufuegen_Knopp = tk.CTkButton(self.root, text="Änderungen speichern", fg_color=self.f_bg, border_color=self.gruen_hell, border_width=1, text_color="White", hover_color=self.f_r_1, cursor="hand2")
        self.Aufgabe_entfernen = tk.CTkButton(self.root, text="Aufgabe entfernen", command=self.aufgabe_loeschen_frage, fg_color=self.f_bg, border_color=self.Border_Farbe, border_width=1, text_color="White", hover_color=self.f_r_1, cursor="hand2")
        self.Aufgabe_hinzufuegen_Knopp.grid(row=2, column=3, padx=(10,10), pady=(10,15), sticky="w")
        self.An_Kalender_senden_start = tk.CTkButton(self.root, text="Kalender Eintrag...", command=self.Kalender_Dialog, border_color=self.orange, fg_color=self.f_e, border_width=1, text_color="White", hover_color=self.f_r_1, cursor="hand2")
        self.Aufgabe_hinzufuegen_Knopp.bind('<Button-1>', self.task_update_knopp)
        self.root.bind('<Return>', self.create_task_button_vor)
        self.Zhe_Clock = tk.CTkLabel(self.todo_frame_links, text=self.Zeit, text_color="White")
        self.Zhe_Clock.place(x=10,y=10)
        self.Aufgaben_Titel_e.bind("<FocusIn>", self.entry_rein)
        self.root.bind("<Double-1>", self.entry_rein)
        self.Datum_fertsch_e = tk.CTkEntry(self.todo_frame_rechts, text_color="White") # hier hinter noch die ganze funktionalität mit einbauen  ### woher kommt das uns seit wann wird das dings aktiv gespawned!?
        self.Datum_fertsch_e.place(x=250,y=840)
        self.Erledigt_Liste_öffnen_knopp = tk.CTkButton(self.root, text="zeige erledigte", command=self.erledigte_Aufgaben_laden, fg_color=self.f_e, border_color=self.f_border, border_width=1, text_color=self.Txt_farbe, hover_color=self.f_hover_normal, cursor="hand2")
        self.Erledigt_Liste_öffnen_knopp.grid(row=2, column=1, padx=(10,10), pady=(10,15), sticky="w")

        self.Warten_lb_info_l = tk.CTkLabel(self.todo_frame_links, text="wartende Aufgaben:", text_color=self.Txt_farbe)
        self.Warten_lb_info_l.place(x=10,y=320)
        
        self.anzahl_aufgaben_info_l = tk.CTkLabel(self.todo_frame_links, text=f"Zu erledigen: {self.Aufgaben_Zahl}", text_color=self.Txt_farbe)
        self.anzahl_aufgaben_info_l.place(x=10,y=50)
        self.anzahl_aufgaben_erledigt_info_l = tk.CTkLabel(self.todo_frame_links, text="bereits erledigt", text_color=self.Txt_farbe)
        self.anzahl_aufgaben_erledigt_info_l.place(x=10,y=70)

        if self.Windows == True:
            self.warten_lb = Atk.Listbox(self.todo_frame_links, width=35, height=10, background=self.f_e, activestyle="none", fg=self.Txt_farbe)
        else:
            self.warten_lb = Atk.Listbox(self.todo_frame_links, width=30, height=10, background=self.f_e, activestyle="none", fg=self.Txt_farbe)
        self.warten_lb.place(x=10,y=350)

        self.load_tasks() # lädt die akuellen Aufgaben

    def info(self):
        print("Programmiert von Maximilian Becker")
        messagebox.showinfo(title=self.Programm_Name, message=f"{self.Programm_Name}\nProgrammiert von: Maximilian Becker\nVersion: {self.Version}\nTeil des Listendings Sets\n2024/25")

    def task_update_knopp(self, event):
        self.task_update()

    def erledigte_Aufgaben_laden(self):
        print("erledigte_Aufgaben_laden(def)")
        self.clear_tasks_frame()
        tasks = self.load_tasks_from_file()
        for task in tasks:
            self.create_task_button_fertsch(task)
        self.Erledigt_Liste_öffnen_knopp.configure(text="unerledigte Aufgaben anzeigen", command=self.load_tasks)

    def Uhr(self):
        print("Thread gestartet: Uhr(def)")
        while self.Uhr_läuft == True:
            lokaler_zeit_string = time.strftime("%H:%M:%S")
            self.Zeit = time.strftime("%H:%M:%S")
            try:
                self.Zhe_Clock.configure(text=f"🕙 {self.Zeit} Uhr")
                root.title(self.Programm_Name + " " + self.Version + "                                                                          " + self.Zeit)
            except Exception as e:
                print(e)
            if self.Zeit_text:
                self.Zeit_text.configure(text=lokaler_zeit_string)
            time.sleep(1)
        print("Thread Beendet: Uhr(def)")

    def Aufgabe_erledigt(self, jdb_pfad, neue_daten, id_a):
        print("beb_speichern_mit_JSON(def)")
        print(f"Bearbeite nun den Eintrag mit folgender ID: {self.task_übergabe["id"]}")
        with open(jdb_pfad, 'r') as f:
            daten = json.load(f)
        # Eintrag suchen und ersetzen
        ersetzt = False
        for index, eintrag in enumerate(daten):
            if eintrag['id'] == id_a:
                daten[index] = neue_daten  # Den Eintrag ersetzen
                ersetzt = True
                break
        if ersetzt:
            # Datei mit den neuen Daten speichern
            with open(jdb_pfad, 'w') as f:
                json.dump(daten, f, ensure_ascii=False, indent=4)
            print(f"Eintrag mit ID_L {id_a} erfolgreich ersetzt.")
        else:
            print(f"Kein Eintrag mit ID_a {id_a} gefunden.")

    def l_ja(self):
        self.neuer_eintrag = {
            "name": self.task_übergabe["name"],
            "description": self.task_übergabe["description"],
            "Uhrzeit": self.task_übergabe["Uhrzeit"],
            "notizen": self.task_übergabe["notizen"],
            "id": self.task_übergabe["id"],
            "fertsch": True, # das hier wird immer auf True gesetzt weil es ja der sinn der Funktion ist.
            "warten": self.task_übergabe["warten"],
            'warten_seit': "-"
        }
        self.Aufgabe_erledigt(self.tasks_pfad_datei, self.neuer_eintrag, self.task_übergabe["id"])
        self.refresh_tasks()

    def l_nein(self):
        pass

    def Listenname_change(self): # Den Namen der Liste ändern
        print("Listenname_change (def)")
        self.top_ln_f = tk.CTkToplevel()
        self.top_ln_f.configure(resizeable=False)
        self.top_ln_f.title=("Den Namen der Liste bearbeiten")
        self.Ln_beb_e = tk.CTkEntry(self.top_ln_f)
        self.Ln_beb_e.pack()
        width = 100
        height = 100
        def mittig_fenster(width, height):
            fenster_breite = root.winfo_screenwidth()
            fenster_hoehe = root.winfo_screenheight()
            x = (fenster_breite - width) // 2
            y = (fenster_hoehe - height) // 2
            self.top_ln_f.geometry(f"{width}x{height}+{x}+{y}")
        mittig_fenster(width, height)
        self.sp_ln = tk.CTkButton(self.top_ln_f, text="Speichern", command=self.Listennamen_speichern, cursor="hand2")
        self.sp_ln.pack(pady=10,padx=10)
        #btn und dann die funktion

    def todo_zumachen(self):
        print("todo_zumachen(def)")
        try:
            self.button.pack_forget()
        except:
            print("button ist noch da.")
        self.todo_frame_links.place_forget()
        self.todo_frame_rechts.place_forget()
        self.todo_frame_einz.place_forget()
        self.Aufgaben_Titel_t.place_forget()
        self.Aufgaben_Beschreibung_t.place_forget()
        self.Aufgabe_hinzufuegen_Knopp.place_forget()
        self.Todo_offen = False

    def create_task_button_vor(self, event):
        task_name = None
        task_description = None
        task_name = self.Aufgaben_Titel_e.get().strip()
        fertsch_var = False
        warten_seit_var = None
        if task_name == None:
            task_name = self.Aufgaben_Titel_t.get()
        try:
            task_description = self.Aufgaben_Beschreibung_t.get("0.0", "end").strip()
        except:
            print("desc war leer")
            task_description = ""
        try:
            task_notizen = self.Notizen_feld.get("0.0", "end").strip()
        except:
            print("Notizen war leer")
            task_notizen = ""
        #self.Zeit = time.strftime("%H:%M:%S")
        jetzt = time.localtime()
        self.Zeit_mit_Datum = time.strftime("%d.%m.%Y %H:%M:%S", jetzt)
        try:
            self.Datum_fertsch = self.Datum_fertsch_e.get()
        except:
            print("Die Zeit existiert nicht.")
            self.Datum_fertsch = "Die Zeit existiert nicht."
    
        if task_name:
            if task_description == "" or None:
                task_description = "-"
            if task_notizen == "" or None:
                task_notizen = "-"
            if fertsch_var == "" or None:
                fertsch_var = False
            if warten_seit_var == "" or None:
                warten_seit_var = "-"

            
            warten_var = False
            self.task = {'name': task_name, 
                         'description': task_description, 
                         'Uhrzeit': self.Zeit_mit_Datum, 
                         'notizen': task_notizen, 
                         'id': self.ID, 
                         'fertsch': fertsch_var, 
                         'warten': warten_var,
                         'warten_seit': warten_seit_var}
            self.ID += 1
            self.ID_speichern()
            self.Aufgaben_Titel_e.delete(0, tk.END) # das hier wird immmer klappen weil... naja. ohne Aufgabentitel auch keine Aufgabe!
            try:
                self.Notizen_feld.delete("0.0", tk.END)
                self.Aufgaben_Beschreibung_t.delete("0.0", tk.END)
                self.Aufgaben_Titel_t.delete("0.0", tk.END)
            except: # Das failed eigentlich nur wenn man seit dem das Programm offen ist nie eine Aufgabe offen hatte == Die Felder wurden nie gespawned, das heißt: wenn eins failed, würden es auch die anderen.
                pass
            self.save_task(self.task)
            self.create_task_button(self.task)
            self.button.invoke()
        else:
            messagebox.showerror(title=self.Programm_Name, message="Bitte geben Sie zuerst einen Aufgabentitel ein.")
        
        ## kriegt immer die des als letztes gesetzen  // worfür ist diese Notiz??? /// tchjoar... //// naja..

    def jsons_durchsuchen(self): # das hier ist teoretisch der Code zum durchsuchen der json dateien (unfertig))
        try:
            print("lade die momentan gespeicherten Tasks.json...")
            with open(self.tasks_pfad_datei, "r", encoding='utf-8') as t_datei:
                daten_tasks_datei = json.load(t_datei)
                print(f"Das hier hab ich darin gefunden: \n\n {daten_tasks_datei}\n\n")
        except Exception as E:
            daten_tasks_datei = ""
        
    def task_update(self): # Das bearbeite speichern
        print("task_updatae(def)")
        ID_der_gewählten_Aufgabe = None
        task_name = None

        task = self.task_übergabe #  heißt beim cim "self.Eintrag_geladen_jetzt"
        ID_der_gewählten_Aufgabe = task['id']
        tasks = self.load_tasks_from_file()
        tasks = [t for t in tasks if t['id'] != task['id']]
        with open(self.TASK_FILE, 'w') as file:
            json.dump(tasks, file, indent=4)
        
        task_name = self.Aufgaben_Titel_t.get("0.0", "end").strip()
        if not task_name or task_name == "":
            task_name = "Aufgabe"
        task_description = self.Aufgaben_Beschreibung_t.get("0.0", "end").strip()
        task_notizen = self.Notizen_feld.get("0.0", "end").strip()
        self.Zeit_var = self.task['Uhrzeit']
        #print(f"Die Uhrzeit sollte bei {self.task['Uhrzeit']} stehen.")

        if task_description == "" or None:
            task_description = "-"
        if task_notizen == "" or None:
            task_notizen = "-"
        self.task = {'name': task_name, 
                     'description': task_description, 
                     'Uhrzeit': self.Zeit_var, 
                     'notizen': task_notizen, 
                     'id': ID_der_gewählten_Aufgabe, 
                     'fertsch': task["fertsch"], 
                     'warten': task['warten'],
                     'warten_seit': task['warten_seit']}
        self.save_task(self.task)
        self.create_task_button(self.task)
        self.refresh_tasks()
        self.button.invoke()
        

    def create_task_button(self, task):
        self.task = task
        self.task_übergabe = task
        def weghauen(): # callback zum löschen
            self.show_task(task)
            self.aufgabe_loeschen_frage()

        

        try:
            if task['fertsch'] == True:
                self.Aufgaben_Zahl_erledigt += 1
                self.anzahl_aufgaben_erledigt_info_l.configure(text=f"bereits erledigt: {self.Aufgaben_Zahl_erledigt}")
                #print(f"Aufgabe wird versteckt weil task['fertsch'] == {task['fertsch']} ist.")
            else:
                #wenn es fertsch ist müssen wir es nicht im warten fenster lassen, also kein elif

                if task['warten'] == True:
                    self.warten_lb.insert(tk.END, f"ID: {task['id']}    {task['name']}")
                    self.warten_lb.bind("<<ListboxSelect>>", self.show_task(task))
                    #self.warten_lb.bind("<<ListboxSelect>>", lambda t=task: self.show_task(t))
                    self.Aufgaben_Zahl += 1
                    self.anzahl_aufgaben_info_l.configure(text=f"Zu erledigen: {self.Aufgaben_Zahl}")
                else:
                    self.Aufgaben_Zahl += 1
                    self.anzahl_aufgaben_info_l.configure(text=f"Zu erledigen: {self.Aufgaben_Zahl}")
                    self.Knopp_frame = tk.CTkFrame(self.todo_frame_einz, fg_color="transparent")
                    self.Knopp_frame.pack(padx=10, pady=1)
                    self.button = tk.CTkButton(self.Knopp_frame, text=f"ID: {task['id']}    {task['name']}", command=lambda t=task: self.show_task(t), fg_color=self.f_e, border_color=self.f_border, border_width=1, text_color="White", hover_color=self.f_r_1, width=1290, anchor="w", cursor="hand2")
                    self.fertsch_knopp = tk.CTkButton(self.Knopp_frame, text="▢", width=10, command=weghauen, border_color=self.rot, fg_color=self.f_e, border_width=1, text_color="White", hover_color=self.f_r_1, cursor="hand2")
                    self.fertsch_knopp.pack(side=tk.LEFT)
                    self.button.pack(side=tk.LEFT)
        except KeyError:
            print("task['fertsch'] war noch nicht in der DB vorhanden.")
            self.Aufgaben_Zahl += 1
            self.anzahl_aufgaben_info_l.configure(text=f"Zu erledigen: {self.Aufgaben_Zahl}")
            self.Knopp_frame = tk.CTkFrame(self.todo_frame_einz, fg_color="transparent")
            self.Knopp_frame.pack(padx=10, pady=1)
            self.button = tk.CTkButton(self.Knopp_frame, text=f"ID: {task['id']}    {task['name']}", command=lambda t=task: self.show_task(t), fg_color=self.f_e, border_color=self.f_border, border_width=1, text_color="White", hover_color=self.f_r_1, width=1290, anchor="w", cursor="hand2")
            self.fertsch_knopp = tk.CTkButton(self.Knopp_frame, text="▢", width=10, command=weghauen, border_color=self.rot, fg_color=self.f_e, border_width=1, text_color="White", hover_color=self.f_r_1, cursor="hand2")
            self.fertsch_knopp.pack(side=tk.LEFT)
            self.button.pack(side=tk.LEFT)

    def create_task_button_fertsch(self, task): # :: ich seh schon, irgendwann muss ich das in nen eigenen Thread umlagern wenn die Listen zu groß werden
        def weghauen_fertsch(): # callback zum löschen
            self.show_task(task)
            self.Aufgabe_wiederherstellen_frage()

        try:
            if task['fertsch'] == False:
                #print(f"Aufgabe wird versteckt weil task['fertsch'] == {task['fertsch']} ist. (Die fertigen Aufgaben werden angezeigt.)")
                pass
            else:
                if task['warten'] == True:
                    print("Es wird gewartet und diese task in die treeview gepackt")
                self.Knopp_frame = tk.CTkFrame(self.todo_frame_einz, fg_color="transparent")
                self.Knopp_frame.pack(padx=10, pady=1)
                self.button = tk.CTkButton(self.Knopp_frame, text=f"ID: {task['id']}    {task['name']}", command=lambda t=task: self.show_task(t), fg_color=self.f_e, border_color=self.f_border, border_width=1, text_color="White", hover_color=self.f_r_1, width=1290, anchor="w", cursor="hand2")
                self.fertsch_knopp = tk.CTkButton(self.Knopp_frame, text="☑", width=10, command=weghauen_fertsch, border_color=self.gruen_hell, fg_color=self.f_e, border_width=1, text_color="White", hover_color=self.f_r_1, cursor="hand2")
                self.fertsch_knopp.pack(side=tk.LEFT)
                self.button.pack(side=tk.LEFT)
        except KeyError:
            print("task['fertsch'] war noch nicht in der DB vorhanden und wird dennoch angezeigt.")
            self.Knopp_frame = tk.CTkFrame(self.todo_frame_einz, fg_color="transparent")
            self.Knopp_frame.pack(padx=10, pady=1)
            self.button = tk.CTkButton(self.Knopp_frame, text=f"ID: {task['id']}    {task['name']}", command=lambda t=task: self.show_task(t), fg_color=self.f_e, border_color=self.f_border, border_width=1, text_color="White", hover_color=self.f_r_1, width=1290, anchor="w", cursor="hand2")
            self.fertsch_knopp = tk.CTkButton(self.Knopp_frame, text="X", width=10, command=weghauen_fertsch, border_color=self.gruen_hell, fg_color=self.f_e, border_width=1, text_color="White", hover_color=self.f_r_1, cursor="hand2")
            self.fertsch_knopp.pack(side=tk.LEFT)
            self.button.pack(side=tk.LEFT)


    def Aufgabe_wiederherstellen_frage(self):
        print("Aufgabe_wiederherstellen_frage(def)")
        antw = messagebox.askyesno(title=self.Programm_Name, message=f"Soll diese Aufgabe wiederhergestellt werden?")
        if antw == True:
            print("Wiederherstellung vom Nutzer bestätigt.")
            self.Aufgabe_wiederherstellen()
        else:
            print("Wiederherstellung vom Nutzer abgebrochen.")

    def Aufgabe_wiederherstellen(self):  ### jetzt hab ich hier schonwieder nachträglich was ändern müssen, können wir das nicht mal in EINE methode auslagern statt drei?
        try:
            self.neuer_eintrag = {
                "name": self.task_übergabe["name"],
                "description": self.task_übergabe["description"],
                "Uhrzeit": self.task_übergabe["Uhrzeit"],
                "notizen": self.task_übergabe["notizen"],
                "id": self.task_übergabe["id"],
                "fertsch": False, # das hier wird immer auf False gesetzt, weil es ja der Sinn der Funktion ist.
                "warten": False,
                "warten_seit": self.task_übergabe["warten_seit"]
            }
        except KeyError:
            messagebox.showerror(title=self.Programm_Name, message="Schwerer Fehler beim schreiben in die Datenbank: KeyError, Vorgang wird abgebrochen.")
            return
        self.Aufgabe_erledigt(self.tasks_pfad_datei, self.neuer_eintrag, self.task_übergabe["id"])
        self.refresh_tasks()
    

    

    def entry_rein(self, event):
        print("despawn durch entry")
        self.todo_r_dispawn()
        self.todo_r_dispawn() # das ganze hier wird zweimal gemacht damit FALLS ich mal vergessen hab was zu entfernen / es da irgendwie nen bug gibt, ich sicher gehen kann dass alles verschwindet. entfern die Zeile mal und schau was passiert! :P
        self.Aufgaben_erstellen_akt(event)

    def todo_r_dispawn(self):
        try: ### Bitte frag nicht wie es zu diesem shais hier gekommen ist...
            self.Aufgaben_Beschreibung_t.delete("1.0", tk.END)
        except Exception as e:
            print(f"Fehler beim Löschen von Aufgaben_Beschreibung_t: {e}")
        try:
            self.Notizen_feld.delete("1.0", tk.END)
        except Exception as e:
            print(f"Fehler beim Löschen von Notizen_feld: {e}")
        try:
            self.Aufgaben_Titel_t.grid_forget()
        except Exception as e:
            print(f"Fehler beim Verstecken von Aufgaben_Titel_t: {e}")
        try:
            self.Aufgabe_entfernen.grid_forget()
        except Exception as e:
            print(f"Fehler beim Verstecken von Aufgabe_entfernen: {e}")
        try:
            self.Aufgaben_Beschreibung_t.grid_forget()
        except Exception as e:
            print(f"Fehler beim Verstecken von Aufgaben_Beschreibung_t: {e}")
        try:
            self.Notizen_feld.grid_forget()
        except Exception as e:
            print(f"Fehler beim Verstecken von Notizen_feld: {e}")
        try:
            self.Uhrzeit_text_l.grid_forget()
        except Exception as e:
            print(f"Fehler beim Verstecken von Uhrzeit_text_l: {e}")
        try:
            self.ID_label.grid_forget()
        except Exception as e:
            print(f"Fehler beim Verstecken von ID_label: {e}")
        try:
            self.Aufgaben_Beschreibung_l.grid_forget()
        except Exception as e:
            print(f"Fehler beim Verstecken von Aufgaben_Beschreibung_l: {e}")
        try:
            self.Aufgaben_Notizen_l.grid_forget()
        except Exception as e:
            print(f"Fehler beim Verstecken von Aufgaben_Beschreibung_l: {e}")
        try:
            self.Datum_fertsch_e.grid_forget()
        except Exception as e:
            print(f"Fehler beim Verstecken von Aufgaben_Beschreibung_l: {e}")      
        try:
             self.warten_aktivieren_knopp.grid_forget()
        except Exception as e:
            print(f"Fehler beim Verstecken von self.warten_aktivieren_knopp: {e}")
        try:
            self.An_Kalender_senden_start.grid_forget()
        except:
            pass
        try:
            self.warten_aus_knopp.grid_forget()
        except:
            pass
        try:
            self.warten_seit_l.grid_forget()
        except:
            pass
        try:
            self.kalender_eintrag_am_l.grid_forget()
        except:
            pass

    def Aufgaben_erstelle_deak(self, event):
        print("Aufgaben_erstelle_deak(def)")
        self.root.unbind('<Return>')

    def Aufgaben_erstellen_akt(self, event):   # Das hier wird immer ausgeführt wenn ich aufs Fenster clicke um die Enter Taste zu reaktivieren und zukünftig die Aufgabe gleich mit zu speichern
        print("Aufgaben_erstellen_akt(def)")
        self.root.bind('<Return>', self.create_task_button_vor)
        try:
            self.Aufgaben_Titel_t.unbind("<FocusIn>")
        except:
            print("self.Aufgaben_Titel_t.unbind fehlgeschlagen")
        try:
            self.Notizen_feld.unbind("<FocusIn>")
        except:
            print("self.Notizen_feld.unbind fehlgeschlagen")
        try:
            self.Aufgaben_Titel_t.unbind("<FocusIn>")
        except:
            print("self.Aufgaben_Titel_t.unbind fehlgeschlagen")

    def show_task(self, task): # Das hier wird jedesmal ausgeführt wenn jemand eine Aufgabe anclickt
        print("Aufgabe anzeigen")
        self.task = task
        self.task_übergabe = task # im cim würde diese Variable jetzt "self.Eintrag_geladen_jetzt" oderso heißen << RT Danke für diese Doku, hätte jetzt wieder ewig gesucht
        ## Das hier oben ist auch wieder mega dumm gelöst weil die var drüber bereits existert, 
        ## ich bin nur gerade zu faul zu gucken ob die zu fürhezeitig wieder freigegeben wird.
        self.todo_r_dispawn()

        self.Notizen_feld = tk.CTkTextbox(self.todo_frame_rechts, text_color="White", fg_color=self.f_r_1, wrap="word", border_width=0, width=380)  # Das hier ist das einzige, das in der breite angepasst werden muss.
        self.ID_label = tk.CTkLabel(self.todo_frame_rechts, text=f"Aufgaben-ID:  {task['id']}", text_color="White", font=self.Schriftart_n)
        
        try:
            self.kalender_eintrag_am_l = tk.CTkLabel(self.todo_frame_rechts, text=f"Kalendereintrag am: {task['Kalendereintrag_am']}", text_color="White") 
        except KeyError:
            print("Key Error für task['Kalendereintrag_am']")
            self.kalender_eintrag_am_l = tk.CTkLabel(self.todo_frame_rechts, text=f"Kalendereintrag am: -", text_color="White") 

        self.Aufgaben_Titel_t = tk.CTkTextbox(self.todo_frame_rechts, width=330, height=45, text_color="White", fg_color=self.f_r_1, wrap="word", border_width=0, activate_scrollbars=False)
        self.Aufgaben_Beschreibung_t = tk.CTkTextbox(self.todo_frame_rechts, width=330, height=120, text_color="White", fg_color=self.f_r_1, wrap="word", border_width=0)
        self.Aufgaben_Beschreibung_l = tk.CTkLabel(self.todo_frame_rechts, text="Beschreibung:", text_color="White")
        self.Aufgaben_Notizen_l = tk.CTkLabel(self.todo_frame_rechts, text="Notizen:", text_color="White")
        self.Uhrzeit_text_l = tk.CTkLabel(self.todo_frame_rechts, text=f"Aufgabe von: {task['Uhrzeit']}Uhr", text_color="White")
        self.Notizen_feld.insert(tk.END, f"{task['notizen']}")
        self.Aufgaben_Titel_t.insert(tk.END, f"{task['name']}")
        self.Aufgaben_Titel_t.grid(row=0, column=0, padx=10, pady=(0, 20), sticky="ew")   # Aufgaben-Titel oben
        self.ID_label.grid(row=1, column=0, padx=10, pady=(0, 5), sticky="w")             # ID unter dem Titel
        self.kalender_eintrag_am_l.grid(row=1, column=0, padx=10, pady=(45, 0), sticky="w")  
        self.Uhrzeit_text_l.grid(row=0, column=0, padx=10, pady=(50, 0), sticky="w")       # Uhrzeit unter der ID
        self.Aufgaben_Beschreibung_l.grid(row=3, column=0, padx=10, pady=(5, 5), sticky="w")  # "Beschreibung"-Label
        self.Aufgaben_Beschreibung_t.grid(row=4, column=0, padx=10, pady=(5, 5), sticky="ew") # Beschreibungstextfeld
        self.Aufgaben_Notizen_l.grid(row=5, column=0, padx=10, pady=(5, 5), sticky="w")   # "Notizen"-Label
        self.Notizen_feld.grid(row=6, column=0, padx=10, pady=(5, 10), sticky="ew")       # Notizenfeld am Ende
        self.Aufgaben_Beschreibung_t.insert(tk.END, f"{task['description']}")
        self.Aufgaben_Beschreibung_t.bind("<FocusIn>", self.Aufgaben_erstelle_deak)
        self.Notizen_feld.bind("<FocusIn>", self.Aufgaben_erstelle_deak)

        self.warten_aktivieren_knopp = tk.CTkButton(self.root, text="warten", command=self.warten_stellen, width=100, border_color=self.helle_farbe_für_knopfe, fg_color=self.f_e, border_width=1, text_color="White", hover_color=self.f_r_1, cursor="hand2")
        self.warten_aus_knopp = tk.CTkButton(self.root, text="freigeben", command=self.warten_nicht_stellen, width=100, border_color=self.helle_farbe_für_knopfe, fg_color=self.f_e, border_width=1, text_color="White", hover_color=self.f_r_1, cursor="hand2")
        self.warten_lb.bind("<<ListboxSelect>>",  self.LB_ausgewaehlt)
        
        self.An_Kalender_senden_start.grid(row=2, column=3, padx=(170,00), pady=(10,15), sticky="w")
        if self.task_übergabe["warten"] == True:
            self.warten_aus_knopp.grid(row=2, column=3, padx=(320,00), pady=(10,15), sticky="w")
        else:
            self.warten_aktivieren_knopp.grid(row=2, column=3, padx=(320,00), pady=(10,15), sticky="w")

        try:
            self.warten_seit_l = tk.CTkLabel(self.todo_frame_rechts, text=f"Warten seit: {task['warten_seit']}", text_color="White")
        except KeyError:
            print("Key Error für task['warten_seit']")
            self.warten_seit_l = tk.CTkLabel(self.todo_frame_rechts, text="Warten seit: -", text_color="White")
        self.warten_seit_l.grid(row=2, column=0, padx=10, pady=(0, 5), sticky="w") 

        


    def lade_eintrag_aus_json_nach_id(self, aufgaben_id):
        Eintrag_v = self.load_tasks_from_file()
        for Dings in Eintrag_v:
            if Dings['id'] == aufgaben_id:
                self.ausgewaehlter_Eintrag = Dings
                return Dings
        return None

    def LB_ausgewaehlt(self, event):
        print("LB_ausgewaehlt(def)")
        auswahl = self.warten_lb.curselection()
        print(f"Das hier wurde ausgewählt: {auswahl}")
        if auswahl:
            print("auswahl existiert.")
            index = auswahl[0]
            auswahl = self.warten_lb.get(index)
            # ach du shaise, bitte frag nicht, ich weiß doch auch nichts besseres
       
            dings_in_lb_suchen = re.search(r'ID:\s*(\d+)', auswahl)
            eintrag_id = int(dings_in_lb_suchen.group(1)) if dings_in_lb_suchen else None
            self.task_übergabe = self.lade_eintrag_aus_json_nach_id(eintrag_id) # anhand der ID, duruchsuchen wir jetzt die json nach der zugehörigen Aufgabe

            self.show_task(self.task_übergabe)

    def warten_stellen(self):
        print("warten_stellen(def)")
        jetzt = time.localtime()
        self.Zeit_mit_Datum = time.strftime("%d.%m.%Y %H:%M:%S", jetzt)
        self.neuer_eintrag = {
            "name": self.task_übergabe["name"],
            "description": self.task_übergabe["description"],
            "Uhrzeit": self.task_übergabe["Uhrzeit"],
            "notizen": self.task_übergabe["notizen"],
            "id": self.task_übergabe["id"],
            "fertsch": self.task_übergabe["fertsch"], 
            "warten": True, # das hier wird immer auf True gesetzt weil es ja der sinn der Funktion ist.
            "warten_seit": self.Zeit_mit_Datum
        }
        self.Aufgabe_erledigt(self.tasks_pfad_datei, self.neuer_eintrag, self.task_übergabe["id"])
        self.refresh_tasks()

    def warten_nicht_stellen(self):
        print("warten_stellen(def)")
        self.neuer_eintrag = {
            "name": self.task_übergabe["name"],
            "description": self.task_übergabe["description"],
            "Uhrzeit": self.task_übergabe["Uhrzeit"],
            "notizen": self.task_übergabe["notizen"],
            "id": self.task_übergabe["id"],
            "fertsch": self.task_übergabe["fertsch"], # das hier wird immer auf True gesetzt weil es ja der sinn der Funktion ist.
            "warten": False,
            "warten_seit": "nicht warten"
        }
        self.Aufgabe_erledigt(self.tasks_pfad_datei, self.neuer_eintrag, self.task_übergabe["id"])
        self.refresh_tasks()
    
    def auto_speichern(self):
        print("Thread fürs autospeichern läuft.")
        while self.Autospeichern == True:
            time.sleep(1)
            self.task_update()
        print("Thread fürs autospeichern beendet.")


    def aufgabe_loeschen_frage(self):
        antw = messagebox.askyesno(title=self.Programm_Name, message=f"INFO: gelöschte Aufgaben können wiederhergestellt werden.")
        if antw:
            if antw == True:
                self.l_ja()
            elif antw == False:
                self.l_nein()
        
    def Mod_suche(self): # Das hier ist die Funktion die jede sekunde nachschaut ob es vom CiM eine neue Aufgabe gibt.
        print(f"Mod suche läuft, suche unter {self.cim_txt_pfad}") # Das ist mega fehleranfällig und manchmal stürzt das ding auch einfach so krass ab dass sich das ganze Programm schließt aber ich bin zu faul einfach die JSON zu bearbeiten.
        while self.Mod_Suche_aktiv == True:
            try:
                with open(self.cim_txt_pfad, "r") as cim_g:
                    self.cim = cim_g.read()
                    try:
                        os.remove(self.cim_txt_pfad)
                        print("cim.txt wieder gelöscht.")
                    except:
                        pass
                if self.cim != None:
                    match = None
                    print("wir haben nun eine Aufgabe vom M.U.L.M erhalten")
                    match = re.search(r'Anrufer: (.+)', self.cim)
                    if match != None:
                        anrufer_info = match.group(1)
                        print(f'Anrufer: {anrufer_info}')
                    else:
                        print('Anrufer nicht gefunden')
                        anrufer_info = "Aufgabe aus dem M.U.L.M"

                    task_name = anrufer_info
                    task_description = self.cim
                    task_notizen = "Aufgabe aus dem M.U.L.M"
                    self.Zeit_var = time.strftime("%H:%M:%S")
                    if task_name:
                        if not task_description:
                            task_description = "-"
                        if not task_notizen:
                            task_notizen = "-"
                        self.task = {'name': task_name, 
                                     'description': task_description, 
                                     'Uhrzeit': self.Zeit_var, 
                                     'notizen': task_notizen, 
                                     'id': self.ID, 
                                     'fertsch': False, 
                                     'warten': False,
                                     'warten_seit': "-"}
                        print(f"ich speichere jetzt das hier: {self.task}")
                        self.ID += 1
                        self.cim = None
                        self.ID_speichern()
                        self.save_task(self.task)
                        self.create_task_button(self.task)
                        self.button.invoke()
            except:
                pass
            time.sleep(1)
    
    def Checklisten_editor_start(self):
        print("Checklisten_editor_start(def)")
        Checklisten_Editor_Fenster = tk.CTkToplevel()

    def Kalender_eintrag_erstellen(self):
        print("Erstelle einen Kalendereintrag")

        self.icalendar_event = None
        startzeit = self.ausgw_zeitpunkt
        endzeit = startzeit + timedelta(minutes=self.dauer_k)
        
        Kalender_Eintrag_zusammenfassung = f"{self.task_übergabe['name']}"
        Kalender_eintrag_beschreibung = f"{self.task_übergabe['description']}"
        Kalender_Eintrag_Ort = f"ID: {self.task_übergabe['id']}"
        try:
            client = DAVClient(
                url=f"{self.Einstellung_CalDav_Adresse}",
                username=f"{self.sender_email}",
                password=f"{self.pw_email}",
                ssl_verify_cert=self.SSL_Zustand
            )

            principal = client.principal()
            calendars = principal.calendars()
            if not calendars:
                raise Exception("Keine Kalender gefunden!")
            calendar = calendars[0]  # Erster gefundener Kalender

        # Die formatierung MUSS so sein!
            self.icalendar_event = f"""
BEGIN:VCALENDAR
VERSION:2.0
PRODID:-//CiM//Totdo//DE
BEGIN:VEVENT
UID:unique-id-{datetime.now().timestamp()}@dings.software
DTSTAMP:{datetime.now().strftime('%Y%m%dT%H%M%SZ')}
DTSTART:{startzeit.strftime('%Y%m%dT%H%M%SZ')}
DTEND:{endzeit.strftime('%Y%m%dT%H%M%SZ')}
SUMMARY:{Kalender_Eintrag_zusammenfassung}
DESCRIPTION:{Kalender_eintrag_beschreibung}
LOCATION:{Kalender_Eintrag_Ort}
END:VEVENT
END:VCALENDAR
"""
            
            calendar.add_event(self.icalendar_event)
            print( self.icalendar_event)
            messagebox.showinfo(title=self.Programm_Name, message=f"Kalendereintrag für den {endzeit.strftime('%Y%m%dT%H%M%SZ')} erstellt.")
        except Exception as KDe1:
            messagebox.showerror(title=self.Programm_Name, message=f"Beim erstellen des Kalendereintrages ist ein Fehler aufgreten: {KDe1}")

    
    def Kalender_Dialog(self):
        def speichern_u_zumachen(event=None):
            # Datum und Uhrzeit auslesen
            date = cal.selection_get()
            time = time_entry.get()
            dauer_k = dauer_k_entry.get()

            try:
                ausgw_zeit = datetime.strptime(time, "%H:%M").time()
                self.ausgw_zeitpunkt = datetime.combine(date, ausgw_zeit)
                self.dauer_k = int(dauer_k)
                top.destroy()
                self.Kalender_eintrag_erstellen()
                save_button.unbind('<Button-1>')
                save_button.unbind('<Return>')
            except ValueError:
                fehler_l.config(text="Fehler: Bitte überprüfen Sie die Eingaben.")
            

        top = Atk.Toplevel()
        top.title("Datum, Uhrzeit und Dauer auswählen")
        top.configure(bg=self.f_bg)

        cal_l = Atk.Label(top, text="Wählen Sie ein Datum:", bg=self.f_bg, fg=self.Txt_farbe)
        cal_l.pack(pady=5)
        cal = Calendar(top, date_pattern="yyyy-mm-dd")
        cal.pack(pady=5)
        zeit_l = Atk.Label(top, text="Uhrzeit eingeben (HH:MM):", bg=self.f_bg, fg=self.Txt_farbe)
        zeit_l.pack(pady=5)
        time_entry = Atk.Entry(top)
        time_entry.pack(pady=5)
        dauer_k_label = Atk.Label(top, text="Dauer in Minuten eingeben:", bg=self.f_bg, fg=self.Txt_farbe)
        dauer_k_label.pack(pady=5)
        dauer_k_entry = Atk.Entry(top)
        dauer_k_entry.pack(pady=5)
        fehler_l = Atk.Label(top, text="", fg="red", bg=self.f_bg)
        fehler_l.pack(pady=5)
        save_button = Atk.Button(top, text="Speichern")
        save_button.bind('<Button-1>', speichern_u_zumachen)
        top.bind('<Return>', speichern_u_zumachen) 
        save_button.pack(pady=10)
        
    def save_task(self, task):
        tasks = self.load_tasks_from_file()
        tasks.append(task)
        with open(self.TASK_FILE, 'w') as file:
            json.dump(tasks, file, indent=4)

    def load_tasks(self):
        self.Aufgaben_Zahl = 0
        self.Aufgaben_Zahl_erledigt = 0
        try:
            self.Erledigt_Liste_öffnen_knopp.configure(text="erledigte Aufgaben anzeigen", command=self.erledigte_Aufgaben_laden)
        except Exception as Ex678:
            print(f"self.Erledigt_Liste_öffnen_knopp konnte nicht bearbeitet werden. Fehlermeldung: {Ex678}")
        self.clear_tasks_frame()
        tasks = self.load_tasks_from_file()
        for task in tasks:
            self.create_task_button(task)
                            
    def load_tasks_from_file(self):
        if os.path.exists(self.TASK_FILE):
            with open(self.TASK_FILE, 'r') as file:
                return json.load(file)
        return []

    def delete_task(self, task): ## obsolete
        tasks = self.load_tasks_from_file() # jetzt fehlt hier nurnoch etwas um anhand der ID "fertsch" auf True zu setzen.
        tasks = [t for t in tasks if t['id'] != task['id']]
        with open(self.TASK_FILE, 'w') as file:
            json.dump(tasks, file, indent=4)
        self.refresh_tasks()

    def refresh_tasks(self):
        self.todo_r_dispawn()
        self.clear_tasks_frame()
        self.load_tasks()

    def clear_tasks_frame(self): # entfernt alle bisher gelisteteten Aufgaben (UND ALLE WIDGETS!!!!) aus Frame_einz
        self.warten_lb.delete(0, Atk.END)
        for widget in self.todo_frame_einz.winfo_children():
            widget.destroy()
    
    def neustarten(self):
        self.clear_tasks_frame()
        self.ID_laden()
        self.Listennamen_laden()
        self.todo_aufmachen()

    def bye(self):
        print("(ENDE) Das Programm wurde Beendet, auf wiedersehen! :3 ")
        self.Programm_läuft = False
        self.Uhr_läuft = False
        self.thread_uhr.cancel()
        sys.exit()

if __name__ == "__main__":
    root = tk.CTk()
    width = 1000
    height = 600
    def mittig_fenster(root, width, height):
        fenster_breite = root.winfo_screenwidth()
        fenster_hoehe = root.winfo_screenheight()
        x = (fenster_breite - width) // 2
        y = (fenster_hoehe - height) // 2
        root.geometry(f"{width}x{height}+{x}+{y}")
        root.wm_minsize(1000, 600)
    mittig_fenster(root, width, height)
    app = TodoApp(root)
    root.mainloop()
