import customtkinter as tk
from tkinter import messagebox
import os
import subprocess
import platform



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
                print("Thread wurde erfolgreich beendet.")
            except Exception as E_t:
                print(f"Konnte den Thread self.thread_suche nicht beenden, Fehlermeldung: {E_t}")

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
                print("Thread wurde erfolgreich beendet.")
            except Exception as E_t:
                print(f"Konnte den Thread self.thread_suche nicht beenden, Fehlermeldung: {E_t}")
        else:
            self.Ergebnisse_Listbox.unbind("<Double-1>")
            dmsg = "Dazu konnte ich leider nichts finden."
            try:
                self.erg_text_widget.insert("0.0", "Keine Ergebnisse")
            except:
                pass
            self.etwas_suchen1 = False
            self.Suche_suche = ""
            self.Ort_wo_gesucht_wird = ""
            self.suchfenster_ergebnisse.destroy()
            try:
                self.thread_suche.join()
                print("Thread wurde erfolgreich beendet.")
            except Exception as E_t:
                print(f"Konnte den Thread self.thread_suche nicht beenden, Fehlermeldung: {E_t}")
            messagebox.showinfo(title="CiM Suche", message=dmsg)
            
    else:
        print("gab nüscht")
        self.Ergebnisse_Listbox.unbind("<Double-1>")
        dmsg = "Dazu konnte ich leider nichts finden..."
        self.Suche_suche = ""
        self.etwas_suchen1 = False
        try:
            self.thread_suche.join()
            print("Thread wurde erfolgreich beendet.")
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