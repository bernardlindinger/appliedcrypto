files = ["bc1.txt", "bc2.txt","bc3.txt","bc4.txt", "bc5.txt"]

import numpy as np
from collections import Counter 

# Frequency analysis
for file in files:
    f = open(file, "r")
    letters = f.read()
    
    f.close()

    womp = Counter(c for c in letters if c.isalpha)

    freq = list(range(26))                                                          
    for ascii in range(ord('a'), ord('a')+26):
        freq[ascii-97] = float(letters.count(chr(ascii)))/len(letters)
    #print(freq)
    sumFreqSq = 0.0
    for index in range(len(freq)):
        sumFreqSq += freq[index]*freq[index]

    print(sumFreqSq)
    print(letters)
    print(womp)
    print("\n")
# From this analysis, ciphers 1, 4, and 5 are candidates for ciphers that are encrypted
# since they alter the frequency of the letters. This means ciphers 2 and 3
# will be easier to crack, ie. vigenere and Hill 2x2. We are going to further 
# elimininate these since we know viginiere is using a word 10 letters long, so every 
# 10 chunks should have the same frequency.

# Hill 2x2

'''
def autocorrelation(ciphertext, lag):
    
    # Compute autocorrelation function for a given lag.
    
    return np.correlate(ciphertext, ciphertext, mode='full')[len(ciphertext)-lag:]

def find_key_length(ciphertext, max_key_length):
    
    # Find potential key lengths using autocorrelation.

    autocorr_values = []
    for lag in range(1, max_key_length + 1):
        autocorr_values.append(sum(autocorrelation(ciphertext, lag)) / lag)
    # Find peaks in the autocorrelation function
    peaks = find_peaks(autocorr_values)
    return peaks

def find_peaks(values, threshold=0.2):
    
    # Find peaks in a list of values.
    
    peaks = []
    for i in range(1, len(values) - 1):
        if values[i] > threshold * max(values[i-1], values[i+1]):
            peaks.append(i + 1)  # Add 1 to shift to 1-based indexing
    return peaks


print("Got to function")

for i in range(0,5):
    print(files[i])
    f = open(files[i], "r")
    letters = f.read()
    f.close()
    
    ciphertext = list(ord(letter) for letter in letters)
    #print(ciphertext)
    max_key_length = 20  # Maximum expected key length

# Find potential key lengths using autocorrelation
    potential_key_lengths = find_key_length(ciphertext, max_key_length)
    print("Potential key lengths:", potential_key_lengths)
'''


# Columnar looks like english. 3.
# Playfair has no js. Could be 1. 
# Hill 2x2 preserves some pair frequencies. It is 5 hooray.
# Viginiere is the most uniform among letters. It is 4. 
# From website, key length is probably 14.
# Substitution has english frequencies but on different letters. Could be 2.







