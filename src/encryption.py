from Crypto.Cipher import AES, DES
from Crypto.Util.Padding import pad
from Crypto.Random import get_random_bytes

def aes_encrypt(plaintext: str, key: bytes) -> bytes:
    cipher = AES.new(key, AES.MODE_CBC)
    ciphertext = cipher.encrypt(pad(plaintext.encode(), AES.block_size))
    return cipher.iv + ciphertext  # Prefix IV to the ciphertext for decryption

def des_encrypt(plaintext: str, key: bytes) -> bytes:
    cipher = DES.new(key, DES.MODE_CBC)
    ciphertext = cipher.encrypt(pad(plaintext.encode(), DES.block_size))
    return cipher.iv + ciphertext
