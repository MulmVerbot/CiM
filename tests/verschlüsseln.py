from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC
from cryptography.hazmat.primitives.kdf.scrypt import Scrypt
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC
from cryptography.hazmat.primitives.kdf.scrypt import Scrypt
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC
from cryptography.hazmat.primitives.kdf.scrypt import Scrypt
from cryptography.hazmat.backends import default_backend
import os
import binascii

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
        print(f"Der derived_key ist: {derived_key}\nder key ist: {key}\n der encrypted key: {encrypted_key}")

    return key

# Beispielnutzung
password = 'Dings_Passwort'
key = os.urandom(32)
file_path = 'encrypted_key.bin'

encrypt_and_store_key(key, file_path, password)
loaded_key = decrypt_and_load_key(file_path, password)

print(f'Original Key: {binascii.hexlify(key)}')
print(f'Loaded Key:   {binascii.hexlify(loaded_key)}')

Dings = input()
