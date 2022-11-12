from cryptography.fernet import Fernet

with open('filekey.key', 'rb') as filekey:
    key = filekey.read()

fernet = Fernet(key)

with open('Dengue_negative.pdf', 'rb') as enc_file:
    encrypted = enc_file.read()

decrypted = fernet.decrypt(encrypted)

with open('Dengue_negative.pdf', 'wb') as dec_file:
    dec_file.write(decrypted)