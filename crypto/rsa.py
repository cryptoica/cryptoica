from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_OAEP

# Generate RSA Key Pair (public + private)
key = RSA.generate(2048)
public_key = key.publickey()

cipher = PKCS1_OAEP.new(public_key)

text = input("Enter text: ").encode()

# Encryption
ciphertext = cipher.encrypt(text)
print("Encrypted:", ciphertext)

# Decryption
decipher = PKCS1_OAEP.new(key)
decrypted = decipher.decrypt(ciphertext)

print("Decrypted:", decrypted.decode())