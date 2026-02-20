def generate_matrix(key):
    key = key.upper().replace("J", "I")
    matrix = []
    used = set()

    for ch in key + "ABCDEFGHIKLMNOPQRSTUVWXYZ":
        if ch not in used and ch.isalpha():
            used.add(ch)
            matrix.append(ch)

    return [matrix[i:i+5] for i in range(0, 25, 5)]


def find_position(matrix, ch):
    for i in range(5):
        for j in range(5):
            if matrix[i][j] == ch:
                return i, j


def prepare_text(text):
    text = text.upper().replace("J", "I").replace(" ", "")
    result = ""
    i = 0
    while i < len(text):
        a = text[i]
        b = text[i+1] if i+1 < len(text) else "X"

        if a == b:
            result += a + "X"
            i += 1
        else:
            result += a + b
            i += 2

    if len(result) % 2 != 0:
        result += "X"
    return result


def encrypt(text, matrix):
    result = ""
    for i in range(0, len(text), 2):
        a, b = text[i], text[i+1]
        r1, c1 = find_position(matrix, a)
        r2, c2 = find_position(matrix, b)

        if r1 == r2:  # Same row
            result += matrix[r1][(c1+1)%5] + matrix[r2][(c2+1)%5]
        elif c1 == c2:  # Same column
            result += matrix[(r1+1)%5][c1] + matrix[(r2+1)%5][c2]
        else:  # Rectangle rule
            result += matrix[r1][c2] + matrix[r2][c1]

    return result


def decrypt(text, matrix):
    result = ""
    for i in range(0, len(text), 2):
        a, b = text[i], text[i+1]
        r1, c1 = find_position(matrix, a)
        r2, c2 = find_position(matrix, b)

        if r1 == r2:
            result += matrix[r1][(c1-1)%5] + matrix[r2][(c2-1)%5]
        elif c1 == c2:
            result += matrix[(r1-1)%5][c1] + matrix[(r2-1)%5][c2]
        else:
            result += matrix[r1][c2] + matrix[r2][c1]

    return result


key = input("Enter key: ")
text = input("Enter text: ")

matrix = generate_matrix(key)
prepared_text = prepare_text(text)

encrypted = encrypt(prepared_text, matrix)
decrypted = decrypt(encrypted, matrix)

print("Encrypted text:", encrypted)
print("Decrypted text:", decrypted)