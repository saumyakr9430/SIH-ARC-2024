from flask import Flask, request, jsonify
from flask_cors import CORS
import base64
import binascii

app = Flask(__name__)
CORS(app) 

def is_base64(s):
    try:
        base64.b64decode(s, validate=True)
        return True
    except Exception:
        return False

def identify_algorithm(ciphertext):
    clean_text = ciphertext.replace(" ", "").replace("\n", "")

    if is_base64(clean_text):
        try:
            decoded_data = base64.b64decode(clean_text)
            clean_text = binascii.hexlify(decoded_data).decode('ascii')
        except Exception:
            return "Error in Base64 decoding"
    else:
        try:
            decoded_data = bytes.fromhex(clean_text)
        except Exception:
            return "Error in Hex decoding"

   
    if "-----BEGIN RSA PUBLIC KEY-----" in ciphertext or "-----BEGIN RSA PRIVATE KEY-----" in ciphertext:
        return "RSA"

  
    return differentiate_aes_des(ciphertext)

def differentiate_aes_des(ciphertext):
    clean_text = ciphertext.replace(" ", "")
    ciphertext_len = len(clean_text) // 2  

    if ciphertext_len % 16 == 0 and ciphertext_len > 16:
        return "AES"
    elif ciphertext_len % 8 == 0 and ciphertext_len % 16 != 0:
        return "DES"
    else:
        return "Unknown Algorithm"

@app.route('/identify', methods=['POST'])
def identify():
    data = request.json
    ciphertext = data.get('ciphertext', '')
    algorithm = identify_algorithm(ciphertext)
    return jsonify({"algorithm": algorithm})

if __name__ == "__main__":
    app.run(debug=True, port=5001)