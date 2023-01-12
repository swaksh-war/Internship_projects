from cryptography.fernet import Fernet
import os

def decryptl1(filename):
    filename_key = filename.split('.')[0]
    with open(f'media/key/{filename_key}_filekeyl3.key', 'rb') as f:
        key = f.read()
    fernet = Fernet(key)
    with open(f'media/files/{filename}', 'rb') as g:
        enced = g.read()
    decrypted = fernet.decrypt(enced)
    with open(f'media/non_enc_file/{filename}', 'wb') as f:
        f.write(decrypted)
    

def decryptl2(FILE, filename):
    filename_key = filename.split('.')[0]
    with open(f'media/key/{filename_key}_filekeyl2.key', 'rb') as f:
        key = f.read()
    fernet = Fernet(key)
    with open(f'media/non_enc_file/{filename}', 'rb') as f:
        enc_file = f.read()
    dec_file = fernet.decrypt(enc_file)    
    with open(f'media/non_enc_file/{filename}', 'wb') as f:
        f.write(dec_file)

def decryptl3(filename):
    filename_key = filename.split('.')[0]
    with open(f'media/key/{filename_key}_filekey.key', 'rb') as f:
        key = f.read()
    fernet = Fernet(key)
    with open(f'media/non_enc_file/{filename}', 'rb') as f:
        enc_file = f.read()
    original = fernet.decrypt(enc_file)
    with open(f'media/non_enc_file/{filename}', 'wb') as f:
        f.write(original)