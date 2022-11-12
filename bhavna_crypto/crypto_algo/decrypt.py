import rsa
from cryptography.fernet import Fernet

def decrypt():
    prkey = open('privateKey.key', 'rb')
    pkey = prkey.read()
    private_key = rsa.PrivateKey.load_pkcs1(pkey)
    e = open('encryptedMessageKey', 'rb')
    ekey = e.read()
    dpubkey = rsa.decrypt(ekey, private_key)

    cipher = Fernet(dpubkey)

    encrypted_data = open('EncryptedKey', 'rb')
    edata = encrypted_data.read()

    decrypted_data = cipher.decrypt(edata)

    print(decrypted_data.decode())