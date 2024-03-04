# This file will decode the input file given a keyword as the type of cipher

def decode(file, keyword)
    match keyword:
        case "viginiere":
            x=1
        case "playfair":
            x=2
        case "hill2x2":
            keyword = input("Please input the )
        case "columnar":
            x=4
        case "substitution":
            x=5

output = decode(input("Filename: "), input("Type of cipher: "))
        
