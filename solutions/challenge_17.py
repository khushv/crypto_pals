from random import choice
from os import urandom
from Cryptodome.Cipher import AES

from challenge_6 import keysize_blocks
from challenge_9 import pad
from challenge_15 import pkcs7_pad_validate_bytes

def encrypt_func(plaintext, encryption_key, iv):
    #print("Character should be: ", plaintext[-1])
    cipher_obj = AES.new(encryption_key, AES.MODE_CBC, iv)
    encrypted_bytes = cipher_obj.encrypt(plaintext)  
    return encrypted_bytes
    

def decrypt_func(cipher_text, key, iv):
    cipher_obj = AES.new(key, AES.MODE_CBC, iv)
    decrypted_bytes = cipher_obj.decrypt(cipher_text)
    #print("******")    
    #print(decrypted_bytes)
    if pkcs7_pad_validate_bytes(decrypted_bytes):
        return True
    else:
        return False


 

if __name__ == '__main__':
    BLOCK_SIZE = 16
    key = bytes(16) #urandom(BLOCK_SIZE)
    iv = bytes(16) #urandom(BLOCK_SIZE)

    sample = """MDAwMDAwTm93IHRoYXQgdGhlIHBhcnR5IGlzIGp1bXBpbmc=
    MDAwMDAxV2l0aCB0aGUgYmFzcyBraWNrZWQgaW4gYW5kIHRoZSBWZWdhJ3MgYXJlIHB1bXBpbic=
    MDAwMDAyUXVpY2sgdG8gdGhlIHBvaW50LCB0byB0aGUgcG9pbnQsIG5vIGZha2luZw==
    MDAwMDAzQ29va2luZyBNQydzIGxpa2UgYSBwb3VuZCBvZiBiYWNvbg==
    MDAwMDA0QnVybmluZyAnZW0sIGlmIHlvdSBhaW4ndCBxdWljayBhbmQgbmltYmxl
    MDAwMDA1SSBnbyBjcmF6eSB3aGVuIEkgaGVhciBhIGN5bWJhbA==
    MDAwMDA2QW5kIGEgaGlnaCBoYXQgd2l0aCBhIHNvdXBlZCB1cCB0ZW1wbw==
    MDAwMDA3SSdtIG9uIGEgcm9sbCwgaXQncyB0aW1lIHRvIGdvIHNvbG8=
    MDAwMDA4b2xsaW4nIGluIG15IGZpdmUgcG9pbnQgb2g=
    MDAwMDA5aXRoIG15IHJhZy10b3AgZG93biBzbyBteSBoYWlyIGNhbiBibG93"""
    clean_sample = sample.split("\n")
    clean_sample = [string.strip(" ") for string in clean_sample]
    #plaintext = pad(choice(clean_sample).encode('ascii'), BLOCK_SIZE)
    plaintext = pad(clean_sample[1].encode('ascii'), BLOCK_SIZE)
    print(plaintext)

    cipher_text = encrypt_func(plaintext, key, iv)
    print("Cipher text is: ", cipher_text)
    #print("Length of cipher text is: ", len(cipher_text))
    decrypted = decrypt_func(cipher_text, key, iv)
    print("test")


    blocks = keysize_blocks(BLOCK_SIZE, cipher_text)
    second_last = bytearray(blocks[-2])
    last_char = second_last[-1]
    print("last character is: ", last_char)
    for i in range(0, 255):
        #import pdb; pdb.set_trace()
        mod_second_last = second_last[0:-1]
        mod_second_last.append(i)
        mod_blocks = blocks
        mod_blocks[-2] = mod_second_last
        a = bytes().join(mod_blocks)
        #
        if decrypt_func(a, key, iv) and i != last_char:
            print("Character in dec: ", i, " and in hex: ", hex(i), " and in ascii: ", chr(i))







