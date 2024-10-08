
from Crypto.Cipher import AES
import datetime
from Crypto.Random import get_random_bytes

# 1. create a text
plaintext = b'I am sending the encrypted message.'

# get the start datetime
st = datetime.datetime.now()

# 2. create the key
key = get_random_bytes(16)

# 3. encrypt the message by key and sign it
cipher = AES.new(key, AES.MODE_EAX)
ciphertext, tag = cipher.encrypt_and_digest(plaintext)

# get the end datetime
et = datetime.datetime.now()
# get execution time
elapsed_time = et - st
print('Execution time:', elapsed_time, 'seconds')

print(plaintext) # print original message
print(cipher.nonce)
print(key)
print(ciphertext)