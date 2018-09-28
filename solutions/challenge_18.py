from Cryptodome.Cipher import AES
from base64 import b64decode

from challenge_6 import keysize_blocks
from challenge_10 import encrypt_AES_ECB #(plaintext, key)

def xor_byte_block(first, second):
    result = bytearray()
    for i,v in zip(first, second):
        result.append(i ^ v)
    return result

def AES_CTR_encrypt(key, nonce, plaintext):
    #sanitise input
    key = key.encode('ascii')
    #nonce = nonce.encode('ascii')
    plaintext = plaintext.encode('ascii')
    cipher_obj = AES.new(key, AES.MODE_CTR, nonce=nonce)
    encrypted_bytes = cipher_obj.encrypt(plaintext)
    return encrypted_bytes

def AES_CTR_decrypt(key, nonce, ciphertext):
    key = key.encode('ascii')
    #nonce = nonce.encode('ascii')
    #ciphertext = ciphertext.encode('ascii')
    cipher_obj = AES.new(key, AES.MODE_CTR, nonce=nonce)
    decrypted_bytes = cipher_obj.decrypt(cipher_text)
    return decrypted_bytes

def AES_CTR_crypt(key, nonce, text, BLOCK_SIZE=16):
    blocks = keysize_blocks(BLOCK_SIZE, text)
    if type(key) != bytes:
        key = key.encode('ascii')
    counter = 0
    final_text = bytearray()
    for block in blocks:
        to_encrypt = nonce + counter.to_bytes(8, byteorder="little")
        encrypted_text = encrypt_AES_ECB(to_encrypt, key)
        xor_encrypted_text = xor_byte_block(encrypted_text, block)
        final_text.extend(xor_encrypted_text)
        counter += 1
    return final_text



if __name__ == '__main__':
    BLOCK_SIZE = 16
    cipher_text = b64decode("L77na/nrFsKvynd6HzOoG7GHTLXsTVu9qvY/2syLXzhPweyyMTJULu/6/kXX0KSvoOLSFQ==")
    print(cipher_text)
    key = "YELLOW SUBMARINE"
    nonce = (0).to_bytes(8, byteorder="little")

    result = AES_CTR_crypt(key, nonce, cipher_text)
    #print(result.decode('ascii'))
    print(len(result))
