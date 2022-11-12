from cryptography.fernet import Fernet

key = Fernet.generate_key()
print(key)
with open('filekey.key', 'wb') as filekey:
    filekey.write(key)

with open('filekey.key', 'rb') as filekey:
    key = filekey.read()
fernet = Fernet(key)

with open('Dengue_negative.pdf', 'rb') as file:
    original = file.read()

encrypted = fernet.encrypt(original)

with open('Dengue_negative.pdf', 'wb') as encrypted_file:
    encrypted_file.write(encrypted)
