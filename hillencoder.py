import random
import numpy as np

def c2i(character):
    return ord(character)-ord('A')

def i2c(encoded):
    return chr(ord('a') + encoded)

def hill_enc(plain):
    found = False
    a=7
    b=8
    c=11
    d=11
    '''
    while not found:
        a,b,c,d = [random.randint(0,25) for i in range(4)]
        det = (a*d - b*c) % 26
        det2 = ((a-1)*d - b*(c-1)) % 26
        if (det % 2 != 0 )and (det % 13 != 0) and (det2 % 26 != 0):
            found = True
    '''
    secret = ''
    # For each diagraph, get first and second letter in list.
    # Convert character to integer. a gets mapped to 
    for i in range(0, len(plain), 2):
        i1 = c2i(plain[i])
        i2 = c2i(plain[i+1])
        #print(i1,i2)
        c1 = (i1*a + i2*b) % 26
        c2 = (i1*c + i2*d) % 26
        #print(c1,c2)
        #print(i2c(c1),i2c(c2))
        secret += i2c(c1) + i2c(c2)
    plaindigraphs = [plain[i:i+2] for i in range(0, len(plain), 2)]
    return secret, [a,b,c,d], plaindigraphs

def hill_keys():
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

def multiplicative_inverse(det, modulus):
    a, b = det, modulus
    # Initialization of variables
    x0, x1 = 1, 0
    y0, y1 = 0, 1
    
    while b != 0:
        q, a, b = a // b, b, a % b
        x0, x1 = x1, x0 - q * x1
        y0, y1 = y1, y0 - q * y1
        
    # Ensure the multiplicative inverse exists
    if a != 1:
        return 0
    else:
        return x0 % modulus


def hill_dec(text): # add in second argument for key to test functionality at the end for a specific key.
    outputfile = open("test.txt", "w")
    ciphertext = text
    target_words = ["that", "the", "it", "and"]
    max_count = 0
    text_with_max_count = ""
    keys = hill_keys()
    for key in keys:
        #print(key)
        #print([item for sublist in key for item in sublist])
        key = [cell for row in key for cell in row]
        i,j,k,l = key[0], key[1], key[2], key[3]
        cipher = list()
        key = np.array([[i,j],[k,l]])
        #print("Key is " + str(key))
        det = int(round(np.linalg.det(key) % 26,0))
        #print("det is " + str(det))
        detInv = multiplicative_inverse(det, 26)
        adjugateMatrix = np.array([[l, -j+26], [-k+26, i]])
        #print("adj matrix is " + str(adjugateMatrix))
        inverseKeyMatrix = (detInv*adjugateMatrix)%26
        digraphs = [ciphertext[i:i+2] for i in range(0, len(ciphertext), 2)]
        #print(digraphs)
        for digraph in digraphs:
            arr = np.array([[ord(digraph[0])-97],[ord(digraph[1])-97]])
            outarr = np.matmul(inverseKeyMatrix,arr)%26
            for row in outarr:
                for value in row:
                    cipher.append(chr(value+97))

        result = ''.join(cipher)
        '''
        for text in result:
            total_count = sum(text.count(word) for word in target_words)
            if total_count > max_count:
                max_count = total_count
                text_with_max_count = text
        '''
        count = 0  
        for word in target_words:
            # Count occurrences of the current word in the string
            count += result.count(word)
        
        # Update max_count and text_with_max_count if the current count is higher
        if count > max_count:
            max_count = count
            text_with_max_count = result              
    
    outputfile.write("\n")
    outputfile.write(text_with_max_count)
    outputfile.write("\n")
    outputfile.write(str(max_count))
    outputfile.close()
    #print(max_count)
    #print(result)
# This is a test for ensuring the decoedr works.
# output = hill_enc("THISTHATANDTHISNADTHATSHORTEXAMPLEIAMTHEBOYTHEONEISTHATANDIAMTHECOOLESTGUY")
output= "xndgeimmxcmpagajktbhsmzunttlzvbjdgjzmionzkzwnldjzvbjdgcebjbhnnfuoqcemnejajqhxxgwzkbhpzaylnyyomgidglhimmaijiuezsnlueiyuijlhbhnlsztnieujshmirwsawicayizwxnvvwzgmqjumpjmwnnmpdhumswojbpsasnzkumswojuzrplhenbhqzywajhgjzqunnszdgxngaicagbjueagdkmnajdgagdtonvinjbhuzyfufqaorscbhcjmjmvlnezuflucjzwrxsywofnyrqztnieaemnszkuxuszmnajojfnyzqjxnvhnneragdkznwgmiuflnrzwpmnajyzqjvhszyaiszkqjrxhzcmaiuiuimmrkqjrxqaxtdhbhlnyswfufbhmqiwcfivrxewdgxprvwmgjajkpcagfqaafdjkskrsfltcjswnnbhieyfejlnmiszkpnneryfejqaezdgvjnnjgeiottzujbhqzpjeixtfncjamxldjmidglfdpiosawsufaevhwrmndglfierxszcawwvhampjyuysxvnjsazkatjcksyheimomqzv"

#print(output[2])
hill_dec(output)

    
