import os
import re
import sys
from Cryptodome.Cipher import AES
from challenge_9 import pad
from challenge_6 import keysize_blocks

def encrypt_AES_CBC(plaintext, key):
	plaintext = plaintext.replace('&', '').replace('=', '')
	plaintext = "comment1=cooking%20MCs;userdata=" + plaintext + ";comment2=%20like%20a%20pound%20of%20bacon"
	plaintext = plaintext.encode('ascii')
	print(keysize_blocks(BLOCK_SIZE, plaintext))
	padded_plaintext = pad(plaintext, BLOCK_SIZE)
	cipher_obj = AES.new(key, AES.MODE_CBC, iv)
	encrypted_bytes = cipher_obj.encrypt(padded_plaintext)
	return encrypted_bytes


def is_admin(cipher_bytes, key):
	cipher_obj = AES.new(key, AES.MODE_CBC, iv)
	decrypted_bytes = cipher_obj.decrypt(cipher_bytes)
	print(keysize_blocks(BLOCK_SIZE, decrypted_bytes))
	match_obj = re.search(r';admin=true;', decrypted_bytes.decode('ascii', errors='ignore'))
	if match_obj:
		print("True")
		return True
	else:
		print("False")
		return False



if __name__ == '__main__':
	BLOCK_SIZE = 16
	
	# static for now
	#key = os.urandom(BLOCK_SIZE)
	key = bytes(16)
	
	iv = ("\x00" * BLOCK_SIZE).encode('ascii')
	
	encrypted = encrypt_AES_CBC("AAAAAAAAAAAAAAAABadminBtrue", key)
	encrypted_blocks = (keysize_blocks(BLOCK_SIZE, encrypted))
	print(encrypted_blocks)

	
	# bit flip here
	# use bin(byte) to get binary
	# use int('0b10101201', 2) to get back into byte
	# bytearray.append(97)
	
	# lets start by changing 3rd block
	block_to_change = encrypted_blocks[2]

	
	print("First character is: ", block_to_change[0])
	first_char_bin = bin(block_to_change[0])

	first_char_byte = 90 ^ ord(';')
	print("Changing to: ", first_char_byte)
	
	second_char_byte = block_to_change[1]
	print("Second character is: ", second_char_byte)
	second_char_byte = 162 ^ ord('=')
	print("Changing second character to: ", second_char_byte)
	
	block_array = bytearray(block_to_change)
	block_array[0] = first_char_byte
	block_array[6] = second_char_byte

	encrypted_blocks[2] = block_array
	encrypted = bytes().join(encrypted_blocks)

	bb = is_admin(encrypted, key)
	


