import decrypt
import encrypt
import keycreate

class App:
    @staticmethod
    def KeyCreationg():
        keycreate.keygen()
    @staticmethod
    def Dataencryption(message):
        encrypt.Encryption(message)
    @staticmethod
    def DataDecryption():
        decrypt.decrypt()

App.KeyCreationg()
App.Dataencryption('Hello i am under the water')
App.DataDecryption()
