from cryptography.fernet import Fernet

# Generate a new Fernet key
fernet_key = Fernet.generate_key()

# Display the base64-encoded key
print("Fernet Key:", fernet_key)

# If you want to save the key to a file
with open('enc_key.txt', 'wb') as f:
    f.write(fernet_key)
