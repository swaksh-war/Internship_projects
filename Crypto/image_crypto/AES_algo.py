from Crypto.Cipher import AES
from Crypto.Random import get_random_bytes
import cv2
import numpy as np

def generate_key():
    key = get_random_bytes(32)
    randomByteArray = bytearray(key)
    flatNumpyArray = np.array(randomByteArray)
    grayImage = flatNumpyArray.reshape(4,8)
    cv2.imwrite('aeskey.png', grayImage)


def encaes(data_file, filename):
    img = cv2.imread('aeskey.png', 0)
    img = img.ravel()
    key = np.ndarray.tobytes(img)
    cipher = AES.new(key, AES.MODE_EAX)
    with open(f'{data_file}', "rb") as f:
        data = f.read()
    ciphertext, tag = cipher.encrypt_and_digest(data)

    file_out = open(f"{filename}.bin", "wb")
    [file_out.write(x) for x in (cipher.nonce, tag, ciphertext)]
    file_out.close()

def decaes(data_file, filename):
    img = cv2.imread('aeskey.png', 0)
    img = img.ravel()
    key = np.ndarray.tobytes(img)
    file_in = open(f'{data_file}', 'rb')
    nonce, tag, ciphertext = [file_in.read(x) for x in (16, 16, -1)]
    cipher = AES.new(key, AES.MODE_EAX, nonce)
    data = cipher.decrypt_and_verify(ciphertext, tag)
    filename = filename.split('.')
    filename.pop()
    act_filename = ''.join(filename)

    with open(f'decrypted_{act_filename}', 'wb') as f:
        f.write(data)

generate_key()
encaes('file.txt', 'file.txt')
decaes('file.txt.bin', 'file.txt.bin')