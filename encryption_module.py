from Crypto.Cipher import AES
from Crypto.Random import get_random_bytes
import base64

class AESCipher:
    def __init__(self, key):
        self.key = key.ljust(32, b'0')[:32]  # Ensure 256-bit key

    def pad(self, data):
        padding_len = AES.block_size - len(data) % AES.block_size
        return data + bytes([padding_len]) * padding_len

    def unpad(self, data):
        return data[:-data[-1]]

    def encrypt(self, plaintext):
        iv = get_random_bytes(AES.block_size)
        cipher = AES.new(self.key, AES.MODE_CBC, iv)
        padded = self.pad(plaintext)
        encrypted = cipher.encrypt(padded)
        return base64.b64encode(iv + encrypted).decode()

    def decrypt(self, encrypted_b64):
        raw = base64.b64decode(encrypted_b64)
        iv = raw[:AES.block_size]
        cipher = AES.new(self.key, AES.MODE_CBC, iv)
        decrypted = cipher.decrypt(raw[AES.block_size:])
        return self.unpad(decrypted).decode()

if __name__ == "__main__":
    key = get_random_bytes(32)  # Generate AES key

    # Save the key to a file for later decryption
    with open("aes_key.bin", "wb") as f:
        f.write(key)

    aes = AESCipher(key)

    with open("genomic_data.txt", "rb") as f:
        plaintext = f.read()

    encrypted_data = aes.encrypt(plaintext)
    print("Encrypted Data (first 100 chars):", encrypted_data[:100], "...")

    with open("encrypted_genomic_data.txt", "w") as f:
        f.write(encrypted_data)
