from random import choice
from os import urandom
from base64 import b64decode
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

def decrypt_func2(cipher_text, key, iv):
    cipher_obj = AES.new(key, AES.MODE_CBC, iv)
    decrypted_bytes = cipher_obj.decrypt(cipher_text)
    #print("******")    
    print(decrypted_bytes)
    if pkcs7_pad_validate_bytes(decrypted_bytes):
        return True
    else:
        return False
 

if __name__ == '__main__':
    BLOCK_SIZE = 16
    key = urandom(BLOCK_SIZE)
    iv = urandom(BLOCK_SIZE)

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
    plaintext = pad(b64decode(choice(clean_sample)), BLOCK_SIZE)
    #plaintext = pad(clean_sample[1].encode('ascii'), BLOCK_SIZE)
    print(plaintext)
    
    cipher_text_original = encrypt_func(plaintext, key, iv)
    
    #cipher_text = bytearray(16) + cipher_text_original
    cipher_text = bytearray(b'0' * BLOCK_SIZE) + cipher_text_original    
    #import pdb; pdb.set_trace()
    print("Cipher text is: ", cipher_text)
    decrypted = decrypt_func(cipher_text, key, iv)

    # To derive intermediate 
    # P = Plaintext, I = intermediate, E = 16
    # P16 = I16 ^ E16
    # x01 = I16 ^ E'16
    # I16 = x01 ^ E'16
    # P16 = E16 ^ I16
    # P16 = E16 ^ x01 ^ E'16

    first_flag = True
    intermediate_full = bytearray()
    intermediate = bytearray()
    plaintext_full = ""
    char_count = 0
    


    block_number = len(cipher_text_original) // BLOCK_SIZE
    for i in range(0, block_number * BLOCK_SIZE):
        char_count += 1
        #print(cipher_text)
        #print("Char count is: ", char_count)
        counter = len(cipher_text) - BLOCK_SIZE - char_count 
        #print("Counter: ", counter)
        cipher_bytearray = bytearray(cipher_text)
        analysis_char = cipher_bytearray[counter]
        temp_counter = 0
        for val in intermediate:
            temp_counter += 1  
            cipher_bytearray[counter + temp_counter] = val ^ char_count


        for i in range(0, 255):
            cipher_bytearray[counter] = i
            if decrypt_func(bytes(cipher_bytearray), key, iv):          
                if first_flag:
                    if i == analysis_char:
                        continue       
                first_flag = False
                i_value = i ^ char_count
                intermediate.insert(0, i_value) 
                #print("Char is: ", chr(analysis_char ^ i_value) )
                print("Char is: ", analysis_char ^ i_value)
                print("Intermediate is: ", i_value)                
                plaintext_full = chr(analysis_char ^ i_value) + plaintext_full
                
                break 

        if char_count == BLOCK_SIZE:
            
            print("Rotating blocks")
            cipher_text = cipher_text[:-BLOCK_SIZE]
            print("Cipher text")
            print(cipher_text)
            char_count = 0     
            first_flag = True  
            intermediate_full += intermediate
            intermediate = bytearray()
    #print(plaintext[16:])        
    print(plaintext_full[16:])


