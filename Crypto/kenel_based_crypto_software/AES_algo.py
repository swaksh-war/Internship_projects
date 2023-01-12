from Crypto.Cipher import AES
from Crypto.Random import get_random_bytes

def generate_key():
    key = get_random_bytes(16)
    with open('aeskeyfile', 'wb') as f:
        f.write(key)



def encaes(data_file, filename):
    with open('aeskeyfile', 'rb') as f:
        key = f.read()
    cipher = AES.new(key, AES.MODE_EAX)
    with open(f'{data_file}', "rb") as f:
        data = f.read()
    ciphertext, tag = cipher.encrypt_and_digest(data)

    file_out = open(f"{filename}.bin", "wb")
    [file_out.write(x) for x in (cipher.nonce, tag, ciphertext)]
    file_out.close()

def decaes(data_file, filename):
    with open('aeskeyfile', 'rb') as f:
        key = f.read()
    
    file_in = open(f'{data_file}', 'rb')
    nonce, tag, ciphertext = [file_in.read(x) for x in (16, 16, -1)]
    cipher = AES.new(key, AES.MODE_EAX, nonce)
    data = cipher.decrypt_and_verify(ciphertext, tag)
    filename = filename.split('.')
    filename.pop()
    act_filename = ''.join(filename)

    with open(f'decrypted_{act_filename}', 'wb') as f:
        f.write(data)

# generate_key()
# encaes('file.txt')
# decaes()
