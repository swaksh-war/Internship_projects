from cryptography.fernet import Fernet
import os
from . import RSA_algo_three as rsa

def encrypt3l1(FILE):

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

def encrypt3l2(FILE, filename):
    layerkey2 = Fernet.generate_key()
    with open('media/key/filekeyl2.key', 'wb') as filekey:
        filekey.write(layerkey2)
    
    with open('media/key/filekeyl2.key', 'rb') as filekey:
        key = filekey.read()
    
    fernet = Fernet(key)
    with open(FILE, 'rb') as file:
        original = file.read()
    encrypted = fernet.encrypt(original)
    with open(f'media/non_enc_file/{filename}', 'wb') as encrypted_file:
        encrypted_file.write(encrypted)
    
    return layerkey2


def encrypt3l3(FILE, filename):
    key = rsa.generate_rsa_key(filename)
    file_path = rsa.rsaenc(FILE, filename)
    return key, file_path



# def encrypt3l3(FILE, filename):
#     layerkey3 = Fernet.generate_key()
#     with open('media/key/filekeyl3.key', 'wb') as filekey:
#         filekey.write(layerkey3)
    
#     with open('media/key/filekeyl3.key', 'rb') as filekey:
#         key = filekey.read()
    
#     fernet = Fernet(key)

#     with open(FILE, 'rb') as file:
#         original = file.read()
#     encrypted = fernet.encrypt(original)
#     with open(f'media/files/{filename}', 'wb') as encrypted_file:
#         encrypted_file.write(encrypted)
#     os.remove(FILE)
#     PATH_OF_FILE = f'media/files/{filename}'

#     return layerkey3, PATH_OF_FILE