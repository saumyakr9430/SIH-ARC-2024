from Crypto.Cipher import Blowfish
from struct import pack
import datetime

# 1. create text
plaintext = b'I am sending the encrypted message.'

# get the start datetime
st = datetime.datetime.now()

# 2. create the key
key = b'An arbitrarily long key'

# 3. encrypt the message
bs = Blowfish.block_size
cipher = Blowfish.new(key, Blowfish.MODE_CBC)
plen = bs - len(plaintext) % bs
padding = [plen]*plen
padding = pack('b'*plen, *padding)
ciphertext = cipher.iv + cipher.encrypt(plaintext + padding)

# get the end datetime
et = datetime.datetime.now()
# get execution time
elapsed_time = et - st
print('Execution time:', elapsed_time, 'seconds')


print(plaintext)
print(key)
print(ciphertext)