import hmac
import hashlib

message = input("Enter message: ")
key = input("Enter secret key: ")

# Convert to bytes
message_bytes = message.encode()
key_bytes = key.encode()

# Create HMAC
hmac_result = hmac.new(key_bytes, message_bytes, hashlib.sha512)

# Get hexadecimal digest
final_hmac = hmac_result.hexdigest()

print("HMAC (SHA-512):", final_hmac)