text = input("Enter text (CAPITAL letters only): ")
key = input("Enter key (same length, CAPITAL letters only): ")

if len(text) != len(key):
    print("Error: Key must be same length as text")
else:
    encrypted = ""
    decrypted = ""

    # Encryption
    for i in range(len(text)):
        p = ord(text[i]) - 65
        k = ord(key[i]) - 65
        encrypted += chr((p + k) % 26 + 65)

    print("Encrypted text:", encrypted)

    # Decryption
    for i in range(len(text)):
        c = ord(encrypted[i]) - 65
        k = ord(key[i]) - 65
        decrypted += chr((c - k) % 26 + 65)

    print("Decrypted text:", decrypted)