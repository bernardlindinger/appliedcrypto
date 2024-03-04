import numpy as np

def valid_hill_2x2_keys():
    valid_keys = []
    for i in range(26):
        for j in range(26):
            for k in range(26):
                for l in range(26):
                    # Create the key matrix
                    key_matrix = [[i, j], [k, l]]
                    # Calculate the determinant using integer arithmetic
                    det = i * l - j * k
                    # Check if the determinant is non-zero
                    if det != 0:
                        # Check if the determinant is relatively prime to 26
                        if np.gcd(det, 26) == 1:
                            valid_keys.append(key_matrix)
    return valid_keys

# Example usage:
valid_keys = valid_hill_2x2_keys()
print(len(valid_keys))


