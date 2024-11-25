# Peyton Chandler
# UWYO COSC 1010
# 11/24/24
# Lab 10
# Lab Section: 11
# Sources, people worked with, help given to: used chatGpt to debug what was wrong with my code, was getting return errors on line 27 that I couldnt figure out and didnt realize I hadnt made my last print statement an f statement which it also fixed
# Chat-GPT (2024, November 22th) can you help me figure out why my code doesn't work? " copy and pasted code" https://chat.openai.com/
# your
# comments
# here

#import modules you will need 

from hashlib import sha256 
from pathlib import Path

def get_hash(to_hash):
    """You can use """
    return sha256(to_hash.encode('utf-8')).hexdigest().upper()
def password_cracking():
    rockyoupath = Path("rockyou.txt")
    hashpath = Path("hash")

    try:
        storedhash = hashpath.read_text().strip()
    except FileNotFoundError:
        print ("error: 'hash' file cannot be found")
        return
    except Exception as e:
        print(f"error reading hash file: {e}")
        return

# Files and Exceptions

# For this assignment, you will be writing a program to "crack" a password. You will need to open the file `hash` as this is the password you are trying to "crack."

# To begin, you will need to open the 'rockyou.txt' file:
# - This file contains a list of compromised passwords from the rockyou dump.
# - This is an abridged version, as the full version is quite large.
# - The file contains the plaintext version of the passwords. You will need to hash them to check against the password hash you are trying to crack.
#   - You can use the provided `get_hash()` function to generate the hashes.
#   - Be careful, as "hello" and "hello " would generate a different hash.
    try:
        passwords = rockyoupath.read_text().splitlines()
    except FileNotFoundError:
        print("errors: 'rockyou.txt' file not found")
        return
    except Exception as e:
        print(f"error reading 'rockyou.txt: {e}")
        return
    else:
        print("passwords loaded in from 'rockyou.txt'")

    for password in passwords:
        if get_hash(password) == storedhash:
            print(f"password cracked, password is: {password}")
            return

print("password not found in 'rockyou.txt' ")

if __name__ == "__main__":
    password_cracking()
# You will need to include a try-except-catch block in your code.
# - The reading of files needs to occur in the try blocks.


# - Read in the value stored within `hash`.
#   - You must use a try and except block.


# Read in the passwords in `rockyou.txt`.
# - Again, you need a try-except-else block.
# Hash each individual password and compare it against the stored hash.
# - When you find the match, print the plaintext version of the password.
# - End your loop.
