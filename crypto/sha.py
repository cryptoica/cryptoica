import hashlib
# Step 2: Take input from user
text = input("Enter text: ")
# Step 3: Convert text into bytes
print("Converting text to bytes...")
byte_data = text.encode('utf-8')
# Step 4: Create SHA-512 hash object
print("Creating SHA-512 hash object...")
sha512_hash = hashlib.sha512()
# Step 5: Update hash object with byte data
print("Updating hash with input data...")
sha512_hash.update(byte_data)
# Step 6: Get hexadecimal digest
final_hash = sha512_hash.hexdigest()
# Step 7: Display result
print("\nOriginal Text:", text)
print("SHA-512 Hash Value:", final_hash)
print("Length of Hash:", len(final_hash), "hex characters")