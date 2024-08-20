from Crypto.Cipher import DES
from Crypto.Util.Padding import pad
import base64
import os

def generate_des_ciphertext(plaintext, key, iv):
    # Create DES cipher object
    cipher = DES.new(key, DES.MODE_CBC, iv)
    
    # Pad plaintext to be a multiple of the block size
    padded_plaintext = pad(plaintext.encode(), DES.block_size)
    
    # Encrypt the plaintext
    ciphertext = cipher.encrypt(padded_plaintext)
    
    # Encode the ciphertext in Base64 to make it printable
    return base64.b64encode(ciphertext).decode('utf-8')

# Example usage
key = os.urandom(8)  # 64-bit key for DES
iv = os.urandom(8)   # 64-bit IV for CBC mode

plaintexts = ["testdata", "exampletext", "thisisaverysecretmessage"]

for plaintext in plaintexts:
    ciphertext = generate_des_ciphertext(plaintext, key, iv)
    print(f"Plaintext: {plaintext}")
    print(f"Ciphertext: {ciphertext}")
    print()
