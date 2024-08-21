from Crypto.Cipher import DES3
import datetime
from Crypto.Random import get_random_bytes

# 1. create text
plaintext = b'I am sending the encrypted message.'

# get the start datetime
st = datetime.datetime.now()

# 2. create the key, avoid Option 3
key = DES3.adjust_key_parity(get_random_bytes(24))
cipher = DES3.new(key, DES3.MODE_CFB)

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