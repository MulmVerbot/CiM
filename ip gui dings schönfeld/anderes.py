import ipaddress

# Definiere die IP-Adresse und die Netzwerkpräfixlänge
ip_address = '192.168.178.10'
prefix_length = 24  # Beispiel: 24 bedeutet eine Subnetzmaske von 255.255.255.0

# Parse die IP-Adresse und erstelle ein IPv4Network-Objekt
network = ipaddress.IPv4Network(f"{ip_address}/{prefix_length}", strict=False)

# Gib die Subnetzmaske aus
subnet_mask = network.netmask
print("Subnetzmaske:", subnet_mask)

# Gib die Netzwerkadresse aus (ist identisch mit der IP-Adresse bei /32-Netzwerken)
network_address = network.network_address
print("Netzwerkadresse:", network_address)

# Gib die Broadcast-Adresse aus
broadcast_address = network.broadcast_address
print("Broadcast-Adresse:", broadcast_address)

# Gib die erste Hostadresse aus (identisch mit der Netzwerkadresse)
first_host = network_address + 1
print("Erste Host-Adresse:", first_host)

# Gib die letzte Hostadresse aus (identisch mit der Broadcast-Adresse bei /32-Netzwerken)
last_host = broadcast_address - 1
print("Letzte Host-Adresse:", last_host)
