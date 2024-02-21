from ecdsa import SigningKey

# Generate a new private key
private_key = SigningKey.generate()

# Save the private key to a file in PEM format
with open('private_key.pem', 'wb') as f:
    f.write(private_key.to_pem())

# Load the private key from file
with open('private_key.pem', 'rb') as f:
    private_key = SigningKey.from_pem(f.read())

# Obtain the corresponding public key
public_key = private_key.verifying_key

# Save the public key to a file in PEM format
with open('public_key.pem', 'wb') as f:
    f.write(public_key.to_pem())
