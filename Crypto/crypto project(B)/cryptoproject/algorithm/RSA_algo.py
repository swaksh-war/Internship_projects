from Crypto.PublicKey import RSA
from Crypto.Random import get_random_bytes
from Crypto.Cipher import AES, PKCS1_OAEP

def generate_rsa_key(filename):
    key = RSA.generate(2048)
    private_key = key.export_key()
    file_out = open(f"media/key/{filename}_RSA_private.pem", "wb")
    file_out.write(private_key)
    file_out.close()

    public_key = key.publickey().export_key()
    file_out = open(f"media/key/{filename}_RSA_receiver.pem", "wb")
    file_out.write(public_key)
    file_out.close()
    return private_key

def rsaenc(data_path, filename):
    with open(f'{data_path}', 'rb') as f:
        data = f.read()
    file_out_path = f'media/files/{filename}.bin'
    file_out = open(f'media/files/{filename}.bin', 'wb')

    recipient_key = RSA.import_key(open(f"media/key/{filename}_RSA_receiver.pem").read())
    session_key = get_random_bytes(16)

    cipher_rsa  = PKCS1_OAEP.new(recipient_key)
    enc_session_key = cipher_rsa.encrypt(session_key)

    cipher_aes = AES.new(session_key, AES.MODE_EAX)
    ciphertext, tag = cipher_aes.encrypt_and_digest(data)
    [file_out.write(x) for x in (enc_session_key, cipher_aes.nonce, tag, ciphertext) ]
    file_out.close()
    return file_out_path

def rsadec(data_path, filename, key):
    file_in = open(f'{data_path}', 'rb')

    # private_key = key.read()

    enc_session_key, nonce, tag, ciphertext = [file_in.read(x) for x in (key.size_in_bytes(), 16, 16, -1)]
    cipher_rsa = PKCS1_OAEP.new(key)
    session_key = cipher_rsa.decrypt(enc_session_key)

    cipher_aes = AES.new(session_key, AES.MODE_EAX, nonce)
    data = cipher_aes.decrypt_and_verify(ciphertext, tag)
    with open(f'media/non_enc_file/{filename}', 'wb') as f:
        f.write(data)

