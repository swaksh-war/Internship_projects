import rsa

def generateKeys():
    (publicKey, privateKey) = rsa.newkeys(1024)
    with open ('publcKey.pem', 'wb') as p:
        p.write(publicKey.save_pkcs1('PEM'))
    with open('privateKey.pem', 'wb') as p:
        p.write(privateKey.save_pkcs1('PEM'))

def loadKeys():
    with open('publcKey.pem', 'rb') as p:
        publickey = rsa.PublicKey.load_pkcs1(p.read())
    
    with open('privateKey.pem', 'rb') as p:
        privateKey = rsa.PrivateKey.load_pkcs1(p.read())
    
    return privateKey, publickey

def encrypt(message, key):
    return rsa.encrypt(message.encode('ascii'), key)

def decrypt(ciphertext, key):
    try:
        return rsa.decrypt(ciphertext, key).decode('ascii')
    except:
        return False

def sign(message, key):
    return rsa.sign(message, key, 'SHA-1')

def verify(message, signature, key):
    try:
        return rsa.verify(message.encode('ascii'), signature, key,) == 'SHA-1'
    except:
        return False


generateKeys()
publicKey, privateKey = loadKeys()

message = input('Message: ')
ciphertext = encrypt(message, publicKey)
signature = sign(message, privateKey)
text = decrypt(ciphertext, privateKey)

if verify(text, signature, publicKey):
    print('Successfully Verified signature')
else:
    print(f'the message signature could not be verified')

print(f'Cipher text: {ciphertext}')
print(f'signature: {signature}')

if text:
    print(f'Message text: {text}')
else:
    print('Unable to decrypt the message')