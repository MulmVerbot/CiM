try:
    import customtkinter as tk
    ###import tkinter as tk
    from tkinter import ttk
    from tkinter import messagebox
    from tkinter import filedialog
    from tkinter import Menu
    import time
    import os
    import sys
    import csv
    import ctypes
    import json
    from csv2pdf import convert as c2p_convert
    from threading import Thread
except:
    print("(FATAL) Konnte die wichtigen Bilbioteken nicht Laden!")
    messagebox.showerror(title="Kritischer Fehler", message="(FATAL) Konnte die wichtigen Bilbioteken nicht Laden! Das Programm wird nun Beendet.")
    sys.exit()

root = tk.CTk()

class Listendings:
    class Logger(object):
        def __init__(self): #eine init welche nur das "unwichtige" vorgeplänkel macht
            self.tag_und_zeit_string = time.strftime("%m/%d/%Y, %H:%M:%S")
            self.tag_string = str(time.strftime("%d %m %Y"))
            print("[-INFO-] ", self.tag_und_zeit_string)
            try:
                log_pfad = ("CiM Logs/" + self.tag_string + ".log")
                self.terminal = sys.stdout
                self.log = open(log_pfad, "w")
            except:
                try:
                    log_pfad = ("CiM Logs/" + self.tag_string + ".log")
                    self.terminal = sys.stdout
                    self.log = open(log_pfad, "w+")
                except:
                    print("heute keine Logs")
        def write(self, message):
            self.terminal.write(message)
            self.log.write(message)
        def flush(self):
            #für Python 3 wichtig wegen kompatibilität, hab aber keine wirkliche ahnung was das macht
            pass    
    sys.stdout = Logger()

    def __init__(self, master):
        self.master = master
        self.DB = "liste.txt"
        self.Listen_Speicherort_Netzwerk_geladen = None
        self.Zeit_text = None
        Pause = True
        
        self.zeit_string = time.strftime("%H:%M:%S")
        self.tag_string = str(time.strftime("%d %m %Y"))
        print(self.tag_string)
        
        

        try:
            with open("Listendingsspeicherort.json" , "r") as Liste_Speicherort_data:
                self.Listen_Speicherort = json.load(Liste_Speicherort_data)
                self.Listen_Speicherort_geladen = (self.Listen_Speicherort["ListenDings_Speicherort"])
                Listen_Speicherort_Netzwerk_geladen = self.Listen_Speicherort_Netzwerk_geladen
        except PermissionError:
                messagebox.showerror(title="Listendings Speicherort", message="Es Fehlt für diesen Ordner die nötige Berechtigung, Die Kontakliste konnte nicht aufgerufen werden.")
        except:
            messagebox.showerror(title="Listendings Speicherort", message="Der Pfad konnte zwar gelesen werden, allerdings scheint der Ausgewählte Ordner nicht zu existieren.")

        try:
            with open("Listendingsspeicherort_Netzwerk.json" , "r") as Liste_Speicherort_Netzwerk_data:
                self.Listen_Speicherort_Netzwerk = json.load(Liste_Speicherort_Netzwerk_data)
                self.Listen_Speicherort_Netzwerk_geladen = (self.Listen_Speicherort_Netzwerk["ListenDings_Speicherort_Netzwerk"])
        except PermissionError:
                messagebox.showerror(title="Listendings Speicherort", message="Es Fehlt für diesen Ordner die nötige Berechtigung, Der Gespeicherte Netzwerkpfad konnte nicht aufgerufen werden.")
        except Exception as e:
            ex = "Irgendwas ist passiert: ", e
            messagebox.showerror(title="Listendings Speicherort", message=ex)
        Listen_Speicherort_Netzwerk_geladen = self.Listen_Speicherort_Netzwerk_geladen
        



        self.Programm_Name = "Flimmerchen"
        self.Version = "Alpha 1.2.0"
        master.title(self.Programm_Name + " " + self.Version)

        # Labels für Textfelder
        self.kunde_label = tk.CTkLabel(master, text="Kunde:")
        self.problem_label = tk.CTkLabel(master, text="Problem:")
        self.info_label = tk.CTkLabel(master, text="Info:")        

        # Textfelder
        self.kunde_entry = tk.CTkEntry(master,width=1200)
        self.problem_entry = tk.CTkEntry(master,width=1200)
        self.info_entry = tk.CTkEntry(master,width=1200)
        

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
        self.ausgabe_text = tk.CTkTextbox(master, width=1250, height=400)
        ###self.ausgabe_text.configure(highlightthickness=0)
        self.ausgabe_text.configure(state='disabled')
        #self.ausgabe_text.configure(font=("Helvetica", "14"))

        # Positionierung von Labels und Textfeldern
        self.kunde_label.grid(row=0, column=0)
        self.problem_label.grid(row=1, column=0)
        self.info_label.grid(row=2, column=0)

        self.kunde_entry.grid(row=0, column=1)
        self.problem_entry.grid(row=1, column=1)
        self.info_entry.grid(row=2, column=1)
        self.senden_button.grid(row=3, column=1)
        self.ausgabe_text.grid(row=4, column=0, columnspan=2)


        # erschaffen des Column Menü Dings
        self.menu = Menu(root)
        root.configure(menu=self.menu)
        self.menudings = Menu(self.menu, tearoff=0)
        self.Einstellungen = Menu(self.menu, tearoff=0)
        self.Speichern_Menu = Menu(self.menu, tearoff=0)
        self.test_Menu = Menu(self.menu, tearoff=0)
        self.menu.add_cascade(label=self.Programm_Name + self.Version, menu=self.menudings)
        self.menu.add_cascade(label="Einstellungen", menu=self.Einstellungen)
        self.menu.add_cascade(label="Speichern", menu=self.Speichern_Menu)
        self.menu.add_cascade(label="Test", menu=self.test_Menu)
        self.menudings.add_command(label="Info", command=self.info)
        self.menudings.add_command(label="Admin rechte aktivieren", command=self.Admin_rechte)
        self.Einstellungen.add_command(label="Speicherort des ListenDings ändern...", command=self.ListenDings_speicherort_ändern)
        self.Speichern_Menu.add_command(label="als CSV Speichern", command=self.als_csv_speichern_eigener_ort)
        self.Speichern_Menu.add_command(label="Speichern als...", command=self.als_csv_speichern)
        self.test_Menu.add_command(label="Neue GUI starten...", command=self.neue_GUI)
        self.Speichern_Menu.add_command(label="auf dem Netzlaufwerk als CSV Speichern", command=self.Netzlaufwerk_speichern)
        self.Einstellungen.add_command(label="Netzlaufwerk einstellen", command=self.ListenDings_speicherort_Netzwerk_ändern)
        self.Einstellungen.add_command(label="Auto Speichern ändern (Beim schließen)", command=self.Auto_sp_ändern)
        self.test_Menu.add_command(label="Pause", command=self.pause)
        
        # Initialisierung wichtiger Variablen

        self.beb = "0"
        
        try:
            # Ausgabe-Textfeld aktualisieren
            print("(INFO) versuche die alten Aufzeichenungen zu Laden")
            self.ausgabe_text.configure(state='normal')
            with open("liste.txt", "r") as f:
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
        self.menu_frame.place(x=master.winfo_width(), y=50)  # Position it outside the visible area to the right

        # Add buttons to the menu frame
        self.beb_knopp = tk.CTkButton(self.menu_frame, text="Bearbeiten", command=self.beb_c)
        self.beb_knopp.pack(pady=10)  # Add more buttons as needed
        self.alles_löschen_knopp = tk.CTkButton(self.menu_frame, text="Alle Eintrage löschen", command=self.alles_löschen)
        self.alles_löschen_knopp.pack(pady=10)

        # Initially, the menu is hidden
        self.menu_visible = False

        self.toggle_menu_button = tk.CTkButton(master, text="Menü umklappen", command=self.toggle_menu)
        #self.toggle_menu_button.place(x=master.winfo_width() - 200, y=90)  # Adjust position as needed
        self.toggle_menu_button.grid(row=3, column=1)

    def toggle_menu(self):
        start_x = self.master.winfo_width() if self.menu_visible else self.master.winfo_width() - 200  # Assume menu width is 200
        end_x = self.master.winfo_width() - 200 if self.menu_visible else self.master.winfo_width()
        delta_x = -10 if self.menu_visible else 10
        
        for x in range(start_x, end_x, delta_x):
            self.menu_frame.place(x=x, y=50)
            self.menu_frame.update()
            time.sleep(0.01)  # Adjust for smoother animation
        
        self.menu_visible = not self.menu_visible
    
    #### emde der werbung #######
    def info(self):
        print("(INFO) Info(def)")
        messagebox.showinfo(title="Info", message=self.Programm_Name + " " + self.Version + "\n Programmiert von Maximilian Becker, \n https://dings.software für mehr Informationen")

    def Auto_sp_ändern(self):
        print("auto_speichern(def)")
        try:
            with open("auto_speichern.txt", "r") as r_gel:
                self.aSp_var = r_gel.read()
            if self.aSp_var == "Ja":
                self.aSp_var = "Nein"
                with open("auto_speichern.txt", "wb+") as nsp:
                    nsp.write(self.aSp_var)
                    nsp.close()
                    messagebox.showinfo(title="CiM Info", message="Das automatische Speichern wurde deaktiviert.")
            elif self.aSp_var == "Nein":
                self.aSp_var = "Ja"
                with open("auto_speichern.txt", "wb+") as nsp:
                    nsp.write(self.aSp_var)
                    nsp.close()
                    messagebox.showinfo(title="CiM Info", message="Das automatische Speichern wurde aktiviert.")
            else:
                self.aSp_var = "Nein"
                messagebox.showerror(title="CiM", message="Herzlichen Glückwunsch! Du hast das ganze Speicher Dings Kaputt gemacht! Das Automatische speichern wurde deaktiviert. Versuche nun nochmal, diese Funktion zu nutzen.")
                with open("auto_speichern.txt", "wb+") as nsp:
                    nsp.write(self.aSp_var)
                    nsp.close()
                    messagebox.showinfo(title="CiM Info", message="Das automatische Speichern wurde aktiviert.")
        except FileNotFoundError:
            print("Die Datei gabs nicht.")
            self.aSp_var = "Nein"
            with open("auto_speichern.txt", "wb+") as nsp:
                    nsp.write(self.aSp_var)
                    nsp.close()
                    messagebox.showinfo(title="CiM Info", message="Das automatische Speichern wurde aktiviert.")
        except Exception as E:
            Esxi = "Es ist irgendwas Kaputt gegangen, keine Ahnung was. Viel Spaß: ", E
            messagebox.showerror(title="CiM Fehler", message=Esxi)

            


        
        


    def Neuladen_der_Liste(self):
        try:
            # Ausgabe-Textfeld aktualisieren
            print("(INFO) versuche die alten Aufzeichenungen zu Laden")
            self.ausgabe_text.configure(state='normal')
            with open("liste.txt", "r") as f:
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
        self.ausgabe_text.configure(state='normal')
        self.zeit_string = time.strftime("%H:%M:%S")
        
        if kunde or problem or info != "":
            #print("(INFO) Enter gedrückt obwohl etwas geschrieben wurde.")
            if self.kunde_entry.get() == "":
                kunde = "-"
            if self.problem_entry.get() == "":
                problem = "-"
            if self.info_entry.get() == "":
                info = "-"

            # Inhalte in Textdatei speichern
            if os.path.exists("liste.txt"):
                with open("liste.txt", "a") as f:
                    f.write(f"Uhrzeit: {self.zeit_string}\nKunde: {kunde}\nProblem: {problem}\nInfo: {info}\n\n")
                with open("liste.txt", "r") as f:
                    feedback_text = f.read()
                    self.ausgabe_text.delete("1.0", tk.END)
                    self.ausgabe_text.insert(tk.END, feedback_text)
                self.ausgabe_text.configure(state='disabled')
                self.ausgabe_text.see(tk.END)
            else:
                print("(INFO) Liste zum beschreiben existiert bereits.")
                with open("liste.txt", "w+") as f:
                    f.write(f"Uhrzeit: {self.zeit_string}\nKunde: {kunde}\nProblem: {problem}\nInfo: {info}\n\n")
                    # Ausgabe-Textfeld aktualisieren
                with open("liste.txt", "r") as f:
                    feedback_text = f.read()
                    self.ausgabe_text.delete("1.0", tk.END)
                    self.ausgabe_text.insert(tk.END, feedback_text)
                    self.ausgabe_text.configure(state='disabled')

            
        else:
            print("(ERR) Da hat wer Enter gedrückt obwohl noch nicht geschrieben war.")
            messagebox.showinfo(title="Fehler", message="Bitte geben Sie zuerst in wenigsten eine Spalte etwas ein.")
            self.ausgabe_text.configure(state='disabled')
            return
        
        self.kunde_entry.delete(0, tk.END)
        self.problem_entry.delete(0, tk.END)
        self.info_entry.delete(0, tk.END)
    
    def beb_c(self):
        self.text_tk_text = self.ausgabe_text.get("1.0", "end-1c")
        if self.beb == "0":
            print("beb is jetzt = 1")
            self.ausgabe_text.configure(state='normal')
            self.beb_knopp.configure(text="Fertig")# , fg="red"
            #self.alles_löschen_knopp.place_forget()
            self.alles_löschen_knopp.pack_forget()
            self.senden_button.grid_forget()
            self.beb = "1"
            root.unbind('<Return>')
        else:
            print("beb = 0")
            self.ausgabe_text.configure(state='disabled')
            root.bind('<Return>', self.senden)
            self.beb_knopp.configure(text="Bearbeiten") # , fg="black"
            self.senden_button.grid(row=3, column=1)
            #self.alles_löschen_knopp.place(x=1350,y=400)
            self.alles_löschen_knopp.pack(pady=10)
            self.beb = "0"
            with open("liste.txt", "w+") as f:
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
                    #self.ausgabe_text.insert(tk.END, "")
                   # try:                                                                   # aus irgendeinem Grund kackt das Ding bei dem Abschnitt wenn es mehrere einträge gibt ABOSLUT UND KATASTROHPAL AB-> objc[3945]: autorelease pool page 0x7fb7e9b26000 corrupted
                                                                                                                                                                                                                #'''magic     0x00000000 0x00000000 0x00000000 0x00000000
                                                                                                                                                                                                                #should be 0xa1a1a1a1 0x4f545541 0x454c4552 0x21455341
                                                                                                                                                                                                                #pthread   0x10e65e600
                                                                                                                                                                                                                #should be 0x10e65e600'''
                    #    print("try2")
                        #with open ("liste.txt", "w+") as a:
                            #self.Neuladen_der_Liste()
                     #   messagebox.showinfo(title="Info", message="Alle vorehigen einträge wurden gelöscht.")
                      #  print("datei geöffnet")
                    #except:
                     #   print("Beim Erstellen der neuen Liste ist ein Fehler aufgetreten")
                else:
                    messagebox.showerror(title="Fehler", message="Es gab keine alten Einträge zum löschen.")
            except:
                messagebox.showerror(title="Fehler", message="Es ist ein unbekannter Fehler beim Löschen der alten Einträge aufgetreten, Fehlercode: 0")
        elif abfrage_wegen_löschen_db == "no":
            print("löschen der db vom Nutzer abgerbrochen.")
        else:
            print("db löschen fehler.")
            messagebox.showerror(title="Fehler", message="Kaputt")

    def pause(self,Pause):
        print("pause(def)")
        try:
            self.alles_löschen_knopp.pack_forget()
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
        T1 = Thread(target = self.Uhr(Pause))
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


    def Uhr(self, Pause):
        print(Pause)
        while Pause:
            lokaler_zeit_string = time.strftime("%H:%M")
            self.Zeit = time.strftime("%H:%M")
            print(Pause)
            #print("Uhrzeit: ", lokaler_zeit_string)
            if self.Zeit_text:
                self.Zeit_text.configure(text=lokaler_zeit_string)
            time.sleep(1)
        else:
            print("Thread und Programm wird beendet. Weil die var 'Pause' nicht bei 'ja' lag.")
            sys.exit()
            

    
    def pause_beenden_c(self,T1,Pause):
        print("pause_beenden(def)")
        T1.join()
        Pause = False
        
        


            


    def als_csv_speichern(self):
        print("Als CSV speichern")
        self.csv_datei_pfad = filedialog.askdirectory()

        if self.csv_datei_pfad:
            # Öffnen der Textdatei zum Lesen
            with open("liste.txt", 'r') as text_datei:
                daten = text_datei.read()

            # Aufteilen des Texts in Zeilen
            zeilen = daten.strip().split('\n')

            # Initialisieren einer Liste für die Datensätze
            datensaetze = []

            # Initialisieren der Variablen für Kundeninformationen
            uhrzeit, kunde, problem, info = "", "", "", ""

            # Durchlaufen der Zeilen und Extrahieren der Informationen
            for zeile in zeilen:
                print(zeilen)
                print("=")
                print(zeile)
                if zeile.startswith("Uhrzeit:"):
                    uhrzeit = zeile.replace("Uhrzeit:", "").strip()
                elif zeile.startswith("Kunde:"):
                    kunde = zeile.replace("Kunde:", "").strip()
                elif zeile.startswith("Problem:"):
                    problem = zeile.replace("Problem:", "").strip()
                elif zeile.startswith("Info:"):
                    info = zeile.replace("Info:", "").strip()
                
                    
                if kunde and problem and info and uhrzeit:
                    datensaetze.append([ uhrzeit,kunde, problem, info])
                    uhrzeit, kunde, problem, info  = "", "", "", ""

            if datensaetze:
                self.tag_string = str(time.strftime("%d %m %Y"))
                # Schreiben der Daten in die CSV-Datei
                with open(self.csv_datei_pfad + "/AnruferlistenDings" + self.tag_string + ".csv" , 'w', newline='') as datei:
                    schreiber = csv.writer(datei)
                    schreiber.writerow(["Uhrzeit", "Kunde", "Problem", "Info"])
                    schreiber.writerows(datensaetze)
                    self.zeit_string = time.strftime("%H:%M:%S")
                    self.tag_string = str(time.strftime("%d %m %Y"))
                    #schreiber.writerow(["Ende der Datensätze, Exportiert am " + self.tag_string + "um " + self.zeit_string], "Diese Liste wird jeden Tag neu Angelegt.")
                print("Daten wurden in die CSV-Datei gespeichert.")
                messagebox.showinfo(title="Gespeichert", message="Daten wurden erfolgreich gespeichert.")
            else:
                print("Fehler: Keine vollständigen Informationen wurden in der Textdatei gefunden.")
                messagebox.showerror(title="Fehler", message="Das ist etwas beim Speichern schiefgelaufen.")

    def als_csv_speichern_eigener_ort(self):
        print("Als CSV speichern, im Standard Ort")
        self.csv_datei_pfad = self.Listen_Speicherort_geladen

        if self.csv_datei_pfad:
            # Öffnen der Textdatei zum Lesen
            with open("liste.txt", 'r') as text_datei:
                daten = text_datei.read()

            # Aufteilen des Texts in Zeilen
            zeilen = daten.strip().split('\n')

            # Initialisieren einer Liste für die Datensätze
            datensaetze = []

            # Initialisieren der Variablen für Kundeninformationen
            uhrzeit, kunde, problem, info = "", "", "", ""

            # Durchlaufen der Zeilen und Extrahieren der Informationen
            for zeile in zeilen:
                print(zeilen)
                print("=")
                print(zeile)
                if zeile.startswith("Uhrzeit:"):
                    uhrzeit = zeile.replace("Uhrzeit:", "").strip()
                elif zeile.startswith("Kunde:"):
                    kunde = zeile.replace("Kunde:", "").strip()
                elif zeile.startswith("Problem:"):
                    problem = zeile.replace("Problem:", "").strip()
                elif zeile.startswith("Info:"):
                    info = zeile.replace("Info:", "").strip()
                
                    
                if kunde and problem and info and uhrzeit:
                    datensaetze.append([ uhrzeit,kunde, problem, info])
                    uhrzeit, kunde, problem, info  = "", "", "", ""

            if datensaetze:
                self.tag_string = str(time.strftime("%d %m %Y"))
                # Schreiben der Daten in die CSV-Datei
                self.der_richtige_pdf_pfad = self.csv_datei_pfad + "/AnruferlistenDings" + self.tag_string + ".csv"
                with open(self.csv_datei_pfad + "/AnruferlistenDings" + self.tag_string + ".csv" , 'w', newline='') as datei:
                    schreiber = csv.writer(datei)
                    schreiber.writerow(["Uhrzeit", "Kunde", "Problem", "Info"])
                    schreiber.writerows(datensaetze)
                    self.zeit_string = time.strftime("%H:%M:%S")
                    self.tag_string = str(time.strftime("%d %m %Y"))
                    #schreiber.writerow(["Ende der Datensätze, Exportiert am " + self.tag_string + "um " + self.zeit_string], "Diese Liste wird jeden Tag neu Angelegt.")
                print("Daten wurden in die CSV-Datei gespeichert.")
                messagebox.showinfo(title="Gespeichert", message="Daten wurden erfolgreich gespeichert. Wandle nun in PDF um...")
                ###c2p_convert(self.der_richtige_pdf_pfad,"Datensätze.pdf")
                ###messagebox.showinfo(title="Dings", message="PDF Fertig erstellt.")
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
            with open("Listendingsspeicherort.json", "w+" ) as fn:
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
            with open("Listendingsspeicherort_Netzwerk.json", "w+" ) as fn:
                json.dump(self.zu_speichernder_Ort_des_ListenDings_Netzwerk, fn)
                messagebox.showinfo(title="Erfolg", message="Der Pfad des Listendings wurde erfolgreich geändert und wird beim nächsten Programmstart aktiv.")
        except Exception as e:
            ei = "Das ändern des ListenDings Pfades hat nicht geklappt, ich hab aber auch keine Ahnung wieso, versuch mal den Text hier zu entziffern: " , e
            messagebox.showerror(title="Fehler", message=ei)

    def neue_GUI(self):
        print("neue_GUI (def)")
        self.senden_button.unbind('<Button-1>')
        root.unbind('<Return>')
        self.alles_löschen_knopp.place_forget()
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
        Listen_Speicherort_Netzwerk_geladen = self.Listen_Speicherort_Netzwerk_geladen

        if self.csv_datei_pfad_Netzwerk:
            # Öffnen der Textdatei zum Lesen
            with open("liste.txt", 'r') as text_datei:
                daten = text_datei.read()

            zeilen = daten.strip().split('\n')

            # Initialisieren einer Liste für die Datensätze
            datensaetze = []

            # Initialisieren der Variablen für Kundeninformationen
            uhrzeit, kunde, problem, info = "", "", "", ""

            # Durchlaufen der Zeilen und Extrahieren der Informationen
            for zeile in zeilen:
                print(zeilen)
                print("=")
                print(zeile)
                if zeile.startswith("Uhrzeit:"):
                    uhrzeit = zeile.replace("Uhrzeit:", "").strip()
                elif zeile.startswith("Kunde:"):
                    kunde = zeile.replace("Kunde:", "").strip()
                elif zeile.startswith("Problem:"):
                    problem = zeile.replace("Problem:", "").strip()
                elif zeile.startswith("Info:"):
                    info = zeile.replace("Info:", "").strip()
                
                    
                if kunde and problem and info and uhrzeit:
                    datensaetze.append([ uhrzeit,kunde, problem, info])
                    uhrzeit, kunde, problem, info  = "", "", "", ""

            if datensaetze:
                self.tag_string = str(time.strftime("%d %m %Y"))
                # Schreiben der Daten in die CSV-Datei
                with open(self.csv_datei_pfad_Netzwerk + "/AnruferlistenDings" + self.tag_string + ".csv" , 'w', newline='') as datei:
                    schreiber = csv.writer(datei)
                    schreiber.writerow(["Uhrzeit", "Kunde", "Problem", "Info"])
                    schreiber.writerows(datensaetze)
                    self.zeit_string = time.strftime("%H:%M:%S")
                    self.tag_string = str(time.strftime("%d %m %Y"))
                    #schreiber.writerow(["Ende der Datensätze, Exportiert am " + self.tag_string + "um " + self.zeit_string], "Diese Liste wird jeden Tag neu Angelegt.")
                print("Daten wurden in die CSV-Datei gespeichert.")
                messagebox.showinfo(title="Gespeichert", message="Daten wurden erfolgreich auf dem Netzlaufwerk gespeichert.")
                
            else:
                print("Fehler: Keine vollständigen Informationen wurden in der Textdatei gefunden.")
                messagebox.showerror(title="Fehler", message="Das ist etwas beim Speichern schiefgelaufen.")
    
    
    '''optionmenu = tk.CTkOptionMenu(root, values=["option 1", "option 2"], command=self.weiterleitung_an)

    def change_scaling_event(self):
        new_scaling_float = int(new_scaling.replace("%", "")) / 100
        tk.set_widget_scaling(new_scaling_float)

    def weiterleitung_an(self):'''

    



