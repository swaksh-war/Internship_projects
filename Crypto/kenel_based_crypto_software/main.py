import AES_algo as algoaes
import RSA_algo as algorsa
import fernet_algo as fa
import utils
print(
    '''

    WelCome to Multialgo File Encryption Software.

    You need to follow the following steps... 
    
            1. Choose a methodology ([0] Decryption, [1] Encryption, [2] Comparing encryted and decrypted file)
            2. Choose an algo
            3. Enter the File path
            4. Enter a key of your wish that will act as password for encryption and decryption
            5. If you have chosed decryption pass nonce value if your Algo is AES or Salsa20
    
    '''
)

method = int(input("Please Choose your methodology([0] Decryption, [1] Encryption, [2] Comparing encrypted and decrypted file): "))

if method == 0:
    algonum = int(input("Please Enter the Algorithm You want to use([0] AES algorithm, [1] RSA algorithm, [2] Fernet algorithm): "))
    data_path = str(input("Please Enter the Path to the Data file you want to decrypt: "))
    filename = data_path.split('/')[-1]
    if algonum == 0:
        algoaes.decaes(data_path, filename)
        print(f'File decrypted and saved as {filename} in the current working directory.')
    
    if algonum == 1:
        algorsa.rsadec(data_path, filename)
        print(f'File decrypted and saved as {filename} in the current working directory.')
    
    if algonum == 2:
        fa.decrypt(data_path, filename)
        print('your file is decrypted and ready to read!')

        

if method == 1:

    print(
        '''

        IMPORTANT: you will create a key in this step that will be used for decrypting the same file and you will be given a nonce value as a text format put that value when nonce value is asked for decrypting a file

        '''
    )

    algonum = int(input("Please Enter the Algorithm You want to use([0]AES algorithm, [1] RSA algorithm, [2] Fernet Algorithm): "))
    data_path = str(input("Please Enter the Path to the Data file you want to Encrypt: "))
    filename = data_path.split('/')[-1]
    if algonum == 0:
    
        print('A 16 bytes key has been generated for you have been saved for You in keyfile')
        algoaes.generate_key()


        algoaes.encaes(data_path, filename)
        
        print(f'Encrypted file saved as {filename}.bin file in current working directory.')


    elif algonum == 1:
        algorsa.generate_rsa_key()
        print('Key saved as reviever key')
        algorsa.rsaenc(data_path, filename)
        print('file encryption Done')
    
    elif algonum == 2:
        fa.generate_key()
        print('Key saved as fernetpass.key on current working directory!')
        fa.encrypt(data_path, filename)

if method == 2:
    num_files =  int(input('enter number of files that you want to compare: '))
    files = []
    for _ in range(num_files):
        filename = str(input('Enter file name for comparison: '))
        files.append(filename)
    utils.size_compaison(files)
    print('Figure has been saved as fig.png in the present working directory')