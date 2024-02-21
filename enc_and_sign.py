from cryptography.fernet import Fernet
from ecdsa import SigningKey, VerifyingKey, BadSignatureError

def read_key_from_file(file_path='key.txt'):
    # Read the Fernet key from the specified file
    with open(file_path, 'rb') as key_file:
        key = key_file.read()
    return key

def encrypt_file(file_path):
    key = read_key_from_file('enc_key.txt')

    f = Fernet(key)

    with open(file_path, 'rb') as original_file:
        original = original_file.read()

    encrypted = f.encrypt(original)


    enc_file_path = 'enc_' + file_path 

    with open (enc_file_path, 'wb') as encrypted_file:
        encrypted_file.write(encrypted)

def sign_file(file_to_sign):

    # Load private key from file
    with open('private_key.pem', 'rb') as f:
        private_key = SigningKey.from_pem(f.read())

    # Load public key from file
    with open('public_key.pem', 'rb') as f:
        public_key = VerifyingKey.from_pem(f.read())

    # Function to sign a file
    def sign_file(file_path):
        with open(file_path, 'rb') as f:
            file_contents = f.read()
            signature = private_key.sign(file_contents)
            return signature

    signature = sign_file(file_to_sign)

    # Save the signature to a file if needed
    with open('signature.pem', 'wb') as f:
        f.write(signature)


file_path_for_encryption = input("Enter the file name you want to encrypt : ")
encrypt_file(file_path_for_encryption)

file_path_for_sign = input("Enter the encrypted file path : ")
sign_file(file_path_for_sign)