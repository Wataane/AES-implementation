# Brief on AES and DES


Advanced Encryption Standard (AES)\
AES is a symmetric encryption algorithm widely used for its security and efficiency. It uses key sizes of 128, 192, or 256 bits.\
Encryption: AES operates in blocks of 128 bits and typically uses modes like CBC (Cipher Block Chaining) for added security. Each block of plaintext is encrypted using a key and an initialization vector (IV).\
Decryption: AES decryption reverses the encryption process by applying the same key and IV to retrieve the original plaintext.\
\
Data Encryption Standard (DES)\
DES is an older symmetric encryption algorithm that operates on 64-bit blocks and uses a 56-bit key.\
Encryption: DES also supports the CBC mode, where an IV is used to add randomness to each block of plaintext.\
Decryption: To decrypt DES-encrypted data, the same key and IV used for encryption must be applied.\


\
\
\
___________________________________
\
\
# How I implemented it:
\
AES and DES Encryption (encryption.py):\
The function aes_encrypt takes plaintext and a randomly generated 16-byte key. It encrypts the text in CBC mode, using a unique initialization vector (IV) for each operation. The IV is combined with the ciphertext so it can be reused during decryption.\
\
AES and DES Decryption (decryption.py):\
The aes_decrypt function takes the encrypted data and key, extracts the IV, and then decrypts the ciphertext by reversing the AES encryption process. The text is unpadded to remove extra bytes added during encryption.\
\
