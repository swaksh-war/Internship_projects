from cryptography.fernet import Fernet
import os
from . import RSA_algo as rsa

def encrypt(FILE):

    layerkey1 = Fernet.generate_key()

    with open('media/key/filekey.key', 'wb') as filekey:
        filekey.write(layerkey1)

    with open('media/key/filekey.key', 'rb') as filekey:
        key = filekey.read()

    fernet = Fernet(key)
    with open(FILE, 'rb') as file:
        original =  file.read()

    encrypted = fernet.encrypt(original)

    with open(FILE, 'wb') as encrypted_file:
        encrypted_file.write(encrypted)
    
    return layerkey1


def encryptl2(File, filename):
    key = rsa.generate_rsa_key(filename)
    file_path = rsa.rsaenc(File, filename)
    return key, file_path
