from cryptography.fernet import Fernet
import os
from . import RSA_algo as rsa
from Crypto.PublicKey import RSA
# def decryptl1(FILE, filename, keyl1):
#     key = keyl1.read()
#     fernet = Fernet(key)
#     with open(FILE, 'rb') as f:
#         enc_file = f.read()
#     dec_file = fernet.decrypt(enc_file)    
#     with open(f'media/non_enc_file/{filename}', 'wb') as f:
#         f.write(dec_file)


def decryptl1(FILE, filename):
    keyl1 = open(f'media/key/{filename}_RSA_private.pem', 'rb')
    keyl1 = RSA.import_key(keyl1.read())
    rsa.rsadec(FILE, filename, keyl1)




def decryptl2(filename,keyl2):
    key = keyl2.read()
    fernet = Fernet(key)
    with open(f'media/non_enc_file/{filename}', 'rb') as f:
        enc_file = f.read()
    original = fernet.decrypt(enc_file)
    with open(f'media/non_enc_file/{filename}', 'wb') as f:
        f.write(original)
    

    