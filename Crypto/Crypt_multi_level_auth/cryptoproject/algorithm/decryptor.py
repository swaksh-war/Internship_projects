from filesplit.merge import Merge
from cryptography.fernet import Fernet
import os
# import shutil

def decryption(filename, fernet_key):
    enc_file_path = f'media/files/{filename}'
    key = fernet_key.read()
    fernet = Fernet(key)
    for file in os.listdir(enc_file_path):
        if file != 'manifest':
            with open(f'{enc_file_path}/{file}', 'rb') as f:
                data = f.read()
                dec_file = fernet.decrypt(data)
            with open(f'{enc_file_path}/{file}', 'wb') as f:
                f.write(dec_file)
    mg = Merge(inputdir=enc_file_path, outputdir='media/temp', outputfilename=filename)
    mg.merge(cleanup=False)
    # shutil.rmtree(f'media/files/{filename}')