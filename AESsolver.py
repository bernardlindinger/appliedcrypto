from Crypto.Cipher import AES
import os
from PIL import Image
from Crypto.Util.Padding import pad, unpad

filename = input("Enter the filename of the image file: ")
key = input("Enter the key you used: ")
key = key.encode('utf-8')
print(key)

im = Image.open(filename)
#cipher = AES.new(key, AES.MODE_ECB)
iv = "sixteen byteswow"
iv = iv.encode('utf-8')
#cipher = AES.new(key, AES.MODE_CBC, iv)
print(im.size)
print(im.mode)

#encryptedimagedata = pad(im.tobytes(), 16)
encryptedimagedata = im.tobytes()
print(len(im.tobytes()))
mode = input("Do you want to encrypt or decrypt (e/d)?")
cipher = input("ECB, CBC, CTR, or OFB: ")
match cipher:
    case "ECB":
        cipher = AES.new(key, AES.MODE_ECB)
    case "CTR":
        nonce = input("Nonce: ")
        cipher = AES.new(key, AES.MODE_CTR, nonce, 1)
    case "OFB":
        cipher = AES.new(key, AES.MODE_OFB, iv)
    case "CBC":
        cipher = AES.new(key, AES.MODE_CBC, iv)
if mode == 'e':
    raw = cipher.encrypt(encryptedimagedata)
    newim = Image.frombytes(im.mode, im.size, raw)
    newim.save("encrypted.png")
    print("okay")
elif mode == 'd':
    raw = cipher.decrypt(encryptedimagedata)
    newim = Image.frombytes(im.mode, im.size, raw)
    newim.save("decrypted.png")
else:
    print("Enter a valid input.")
