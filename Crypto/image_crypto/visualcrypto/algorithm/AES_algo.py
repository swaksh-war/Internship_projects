from Crypto.Cipher import AES
from Crypto.Random import get_random_bytes
import cv2
import numpy as np

def generate_key(filename):
    key = get_random_bytes(32)
    randomByteArray = bytearray(key)
    flatNumpyArray = np.array(randomByteArray)
    grayImage = flatNumpyArray.reshape(4,8)
    cv2.imwrite(f'media/key/{filename}_aeskey.png', grayImage)
    path = f'/media/key/{filename}_aeskey.png'
    return path


def encaes(data_file, filename):
    img = cv2.imread(f'media/key/{filename}_aeskey.png', 0)
    img = img.ravel()
    key = np.ndarray.tobytes(img)
    cipher = AES.new(key, AES.MODE_EAX)
    with open(f'{data_file}', "rb") as f:
        data = f.read()
    ciphertext, tag = cipher.encrypt_and_digest(data)
    enc_file_path = f'media/files/{filename}.bin'
    file_out = open(f"media/files/{filename}.bin", "wb")
    [file_out.write(x) for x in (cipher.nonce, tag, ciphertext)]
    file_out.close()
    return enc_file_path

def decaes(data_file, filename):
    img = cv2.imread(f'media/key_upload/{filename}_aeskey.png', 0)
    img = img.ravel()
    key = np.ndarray.tobytes(img)
    file_in = open(f'{data_file}', 'rb')
    nonce, tag, ciphertext = [file_in.read(x) for x in (16, 16, -1)]
    cipher = AES.new(key, AES.MODE_EAX, nonce)
    original = cipher.decrypt_and_verify(ciphertext, tag)

    with open(f'media/non_enc_file/{filename}', 'wb') as f:
        f.write(original)
