from flask import Flask, request, jsonify
from flask_cors import CORS
import base64

app = Flask(__name__)
CORS(app)  # Enable CORS for all routes

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
            clean_text = decoded_data.hex()
        except Exception:
            return "Error in Base64 decoding"
    else:
        try:
            decoded_data = bytes.fromhex(clean_text)
        except ValueError:
            return "Error in Hex decoding"
    
    
    data_length = len(decoded_data)
    
    
    block_sizes = {
        "AES": [16, 24, 32], 
        "DES": [8],           
        "3DES": [8],          
        "Blowfish": [8, 16],  
        "Twofish": [16],      
        "IDEA": [8],          
        "RC4": [16, 32]      
    }
    


  
    if "-----BEGIN RSA PUBLIC KEY-----" in ciphertext or "-----BEGIN RSA PRIVATE KEY-----" in ciphertext:
        return "RSA"
    
    
    if len(clean_text) % 32 == 0 and len(clean_text) > 32:
        return "AES"
    elif len(clean_text) % 8 == 0 and len(clean_text) % 16 != 0:
        return "DES"
    elif len(clean_text) % 8 == 0 and len(clean_text) % 24 == 0:
        return "3DES"
    elif len(clean_text) % 8 == 0 and len(clean_text) % 16 == 0:
        return "Blowfish"
    elif len(clean_text) % 16 == 0 and len(clean_text) % 32 != 0:
        return "Twofish"
    elif len(clean_text) % 8 == 0 and len(clean_text) % 16 == 0:
        return "IDEA"
    elif len(clean_text) % 16 == 0 or len(clean_text) % 32 == 0:
        return "RC4"
    else:
        return "Unknown Algorithm"


    
    return "Unknown Algorithm"



@app.route('/identify', methods=['POST'])
def identify():
    try:
        data = request.json
        if 'ciphertext' not in data:
            return jsonify({"error": "Ciphertext is required"}), 400
        
        ciphertext = data.get('ciphertext', '')
        if not ciphertext:
            return jsonify({"error": "Ciphertext cannot be empty"}), 400
        
        algorithm = identify_algorithm(ciphertext)
        return jsonify({"algorithm": algorithm})
    
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == "__main__":
    app.run(debug=True, port=5001) 
