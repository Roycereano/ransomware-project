# Ransomware Simulator 🔐💻

## Project Overview: This is a ransomware simulation project that demonstrates how files can be encerypted and decrypted using Python scripting. 

# This project is strictly for educational purposes and after reading and studying the basics of python and searching for outside resources I was able to write this script. 

## Features 
✅ Encrypts a select number of files. 
✅ Generates a unique encryption key to encrypt files and lock them. 
✅ Requires a password from the user in order to decrypt files. 
✅ Uses Fernet encryption from a cryptography library. 

## How it works 

1️⃣  ** Encryption (danger.py)**
- Scans all files except for the itself, the generated key, and the decryption script. 
- Encrypted files have a key that's randomly generated that locks them away. 
- A Print command will display a ransom message. 

2️⃣** Decryption (decrypt.py)**
- Requires a password to decrypt files (Bitcoin)
- Uses the saved encryption key to restore files. 

## Installation and usage. 

### Clone the repository 
- Please use a virtual machine or what I used was linode to generate a ubunutu machine. DO NOT USE your personal computer. 
- Have fun!  
