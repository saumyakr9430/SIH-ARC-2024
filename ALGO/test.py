import base64
import re

def is_base64(s):
    try:
        # Attempt to decode the string from Base64 without converting it to text
        base64.b64decode(s, validate=True)
        return True
    except Exception:
        return False

def identify_algorithm(ciphertext):
    # Clean the ciphertext by removing spaces and newlines
    clean_text = ciphertext.replace(" ", "").replace("\n", "")
    
    # Check if the ciphertext is Base64 encoded
    if is_base64(clean_text):
        print("Detected Base64 Encoding")
    
    # Check for RSA format (PEM headers)
    if "-----BEGIN RSA PUBLIC KEY-----" in ciphertext or "-----BEGIN RSA PRIVATE KEY-----" in ciphertext:
        return "RSA"
    
    # Check for AES (Look for common AES Base64 patterns or known headers)
    if "Salted__" in clean_text or re.search(r'U2FsdGVkX1[0-9A-Za-z+/=]*', clean_text):
        return "AES"
    
    # Check for DES (Look for known DES patterns or headers)
    if re.search(r'Z[0-9A-Za-z+/=]{11}', clean_text):  # DES in Base64
        return "DES"
    
    # Check for Blowfish (Specific patterns or headers unique to Blowfish)
    if re.search(r'^[A-Za-z0-9+/]{16,24}={0,2}$', clean_text):  # Blowfish in Base64
        return "Blowfish"
    
    return "Unknown Algorithm"

# Sample ciphertext inputs (replace these with real examples)
sample_ciphertexts = [
    "U2FsdGVkX19/nWQr58NmjJZqXgXRIJ2FOP3Vix2QaIY=",  # AES in Base64
    "MIIBIjANBgkqhkiG9w0BAQEFAAOCAQ8AMIIBCgKCAQEAn",  # RSA Public Key
    "Z8mD3vBZ7Ww=",  # DES in Base64
    "-----BEGIN RSA PUBLIC KEY-----\nMIIBIjANBgkqhkiG9w0BAQEFAAOCAQ8AMIIBCgKCAQEA",  # RSA PEM format
    "8bywOWRUklb0BBs=",  # Blowfish in Base64
]

# Loop through sample ciphertexts and identify the algorithm
for i, ciphertext in enumerate(sample_ciphertexts):
    result = identify_algorithm(ciphertext)
    print(f"Sample {i+1}: Detected Algorithm: {result}")
