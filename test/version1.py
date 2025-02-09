import hashlib
import base64
from Crypto.Cipher import AES
from Crypto.Util.Padding import pad, unpad


def ga_jelas():
    return "xwbmrperu123"

def enkripsi(text, shift):
    result = ''

    for i in range(len(text)):
        charCode = ord(text[i])

        # Check if the character is a letter
        if charCode >= 65 and charCode <= 90:
            result += chr((charCode - 65 + shift) % 26 + 65)
        elif charCode >= 97 and charCode <= 122:
            result += chr((charCode - 97 + shift) % 26 + 97)
        else:
            result += text[i]  # Keep non-alphabetic characters unchanged

    return result

def dekripsi(text, shift):
    return enkripsi(text, 26 - shift)

ga_jelas_value = ga_jelas()
shiftValue = 3

def decrypt_aes_js_style(encrypted_text_b64, key):
    """Decrypts AES encrypted text (Base64 encoded) using the given key,
       emulating the CryptoJS behavior.  CryptoJS prepends 'Salted__' + 8-byte salt.
    Args:
        encrypted_text_b64: Base64 encoded string of the encrypted data.
        key: The decryption key (string).

    Returns:
        The decrypted string (UTF-8 encoded).
        Returns None if decryption fails.
    """
    try:
        encrypted_bytes = base64.b64decode(encrypted_text_b64)

        # CryptoJS prepends "Salted__" + 8-byte salt.  Remove it.
        salted_prefix = b"Salted__"
        if encrypted_bytes[:8] != salted_prefix:
            print("Error: Missing 'Salted__' prefix.")
            return None

        salt = encrypted_bytes[8:16]
        ciphertext = encrypted_bytes[16:]

        # Derive key and IV using a simple (insecure, but CryptoJS compatible) KDF
        derived_key, derived_iv = derive_key_and_iv(key, salt)


        cipher = AES.new(derived_key, AES.MODE_CBC, derived_iv)
        padded_plaintext = cipher.decrypt(ciphertext)
        plaintext = unpad(padded_plaintext, AES.block_size).decode('utf-8')

        return plaintext

    except ValueError as e:
        print(f"Decryption Error: {e}")
        return None
    except Exception as e:
        print(f"Unexpected error: {e}")
        return None

def derive_key_and_iv(password, salt, key_length=32, iv_length=16):
    """Derives a key and IV from the password and salt, replicating CryptoJS behavior.
       This is NOT a secure KDF for real-world applications.

    Args:
        password: The password string.
        salt: The salt (bytes).
        key_length: Desired key length (bytes). Defaults to 32 (AES-256).
        iv_length: Desired IV length (bytes). Defaults to 16.

    Returns:
        A tuple of (key, iv) as bytes.
    """
    password_bytes = password.encode('utf-8')
    key_and_iv = b""
    current_digest = b""

    while len(key_and_iv) < key_length + iv_length:
        current_digest = hashlib.md5(current_digest + password_bytes + salt).digest()  # CryptoJS uses MD5
        key_and_iv += current_digest

    key = key_and_iv[:key_length]
    iv = key_and_iv[key_length:key_length + iv_length]
    return key, iv


# Example usage (replace with your actual encrypted text and key)
mau_bolos = "U2FsdGVkX18Gby0LFwrBesbQzFTnAyvZ23wEehQRZwbQqI8pXGAvhGX1k4VC0jiv3igMbxfhdjSQ794MggQtdQ=="
biar_jelas = dekripsi(ga_jelas_value, shiftValue)


decrypted_text = decrypt_aes_js_style(mau_bolos, biar_jelas)

if decrypted_text:
    print(decrypted_text)
else:
    print("Decryption failed.")