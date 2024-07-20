import os
import binascii
import getpass
import hashlib
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.backends import default_backend

# Gehashtes Passwort (dieses wäre normalerweise sicher gespeichert, hier nur zu Demonstrationszwecken)
# Das Passwort "securepassword" wurde gehasht
stored_password_hash = "5e884898da28047151d0e56f8dc6292773603d0d6aabbdd8395c9f2a324e93e"

def verify_password(input_password: str) -> bool:
    """Vergleicht das eingegebene Passwort mit dem gespeicherten gehashten Passwort."""
    input_password_hash = hashlib.sha256(input_password.encode()).hexdigest()
    return input_password_hash == stored_password_hash

# Schlüsselgenerierung
def generate_key(password: str, salt: bytes, iterations: int = 100_000) -> bytes:
    kdf = PBKDF2HMAC(
        algorithm=hashes.SHA256(),
        length=32,
        salt=salt,
        iterations=iterations,
        backend=default_backend()
    )
    key = kdf.derive(password.encode())
    return key

# Schlüssel verschlüsseln und speichern
def encrypt_and_store_key(key: bytes, file_path: str, password: str):
    salt = os.urandom(16)
    kdf = PBKDF2HMAC(
        algorithm=hashes.SHA256(),
        length=32,
        salt=salt,
        iterations=100_000,
        backend=default_backend()
    )
    derived_key = kdf.derive(password.encode())

    iv = os.urandom(16)
    cipher = Cipher(algorithms.AES(derived_key), modes.CFB(iv), backend=default_backend())
    encryptor = cipher.encryptor()
    encrypted_key = encryptor.update(key) + encryptor.finalize()

    with open(file_path, 'wb') as file:
        file.write(salt + iv + encrypted_key)

# Schlüssel entschlüsseln und laden
def decrypt_and_load_key(file_path: str, password: str) -> bytes:
    with open(file_path, 'rb') as file:
        data = file.read()
        salt = data[:16]
        iv = data[16:32]
        encrypted_key = data[32:]

        kdf = PBKDF2HMAC(
            algorithm=hashes.SHA256(),
            length=32,
            salt=salt,
            iterations=100_000,
            backend=default_backend()
        )
        derived_key = kdf.derive(password.encode())

        cipher = Cipher(algorithms.AES(derived_key), modes.CFB(iv), backend=default_backend())
        decryptor = cipher.decryptor()
        key = decryptor.update(encrypted_key) + decryptor.finalize()

    return key

# Beispielnutzung
def main():
    # Passwort sicher abfragen
    input_password = getpass.getpass(prompt='Bitte geben Sie Ihr Passwort ein: ')

    # Passwortüberprüfung
    if verify_password(input_password):
        print("Passwort korrekt.")
        
        # Generiere einen symmetrischen Schlüssel (zum Beispiel AES-128)
        key = os.urandom(32)
        file_path = 'encrypted_key.bin'

        # Schlüssel verschlüsseln und speichern
        encrypt_and_store_key(key, file_path, input_password)
        print('Schlüssel wurde erfolgreich verschlüsselt und gespeichert.')

        # Schlüssel entschlüsseln und laden
        loaded_key = decrypt_and_load_key(file_path, input_password)

        print(f'Originalschlüssel: {binascii.hexlify(key)}')
        print(f'Geladener Schlüssel: {binascii.hexlify(loaded_key)}')
    else:
        print("Falsches Passwort. Zugriff verweigert.")

if __name__ == '__main__':
    main()
