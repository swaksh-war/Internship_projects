from cryptography.fernet import Fernet
import rsa

def Encryption(message):
    skey = open('message.key', 'rb')
    key = skey.read()

    cipher = Fernet(key)

    encrypted_data = cipher.encrypt(bytes(message, 'utf-8'))
    edata = open('EncryptedFile', 'wb')
    edata.write(encrypted_data)

    pkey = open('publickey.key', 'rb')
    pkdata = pkey.read()

    pubkey = rsa.PublicKey.load_pkcs1(pkdata)
    encrypted_key = rsa.encrypt(key, pubkey)
    ekey = open('encryptMessageKey', 'wb')
    ekey.write(encrypted_key)