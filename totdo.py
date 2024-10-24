import customtkinter as tk
from tkinter import Menu
from tkinter import font
from tkinter import messagebox
import json
import os
import sys
import time
import threading
import re

#            _ .-') _             .-') _                   
#           ( (  OO) )           ( OO ) )                  
#           \     .'_  .---.,--./ ,--,'   ,--.   .-----.  
#           ,`'--..._)/_   ||   \ |  |\  /  .'  / ,-.   \ 
#           |  |  \  ' |   ||    \|  | ).  / -. '-'  |  | 
#           |  |   ' | |   ||  .     |/ | .-.  '   .'  /  
#           |  |   / : |   ||  |\    |  ' \  |  |.'  /__  
#           |  '--'  / |   ||  | \   |  \  `'  /|       | 
#           `-------'  `---'`--'  `--'   `----' `-------'  <-2024 - 2024->

class TodoApp:
    def __init__(self, root):
        self.root = root
        self.Version = "Beta 1.0 (1)"
        self.Programm_Name = "TotDo Liste"
        self.Zeit = "Die Zeit ist eine Illusion."
        self.Zeit_text = None
        self.root.title(self.Programm_Name + " " + self.Version)
        self.Todo_offen = False
        self.Programm_läuft = True
        self.Mod_Suche_aktiv = True
        self.Autospeichern = True
        self.Benutzerordner = os.path.expanduser('~')
        self.tasks_pfad = os.path.join(self.Benutzerordner, 'CiM', 'Db')
        self.tasks_pfad_datei = os.path.join(self.tasks_pfad, 'tasks.json')
        self.Einstellungsordner_pfad = os.path.join(self.Benutzerordner, 'CiM', 'Einstellungen')
        self.Listenname_speicherort = os.path.join(self.Einstellungsordner_pfad, 'Listenname.txt')
        self.cim_txt_pfad = os.path.join(self.Benutzerordner , "CiM", "cim.txt")

    #### Farben ####
        self.Hintergrund_farbe = "AntiqueWhite2"
        self.Hintergrund_farbe_Text_Widget = "AntiqueWhite2"
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

    #wichtige
        self.f_bg = "gray11"
        self.f_l = "gray13"
        self.f_r = "#272727"   # Die Farbcode aus dem Todo sind aber schon weird oder? hab mich einfach mal an den ihrem Design orientiert
        self.f_e = "#2A2A2A"
        self.f_border = "#232323"
        self.f_r_1 = "#323232"
        self.gruen_hell = "LawnGreen"
        self.rot = "firebrick"
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
        
        self.ID_laden()
        self.todo_aufmachen()
        self.fake_laden()
        self.todo_r_dispawn()
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

    def fake_laden(self):
        print("lade nun die ganzen Konzept Sachen")
        y1 = 100
        i = 1
        while i <= 20:
            l = tk.CTkLabel(self.todo_frame_links, text=f"{i}. Liste (zukünftig anclickbar)", text_color="White")
            l.place(x=10,y=y1)
            y1 += 40
            i += 1
        print("Alle Fakes/ Konzepte wurden geladen")

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
        self.Bearbeiten_Menu = Menu(self.menu, tearoff=0)
        self.menu.add_cascade(label=self.Programm_Name  + " " + self.Version, menu=self.menudings)
        self.menu.add_cascade(label="Einstellungen", menu=self.Einstellungen)
        self.menu.add_cascade(label="Bearbeiten", menu=self.Bearbeiten_Menu)
        self.menudings.add_command(label="Info", command=self.info)
        self.Bearbeiten_Menu.add_command(label="Listenmamen ändern", command=self.Listenname_change)
        self.Einstellungen.add_command(label="Liste aktualisieren", command=self.refresh_tasks)
        self.Einstellungen.add_command(label="Aufgabe aktualisieren", command=self.task_update)
        self.Einstellungen.add_command(label="GUI Neustarten", command=self.neustarten)

        self.todo_frame_links = tk.CTkFrame(self.root, fg_color=self.f_bg, border_color=self.f_border, border_width=1, corner_radius=5)
        self.todo_frame_rechts = tk.CTkScrollableFrame(self.root, fg_color=self.f_bg, border_color=self.f_border, border_width=1, corner_radius=5)
        self.todo_frame_einz = tk.CTkScrollableFrame(self.root, fg_color=self.f_bg, border_color=self.f_border, border_width=1, corner_radius=5)
        self.todo_frame_links.grid(row=1, column=1, padx=(0,0), pady=0, sticky="nsw")  # Links von oben nach unten
        self.todo_frame_einz.grid(row=1, column=2, padx=(0,0), pady=0, sticky="nsew")  # Mittlerer Frame ohne Abstand zu den Seiten
        self.todo_frame_rechts.grid(row=1, column=3, padx=(0,0), pady=0, sticky="nswe")  # Rechts ohne Lücke, füllt bis zum Rand

        # Entry unterm mittleren Frame
        self.Aufgaben_Titel_e = tk.CTkEntry(self.root, text_color="White", fg_color=self.f_e, border_color=self.f_border, border_width=1, corner_radius=5)
        self.Aufgaben_Titel_e.grid(row=2, column=2, padx=(0,0), pady=(10,15), sticky="ew")  # Entry unter dem mittleren Frame

        # Konfiguriere das Grid, damit es sich bei Größenänderungen anpasst
        self.root.grid_columnconfigure(1, weight=0)  # Linker Frame bleibt fest
        self.root.grid_columnconfigure(2, weight=3)  # Mittlerer Frame (self.todo_frame_einz) bekommt den meisten Platz
        self.root.grid_columnconfigure(3, weight=1)  # Rechter Frame passt sich an und füllt bis zum Fensterrand
        self.root.grid_rowconfigure(1, weight=10)    # Erste Zeile (Frames) passt sich der Fenstergröße an
        self.root.grid_rowconfigure(2, weight=0)     # Zweite Zeile (Entry) bleibt fest

        self.Aufgabe_hinzufuegen_Knopp = tk.CTkButton(self.root, text="Änderungen speichern", fg_color=self.f_bg, border_color=self.gruen_hell, border_width=1, text_color="White", hover_color=self.f_r_1)
        self.Aufgabe_entfernen = tk.CTkButton(self.root, text="Aufgabe entfernen", command=self.aufgabe_loeschen_frage, fg_color=self.f_bg, border_color=self.Border_Farbe, border_width=1, text_color="White", hover_color=self.f_r_1)
        self.Aufgabe_hinzufuegen_Knopp.grid(row=2, column=3, padx=(10,10), pady=(10,15), sticky="w")
        #self.Aufgabe_entfernen.grid(row=2, column=3, padx=(10,10), pady=(10,15), sticky="w") # das bleibt ersma weg weil das feature eh ersetzt wird.
        
        self.Aufgabe_hinzufuegen_Knopp.bind('<Button-1>', self.task_update_knopp)
        self.root.bind('<Return>', self.create_task_button_vor)
        self.Zhe_Clock = tk.CTkLabel(self.todo_frame_links, text=self.Zeit, text_color="White")
        self.Zhe_Clock.place(x=10,y=10)
        
        self.Aufgaben_Titel_e.bind("<FocusIn>", self.entry_rein)
        self.root.bind("<Double-1>", self.entry_rein)
        try:
            self.Aufgaben_Beschreibung_t.delete("0.0", "end")  # keine Ahnung was das hier macht, aber ich lass das einfach mal hier so stehen.
        except:
            pass

        self.Datum_fertsch_e = tk.CTkEntry(self.todo_frame_rechts, text_color="White") # hier hinter noch die ganze funktionalität mit einbauen
        self.Datum_fertsch_e.place(x=250,y=840)
        self.load_tasks()

    def info(self):
        print("Programmiert von Maximilian Becker")
        messagebox.showinfo(title=self.Programm_Name, message=f"{self.Programm_Name}\nProgrammiert von: Maximilian Becker\nVersion: {self.Version}\nTeil des Listendings Sets\n2024")

    def task_update_knopp(self, event):
        self.task_update()

    def Uhr(self):
        print("Thread gestartet: Uhr(def)")
        while self.Uhr_läuft == True:
            lokaler_zeit_string = time.strftime("%H:%M:%S")
            self.Zeit = time.strftime("%H:%M:%S")
            try:
                self.Zhe_Clock.configure(text=self.Zeit)
                root.title(self.Programm_Name + " " + self.Version + "                                                                          " + self.Zeit)
            except Exception as e:
                print(e)
            if self.Zeit_text:
                self.Zeit_text.configure(text=lokaler_zeit_string)
            time.sleep(1)
        print("Thread Beendet: Uhr(def)")

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
        self.sp_ln = tk.CTkButton(self.top_ln_f, text="Speichern", command=self.Listennamen_speichern)
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
        if task_name == None:
            task_name = self.Aufgaben_Titel_t.get()
        try:
            task_description = self.Aufgaben_Beschreibung_t.get("0.0", "end").strip()
        except:
            print("desc war leeer")
            task_description = ""
        try:
            task_notizen = self.Notizen_feld.get("0.0", "end").strip()
        except:
            print("Notizen war leer")
            task_notizen = ""
        self.Zeit = time.strftime("%H:%M:%S")
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
            #print(f"Hier haste die scheiße ma im Log: {task_notizen} und jetzt die kack beschreibung: {task_description}")
            self.task = {'name': task_name, 'description': task_description, 'Uhrzeit': self.Zeit, 'notizen': task_notizen, 'id': self.ID}
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
            messagebox.showinfo(title=self.Programm_Name, message="Bitte geben Sie zuerst einen Aufgabentitel ein.")
        
        ## kriegt immer die des als letztes gesetzen  // worfür ist diese Notiz???

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

        task = self.task_übergabe
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
        self.Zeit = self.task['Uhrzeit']
        print(f"Die Uhrzeit sollte bei {self.task['Uhrzeit']} stehen.")

        if task_description == "" or None:
            task_description = "-"
        if task_notizen == "" or None:
            task_notizen = "-"
        self.task = {'name': task_name, 'description': task_description, 'Uhrzeit': self.Zeit, 'notizen': task_notizen, 'id': ID_der_gewählten_Aufgabe}
        self.save_task(self.task)
        self.create_task_button(self.task)
        self.refresh_tasks()
        self.button.invoke()
        

    def create_task_button(self, task):
        def weghauen(): # callback zum löschen
            self.show_task(task)
            self.aufgabe_loeschen_frage()

        self.Knopp_frame = tk.CTkFrame(self.todo_frame_einz, fg_color="transparent")
        self.Knopp_frame.pack(padx=10, pady=1)
        self.button = tk.CTkButton(self.Knopp_frame, text=f"Nr. {task['id']}    {task['name']}", command=lambda t=task: self.show_task(t), fg_color=self.f_e, border_color=self.f_border, border_width=1, text_color="White", hover_color=self.f_r_1, width=1290, anchor="w")
        self.fertsch_knopp = tk.CTkButton(self.Knopp_frame, text="X", width=10, command=weghauen, border_color=self.rot, fg_color=self.f_e, border_width=1, text_color="White", hover_color=self.f_r_1)
        self.fertsch_knopp.pack(side=tk.LEFT)
        self.button.pack(side=tk.LEFT)

    

    def l_ja(self):
        self.delete_task(self.task)

    def l_nein(self):
        pass

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

    def Aufgaben_erstelle_deak(self, event):
        print("Aufgaben_erstelle_deak(def)")
        self.root.unbind('<Return>')

    def Aufgaben_erstellen_akt(self, event):   # Das hier wird immer ausgeführt wenn ich aufs Fenster clicke um die Enter Taste zu reaktivieren und zukünftig die Aufgabe gleich mit zu speichern
        print("Aufgaben_erstellen_akt(def)")
        self.root.bind('<Return>', self.create_task_button_vor)
        self.Aufgaben_Titel_t.unbind("<FocusIn>")
        self.Notizen_feld.unbind("<FocusIn>")
        self.Aufgaben_Titel_t.unbind("<FocusIn>")

    def show_task(self, task): # Das hier wird jedesmal ausgeführt wenn jemand eine Aufgabe anclickt
        print("Aufgabe anzeigen")
        self.task = task
        self.task_übergabe = task 
        ## Das hier oben ist auch wieder mega dumm gelöst weil die var drüber bereits existert, 
        ## ich bin nur gerade zu faul zu gucken ob die zu fürhezeitig wieder freigegeben wird. Sorry zukunfst Max!
        self.todo_r_dispawn()

        # Definiere die Widgets im rechten Frame
        self.Notizen_feld = tk.CTkTextbox(self.todo_frame_rechts, text_color="White", fg_color=self.f_r_1, wrap="word", border_width=0)
        self.ID_label = tk.CTkLabel(self.todo_frame_rechts, text=f"Aufgaben-ID:  {task['id']}", text_color="White", font=self.Schriftart_n)
        self.Aufgaben_Titel_t = tk.CTkTextbox(self.todo_frame_rechts, width=330, height=40, text_color="White", fg_color=self.f_r_1, wrap="word", border_width=0, activate_scrollbars=False)
        self.Aufgaben_Beschreibung_t = tk.CTkTextbox(self.todo_frame_rechts, width=330, height=120, text_color="White", fg_color=self.f_r_1, wrap="word", border_width=0)
        self.Aufgaben_Beschreibung_l = tk.CTkLabel(self.todo_frame_rechts, text="Beschreibung:", text_color="White")
        self.Aufgaben_Notizen_l = tk.CTkLabel(self.todo_frame_rechts, text="Notizen:", text_color="White")
        self.Uhrzeit_text_l = tk.CTkLabel(self.todo_frame_rechts, text=f"Aufgabe von: {task['Uhrzeit']}Uhr", text_color="White")
        self.Notizen_feld.insert(tk.END, f"{task['notizen']}")
        self.Aufgaben_Titel_t.insert(tk.END, f"{task['name']}")
        self.Aufgaben_Titel_t.grid(row=0, column=0, padx=10, pady=(10, 5), sticky="ew")   # Aufgaben-Titel oben
        self.ID_label.grid(row=1, column=0, padx=10, pady=(5, 5), sticky="w")             # ID unter dem Titel
        self.Uhrzeit_text_l.grid(row=2, column=0, padx=10, pady=(5, 5), sticky="w")       # Uhrzeit unter der ID
        self.Aufgaben_Beschreibung_l.grid(row=3, column=0, padx=10, pady=(5, 5), sticky="w")  # "Beschreibung"-Label
        self.Aufgaben_Beschreibung_t.grid(row=4, column=0, padx=10, pady=(5, 5), sticky="ew") # Beschreibungstextfeld
        self.Aufgaben_Notizen_l.grid(row=5, column=0, padx=10, pady=(5, 5), sticky="w")   # "Notizen"-Label
        self.Notizen_feld.grid(row=6, column=0, padx=10, pady=(5, 10), sticky="ew")       # Notizenfeld am Ende
        self.Aufgaben_Beschreibung_t.insert(tk.END, f"{task['description']}")
        self.Aufgaben_Beschreibung_t.bind("<FocusIn>", self.Aufgaben_erstelle_deak)
        self.Notizen_feld.bind("<FocusIn>", self.Aufgaben_erstelle_deak)
        
    
    def auto_speichern(self):
        print("Thread fürs autospeichern läuft.")
        while self.Autospeichern == True:
            time.sleep(1)
            self.task_update()
        print("Thread fürs autospeichern beendet.")


    def aufgabe_loeschen_frage(self):
        antw = messagebox.askyesno(title=self.Programm_Name, message=f"INFO: gelöschte Aufgaben können nicht wiederhergestellt werden.")
        if antw:
            if antw == True:
                self.l_ja()
            elif antw == False:
                self.l_nein()
        
    def Mod_suche(self): # Das hier ist die Funktion die jede sekunde nachschaut ob es vom CiM eine neue Aufgabe gibt.
        print("Mod suche läuft")
        print(self.cim_txt_pfad)
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
                    self.Zeit = time.strftime("%H:%M:%S")
                    if task_name:
                        if not task_description:
                            task_description = "-"
                        if not task_notizen:
                            task_notizen = "-"
                        self.task = {'name': task_name, 'description': task_description, 'Uhrzeit': self.Zeit, 'notizen': task_notizen, 'id': self.ID}
                        print(f"ich speichere jetzt das hier: {self.task}")
                        self.ID += 1
                        self.cim = None
                        self.ID_speichern()
                        self.save_task(self.task)
                        self.create_task_button(self.task)
                        self.button.invoke()
                        self.refresh_tasks()
            except:
                pass
            time.sleep(1)
    
    def Checklisten_editor_start(self):
        print("Checklisten_editor_start(def)")
        Checklisten_Editor_Fenster = tk.CTkToplevel()


    def save_task(self, task):
        tasks = self.load_tasks_from_file()
        tasks.append(task)
        with open(self.TASK_FILE, 'w') as file:
            json.dump(tasks, file, indent=4)

    def load_tasks(self):
        self.clear_tasks_frame()
        tasks = self.load_tasks_from_file()
        for task in tasks:
            self.create_task_button(task)
                            
    def load_tasks_from_file(self):
        if os.path.exists(self.TASK_FILE):
            with open(self.TASK_FILE, 'r') as file:
                return json.load(file)
        return []

    def delete_task(self, task):
        tasks = self.load_tasks_from_file()
        tasks = [t for t in tasks if t['id'] != task['id']]
        with open(self.TASK_FILE, 'w') as file:
            json.dump(tasks, file, indent=4)
        self.refresh_tasks()

    def refresh_tasks(self):
        self.todo_r_dispawn()
        self.clear_tasks_frame()
        self.load_tasks()

    def clear_tasks_frame(self):
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
    mittig_fenster(root, width, height)
    app = TodoApp(root)
    root.mainloop()
