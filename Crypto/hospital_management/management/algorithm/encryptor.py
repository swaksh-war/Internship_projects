from cryptography.fernet import Fernet
import os

def encrypt(FILE,filename):
    filename_key = filename.split('.')[0]
    layerkey1 = Fernet.generate_key()

    with open(f'media/key/{filename_key}_filekey.key', 'wb') as filekey:
        filekey.write(layerkey1)

    with open(f'media/key/{filename_key}_filekey.key', 'rb') as filekey:
        key = filekey.read()

    fernet = Fernet(key)
    with open(FILE, 'rb') as file:
        original =  file.read()

    encrypted = fernet.encrypt(original)

    with open(FILE, 'wb') as encrypted_file:
        encrypted_file.write(encrypted)
    
    return layerkey1

def encryptl2(FILE, filename):
    filename_key = filename.split('.')[0]
    layerkey2 = Fernet.generate_key()
    with open(f'media/key/{filename_key}_filekeyl2.key', 'wb') as filekey:
        filekey.write(layerkey2)
    
    with open(f'media/key/{filename_key}_filekeyl2.key', 'rb') as filekey:
        key = filekey.read()
    
    fernet = Fernet(key)
    with open(FILE, 'rb') as file:
        original = file.read()
    encrypted = fernet.encrypt(original)
    with open(f'media/files/{filename}', 'wb') as encrypted_file:
        encrypted_file.write(encrypted)

    os.remove(FILE)

    PATH_OF_FILE = f'media/files/{filename}'
    
    return layerkey2, PATH_OF_FILE

def encryptl3(filename):
    filename_key = filename.split('.')[0]
    layerkey3 = Fernet.generate_key()
    with open(f'media/key/{filename_key}_filekeyl3.key', 'wb') as filekey:
        filekey.write(layerkey3)
    with open(f'media/key/{filename_key}_filekeyl3.key', 'rb') as filekey:
        key = filekey.read()
    fernet = Fernet(key)
    with open(f'media/files/{filename}', 'rb') as file:
        original = file.read()
    encrypted = fernet.encrypt(original)
    with open(f'media/files/{filename}', 'wb') as encrypted_file:
        encrypted_file.write(encrypted)
    PATH_OF_FILE = f'media/files/{filename}'

    return PATH_OF_FILE