from cryptography.fernet import Fernet

def generate_key():
    key = Fernet.generate_key()
    with open('fernetpass.key', 'wb') as f:
        f.write(key)
    

def call_key():
    return open('fernetpass.key', 'rb').read()

def encrypt(data_file, filename):
    filename = filename
    key = call_key()
    slogan = open(f'{data_file}', 'rb').read()
    a = Fernet(key)
    coded_slogan = a.encrypt(slogan)
    with open('encrypted_{filename}.bin', 'wb') as f:
        f.write(coded_slogan)

def decrypt(data_file, filename):
    with open('fernetpass.key', 'rb') as f:
        key = f.read()
    
    fernet = Fernet(key)

    with open(f'{data_file}', 'rb') as f:
        data = f.read()
    original = fernet.decrypt(data)

    filename = filename.split('.')
    filename.pop()
    act_filename = ''.join(filename)

    with open(f'decrypted_{act_filename}', 'wb') as f:
        f.write(original)

# if __name__ == '__main__':
#     generate_key()
#     call_key()
#     encrypt()