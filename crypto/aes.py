#python -m pip install pycryptodome

from Crypto.Cipher import AES
from Crypto.Util.Padding import pad, unpad
from Crypto.Random import get_random_bytes

key = get_random_bytes(16)

cipher = AES.new(key, AES.MODE_CBC)

text = input("Enter text: ").encode()

# Encryption
ciphertext = cipher.encrypt(pad(text, AES.block_size))
print("Encrypted:", ciphertext)

# Decryption
decipher = AES.new(key, AES.MODE_CBC, cipher.iv)
decrypted = unpad(decipher.decrypt(ciphertext), AES.block_size)
print("Decrypted:", decrypted.decode())