from ecdsa import VerifyingKey, BadSignatureError
from cryptography.fernet import Fernet


# Function to verify a signature on a file
def verify_signature(file_path):
    with open('public_key.pem', 'rb') as f:
        public_key = VerifyingKey.from_pem(f.read())
    
    with open('signature.pem', 'rb') as f:
        signature = f.read()

    with open(file_path, 'rb') as f:
        file_contents = f.read()
        try:
            public_key.verify(signature, file_contents)
            print("Signature verification successful for", file_path)
            return True
        except BadSignatureError:
            print("Signature verification failed for", file_path)
            return False

def read_key_from_file(file_path='key.txt'):
    # Read the Fernet key from the specified file
    with open(file_path, 'rb') as key_file:
        key = key_file.read()
    return key

def signed_then_decrypt(file_path):
        key = read_key_from_file('enc_key.txt')

        f = Fernet(key)

        with open(file_path, 'rb') as encrypted_file:
            encrypted = encrypted_file.read()

        decrypted = f.decrypt(encrypted)

        dec_file_path = 'dec_' + file_path 

        with open(dec_file_path, 'wb') as decrypted_file:
            decrypted_file.write(decrypted)

files_to_verify = input('filename :')

isSigned = verify_signature(files_to_verify)

if isSigned == True:
    signed_then_decrypt(files_to_verify)
    print(True)
else:
    print(False)