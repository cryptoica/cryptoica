text = input("Enter text: ")
rails = int(input("Enter number of rails: "))

rail = ['' for _ in range(rails)]
row = 0
direction = 1

for char in text:
    rail[row] += char
    row += direction
    if row == 0 or row == rails - 1:
        direction *= -1

cipher = ''.join(rail)
print("Encrypted text:", cipher)


# Step 1: Mark pattern
pattern = [[] for _ in range(rails)]
row = 0
direction = 1

for _ in cipher:
    pattern[row].append('*')
    row += direction
    if row == 0 or row == rails - 1:
        direction *= -1

# Step 2: Fill letters
index = 0
for i in range(rails):
    for j in range(len(pattern[i])):
        pattern[i][j] = cipher[index]
        index += 1

# Step 3: Read zig-zag
result = ""
row = 0
direction = 1

for _ in cipher:
    result += pattern[row].pop(0)
    row += direction
    if row == 0 or row == rails - 1:
        direction *= -1

print("Decrypted text:", result)