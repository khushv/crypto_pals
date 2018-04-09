from random import choice
from os import urandom
from Cryptodome.Cipher import AES

from challenge_9 import pad

def rand_string(encryption_key, iv):
    sample = """MDAwMDAwTm93IHRoYXQgdGhlIHBhcnR5IGlzIGp1bXBpbmc=
    MDAwMDAxV2l0aCB0aGUgYmFzcyBraWNrZWQgaW4gYW5kIHRoZSBWZWdhJ3MgYXJlIHB1bXBpbic=
    MDAwMDAyUXVpY2sgdG8gdGhlIHBvaW50LCB0byB0aGUgcG9pbnQsIG5vIGZha2luZw==
    MDAwMDAzQ29va2luZyBNQydzIGxpa2UgYSBwb3VuZCBvZiBiYWNvbg==
    MDAwMDA0QnVybmluZyAnZW0sIGlmIHlvdSBhaW4ndCBxdWljayBhbmQgbmltYmxl
    MDAwMDA1SSBnbyBjcmF6eSB3aGVuIEkgaGVhciBhIGN5bWJhbA==
    MDAwMDA2QW5kIGEgaGlnaCBoYXQgd2l0aCBhIHNvdXBlZCB1cCB0ZW1wbw==
    MDAwMDA3SSdtIG9uIGEgcm9sbCwgaXQncyB0aW1lIHRvIGdvIHNvbG8=
    MDAwMDA4b2xsaW4nIGluIG15IGZpdmUgcG9pbnQgb2g=
    MDAwMDA5aXRoIG15IHJhZy10b3AgZG93biBzbyBteSBoYWlyIGNhbiBibG93
    """
    clean_sample = sample.split("\n")
    clean_sample = [string.strip(" ") for string in clean_sample]
    chosen = pad(choice(clean_sample), BLOCK_SIZE)
    cipher_obj = AES.new(encryption_key, AES.MODE_CBC, iv)
	encrypted_bytes = cipher_obj.encrypt(padded_plaintext)
    return encrypted_bytes
    


if __name__ == '__main__':
    BLOCK_SIZE = 16
    key = urandom(BLOCK_SIZE)
    iv = urandom(BLOCK_SIZE)
    rand_string(key, iv)
