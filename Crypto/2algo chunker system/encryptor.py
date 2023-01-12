from cryptography.fernet import Fernet
from Crypto.Cipher import AES
from Crypto.Random import get_random_bytes
from filesplit.split import Split
from filesplit.merge import Merge 
import os

#Encryptor algorithm

#chunker


file_size = os.path.getsize('file.txt')
chunked_size = file_size//2
os.mkdir('chunked/file.txt')
fs = Split(inputfile='file.txt', outputdir='chunked/file.txt')
fs.bysize(chunked_size)

#encryption using Fernet and AES


files = []
for file in os.listdir('chunked/file.txt'):
    if file != 'manifest':
        files.append(f'chunked/file.txt/{file}')
print(files)


#AES Encryption
aes_key = get_random_bytes(16)
with open('aesketfile', 'wb') as f:
    f.write(aes_key)
cipher = AES.new(aes_key, AES.MODE_EAX)
with open(files[0], 'rb') as f:
    data = f.read()

ciphertext, tag = cipher.encrypt_and_digest(data)
file_out = open(files[0], 'wb')
[file_out.write(x) for x in (cipher.nonce, tag, ciphertext)]
file_out.close()

#Fernet Encryption
fernet_key = Fernet.generate_key()
with open('fernetpass.key', 'wb') as f:
    f.write(fernet_key)
fernet_cipher = Fernet(fernet_key)
with open(files[1], 'rb') as f:
    data = f.read()

ciphertext = fernet_cipher.encrypt(data)
with open(files[1], 'wb') as f:
    f.write(ciphertext)
