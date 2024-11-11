from Crypto.Cipher import AES, DES
from Crypto.Util.Padding import unpad

def aes_decrypt(ciphertext: bytes, key: bytes) -> str:
    iv = ciphertext[:AES.block_size]
    cipher = AES.new(key, AES.MODE_CBC, iv)
    plaintext = unpad(cipher.decrypt(ciphertext[AES.block_size:]), AES.block_size)
    return plaintext.decode()

def des_decrypt(ciphertext: bytes, key: bytes) -> str:
    iv = ciphertext[:DES.block_size]
    cipher = DES.new(key, DES.MODE_CBC, iv)
    plaintext = unpad(cipher.decrypt(ciphertext[DES.block_size:]), DES.block_size)
    return plaintext.decode()
