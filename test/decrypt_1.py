import hashlib
import base64
from Crypto.Cipher import AES
from Crypto.Util.Padding import pad, unpad

def get_secret_key():
    """Returns a predefined secret key."""
    return "xwbmrperu123"

def caesar_cipher(text, shift):
    """Encrypts text using a simple Caesar cipher."""
    result = ''
    for char in text:
        char_code = ord(char)
        if 65 <= char_code <= 90:
            result += chr((char_code - 65 + shift) % 26 + 65)
        elif 97 <= char_code <= 122:
            result += chr((char_code - 97 + shift) % 26 + 97)
        else:
            result += char
    return result

def caesar_decipher(text, shift):
    """Decrypts text using a simple Caesar cipher."""
    return caesar_cipher(text, 26 - shift)

def derive_key_and_iv(password, salt, key_length=32, iv_length=16):
    """Derives a key and IV from the password and salt, replicating CryptoJS behavior."""
    password_bytes = password.encode('utf-8')
    key_iv = b""
    digest = b""
    
    while len(key_iv) < key_length + iv_length:
        digest = hashlib.md5(digest + password_bytes + salt).digest()
        key_iv += digest
    
    return key_iv[:key_length], key_iv[key_length:key_length + iv_length]

def decrypt_aes_js_style(encrypted_text_b64, key):
    """Decrypts AES encrypted text (Base64 encoded) using the given key."""
    try:
        encrypted_bytes = base64.b64decode(encrypted_text_b64)
        
        if encrypted_bytes[:8] != b"Salted__":
            print("Error: Missing 'Salted__' prefix.")
            return None
        
        salt = encrypted_bytes[8:16]
        ciphertext = encrypted_bytes[16:]
        derived_key, derived_iv = derive_key_and_iv(key, salt)
        
        cipher = AES.new(derived_key, AES.MODE_CBC, derived_iv)
        decrypted_bytes = cipher.decrypt(ciphertext)
        return unpad(decrypted_bytes, AES.block_size).decode('utf-8')
    
    except ValueError as e:
        print(f"Decryption Error: {e}")
    except Exception as e:
        print(f"Unexpected error: {e}")
    return None

# Main execution
if __name__ == "__main__":
    encrypted_message = "U2FsdGVkX18yFHUUB+bW79HoXXHHF+1e9bZBZXulYqz5sjpNS4hBir7WVLbE0K71dk69YM+99NY8LMSKajXiVQ=="
    secret_key = get_secret_key()
    shift_value = 3
    decryption_key = caesar_decipher(secret_key, shift_value)
    
    decrypted_text = decrypt_aes_js_style(encrypted_message, decryption_key)
    
    print(decrypted_text if decrypted_text else "Decryption failed.")