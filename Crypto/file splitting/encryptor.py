from cryptography.fernet import Fernet
import os

def encrypt(folder):
    key = Fernet.generate_key()
    for i in os.listdir(folder):
        fernet = Fernet(key)
        with open(folder + '/' + i, 'rb') as f:
            data = f.read()
        encrypted = fernet.encrypt(data)
        with open(folder + '/' + i, 'wb') as enc:
            enc.write(encrypted)
    with open('message.key', 'wb') as f:
        f.write(key)

# encrypt(r'store/surplusmed.txt')

def decrypt(folder, key_path):
    with open(key_path, 'rb') as f:
        key = f.read()
    for i in os.listdir(folder):
        fernet = Fernet(key)
        with open(folder+'/'+i, 'rb') as f:
            data = f.read()
        decrypted = fernet.decrypt(data)
        with open(folder+'/'+i, 'wb') as dec:
            dec.write(decrypted)

decrypt(r'store/surplusmed.txt', 'message.key')