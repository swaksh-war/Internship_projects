from cryptography.fernet import Fernet
import os
from Crypto.PublicKey import RSA
from . import RSA_algo_three as rsa
# def decrypt3l1(FILE, filename, keyl1):
#     key = keyl1.read()
#     fernet = Fernet(key)
#     with open(FILE, 'rb') as f:
#         enc_file = f.read()
#     dec_file = fernet.decrypt(enc_file)    
#     with open(f'media/non_enc_file/{filename}', 'wb') as f:
#         f.write(dec_file)


def decrypt3l1(FILE, filename):
    keyl1 = open(f'media/key/{filename}_RSA_private.pem', 'rb')
    keyl1 = RSA.import_key(keyl1.read())
    rsa.rsadec(FILE, filename, keyl1)


def decrypt3l2(filename,keyl2):
    key = keyl2.read()
    fernet = Fernet(key)
    with open(f'media/non_enc_file/{filename}', 'rb') as f:
        enc_file = f.read()
    dec_file = fernet.decrypt(enc_file)
    with open(f'media/non_enc_file/{filename}', 'wb') as f:
        f.write(dec_file)




def decrypt3l3(filename, keyl3):
    key = keyl3.read()
    fernet = Fernet(key)
    with open(f'media/non_enc_file/{filename}', 'rb') as f:
        enc_file = f.read()
    
    original = fernet.decrypt(enc_file)
    with open(f'media/non_enc_file/{filename}', 'wb') as f:
        f.write(original)

