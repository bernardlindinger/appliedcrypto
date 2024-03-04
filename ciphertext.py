import numpy as np
outputfile = open("hill2x2_5th_email.txt", "w")
count = 0
ciphertext = "mclbhtthkwmcqunnkchtfxvxjnpnmyxleweezdjlzdpzsaowfxrjoozjldpxdngcisttdfbznjbzwuuszrouusrrkesyeezllbhtzpkwnvznnnlztjdjuuoumcquskagokuwignv"

#ciphertext = 'APADJTFTWLFJ'
#ciphertext = ciphertext.lower()
# Python program to demonstrate working of extended 
# Euclidean Algorithm 

target_words = ["that", "the", "it", "and"]
max_count = 0  # Initialize maximum total count
text_with_max_count = ""  # Initialize text with maximum total count 
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

for i in range(ord('a'),ord('z')+1):
    for j in range(ord('a'),ord('z')+1):
        #print("Done j")
        for k in range(ord('a'),ord('z')+1):
            for l in range(ord('a'),ord('z')+1):
                # Get keyword and multiplicative inverse
                keyword = np.array([[i,j],[k,l]])
                keywordalpha = np.array([[i-97, j-97], [k-97, l-97]])
                cipher = list()
                #keyword = np.array([[ord('h'),ord('i')],[ord('l'),ord('l')]])
                #keywordalpha = np.array([[ord('h')-97,ord('i')-97],[ord('l')-97,ord('l')-97]])
                det = int(round(np.linalg.det(keywordalpha) % 26,0))
                if det != 0:
                    integers = keyword.flatten().tolist()
                    #print(integers)
                    letters = ''.join(chr(num) for num in integers)
                    #print(keywordalpha)
                    #print(letters)
                    #print(det)
                    detInv = multiplicative_inverse(det, 26)
                    #print(detInv)
                    # Find adjugate matrix
                    adjugateMatrix = np.array([[keywordalpha[1,1], -keywordalpha[0,1]+26], [-keywordalpha[1,0]+26, keywordalpha[0,0]]])

                    #print(adjugateMatrix)
                    inverseKeyMatrix = (detInv*adjugateMatrix)%26
                    #print(inverseKeyMatrix % 26)
                    digraphs = [ciphertext[i:i+2] for i in range(0, len(ciphertext), 2)]
                    #print(ord('a'))
                    for digraph in digraphs:
                        arr = np.array([[ord(digraph[0])-97],[ord(digraph[1])-97]])
                        outarr = np.matmul(inverseKeyMatrix,arr)%26
                        #print(digraph)
                        #print(outarr)
                        for row in outarr:
                            for value in row:
                                cipher.append(chr(value+97))

                    result = ''.join(cipher)
                    # Count occurrences of each word in the text

                    for text in result:
                        total_count = sum(text.count(word) for word in target_words)  # Calculate total count for the current text
                        # Update max_count and text_with_max_count if a higher total count is found
                        if total_count > max_count:
                            max_count = total_count
                            text_with_max_count = text                    

                   
                    outputfile.write(letters)
                    outputfile.write("\n")
                    outputfile.write(result)
                    outputfile.write("\n")
                else:
                    outputfile.write("skip\n")
outputfile.write(text_with_max_count)
outputfile.write(str(max_count))
outputfile.close()
print("done")

