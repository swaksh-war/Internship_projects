from Crypto.Cipher import AES
from cryptography.fernet import Fernet
from Crypto.Random import get_random_bytes
from filesplit.split import Split
from filesplit.merge import Merge
import os
#import shutil

#Non encrypted file path will be used as filename i.e. filename = 'media/non_enc_file/{filename} that will be called inside views.py'
def encrypt(filename):
    file_size = os.path.getsize(filename)
    chunked_size = file_size//2
    act_file_name = filename.split('/')[-1]
    os.mkdir(f'media/files/{act_file_name}')
    fs = Split(inputfile=filename, outputdir=f'media/files/{act_file_name}')
    fs.bysize(chunked_size)

    aes_key = get_random_bytes(16)
    fernet_key = Fernet.generate_key()

    files = []
    for file in os.listdir(f'media/files/{act_file_name}'):
        if file != 'manifest':
            files.append(f'media/files/{act_file_name}/{file}')
    
    with open(f'media/key/aeskey.key', 'wb') as f:
        f.write(aes_key)
    with open(f'media/key/fernetpass.key', 'wb') as f:
        f.write(fernet_key)
    
    with open(files[0], 'rb') as f:
        data = f.read()
    
    cipher = AES.new(aes_key, AES.MODE_EAX)

    ciphertext, tag = cipher.encrypt_and_digest(data)

    file_out =  open(files[0], 'wb')
    [file_out.write(x) for x in (cipher.nonce, tag, ciphertext)]
    file_out.close()

    fernet = Fernet(fernet_key)
    with open(files[1], 'rb') as f:
        fer_data = f.read()
    fer_enc_data = fernet.encrypt(fer_data)
    with open(files[1], 'wb') as f:
        f.write(fer_enc_data)
    
    return f'media/files/{filename}'

def decrypt(filename, aes_key, fernet_key):
    aes_key = aes_key.read()
    fernet_key = fernet_key.read()
    files = []
    for file in os.listdir(f'media/files/{filename}'):
        if file != 'manifest':
            files.append(f'media/files/{filename}/{file}')
    file_in = open(files[0], 'rb')
    nonce, tag, aes_cipher_text = [file_in.read(x) for x in (16,16,-1)]
    aes_cipher = AES.new(aes_key, AES.MODE_EAX, nonce=nonce)
    data = aes_cipher.decrypt_and_verify(aes_cipher_text, tag)
    with open(files[0], 'wb') as f:
        f.write(data)
    
    fernet_cipher = Fernet(fernet_key)
    with open(files[1], 'rb') as f:
        data = f.read()
    original = fernet_cipher.decrypt(data)
    with open(files[1], 'wb') as f:
        f.write(original)
    
    mg = Merge(inputdir=f'media/files/{filename}', outputdir='media/temp', outputfilename=filename)
    mg.merge(cleanup=False)
    #shutil.rmtree(f'media/files/{filename}')
