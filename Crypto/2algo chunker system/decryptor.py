from cryptography.fernet import Fernet
from Crypto.Cipher import AES
from Crypto.Random import get_random_bytes
from filesplit.split import Split
from filesplit.merge import Merge 
import os

files = []
for file in os.listdir('chunked/file.txt'):
    if file != 'manifest':
        files.append(f'chunked/file.txt/{file}')
print(files)

#Fernet Decryption
with open('fernetpass.key', 'rb') as f:
    key = f.read()
fernet_cipher = Fernet(key)
with open(files[1], 'rb') as f:
    data = f.read()

original = fernet_cipher.decrypt(data)
with open(files[1], 'wb') as f:
    f.write(original)

#AES Decryptor
with open('aesketfile', 'rb') as f:
    key = f.read()
file_in = open(files[0], 'rb')
nonce, tag, aes_cipher = [file_in.read(x) for x in (16,16,-1)]
cipher = AES.new(key, AES.MODE_EAX, nonce)
data = cipher.decrypt_and_verify(aes_cipher, tag)
with open(files[0], 'wb') as f:
    f.write(data)

# Dechunker 

mg = Merge(inputdir='chunked/file.txt', outputdir='chunked', outputfilename='file(1).txt')
mg.merge(cleanup=False)