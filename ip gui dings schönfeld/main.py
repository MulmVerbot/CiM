try:
    import tkinter as tk
    from tkinter import messagebox
    import customtkinter as ctk
    import ipaddress
except:
    print("Es fehlen die nötigen Bibliotheken!")
    messagebox.showerror(title="Fehler", message="Es fehlen die nötigen Bibliotheken!")

root = ctk.CTk()
root.resizable(False,False)
root.geometry("420x420")
root.title("IP Dings Maximilian Becker FIS22")

Ip_von_var = "-"
invsub_var = "-"
Netza_var = "-"
Brodc_var = "-"
Hostipv_var = "-"
bis_var = "-"


ip_l = ctk.CTkLabel(root, text="IP Adresse:")
ip_l.place(x=10,y=10)
suffix_l = ctk.CTkLabel(root, text="CIDR-Suffix:")
suffix_l.place(x=10, y=40)
subn_l = ctk.CTkLabel(root, text="Subnetzmaske:")
subn_l.place(x=10,y=70)#Dings
invsubn_l = ctk.CTkLabel(root, text="Umgekehrte Subnetzmaske:")
invsubn_l.place(x=10, y=100)
anzH_l = ctk.CTkLabel(root, text="Anzahl Hosts:")
anzH_l.place(x=10,y=130)
Netza_l = ctk.CTkLabel(root, text="Netzadresse:")
Netza_l.place(x=10,y=160)#MB
Brodc_l = ctk.CTkLabel(root, text="Broadcastadresse:")
Brodc_l.place(x=10,y=190)
Hostipv_l = ctk.CTkLabel(root, text="Host-IPs von:")
Hostipv_l.place(x=10,y=210)
bis_l = ctk.CTkLabel(root, text="bis:")
bis_l.place(x=20,y=240)

Ip_e = ctk.CTkEntry(root)
Ip_e.place(x=200,y=10)
suffix_e = ctk.CTkEntry(root)
suffix_e.place(x=200,y=40)
subn_e = ctk.CTkLabel(root, text="-")
subn_e.place(x=200,y=70)#Dings
invsubn_var_l = ctk.CTkLabel(root, text=invsub_var)
invsubn_var_l.place(x=200,y=100)
anzH_e = ctk.CTkLabel(root, text="-")
anzH_e.place(x=200,y=130)
Netza_e = ctk.CTkLabel(root, text=Netza_var)
Netza_e.place(x=200,y=160)
Brodc_var_l = ctk.CTkLabel(root, text=Brodc_var)
Brodc_var_l.place(x=200,y=190)
Hostipv_var_l = ctk.CTkLabel(root, text=Hostipv_var)
Hostipv_var_l.place(x=200,y=210)
bis_var_l = ctk.CTkLabel(root, text=bis_var)
bis_var_l.place(x=200,y=240)




def fürvoll(Ip_von_var,invsub_var,Netza_var,Brodc_var,Hostipv_var,bis_var):
    print("für voll nehmen (def)")
    try:
        ip_adresse = Ip_e.get()
        prefix_length = suffix_e.get()
        prefix_length = int(prefix_length)
    except Exception as Ex1:
        messagebox.showerror(title="Fehler", message=f"Es fehlen für die Berechnung notwendige Werte! Fehler: {Ex1}")

    if ip_adresse and prefix_length != None:
        try:
            network = ipaddress.IPv4Network(f"{ip_adresse}/{prefix_length}", strict=False)
            subnet_maske = network.netmask  
            
            subnet_maske = str(subnet_maske)
            oktete = subnet_maske.split('.')
            umg_oktete = [str(255 - int(octet)) for octet in oktete]
            umg_subnet_maske = '.'.join(umg_oktete)
            invsubn_var_l.configure(text=umg_subnet_maske)
            subn_e.configure(text=subnet_maske)
            netzwerk_adresse = network.network_address
            Netza_e.configure(text=netzwerk_adresse)
            broadcast_address = network.broadcast_address
            Brodc_var_l.configure(text=broadcast_address)
            first_host = netzwerk_adresse + 1
            Hostipv_var_l.configure(text=first_host)
            last_host = broadcast_address - 1
            bis_var_l.configure(text=last_host)
            total_hosts = 2 ** (32 - prefix_length) - 2
            anzH_e.configure(text=total_hosts)
            ip_adresse and prefix_length == None
        except Exception as Ex2:
            print(Ex2)
            messagebox.showerror(title="Fehler", message=f"Fehler beim Berechnen, bitte Überprüfen Sie Ihre Werte! Fehler: {Ex2}")
    else:
        messagebox.showerror(message="Fehler, es wurden nicht alle felder ausgefüllt")

vervollständigen_knopp = ctk.CTkButton(root, text="Vervollständigen", command=lambda: fürvoll(Ip_von_var,invsub_var,Netza_var,Brodc_var,Hostipv_var,bis_var))
vervollständigen_knopp.place(x=150,y=300)

print("gui da")
root.mainloop()
