from Crypto.Cipher import DES
import datetime

# 1. create text
plaintext = b'I am sending the encrypted message.'

# get the start datetime
st = datetime.datetime.now()

# 2. create the key
key = b'-8B key-'
cipher = DES.new(key, DES.MODE_OFB)

# 3. encrypt the message by key
ciphertext = cipher.iv + cipher.encrypt(plaintext)

# get the end datetime
et = datetime.datetime.now()
# get execution time
elapsed_time = et - st
print('Execution time:', elapsed_time, 'seconds')

print(plaintext)
print(key)
print(ciphertext)