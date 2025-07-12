from Crypto.Cipher import AES
from Crypto.Protocol.KDF import PBKDF2
from Crypto.Random import get_random_bytes

KEY_LENGTH = 32  # AES-256
FILENAME_DELIMITER = b'::FILENAME::'  # Unique separator

def derive_key(password, salt):
    return PBKDF2(password.encode(), salt, dkLen=KEY_LENGTH, count=100000)

def encrypt_data(data, password):
    salt = get_random_bytes(16)
    iv = get_random_bytes(16)
    key = derive_key(password, salt)
    cipher = AES.new(key, AES.MODE_CFB, iv=iv)
    encrypted_data = salt + iv + cipher.encrypt(data)
    return encrypted_data

def decrypt_data(data, password):
    if len(data) < 32:
        raise ValueError("Invalid encrypted file format.")
    salt = data[:16]
    iv = data[16:32]
    ciphertext = data[32:]
    key = derive_key(password, salt)
    cipher = AES.new(key, AES.MODE_CFB, iv=iv)
    decrypted_data = cipher.decrypt(ciphertext)
    return decrypted_data
