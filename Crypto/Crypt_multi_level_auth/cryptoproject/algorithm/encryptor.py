from cryptography.fernet import Fernet
from filesplit.split import Split
import os

def encryption(filename):
    filesize = os.path.getsize(filename)
    #splitting the files
    chunkesize = filesize//2
    act_file_name = filename.split('/')[-1]
    direct = f'media/files/{act_file_name}'
    os.mkdir(f'media/files/{act_file_name}')
    fs = Split(inputfile=filename, outputdir=f'media/files/{act_file_name}')
    fs.bysize(chunkesize)
    key = Fernet.generate_key()
    with open('media/keys/fernetpass.key', 'wb') as f:
        f.write(key)
    for i in os.listdir(direct):
        fernet = Fernet(key)
        if i != 'manifest':
            with open(f'media/files/{act_file_name}/{i}', 'rb') as f:
                data = f.read()
                enc = fernet.encrypt(data)
            with open(f'media/files/{act_file_name}/{i}', 'wb') as f:
                f.write(enc)
    return f'media/files/{filename}'