def bye():
    print("(ENDE) Das Programm wurde Beendet, auf wiedersehen! \^_^/ ")
    zeit_string = time.strftime("%H:%M:%S")
    tag_string = str(time.strftime("%d %m %Y"))
    print(zeit_string , tag_string)
    try:
        with open("Listendingsspeicherort_Netzwerk.json" , "r") as Liste_Speicherort_Netzwerk_data:
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
            with open("auto_speichern.txt", "r") as aSp:
                dings_aSp = aSp.read()
                auto_speichern = dings_aSp
        except:
            auto_speichern = "Nein"

        if auto_speichern == "Ja":
            csv_datei_pfad_Netzwerk = Listen_Speicherort_Netzwerk_geladen
            if csv_datei_pfad_Netzwerk:
                # Öffnen der Textdatei zum Lesen
                with open("liste.txt", 'r') as text_datei:
                    daten = text_datei.read()

                zeilen = daten.strip().split('\n')

                # Initialisieren einer Liste für die Datensätze
                datensaetze = []

                # Initialisieren der Variablen für Kundeninformationen
                uhrzeit, kunde, problem, info = "", "", "", ""

                # Durchlaufen der Zeilen und Extrahieren der Informationen
                for zeile in zeilen:
                    print(zeilen)
                    print("=")
                    print(zeile)
                    if zeile.startswith("Uhrzeit:"):
                        uhrzeit = zeile.replace("Uhrzeit:", "").strip()
                    elif zeile.startswith("Kunde:"):
                        kunde = zeile.replace("Kunde:", "").strip()
                    elif zeile.startswith("Problem:"):
                        problem = zeile.replace("Problem:", "").strip()
                    elif zeile.startswith("Info:"):
                        info = zeile.replace("Info:", "").strip()
                    
                        
                    if kunde and problem and info and uhrzeit:
                        datensaetze.append([ uhrzeit,kunde, problem, info])
                        uhrzeit, kunde, problem, info  = "", "", "", ""

                if datensaetze:
                    tag_string = str(time.strftime("%d %m %Y"))
                    # Schreiben der Daten in die CSV-Datei
                    with open(csv_datei_pfad_Netzwerk + "/AnruferlistenDings" + tag_string + ".csv" , 'w', newline='') as datei:
                        schreiber = csv.writer(datei)
                        schreiber.writerow(["Uhrzeit", "Kunde", "Problem", "Info"])
                        schreiber.writerows(datensaetze)
                        zeit_string = time.strftime("%H:%M:%S")
                        tag_string = str(time.strftime("%d %m %Y"))
                        #schreiber.writerow(["Ende der Datensätze, Exportiert am " + self.tag_string + "um " + self.zeit_string], "Diese Liste wird jeden Tag neu Angelegt.")
                    print("Daten wurden in die CSV-Datei gespeichert.")
                    messagebox.showinfo(title="Gespeichert", message="Daten wurden erfolgreich auf dem Netzlaufwerk gespeichert.")
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
root.protocol("WM_DELETE_WINDOW", bye)
root.mainloop()
