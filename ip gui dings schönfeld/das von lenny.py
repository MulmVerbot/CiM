import tkinter as tk
import ipaddress

def calculate_subnet():
    #try:
    ip_address_str = ip_entry.get()
    cidr_suffix = int(cidr_entry.get())
    subnet_mask_str = subnet_mask_entry.get()
    num_hosts = int(hosts_entry.get())

    # Validate input
    ip = ipaddress.ip_interface(ip_address_str)
    subnet = ipaddress.ip_network(f"{ip.network}/{cidr_suffix}", strict=False)

    # Calculate other values
    inverse_subnet_mask = subnet.hostmask
    network_address = subnet.network_address
    broadcast_address = subnet.broadcast_address
    host_range_start = subnet.network_address + 1
    host_range_end = subnet.broadcast_address - 1

    # Update result fields
    inverse_subnet_mask_label.config(text=f"Inverse Subnetzmaske: {inverse_subnet_mask}")
    network_address_label.config(text=f"Netzadresse: {network_address}")
    broadcast_address_label.config(text=f"Broadcastadresse: {broadcast_address}")
    host_range_label.config(text=f"Host-IP-Adressen Range: {host_range_start} bis {host_range_end}")

    '''except ValueError and Exception as E:
        print(E)
        result_label.config(text="Ungültige Eingabe. Bitte überprüfen Sie Ihre Werte.")'''

# GUI setup
root = tk.Tk()
root.title("IPv4 Subnet Calculator")

ip_label = tk.Label(root, text="IP-Adresse:")
ip_entry = tk.Entry(root)
cidr_label = tk.Label(root, text="CIDR-Suffix:")
cidr_entry = tk.Entry(root)
subnet_mask_label = tk.Label(root, text="Subnetzmaske:")
subnet_mask_entry = tk.Entry(root)
hosts_label = tk.Label(root, text="Anzahl der Hosts:")
hosts_entry = tk.Entry(root)

calculate_button = tk.Button(root, text="Berechnen", command=calculate_subnet)

inverse_subnet_mask_label = tk.Label(root, text="")
network_address_label = tk.Label(root, text="")
broadcast_address_label = tk.Label(root, text="")
host_range_label = tk.Label(root, text="")
result_label = tk.Label(root, text="")

# Grid layout
ip_label.grid(row=0, column=0)
ip_entry.grid(row=0, column=1)
cidr_label.grid(row=1, column=0)
cidr_entry.grid(row=1, column=1)
subnet_mask_label.grid(row=2, column=0)
subnet_mask_entry.grid(row=2, column=1)
hosts_label.grid(row=3, column=0)
hosts_entry.grid(row=3, column=1)

calculate_button.grid(row=4, columnspan=2)
inverse_subnet_mask_label.grid(row=5, columnspan=2)
network_address_label.grid(row=6, columnspan=2)
broadcast_address_label.grid(row=7, columnspan=2)
host_range_label.grid(row=8, columnspan=2)
result_label.grid(row=9, columnspan=2)

root.mainloop()