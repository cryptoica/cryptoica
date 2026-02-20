p = 23   # prime number
g = 5    # primitive root

# Private keys (secret)
a = 6    # Alice private key
b = 15   # Bob private key

# Public keys
A = (g ** a) % p
B = (g ** b) % p

print("Alice Public Key:", A)
print("Bob Public Key:", B)

# Shared Secret Key
key_alice = (B ** a) % p
key_bob = (A ** b) % p

print("Shared Key (Alice):", key_alice)
print("Shared Key (Bob):", key_bob)