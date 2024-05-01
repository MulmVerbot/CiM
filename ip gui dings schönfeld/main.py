try:
    import tkinter as tk
    from tkinter import messagebox
    import customtkinter as ctk
    import ipaddress
except:
    print("Es fehlen die nötigen Bibliotheken!")
    messagebox.showerror(title="Fehler", message="Es fehlen die nötigen Bibliotheken!")

root = ctk.CTk()
#root.configure(resizeable=False)
root.geometry("420x520")
root.title("IP Dings Maximilian Becker FIS22")

Ip_von_var = "Hier steht noch nix"
invsub_var = "Hier steht noch nix"
Netza_var = "Hier steht noch nix"
Brodc_var = "Hier steht noch nix"
Hostipv_var = "Hier steht noch nix"
bis_var = "Hier steht noch nix"


ip_l = ctk.CTkLabel(root, text="IP Adresse:")
ip_l.place(x=10,y=10)
suffix_l = ctk.CTkLabel(root, text="CIDR-Suffix:")
suffix_l.place(x=10, y=40)
subn_l = ctk.CTkLabel(root, text="Subnetzmaske:")
subn_l.place(x=10,y=70)#Dings
invsubn_l = ctk.CTkLabel(root, text="Inves Subnetzmaske:")
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
subn_e = ctk.CTkEntry(root)
subn_e.place(x=200,y=70)#Dings
invsubn_var_l = ctk.CTkLabel(root, text=invsub_var)
invsubn_var_l.place(x=200,y=100)
anzH_e = ctk.CTkEntry(root)
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
    ip_address = Ip_e.get()
    prefix_length = suffix_e.get()
    prefix_length = int(prefix_length)

    if ip_address and prefix_length != None:
        network = ipaddress.IPv4Network(f"{ip_address}/{prefix_length}", strict=False)
        subnet_mask = network.netmask

        #inverse_subnet_mask = 

        ip = ipaddress.ip_address(ip_address)   
        reverse_mask = ip.reverse_pointer
        
        
        reversed_octets = ip.exploded.split('.')[::-1]
        print(reversed_octets)
        
        invsubn_var_l.configure(text=reverse_mask)
        subn_e.delete(0, tk.END)
        subn_e.insert(0,subnet_mask)
        network_address = network.network_address
        Netza_e.configure(text=network_address)
        broadcast_address = network.broadcast_address
        Brodc_var_l.configure(text=broadcast_address)
        first_host = network_address + 1
        Hostipv_var_l.configure(text=first_host)
        last_host = broadcast_address - 1
        bis_var_l.configure(text=last_host)
        total_hosts = 2 ** (32 - prefix_length) - 2
        anzH_e.delete(0, tk.END)
        anzH_e.insert(0,total_hosts)
        ip_address and prefix_length == None
        print(ip_address ,prefix_length)
    else:
        messagebox.showerror(message="Fehler, es wurden nicht alle felder ausgefüllt")

vervollständigen_knopp = ctk.CTkButton(root, text="Vervollständigen", command=lambda: fürvoll(Ip_von_var,invsub_var,Netza_var,Brodc_var,Hostipv_var,bis_var))
vervollständigen_knopp.place(x=150,y=300)

print("gui da")
root.mainloop()
