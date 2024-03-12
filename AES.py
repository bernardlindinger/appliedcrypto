# For this homework I wanted to learn how to use a more interactive style of solving the problem.
# I want to be able to allow the user to select images from their computer and then solve the 
# encryption problem by letting them choose certain parameters, such as the mode of AES.

from Crypto.Cipher import AES
from Crypto.Util.Padding import pad
import os
import tkinter as tk
from tkinter import filedialog
from PIL import Image, ImageTk
import io

global selectedMode 
selectedMode = None

def pickImageFile():
    try:
        file_path = filedialog.askopenfilename(filetypes=(("All Files", "*.*"),)) #("Image files", "*.jpg;*.jpeg;*.png")
        if file_path:
            selected_file_label.config(text=f"Selected Image: {file_path}")
            originalImage = tk.Toplevel()
            originalImage.title("Original Image") 
            image = Image.open(file_path)
            if image.width > 800 or image.height > 600:
                image.thumbnail((800,600))
            tkImage = ImageTk.PhotoImage(image)
            label = tk.Label(originalImage, image = tkImage)
            label.image = tkImage
            label.pack()
            #with open(file_path, 'rb') as f:
            #    imagedata = f.read()
            raw = image.tobytes()
            #print(imagedata)
            modePick = AESWindow(raw)
            originalImage.mainloop()
        else:
            print("No image selected.")
    except Exception as e:
        print("Error occurred selecting file.", e)
def AESmode(mode):
    global selectedMode
    selectedMode = mode
    print("Mode:", selectedMode)
def makeButton(parent,mode):
    return tk.Button(parent, text=mode, command = lambda: AESmode(mode))
def updateButton():
    label.config(text = "Image Selected")
def AESencrypt(file, mode):
    if mode is None:
        print("Please pick an encryption mode.")
        return
    key = os.urandom(32)
    iv = os.urandom(16)
    encryptedimg = tk.Toplevel()
    encryptedimg.title("Encrypted Image")
    blocksize = AES.block_size
    paddeddata = pad(file, AES.block_size)
    match mode:
        case "ECB":
            cipher = AES.new(key, AES.MODE_ECB)
            #cipherdata = b''.join(cipher.encrypt(file[i:i+blocksize]) for i in range(0, len(file), blocksize))
            cipherdata = cipher.encrypt(paddeddata)
        case "CBC":
            cipher = AES.new(key, AES.MODE_CBC, iv=iv)
            cipherdata = cipher.encrypt(file)
        case "CFB":
            cipher = AES.new(key, AES.MODE_CFB, iv=iv)
            cipherdata = cipher.encrypt(file)
        case "OFB":
            cipher = AES.new(key, AES.MODE_OFB, iv=iv)
            cipherdata = cipher.encrypt(file)      
        case _:
            print("Please pick an encryption mode.")
            return
    encryptedbytes = Image.frombytes(cipherdata)

    with open('encryptedImage.png', 'wb') as f:
        f.write(encryptedbytes)   
    image = Image.open('encryptedImage.png')
    photo = ImageTk.PhotoImage(image)
    label = tk.Label(encryptedimg, image = photo)
    label.image = photo
    label.pack()
    encryptedimg.mainloop()
def rootDestroy():
    root.destroy()
def deleteOriginalImage():
    originalImage.destroy()

# image file picker

root = tk.Tk()
root.geometry("400x300+3000+0")
root.title("Image File Selector")

select_button = tk.Button(root, text="Select Image", command=pickImageFile)
select_button.pack(pady=10)

selected_file_label = tk.Label(root, text="No image selected")
selected_file_label.pack()
            
exitButton = tk.Button(root, text="Exit Program", command = rootDestroy)
exitButton.pack(pady = 5)

# AES mode picker
def AESWindow(image):
    modePick = tk.Toplevel()
    modePick.geometry("400x300-3000+0")
    modePick.title("AES Mode Selection")

    AESmodes = ["ECB", "CBC", "CFB", "OFB"]

    for modes in AESmodes:
        button = makeButton(modePick, modes)
        button.pack(pady=5)
    encryptButton = tk.Button(modePick, text = "encrypt", command = lambda: AESencrypt(image, selectedMode))
    encryptButton.pack(pady=10) 
    modePick.mainloop()


root.mainloop()