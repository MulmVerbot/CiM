subnet_maske = '255.255.255.0'
oktete = subnet_maske.split('.')
umg_oktete = [str(255 - int(octet)) for octet in oktete]
umg_subnet_maske = '.'.join(umg_oktete)