import rsa
from cryptography.fernet import Fernet

def keygen():
    key = Fernet.generate_key()

    k = open('message.key', 'wb')
    k.write(key)
    k.close()

    (pubkey, privkey) = rsa.newkeys(2048)

    pubkey = open('publicKey.key', 'wb')
    pubkey.write(pubkey.save_pkcs1('PEM'))
    pubkey.close()

    prkey = open('privateKey.key', 'wb')
    prkey.write(privkey.save_pkcs1('PEM'))
    prkey.close()
