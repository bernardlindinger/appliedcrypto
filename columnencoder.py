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
'''    
def col_trans_decode(ciphertext, num_cols, key):
    num_rows = math.ceil(len(ciphertext)/num_cols) #77 for 8 cols, 68 for 9, and 62 for 10
    grid = [ciphertext[i:i+num_rows] for i in range(0, len(ciphertext), num_rows)]
    for i in range(2):
        if i < 2:
            grid[-1] = grid[-1] + 'zzzzzzzzzz'[:num_cols-len(grid[-1])][:num_cols]
            combinations = create_col_combos(int(num_cols))
            testgrid = list(range(len(grid)))
            for combo in combinations:
                numbers = key
                order_of_cols = sorted(range(len(numbers)), key=lambda i: numbers[i])
                i = 0
                plaintext = []
                for col in order_of_cols:
                    testgrid[i] = grid[col]
                    i += 1
                i = 0
                #print(grid)
                for col in testgrid:
                    for letter in col:
                        plaintext.append(col[i])
                    i += 1
            return grid
        else:
            combinations = create_col_combos(int(num_cols))
            testgrid = list(range(len(grid)))
            for combo in combinations:
                numbers = key
                order_of_cols = sorted(range(len(numbers)), key=lambda i: numbers[i])
                i = 0
                plaintext = []
                for col in order_of_cols:
                    testgrid[i] = grid[col]
                    i += 1
                i = 0
                #print(grid)
                for col in testgrid:
                    for letter in col:
                        plaintext.append(col[i])
                    i += 1
            return grid
'''
'''
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
    plaintext_grid = '\n'.join([' '.join(row) for row in grid])  # Convert the grid to a string with newlines
    return plaintext_grid
'''


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
print(output[0])
key = output[1]
print(key)
output=col_trans_decode(output[0], key)
print(output)

# Should see thereoncewasamanfromspainwhodidntknowhowtotypeabunchoflettersintotheterminalsohejustkepttyoingandwhenhewasdonehewentupandlefthisroomandkeptgoingthesunshinesbrighteverymorningthesunisbiganditissunny

  
