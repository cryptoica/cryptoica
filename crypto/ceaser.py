text = input("Enter text: ")
shift = int(input("Enter shift value: "))

encrypted = ""
decrypted = ""

# Encryption
for char in text:
    if char.isupper():
        encrypted += chr((ord(char) - 65 + shift) % 26 + 65)
    elif char.islower():
        encrypted += chr((ord(char) - 97 + shift) % 26 + 97)
    else:
        encrypted += char

# Decryption
for char in encrypted:
    if char.isupper():
        decrypted += chr((ord(char) - 65 - shift) % 26 + 65)
    elif char.islower():
        decrypted += chr((ord(char) - 97 - shift) % 26 + 97)
    else:
        decrypted += char

print("Encrypted text:", encrypted)
print("Decrypted text:", decrypted)