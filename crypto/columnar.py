import math

text = input("Enter text (no spaces): ")
key = input("Enter key: ")

cols = len(key)
rows = math.ceil(len(text) / cols)

matrix = []
index = 0
for r in range(rows):
    row = []
    for c in range(cols):
        if index < len(text):
            row.append(text[index])
            index += 1
        else:
            row.append('X')   # padding
    matrix.append(row)

cipher = ""
key_order = sorted(list(key))

for k in key_order:
    col = key.index(k)
    for r in range(rows):
        cipher += matrix[r][col]

print("Encrypted text:", cipher)


plain_matrix = [['' for _ in range(cols)] for _ in range(rows)]

index = 0
for k in key_order:
    col = key.index(k)
    for r in range(rows):
        plain_matrix[r][col] = cipher[index]
        index += 1

# Read row-wise
decrypted = ""
for r in range(rows):
    for c in range(cols):
        decrypted += plain_matrix[r][c]

print("Decrypted text:", decrypted.rstrip('X'))