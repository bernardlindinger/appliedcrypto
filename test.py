import random
import math
import itertools

plaintext = "thereoncewasamanfromspainwhodidntknowhowtotypeabunchoflettersintotheterminalsohejustkepttyoingandwhenhewasdonehewentupandlefthisroomandkeptgoingthesunshinesbrighteverymorningthesunisbiganditissunny"

def col_trans(plain):
    cols = random.randint(8,10)
    key = list(range(cols))
    random.shuffle(key)
    return "".join(plain[i::cols].lower() for i in key), key
    

def create_col_combos(key_length):
    combinations = list(itertools.permutations(range(key_length), 8))
    combinations_as_strings = [''.join(map(str, combo)) for combo in combinations]
    return combinations_as_strings

def col_trans_decode(ciphertext, key):
    num_cols = len(key)
    num_rows = math.ceil(len(ciphertext) / num_cols)
    grid = [[''] * num_cols for _ in range(num_rows)]  # Initialize an empty grid with the correct dimensions
    for i, col_index in enumerate(key):
        col_start = i * num_rows
        col_end = col_start + num_rows
        col_text = ciphertext[col_start:col_end] + 'z' * (num_rows - len(ciphertext[col_start:col_end]))
        for j, char in enumerate(col_text):
            grid[j][col_index] = char  # Place characters in the correct position in the grid
    plaintext = ''.join(''.join(row) for row in grid)  # Flatten the grid to obtain plaintext
    return plaintext

output = col_trans(plaintext)
print("Encrypted ciphertext:", output[0])
key = output[1]
print("Encryption key:", key)
decrypted_text = col_trans_decode(output[0], key)
print("Decrypted plaintext:", decrypted_text)

# Ensure that decryption is consistent by decrypting multiple times
for _ in range(5):
    decrypted_text = col_trans_decode(output[0], key)
    print("Decrypted plaintext (repeat):", decrypted_text)
